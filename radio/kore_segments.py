#!/usr/bin/env python3
"""Génère un mp3 Kore par segment des scripts radio (Qwen3-TTS, clone de la voix Kore, CPU).

Usage : python3 radio/kore_segments.py <fichier_scripts.json> <dossier_sortie> [id ...]
Prérequis (voir HANDOFF-S4-S5 du projet) : torch CPU, qwen-tts, faster-whisper, num2words, soundfile, scipy.
Par bloc (un paragraphe) : 2 essais en un seul appel, contrôle Whisper (écart de mots), on garde le meilleur.
Lexique : radio/lexique_kore.json (noms propres prononcés à la française). Reprise possible : un bloc déjà rendu n'est pas refait.
"""
import hashlib, json, os, re, sys, time, wave
import numpy as np, soundfile as sf, torch
from num2words import num2words
from scipy.signal import resample_poly
from qwen_tts import Qwen3TTSModel
from faster_whisper import WhisperModel

HERE = os.path.dirname(os.path.abspath(__file__))
KORE = os.environ.get("KORE_DIR", os.path.join(HERE, "..", "voix_kore"))  # ref.wav + ref.txt
GEN = dict(do_sample=True, temperature=0.6, top_p=0.85, top_k=30, repetition_penalty=1.05)
LEX = json.load(open(os.path.join(HERE, "lexique_kore.json"), encoding="utf8"))
SR_OUT = 24000


def lex(t):
    for k in sorted(LEX, key=len, reverse=True):
        t = t.replace(k, LEX[k])
    return t


def norm(s):
    s = re.sub(r"\d+", lambda m: num2words(int(m.group()), lang="fr"), s.lower().replace("'", " ").replace("-", " "))
    return re.findall(r"[a-zàâçéèêëîïôûùüÿœ]+", s)


def wer(a, b):
    p = list(range(len(b) + 1))
    for i, x in enumerate(a, 1):
        c = [i]
        for j, y in enumerate(b, 1):
            c.append(min(p[j] + 1, c[j - 1] + 1, p[j - 1] + (x != y)))
        p = c
    return p[-1] / max(1, len(a))


def main():
    fscripts, out, ids = sys.argv[1], sys.argv[2], sys.argv[3:]
    os.makedirs(out, exist_ok=True)
    d = json.load(open(fscripts, encoding="utf8"))
    segs = [s for s in d["segments"] if not ids or s["id"] in ids]
    w = wave.open(os.path.join(KORE, "ref.wav")); sr0 = w.getframerate()
    ref = np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16).astype(np.float32) / 32768
    ref_text = open(os.path.join(KORE, "ref.txt"), encoding="utf8").read().strip()
    m = Qwen3TTSModel.from_pretrained("Qwen/Qwen3-TTS-12Hz-1.7B-Base", device_map="cpu", dtype=torch.float32)
    prompt = m.create_voice_clone_prompt(ref_audio=(ref, sr0), ref_text=ref_text)
    asr = WhisperModel("small", device="cpu", compute_type="int8")
    t0 = time.time()
    for s in segs:
        blocs = []
        for b in (b.strip() for b in s["texte"].split("\n\n") if b.strip()):
            if blocs and len(blocs[-1].split()) < 8:  # un bloc trop court fait fuiter la référence : on le fond avec le suivant
                blocs[-1] += " " + b
            else:
                blocs.append(b)
        pieces = []
        for bi, b in enumerate(blocs):
            h = hashlib.sha1(b.encode()).hexdigest()[:16]
            f = os.path.join(out, h + ".wav")
            if not os.path.exists(f):
                best = None
                torch.manual_seed(11 + bi)
                ws, sr = m.generate_voice_clone(text=[lex(b)] * 2, language=["French"] * 2, voice_clone_prompt=prompt, **GEN)
                for x in ws:
                    x = np.asarray(x, dtype=np.float32)
                    y = resample_poly(x, 16000, sr).astype(np.float32)
                    segsw, _ = asr.transcribe(y, language="fr")
                    e = wer(norm(b), norm(" ".join(z.text for z in segsw)))
                    if best is None or e < best[0]:
                        best = (e, x, sr)
                sf.write(f, best[1], best[2])
                print(f"{s['id']} bloc {bi + 1}/{len(blocs)} écart {best[0]:.0%} ({time.time() - t0:.0f}s)", flush=True)
            x, sr = sf.read(f, dtype="float32")
            pieces.append(x); pieces.append(np.zeros(int(0.6 * sr), dtype=np.float32))
        sf.write(os.path.join(out, s["id"] + ".wav"), np.concatenate(pieces[:-1]), sr)
        print("fini", s["id"], flush=True)


if __name__ == "__main__":
    main()
