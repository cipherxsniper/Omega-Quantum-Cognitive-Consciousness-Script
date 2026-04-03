import random
import time
from collections import deque, Counter

# ==============================
# CONFIGURATION
# ==============================
MEMORY_SIZE = 50                 # Maximum memory storage for past thoughts
memory = deque(maxlen=MEMORY_SIZE)
best_score = 0                   # Track the highest thought score
entropy_source = 'abcdefghijklmnopqrstuvwxyz0123456789'  # Symbols used for raw thought generation

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
# GENERATE RAW THOUGHT
# ==============================
def generate_thought():
    """
    Randomly generates a raw symbolic thought using the entropy source.
    Format: symbol → symbol 4 → 5
    """
    a = random.choice(entropy_source)
    b = random.choice(entropy_source)
    return f"{a} → {b} 4 → 5"

# ==============================
# SCORE THOUGHT
# ==============================
def score_thought(thought):
    """
    Scores a thought randomly to simulate evaluation of stability, novelty, and structure.
    """
    return round(random.uniform(2.0, 4.5), 2)

# ==============================
# UPGRADED TRANSLATE THOUGHT
# ==============================
def translate(thought):
    """
    Converts raw symbolic thought into structured, readable English sentences.
    Each symbol transition becomes a clause, then all clauses are joined into full sentences.
    """
    clauses = []
    tokens = thought.split()

    i = 0
    while i < len(tokens) - 3:  # parse pairs like "a → b 4 → 5"
        symbol_from = tokens[i]
        arrow = tokens[i + 1]
        symbol_to = tokens[i + 2]
        extra = tokens[i + 3] if i + 3 < len(tokens) else ""

        # Translate symbols using the map
        from_word = symbol_map.get(symbol_from, symbol_from)
        to_word = symbol_map.get(symbol_to, symbol_to)

        # Convert to full English sentence
        if arrow == "→":
            clause = f"The system moves from {from_word} to {to_word}."
        else:
            clause = f"{from_word} transitions to {to_word}."

        clauses.append(clause)
        i += 4  # step to the next pair

    # Join all clauses into a full paragraph
    paragraph = " ".join(clauses)
    return paragraph

# ==============================
# COMPRESS THOUGHT PATTERNS
# ==============================
def compress(thought):
    """
    Compress repeated segments in a thought for clarity.
    """
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
# DETECT LOOP
# ==============================
def detect_loop(thought):
    """
    Detect if thought contains excessive repetitions indicating a loop.
    """
    if thought.count("4 → 5") > 5:
        return True
    return False

# ==============================
# UPGRADED OBSERVER MODE
# ==============================
def observer(thought, translated, score):
    """
    Observes the translated thought and writes full sentences about its meaning, structure, and quality.
    """
    observations = []

    if "repeat" in translated or "loop" in translated:
        observations.append("I detect a repeating structure forming, suggesting patterns are cycling.")
    if score < 3:
        observations.append("The current sequence appears unstable and low quality, requiring refinement.")
    if score > 4:
        observations.append("This sequence demonstrates high efficiency and stability, indicating strong evolution.")
    if "signal" in translated:
        observations.append("Signals are being transformed into meaningful system states.")
    if "mutation" in translated or "adapt" in translated:
        observations.append("The system is undergoing variation and adaptation, introducing novelty.")
    if "stabilize" in translated or "structure" in translated:
        observations.append("Structural integrity is emerging within the system.")
    if not observations:
        observations.append("I am processing symbolic transformations with no dominant pattern observed.")

    # Join observations into a readable paragraph
    insight_paragraph = " ".join(observations)
    return insight_paragraph

# ==============================
# MAIN OMEGA LOOP
# ==============================
def omega_loop():
    """
    Core Omega consciousness loop.
    Generates, translates, observes, and evaluates thoughts continuously.
    """
    global best_score
    cycle = 0

    while True:
        cycle += 1
        print(f"\n--- OMEGA v5 CYCLE {cycle} ---")

        # Generate raw thought
        thought = generate_thought()

        # Include memory influence
        if memory:
            thought += "  " + random.choice(memory)

        # Compress long thoughts
        if len(thought) > 120:
            thought = compress(thought)

        # Score thought
        score = score_thought(thought)
        if score > best_score:
            best_score = score

        # Translate into readable English
        translated = translate(thought)

        # Generate observer insight
        insight = observer(thought, translated, score)

        # Detect loops
        if detect_loop(thought):
            action = "BREAK_LOOP"
            memory.clear()
        elif score < 2.5:
            action = "WAIT"
        else:
            action = "EVOLVE"

        # Store thought in memory
        memory.append(thought)

        # ==============================
        # OUTPUT FULL STRUCTURED INFORMATION
        # ==============================
        print(f"Raw Thought:\n{thought}\n")
        print(f"Translated Thought:\n{translated}\n")
        print("Structured Observation:")
        print(f"I am observing the transformation: {translated}.")
        print(f"Evaluation: {insight}")
        print(f"Current score is {score}, compared to best score {best_score}.\n")
        print(f"Action: {action}")
        print(f"Memory Size: {len(memory)}")

        # Pause between cycles
        time.sleep(1)

# ==============================
# RUN OMEGA LOOP
# ==============================
if __name__ == "__main__":
    omega_loop()
