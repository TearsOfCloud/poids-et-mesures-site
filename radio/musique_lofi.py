#!/usr/bin/env python3
"""Compositeur lo-fi maison pour la radio P&M (synthèse pure, numpy/scipy, aucun échantillon externe).

Chaque piste est composée par code à partir d'une graine : progression d'accords jazz (7e/9e),
piano électrique type Rhodes (synthèse FM), basse, batterie swinguée, mélodie clairsemée,
craquements de vinyle, flottement de bande, réverbération. Tout est généré ici : aucun droit
d'auteur tiers, aucune licence à citer, gratuit, reproductible (même graine = même piste).

Usage :
  python3 radio/musique_lofi.py <dossier_sortie> [nb_pistes] [--jingles]
  python3 radio/musique_lofi.py <dossier_sortie> --une <graine>      (une seule piste, pour tester)
Nécessite : numpy, scipy, ffmpeg (mp3).
"""
import json, os, subprocess, sys
import numpy as np
from scipy.signal import butter, sosfilt, fftconvolve

SR = 44100

# ---------- outils ----------
def mtof(m): return 440.0 * 2 ** ((np.asarray(m, dtype=float) - 69) / 12)

def lp(x, fc, o=2): return sosfilt(butter(o, fc, "lowpass", fs=SR, output="sos"), x)
def hp(x, fc, o=2): return sosfilt(butter(o, fc, "highpass", fs=SR, output="sos"), x)
def bp(x, a, b, o=2): return sosfilt(butter(o, [a, b], "bandpass", fs=SR, output="sos"), x)

def env_adsr(n, a, d, s, r_start, r):
    """Enveloppe simple en échantillons (a,d,r en s ; s niveau de maintien)."""
    t = np.arange(n) / SR
    e = np.minimum(t / max(a, 1e-4), 1.0)
    e = e * (s + (1 - s) * np.exp(-np.maximum(t - a, 0) / max(d, 1e-4)))
    rel = np.clip((r_start - t) / max(r, 1e-4) + 1, 0, 1) if r_start < n / SR else 1
    return e * rel

# ---------- instruments ----------
def rhodes(freq, dur, vel, rng):
    n = int((dur + 0.9) * SR)
    t = np.arange(n) / SR
    out = np.zeros(n)
    for det, g in ((0.0, 1.0), (0.0035, 0.55), (-0.0035, 0.55)):  # léger chorus naturel
        f = freq * (1 + det)
        idx = (0.9 + 2.2 * vel) * np.exp(-t / 0.35) + 0.25          # le « tine » : brillant puis doux
        mod = np.sin(2 * np.pi * f * 14 * t) * np.exp(-t / 0.05) * 0.35 * vel
        out += g * np.sin(2 * np.pi * f * t + idx * np.sin(2 * np.pi * f * t) * 0.9 + mod)
    out *= 1 + 0.12 * np.sin(2 * np.pi * 4.6 * t) * np.minimum(t / 0.6, 1)  # trémolo discret
    a = np.minimum(t / 0.006, 1)
    d = np.exp(-t / (1.8 + 4.0 * (1 - freq / 1500)))
    rel = np.clip((dur - t) / 0.35 + 1, 0, 1)
    return out * a * d * rel * vel

def nappe(freq, dur, vel):
    n = int((dur + 1.2) * SR); t = np.arange(n) / SR
    s = sum(np.sin(2 * np.pi * freq * (1 + d) * t) for d in (-0.004, 0, 0.004)) / 3 + 0.3 * np.sin(2 * np.pi * freq * 2 * t)
    e = np.minimum(t / 0.9, 1) * np.clip((dur - t) / 1.2 + 1, 0, 1)
    return s * e * vel

def pluck(freq, dur, vel):
    n = int((dur + 0.6) * SR); t = np.arange(n) / SR
    s = np.sin(2 * np.pi * freq * t) + 0.35 * np.sin(2 * np.pi * freq * 2 * t) * np.exp(-t / 0.15) + 0.15 * np.sin(2 * np.pi * freq * 3 * t) * np.exp(-t / 0.08)
    e = np.minimum(t / 0.004, 1) * np.exp(-t / 0.5) * np.clip((dur - t) / 0.2 + 1, 0, 1)
    return s * e * vel

def bass(freq, dur, vel):
    n = int((dur + 0.15) * SR); t = np.arange(n) / SR
    s = np.sin(2 * np.pi * freq * t) + 0.3 * np.sin(2 * np.pi * freq * 2 * t) * np.exp(-t / 0.3)
    s = np.tanh(s * 1.4)
    e = np.minimum(t / 0.012, 1) * np.exp(-t / 1.1) * np.clip((dur - t) / 0.08 + 1, 0, 1)
    return s * e * vel

def kick(vel, rng):
    n = int(0.45 * SR); t = np.arange(n) / SR
    f = 46 + 90 * np.exp(-t / 0.035)
    ph = 2 * np.pi * np.cumsum(f) / SR
    s = np.sin(ph) * np.exp(-t / 0.14)
    s += 0.25 * lp(rng.standard_normal(n), 900) * np.exp(-t / 0.008)
    return np.tanh(s * 1.8) * vel

def snare(vel, rng):
    n = int(0.5 * SR); t = np.arange(n) / SR
    nz = bp(rng.standard_normal(n), 1400, 7500) * np.exp(-t / 0.11)
    tone = np.sin(2 * np.pi * 185 * t) * np.exp(-t / 0.06) * 0.5
    return (nz * 0.9 + tone) * vel * np.minimum(t / 0.001, 1)

def hat(vel, rng, open_=False):
    n = int((0.28 if open_ else 0.07) * SR); t = np.arange(n) / SR
    s = hp(rng.standard_normal(n), 7000) * np.exp(-t / (0.09 if open_ else 0.018))
    return s * vel * 0.5

def rimclick(vel, rng):
    n = int(0.08 * SR); t = np.arange(n) / SR
    return (np.sin(2 * np.pi * 1700 * t) * 0.4 + bp(rng.standard_normal(n), 1500, 5000)) * np.exp(-t / 0.012) * vel * 0.5

def put(buf, x, pos, g=1.0, pan=0.0):
    pos = int(pos)
    if pos < 0 or pos >= buf.shape[1]: return
    m = min(len(x), buf.shape[1] - pos)
    l, r = np.sqrt(0.5 * (1 - pan)), np.sqrt(0.5 * (1 + pan))
    buf[0, pos:pos + m] += x[:m] * g * l
    buf[1, pos:pos + m] += x[:m] * g * r

# ---------- harmonie ----------
# degrés en demi-tons depuis la tonique, qualités avec voicings (intervalles depuis la fondamentale)
Q = {
    "m9":   [0, 3, 7, 10, 14], "m7":   [0, 3, 7, 10], "maj9": [0, 4, 7, 11, 14], "maj7": [0, 4, 7, 11],
    "7":    [0, 4, 7, 10], "13":   [0, 4, 10, 14, 21], "m11":  [0, 3, 10, 14, 17], "6":    [0, 4, 7, 9, 14],
    "m7b5": [0, 3, 6, 10], "7sus": [0, 5, 7, 10, 14],
}
PROGS = [  # (nom, [(demi-tons, qualité)], mode: 'maj' ou 'min')
    ("ii-V-I-vi",  [(2, "m9"), (7, "13"), (0, "maj9"), (9, "m7")], "maj"),
    ("I-iii-vi-ii", [(0, "maj9"), (4, "m7"), (9, "m9"), (2, "m9")], "maj"),
    ("i-iv-VII-III", [(0, "m9"), (5, "m11"), (10, "13"), (3, "maj9")], "min"),
    ("vi-ii-V-I",  [(9, "m9"), (2, "m7"), (7, "7sus"), (0, "maj7")], "maj"),
    ("i-VI-III-VII", [(0, "m7"), (8, "maj9"), (3, "maj7"), (10, "6")], "min"),
    ("IV-iii-ii-I", [(5, "maj9"), (4, "m7"), (2, "m9"), (0, "6")], "maj"),
    ("ii-V-i-VI",  [(2, "m7b5"), (7, "7"), (0, "m9"), (8, "maj7")], "min"),
]
PENTA = {"maj": [0, 2, 4, 7, 9], "min": [0, 3, 5, 7, 10]}

def voicing(root, qual, prev):
    """Voicing proche du précédent (conduite des voix), registre MIDI ~ 52-76."""
    iv = Q[qual]
    best, bs = None, 1e9
    for inv in range(len(iv)):
        notes = [root + i for i in iv]
        notes = notes[inv:] + [n + 12 for n in notes[:inv]]
        for shift in (-12, 0, 12):
            v = [n + shift for n in notes]
            if min(v) < 52 or max(v) > 78: continue
            cost = 0 if prev is None else abs(np.mean(v) - np.mean(prev)) + 0.15 * sum(abs(a - b) for a, b in zip(sorted(v), sorted(prev)))
            if cost < bs: best, bs = v, cost
    if best is None:
        best = sorted(((root + i - 12 * (1 if root + i > 76 else 0)) for i in iv))
        best = [n + 12 if n < 50 else n for n in best]
    return best

# ---------- une piste ----------
STYLES = {  # bpm, batterie, motif de batterie, densité mélodie, réverbe, filtre final, accords tenus
    "chill":   dict(bpm=[68, 72, 76, 80], drums=0.85, pat="lofi",   dens=(0.35, 0.65), rev=0.42, cut=7200, pad=0.0),
    "boombap": dict(bpm=[86, 90, 94],     drums=1.0,  pat="boombap", dens=(0.15, 0.35), rev=0.25, cut=5200, pad=0.0),
    "ambient": dict(bpm=[58, 62, 66],     drums=0.0,  pat="none",   dens=(0.2, 0.4),   rev=0.9,  cut=8500, pad=1.0),
    "house":   dict(bpm=[108, 112, 116],  drums=1.0,  pat="house",  dens=(0.4, 0.7),   rev=0.35, cut=9000, pad=0.3),
}

def compose(seed, minutes=3.4, drums=None, style="chill"):
    rng = np.random.default_rng(seed)
    st = STYLES[style]
    key = int(rng.integers(0, 12))                         # tonique (0 = do)
    bpm = float(rng.choice(st['bpm']))
    swing = float(rng.uniform(0.54, 0.62))
    name, prog, mode = PROGS[int(rng.integers(len(PROGS)))]
    has_drums = bool(rng.random() < st['drums']) if drums is None else drums
    density = float(rng.uniform(*st['dens']))                # densité de la mélodie
    beat = 60.0 / bpm
    bar = 4 * beat
    nbars = int(minutes * 60 / bar)
    nbars -= nbars % 4
    total = int((nbars * bar + 4.0) * SR)
    keys = np.zeros((2, total)); bas = np.zeros((2, total)); dr = np.zeros((2, total)); mel = np.zeros((2, total))
    kick_t = []
    prev = None
    base = 48 + key                                         # do2 transposé
    voic = []
    for b in range(nbars):
        deg, qual = prog[b % 4]
        root = base + deg + (12 if deg + key > 8 and False else 0)
        v = voicing(root + 12, qual, prev); prev = v; voic.append((root, qual, v))
    # structure : intro (nuage d'accords seuls) / thème / respiration / thème / fin
    for b in range(nbars):
        t0 = b * bar
        root, qual, v = voic[b]
        sect = b / nbars
        drum_on = has_drums and 0.07 < sect < 0.93 and not (0.46 < sect < 0.54)
        # accords : deux attaques par mesure, rythme « paresseux » ; léger strum
        hits = [(0.0, 2.6), (2.5 + (0.5 if rng.random() < 0.4 else 0.0), 1.5)] if rng.random() < 0.8 else [(0.0, 3.8)]
        for off, dl in hits:
            vel = float(rng.uniform(0.55, 0.85)) * (0.7 if sect < 0.05 or sect > 0.95 else 1)
            for k, n in enumerate(sorted(v)):
                jt = rng.normal(0, 0.008) + k * rng.uniform(0.012, 0.03)
                put(keys, rhodes(mtof(n), dl * beat, vel * rng.uniform(0.85, 1.0), rng), (t0 + off * beat + jt) * SR, 0.17, pan=rng.uniform(-0.25, 0.25))
        if st['pad'] > 0:
            for k, n in enumerate(sorted(v)):
                put(keys, nappe(mtof(n - 12 * (k % 2 == 0 and False)), 4.4 * beat, 0.5), (t0 - 0.05) * SR, 0.1 * st['pad'], pan=(-0.5 + 0.25 * k))
        # basse
        bv = float(rng.uniform(0.6, 0.85))
        put(bas, bass(mtof(root - 12), 1.8 * beat, bv), (t0 + rng.normal(0, 0.006)) * SR, 0.42)
        if rng.random() < 0.55:
            put(bas, bass(mtof(root - 12 + (7 if rng.random() < 0.6 else 12)), 0.9 * beat, bv * 0.7), (t0 + (2.5 if rng.random() < 0.5 else 3.0) * beat) * SR, 0.34)
        # batterie
        if drum_on:
            step = beat / 2
            pat = st['pat']
            sw = lambda i: (i // 2) * beat + (swing * beat if i % 2 else 0)   # croche swinguée
            if pat == 'house':
                for q in range(4):
                    tq = t0 + q * beat + rng.normal(0, 0.002)
                    put(dr, kick(0.95, rng), tq * SR, 0.6); kick_t.append(tq)
                    put(dr, hat(0.5, rng, open_=True), (tq + beat / 2) * SR, 0.3, pan=0.2)
                    if q in (1, 3): put(dr, snare(0.55, rng), tq * SR, 0.3)
                continue
            for i in range(8):
                tt = t0 + sw(i) + rng.normal(0, 0.007 if pat == 'lofi' else 0.003)
                if pat == 'boombap':
                    if i in (0, 3) or (i == 6 and rng.random() < 0.5):
                        put(dr, kick(float(rng.uniform(0.9, 1.0)), rng), tt * SR, 0.75); kick_t.append(tt)
                    if i in (2, 6):
                        put(dr, snare(float(rng.uniform(0.85, 1.0)), rng), tt * SR, 0.6, pan=0.05)
                    put(dr, hat(float(rng.uniform(0.3, 0.7)), rng), tt * SR, 0.3, pan=0.18)
                    continue
                if i in (0,) or (i == 5 and rng.random() < 0.6) or (i == 3 and rng.random() < 0.3):
                    put(dr, kick(float(rng.uniform(0.75, 0.95)), rng), tt * SR, 0.55); kick_t.append(tt)
                if i in (2, 6):
                    put(dr, snare(float(rng.uniform(0.6, 0.85)), rng), (tt + 0.012) * SR, 0.45, pan=0.05)
                if i % 2 == 0 or rng.random() < 0.35:
                    put(dr, hat(float(rng.uniform(0.25, 0.6)) * (1.0 if i % 2 == 0 else 0.6), rng, open_=(i == 7 and rng.random() < 0.25)), tt * SR, 0.32, pan=0.18)
            if rng.random() < 0.15:
                put(dr, rimclick(0.6, rng), (t0 + 3.75 * beat) * SR, 0.3, pan=-0.2)
        # mélodie clairsemée en gamme pentatonique, on la garde pour les sections « thème »
        if 0.14 < sect < 0.9 and not (0.46 < sect < 0.54):
            scale = [base + 24 + key * 0 + s for s in PENTA[mode]] + [base + 36 + s for s in PENTA[mode]]
            t = 0.0
            while t < 4.0:
                if rng.random() < density:
                    n = scale[int(np.clip(rng.normal(5, 2.2), 0, len(scale) - 1))]
                    d = float(rng.choice([0.5, 1.0, 1.5]))
                    put(mel, pluck(mtof(n), d * beat, float(rng.uniform(0.35, 0.7))), (t0 + t * beat + rng.normal(0, 0.01)) * SR, 0.2, pan=rng.uniform(-0.4, 0.4))
                    t += d + float(rng.choice([0.0, 0.5, 1.0]))
                else:
                    t += 0.5
    # sidechain léger : les claviers « respirent » sur chaque grosse caisse
    duck = np.ones(total)
    for tt in kick_t:
        i0 = int(tt * SR); L = int(0.22 * SR)
        if i0 + L < total: duck[i0:i0 + L] *= 1 - 0.25 * np.exp(-np.arange(L) / (0.07 * SR))
    keys *= duck
    bas *= duck
    # chaîne : claviers + mélodie -> bande lo-fi (filtre, flottement, saturation) -> réverbe
    wet = keys + mel * 0.9
    wet = tape(wet, rng)
    rev = reverb(wet, 2.3, rng)
    delay = echo(mel, 0.375 * 60 / bpm * 4 / 3, 0.35, rng)
    mix = wet * 0.95 + rev * st['rev'] + delay * 0.4 + bas * 1.0 + dr * 0.95
    mix[0] = lp(mix[0], st['cut'], 2); mix[1] = lp(mix[1], st['cut'], 2)
    mix = hp(mix, 30)
    # craquements de vinyle + souffle très bas
    mix += vinyl(total, rng) * 0.05
    mix = np.tanh(mix * 1.25) / np.tanh(1.25)
    # fondu d'entrée/sortie
    f = int(2.5 * SR)
    mix[:, :f] *= np.linspace(0, 1, f); mix[:, -f * 2:] *= np.linspace(1, 0, f * 2)
    return norm(mix), dict(seed=seed, style=style, bpm=bpm, tonalite=key, progression=name, mode=mode, batterie=has_drums, duree=round(total / SR, 1))

def tape(x, rng):
    """Flottement de bande (wow/flutter) + filtre doux + saturation."""
    n = x.shape[1]; t = np.arange(n) / SR
    ph = rng.uniform(0, 6, 3)
    # décalage temporel (s) = intégrale d'une petite variation de vitesse
    dev = 0.0016 * np.sin(2 * np.pi * 0.43 * t + ph[0]) + 0.0006 * np.sin(2 * np.pi * 5.1 * t + ph[1]) + 0.0004 * np.sin(2 * np.pi * 0.11 * t + ph[2])
    shift = np.cumsum(dev) / SR
    out = np.stack([np.interp(t + shift, t, ch) for ch in x])
    return np.stack([np.tanh(lp(ch, 6200, 2) * 1.1) for ch in out])

def reverb(x, sec, rng):
    n = int(sec * SR); t = np.arange(n) / SR
    outs = []
    for _ in range(2):
        ir = rng.standard_normal(n) * np.exp(-t / (sec / 5.5))
        ir = lp(ir, 3800, 2) * np.minimum(t / 0.03, 1)
        ir /= np.sqrt(np.sum(ir ** 2))
        outs.append(ir)
    return np.stack([fftconvolve(x[0], outs[0])[:x.shape[1]] * 0.6 + fftconvolve(x[1], outs[1])[:x.shape[1]] * 0.4,
                     fftconvolve(x[1], outs[1])[:x.shape[1]] * 0.6 + fftconvolve(x[0], outs[0])[:x.shape[1]] * 0.4])

def echo(x, d, fb, rng):
    n = x.shape[1]; k = int(d * SR); out = np.zeros_like(x); cur = x.copy(); g = 1.0
    for i in range(1, 5):
        g *= fb
        sh = np.zeros_like(x)
        if i * k < n: sh[:, i * k:] = cur[:, :n - i * k]
        out += sh[::-1] * g if i % 2 else sh * g
    return np.stack([lp(out[0], 3000, 1), lp(out[1], 3000, 1)])

def vinyl(n, rng):
    out = np.zeros((2, n))
    for c in range(2):
        hiss = hp(lp(rng.standard_normal(n), 9000, 1), 1500, 1) * 0.12
        pops = np.zeros(n)
        idx = rng.integers(0, n, int(n / SR * 7))
        pops[idx] = rng.uniform(-1, 1, len(idx)) * rng.uniform(0.3, 1.0, len(idx))
        pops = lp(pops, 8000, 1) * 1.5
        crack = np.zeros(n)
        idx2 = rng.integers(0, n, int(n / SR * 40))
        crack[idx2] = rng.uniform(-1, 1, len(idx2)) * 0.12
        out[c] = hiss + pops + hp(crack, 2500, 1)
    return out

def norm(mix, target_rms=0.105, peak=0.92):
    mono = mix.mean(axis=0)
    r = np.sqrt(np.mean(mono ** 2)) + 1e-9
    mix = mix * (target_rms / r)
    pk = np.abs(mix).max()
    if pk > peak: mix = np.tanh(mix / peak * 1.0) * peak
    return mix

def jingle(seed, nom):
    """Jingle d'antenne ~7 s : motif de 4 notes au Rhodes + nappe + coup de caisse claire douce."""
    rng = np.random.default_rng(seed)
    base = 60 + int(rng.integers(0, 5))
    motif = [base, base + 7, base + 12, base + 16] if rng.random() < 0.5 else [base + 4, base + 11, base + 14, base + 19]
    total = int(8.0 * SR); buf = np.zeros((2, total))
    for i, m in enumerate(motif):
        put(buf, rhodes(mtof(m), 1.6, 0.8, rng), int((0.15 + i * 0.36) * SR), 0.3, pan=-0.3 + 0.2 * i)
    for m in (base - 12, base - 5, base):
        put(buf, rhodes(mtof(m), 4.0, 0.55, rng), int(1.6 * SR), 0.2)
    put(buf, snare(0.5, rng), int(1.6 * SR), 0.25)
    mix = tape(buf, rng); mix = mix + reverb(mix, 2.0, rng) * 0.5
    mix = np.tanh(mix * 1.3) / np.tanh(1.3)
    mix[:, -int(1.5 * SR):] *= np.linspace(1, 0, int(1.5 * SR))
    return norm(mix, 0.09), dict(seed=seed, duree=8.0, nom=nom)

def vers_mp3(mix, chemin, titre):
    pcm = (np.clip(mix, -1, 1).T * 32767).astype("<i2").tobytes()
    subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-f", "s16le", "-ar", str(SR), "-ac", "2", "-i", "-",
                    "-codec:a", "libmp3lame", "-b:a", "96k", "-metadata", f"title={titre}", "-metadata", "artist=Poids & Mesures (musique générée)", chemin],
                   input=pcm, check=True)

def main():
    a = [x for x in sys.argv[1:] if not x.startswith("--")]
    out = a[0]; os.makedirs(out, exist_ok=True)
    if "--une" in sys.argv:
        seed = int(sys.argv[sys.argv.index("--une") + 1]); mix, info = compose(seed)
        vers_mp3(mix, os.path.join(out, f"test-{seed}.mp3"), f"Test {seed}"); print(info); return
    nb = int(a[1]) if len(a) > 1 else 24
    dep = int(sys.argv[sys.argv.index("--depart") + 1]) if "--depart" in sys.argv else 0
    if "--depart" in sys.argv: a = [x for x in a if x != str(dep)] if False else a
    meta = []
    for k in range(nb):
        seed = 2000 + dep + k
        sty = ['chill', 'boombap', 'ambient', 'house'][(dep + k) % 4]
        mix, info = compose(seed, style=sty, minutes=3.4 if sty != 'ambient' else 4.2)
        fid = f"musique-{dep + k + 1:02d}"
        vers_mp3(mix, os.path.join(out, fid + ".mp3"), f"Musique {dep + k + 1:02d}")
        info.update(id=fid, fichier=fid + ".mp3"); meta.append(info); print(info, flush=True)
    if "--jingles" in sys.argv:
        for k in range(3):
            mix, info = jingle(77 + k, f"jingle-{k + 1}")
            vers_mp3(mix, os.path.join(out, f"jingle-{k + 1}.mp3"), f"Jingle {k + 1}")
            info.update(id=f"jingle-{k + 1}", fichier=f"jingle-{k + 1}.mp3"); meta.append(info)
    json.dump(meta, open(os.path.join(out, f"musiques-{dep}.json"), "w"), ensure_ascii=False, indent=1)

if __name__ == "__main__":
    main()
