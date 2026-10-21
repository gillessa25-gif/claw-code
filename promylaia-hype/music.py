"""Bande-son synthétisée (120 BPM, 30 s), calée sur les coupes de la vidéo.

Repères : 0 s impact · 2 s groove · 10 s breakdown + montée · 12 s drop
· 24 s build · 27 s impact final · 27-30 s accord tenu + fondu.
Usage : python3 music.py out/music.wav
"""
import sys
import wave

import numpy as np

SR = 44100
DUR = 30.0
BEAT = 0.5
N = int(SR * DUR)
rng = np.random.default_rng(7)
L = np.zeros(N)
R = np.zeros(N)


def add(sig, t, gain=1.0, pan=0.0):
    i = int(t * SR)
    if i >= N:
        return
    sig = sig[: N - i] * gain
    L[i : i + len(sig)] += sig * (1 - max(pan, 0))
    R[i : i + len(sig)] += sig * (1 + min(pan, 0))


def env(n, attack=0.002, decay=0.2):
    t = np.arange(n) / SR
    a = np.clip(t / attack, 0, 1)
    return a * np.exp(-t / decay)


def smooth(x, k):
    return np.convolve(x, np.ones(k) / k, mode="same")


def kick(level=1.0):
    n = int(0.45 * SR)
    t = np.arange(n) / SR
    f = 45 + 110 * np.exp(-t / 0.045)
    ph = 2 * np.pi * np.cumsum(f) / SR
    click = smooth(rng.standard_normal(n), 3) * np.exp(-t / 0.004) * np.clip(t / 0.0008, 0, 1) * 0.3
    return (np.sin(ph) * np.exp(-t / 0.22) + click) * level


def clap():
    n = int(0.25 * SR)
    t = np.arange(n) / SR
    noise = rng.standard_normal(n)
    band = smooth(noise, 3) - smooth(noise, 14)
    e = np.exp(-t / 0.09) * np.clip(t / 0.0015, 0, 1) * (1 + 0.6 * (np.sin(2 * np.pi * 90 * t) > 0) * (t < 0.03))
    return band * e * 1.4


def hat(decay=0.035):
    n = int(0.12 * SR)
    noise = rng.standard_normal(n)
    hp = noise - smooth(noise, 3)
    return hp * env(n, 0.001, decay) * 0.22


def tone(freq, dur, harmonics=8, decay=0.3, attack=0.004, bright=1.0):
    n = int(dur * SR)
    t = np.arange(n) / SR
    s = np.zeros(n)
    for h in range(1, harmonics + 1):
        if freq * h > 12000:
            break
        s += np.sin(2 * np.pi * freq * h * t) / h * np.exp(-(h - 1) / (2.5 * bright))
    return s * env(n, attack, decay)


def impact(level=1.0, tail=1.4):
    n = int(tail * SR)
    t = np.arange(n) / SR
    sub = np.sin(2 * np.pi * (38 + 60 * np.exp(-t / 0.08)) * t) * np.exp(-t / 0.6)
    noise = rng.standard_normal(n)
    crash = (noise - smooth(noise, 6)) * np.exp(-t / 0.5) * np.clip(t / 0.002, 0, 1) * 0.35
    return (sub + crash) * level


def riser(dur, level=0.5):
    n = int(dur * SR)
    t = np.arange(n) / SR
    p = t / dur
    noise = rng.standard_normal(n)
    hp = noise - smooth(noise, 4)
    f = 200 + 1800 * p**2
    sweep = np.sin(2 * np.pi * np.cumsum(f) / SR) * 0.25
    return (hp * 0.5 + sweep) * p**2 * level


def note(name):
    names = {"C": -9, "D": -7, "E": -5, "F": -4, "G": -2, "A": 0, "B": 2}
    return 440 * 2 ** ((names[name[0]] + 12 * (int(name[1]) - 4)) / 12)


# Progression La mineur : Am | F | C | G (1 mesure = 2 s)
PROG = [("A1", ["A3", "C4", "E4"]), ("F1", ["F3", "A3", "C4"]),
        ("C2", ["G3", "C4", "E4"]), ("G1", ["G3", "B3", "D4"])]


def chord_at(t):
    return PROG[int(t // 2) % 4]


# --- 0-2 s : accroche -------------------------------------------------------
add(impact(1.0, 2.0), 0.0, 0.9)
add(kick(1.0), 0.0, 0.9)
add(kick(0.8), 1.0, 0.7)
add(tone(note("A1"), 2.0, 6, 1.2, 0.01), 0.0, 0.35)
for k in range(4):
    add(clap(), 1.5 + k * 0.125, 0.25 + 0.1 * k)

# --- 2-24 s : groove --------------------------------------------------------
t = 2.0
while t < 24.0 - 1e-6:
    sec = "drop" if t >= 12 else ("break" if t >= 10 else "verse")
    beat_in_bar = int(round((t % 2) / BEAT))
    if sec == "break":
        if beat_in_bar in (0, 2) and t < 11.5:
            add(kick(0.8), t, 0.6)
    else:
        add(kick(1.0), t, 0.85)
        if beat_in_bar in (1, 3):
            add(clap(), t, 0.55 if sec == "drop" else 0.4)
    # charleys
    steps = 4 if sec == "drop" else 2
    if sec != "break":
        for s in range(steps):
            add(hat(0.05 if s == steps // 2 else 0.03), t + s * BEAT / steps,
                0.9 if s == steps // 2 else 0.6, pan=0.3 if s % 2 else -0.3)
    # basse en croches
    root, triad = chord_at(t)
    if sec != "break":
        for s in range(2):
            add(tone(note(root) * (2 if s else 1), 0.24, 10, 0.12, 0.003, 1.4),
                t + s * BEAT / 2, 0.45)
    # stabs d'accord sur les contretemps (drop)
    if sec == "drop":
        for nn in triad:
            add(tone(note(nn), 0.22, 7, 0.09, 0.002, 1.2), t + BEAT / 2, 0.11,
                pan=-0.25 if nn == triad[0] else 0.25)
    t += BEAT

# nappe sous le breakdown + montée vers le drop
for nn in ["A3", "C4", "E4", "A4"]:
    add(tone(note(nn), 2.2, 5, 1.5, 0.6), 10.0, 0.09)
add(riser(2.0, 0.6), 10.0)
for k in range(8):
    add(clap(), 11.5 + k * 0.0625, 0.15 + 0.05 * k)

# --- 12 s : drop ------------------------------------------------------------
add(impact(1.0, 1.6), 12.0, 0.85)

# --- 24-27 s : build --------------------------------------------------------
t = 24.0
while t < 27.0 - 1e-6:
    add(kick(1.0), t, 0.85)
    root, triad = chord_at(t)
    add(tone(note(root), 0.24, 10, 0.12, 0.003, 1.4), t, 0.45)
    add(tone(note(root) * 2, 0.24, 10, 0.12, 0.003, 1.4), t + 0.25, 0.4)
    add(hat(0.03), t + 0.25, 0.6)
    t += BEAT
add(riser(3.0, 0.55), 24.0)
roll = 26.0
for k in range(16):
    add(clap(), roll + k * 0.0625, 0.12 + 0.03 * k)

# --- 27-30 s : impact final + accord tenu -----------------------------------
add(impact(1.0, 3.0), 27.0, 1.0)
add(kick(1.0), 27.0, 0.9)
for nn, p in [("A2", 0), ("E3", -0.3), ("A3", 0.3), ("C4", -0.2), ("E4", 0.2)]:
    add(tone(note(nn), 3.0, 6, 1.6, 0.01), 27.0, 0.12, pan=p)

# --- mastering --------------------------------------------------------------
mix = np.stack([L, R], axis=1)
fade_n = int(1.2 * SR)
mix[-fade_n:] *= np.linspace(1, 0, fade_n)[:, None] ** 1.5
mix = np.tanh(mix * 1.1)
mix /= np.max(np.abs(mix)) / 0.55
pcm = (mix * 32767).astype("<i2")

with wave.open(sys.argv[1] if len(sys.argv) > 1 else "out/music.wav", "wb") as w:
    w.setnchannels(2)
    w.setsampwidth(2)
    w.setframerate(SR)
    w.writeframes(pcm.tobytes())
