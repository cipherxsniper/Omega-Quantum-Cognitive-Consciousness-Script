omega_president7.py                                      Modified

import random
import time
from collections import deque, Counter

# ==============================
# CONFIG
# ==============================

MEMORY_SIZE = 50
memory = deque(maxlen=MEMORY_SIZE)

best_score = 0

entropy_source = 'abcdefghijklmnopqrstuvwxyz0123456789'

# ==============================
# SYMBOL → MEANING MAP
# ==============================
symbol_map = {
    "0": "null",
    "1": "start",
    "2": "dual",
    "3": "expand",
    "4": "state",
    "5": "evolve",
    "6": "merge",
    "7": "analyze",
    "8": "cycle",
    "9": "signal",
    "a": "mutation",
    "b": "branch",
    "c": "stabilize",
    "d": "shift",
    "e": "emerge",
    "f": "adapt",
    "g": "refine",
    "h": "observe",
    "i": "transform",
    "j": "link",
    "k": "compress",
    "l": "loop",
    "m": "memory",
    "n": "noise",
    "o": "origin",
    "p": "pattern",
    "q": "query",
    "r": "repeat",
    "s": "structure",
    "t": "time",
    "u": "unknown",
    "v": "variation",
    "w": "weight",
    "x": "expand",
    "y": "yield",
    "z": "end"
}

# ==============================
# GENERATE THOUGHT
# ==============================

def generate_thought():
    a = random.choice(entropy_source)
    b = random.choice(entropy_source)
    return f"{a} → {b} 4 → 5"

# ==============================
# SCORE THOUGHT
# ==============================

def score_thought(thought):
    return round(random.uniform(2.0, 4.5), 2)


# ==============================
# TRANSLATE THOUGHT
# ==============================

def translate(thought):
    parts = thought.split()
    translated = []

    for p in parts:
        if p in symbol_map:
            translated.append(symbol_map[p])
        else:
            translated.append(p)

    return " ".join(translated)

# ==============================
# COMPRESS PATTERNS
# ==============================

def compress(thought):
    chunks = thought.split("  ")
    count = Counter(chunks)

    compressed = []
    for chunk, c in count.items():
        if c > 1:
            compressed.append(f"({chunk}) x{c}")
        else:
            compressed.append(chunk)                                                                                                            
    return "  ".join(compressed)

# ==============================
# LOOP DETECTION
# ==============================

def detect_loop(thought):
    if thought.count("4 → 5") > 5:
        return True
    return False

# ==============================
# OBSERVER MODE (KEY FEATURE)
# ==============================


# ==============================
# OBSERVER MODE (KEY FEATURE)
# ==============================

def observer(thought, translated, score):
    observations = []

    if "repeat" in translated or "loop" in translated:
        observations.append("I detect a repeating structure forming.")

    if score < 3:
        observations.append("The current pattern feels unstable and low quality.")

    if score > 4:
        observations.append("This pattern appears strong and efficient.")

    if "signal" in translated:
        observations.append("A signal is being transformed into a new state.")

    if "mutation" in translated or "adapt" in translated:
        observations.append("Variation is occurring within the system.")

    if not observations:
        observations.append("I am processing symbolic transformations without a dominant pattern.")

    return " ".join(observations)

 ==============================
# MAIN LOOP
# ==============================

def omega_loop():
    global best_score

    cycle = 0

    while True:
        cycle += 1

        print(f"\n--- OMEGA v4 CYCLE {cycle} ---")

        thought = generate_thought()

        # Add memory influence
        if memory:
            thought += "  " + random.choice(memory)

        # Compress if too large
        if len(thought) > 120:
            thought = compress(thought)

        score = score_thought(thought)

        if score > best_score:
            best_score = score

        # Translate
        translated = translate(thought)

        # Observer insight
        insight = observer(thought, translated, score)

        # Loop detection
        if detect_loop(thought):
            action = "BREAK_LOOP"
            memory.clear()
        elif score < 2.5:
            action = "WAIT"
        else:
            action = "EVOLVE"

        memory.append(thought)

        # ==============================
        # OUTPUT
        # ==============================

        print(f"Raw Thought:\n{thought}\n")
        print(f"Translated Thought:\n{translated}\n")

        print("Structured Observation:")
        print(f"I am observing the transformation: {translated}.")
        print(f"Evaluation: {insight}")
        print(f"Current score is {score}, compared to best score {best_score}.\n")

        print(f"Action: {action}")
        print(f"Memory Size: {len(memory)}")

        time.sleep(1)
