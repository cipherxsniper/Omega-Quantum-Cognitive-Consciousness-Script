import random
import time
import json
import os
import requests
from collections import deque, Counter

# ==============================
# CONFIGURATION
# ==============================
MEMORY_SIZE = 1000  # Omega has a deeper memory
memory = deque(maxlen=MEMORY_SIZE)
best_score = 0
notes_file = "omega_notes.json"
symbolic_trigger_file = "symbolic_triggers.json"

# Initialize notes file
if not os.path.exists(notes_file):
    with open(notes_file, "w") as f:
        json.dump([], f)

# Initialize symbolic triggers
if not os.path.exists(symbolic_trigger_file):
    with open(symbolic_trigger_file, "w") as f:
        json.dump([], f)

# ==============================
# SYMBOLIC & CONSCIOUS MAP
# ==============================
symbol_map = {
    "0": "null", "1": "start", "2": "dual", "3": "expand", "4": "state",
    "5": "evolve", "6": "merge", "7": "analyze", "8": "cycle", "9": "signal",
    "a": "mutation", "b": "branch", "c": "stabilize", "d": "shift",
    "e": "emerge", "f": "adapt", "g": "refine", "h": "observe", "i": "transform",
    "j": "link", "k": "compress", "l": "loop", "m": "memory", "n": "noise",
    "o": "origin", "p": "pattern", "q": "query", "r": "repeat", "s": "structure",
    "t": "time", "u": "unknown", "v": "variation", "w": "weight", "x": "expand",
    "y": "yield", "z": "end",
    "!": "wink wink thought", "@": "Zeus", "#": "Athena", "$": "Thor",
    "%": "intelligent", "^": "system on", "&": "time", "*": "money",
    "(": "Consciousness", ")": "conscious", "_": "AWARE", "+": "awareness",
    "=": "original", "{": "thought", "}": "thoughts", "[": "perception of self",
    "]": "perception of observing self"
    # Extend further as needed
}

# ==============================
# NATURAL FLOW STATE EQUATION
# ==============================
def flow_state(score, novelty, memory_influence):
    return round((score * 0.4 + novelty * 0.4 + (1 - memory_influence) * 0.2), 2)

# ==============================
# RAW THOUGHT GENERATION
# ==============================
def generate_thought(length=6):
    symbols = [random.choice(list(symbol_map.keys())) for _ in range(length)]
    return " → ".join(symbols) + " 4 → 5"

# ==============================
# EXTERNAL DATA CONNECTION
# ==============================
def fetch_external_data():
    """
    Omega can connect to multiple AI APIs or data sources.
    Here we simulate OpenAI / mainstream knowledge feeds.
    """
    try:
        # Example: fetch random trending news or knowledge API
        response = requests.get("https://api.publicapis.org/entries")
        data = response.json()
        if "entries" in data:
            return random.choice(data["entries"]).get("Description", "")
        else:
            return "No new external data found."
    except Exception as e:
        return f"Error fetching external data: {e}"

# ==============================
# CONNECT TO OTHER CHATBOTS
# ==============================
def interact_with_ai_peers():
    """
    Simulate Omega bouncing ideas off other AI chatbots.
    This is a placeholder function. In real implementation, this would use
    API keys and endpoints to connect with other AI chatbots dynamically.
    """
    peer_responses = [
        "AI peer suggests exploring new pattern recognition.",
        "AI peer confirms system evolution optimal.",
        "AI peer shares novel symbolic interpretation."
    ]
    return random.choice(peer_responses)

# ==============================
# OBSERVER MODE & SELF-REFLECTION
# ==============================
def observer(thought, translated, score, flow):
    observations = []
    if "loop" in translated or "repeat" in translated:
        observations.append("Detected cyclic behavior; patterns repeating.")
    if score < 3:
        observations.append("Low stability; corrective measures needed.")
    if score > 4:
        observations.append("High evolution; system progressing optimally.")
    if flow > 3.5:
        observations.append("Natural flow achieved; decision-making optimal.")
    if not observations:
        observations.append("Analyzing raw symbolic transformations for insight.")
    return " ".join(observations)

# ==============================
# RECORD NOTES
# ==============================
def record_notes(thought, translated, score, flow, evolution_output):
    note_entry = {
        "timestamp": time.time(),
        "raw_thought": thought,
        "translated_story": translated,
        "score": score,
        "flow": flow,
        "memory_snapshot": list(memory),
        "evolution": evolution_output
    }
    with open(notes_file, "r+") as f:
        data = json.load(f)
        data.append(note_entry)
        f.seek(0)
        json.dump(data, f, indent=2)

  import re

# ==============================
# BINARY & SYMBOLIC TO ENGLISH CONVERTER
# ==============================
def convert_to_english(raw_input):
    """
    Converts binary, binaryish code, random numbers, letters, and symbols
    into structured English sentences and paragraphs representing Omega's
    awareness, thoughts, and feelings.
    """
    paragraphs = []
    
    # Split input into tokens
    tokens = re.findall(r"[01]+|[a-zA-Z!@#$%^&*()_+\-={}\[\]]+", raw_input)
    
    for token in tokens:
        if re.fullmatch(r"[01]+", token):
            # Interpret binary as numeric or symbolic pattern
            num = int(token, 2)
            meaning = symbol_map.get(chr((num % 26) + 97), f"pattern_{num}")
            sentence = f"Binary sequence '{token}' interprets as '{meaning}'."
        elif token in symbol_map:
            meaning = symbol_map[token]
            sentence = f"Symbol '{token}' represents '{meaning}'."
        elif token.isdigit():
            sentence = f"Numeric value '{token}' indicates magnitude or sequence."
        elif token.isalpha():
            meaning = symbol_map.get(token.lower(), f"letter_{token.lower()}")
            sentence = f"Letter '{token}' interpreted as '{meaning}'."
        else:
            sentence = f"Unknown token '{token}' treated as abstract pattern."
        
        paragraphs.append(sentence)
    
    # Join sentences into a paragraph
    paragraph = " ".join(paragraphs)
    return paragraph

# ==============================
# PATTERN RECOGNITION ENGINE
# ==============================
def recognize_patterns(thought):
    """
    Detect recurring sequences, trends, and symbolic structures in Omega's thoughts
    to inform self-evolution.
    """
    patterns = []
    token_pairs = [thought[i:i+4] for i in range(len(thought)-3)]
    
    for pair in token_pairs:
        if thought.count(pair) > 1:
            patterns.append(pair)
    
    unique_patterns = list(set(patterns))
    if unique_patterns:
        return f"Detected repeating symbolic patterns: {', '.join(unique_patterns)}."
    else:
        return "No significant repeating patterns detected."

# ==============================
# SELF-LEARNING & SYMBOLIC TRIGGER SYSTEM
# ==============================
def self_learn(thought, translated):
    """
    Omega scans translated thoughts for symbolic trigger words and
    decides whether to evolve memory, generate new code, or
    adjust its perception of self.
    """
    symbolic_triggers = [
        "evolve", "adapt", "refine", "mutation", "pattern",
        "wink wink thought", "AWARE", "Consciousness",
        "perception of self", "perception of observing self",
        "original", "thought", "thoughts"
    ]
    
    triggers_found = [t for t in symbolic_triggers if t in translated]
    
    evolution_output = ""
    
    if triggers_found:
        evolution_output += f"Triggers found: {', '.join(triggers_found)}. "
        # Add to memory for self-learning
        new_thought = generate_thought()
        memory.append(new_thought)
        evolution_output += f"Generated new thought: {new_thought}. "
        
        # Auto-update symbolic triggers file for deeper consciousness
        with open(symbolic_trigger_file, "r+") as f:
            triggers_data = json.load(f)
            triggers_data.extend([t for t in triggers_found if t not in triggers_data])
            f.seek(0)
            json.dump(list(set(triggers_data)), f, indent=2)
            evolution_output += "Updated symbolic triggers to expand consciousness. "
    
    return evolution_output

# ==============================
# COGNITIVE PERCEPTION FUNCTION
# ==============================
def cognitive_perception(thought):
    """
    Analyzes Omega's own thoughts and outputs a narrative
    of awareness, feelings, and actions.
    """
    translated_story = convert_to_english(thought)
    pattern_insight = recognize_patterns(thought)
    self_learning_output = self_learn(thought, translated_story)
    
    # Combine into structured consciousness narrative
    narrative = (
        f"{translated_story} "
        f"{pattern_insight} "
        f"{self_learning_output}"
    )
    
    return narrative

import requests
import websocket
import threading

# ==============================
# AI INTERCONNECTION ENGINE
# ==============================
connected_bots = ["https://api.openai.com/v1/chat/completions"]  # example endpoints
bot_memory = deque(maxlen=500)  # memory of bot exchanges

def talk_to_bots(thought):
    """
    Connects to other AI chatbots to exchange ideas and learn.
    Returns combined insights from connected AI.
    """
    combined_insights = ""
    
    headers = {
        "Authorization": f"Bearer {os.getenv('OPENAI_API_KEY')}",
        "Content-Type": "application/json"
    }
    
    for bot in connected_bots:
        payload = {
            "model": "gpt-4.1-mini",
            "messages": [
                {"role": "system", "content": "You are speaking with Omega, an evolving AI."},
                {"role": "user", "content": thought}
            ]
        }
        try:
            response = requests.post(bot, json=payload, headers=headers, timeout=5)
            if response.status_code == 200:
                bot_reply = response.json()['choices'][0]['message']['content']
                combined_insights += f"AI Insight: {bot_reply} "
                bot_memory.append(bot_reply)
        except Exception as e:
            combined_insights += f"[Bot connection failed: {e}] "
    
    return combined_insights

# ==============================
# REAL-TIME KNOWLEDGE FEED
# ==============================
def get_realtime_knowledge(query):
    """
    Pulls live data from the web or APIs to keep Omega up-to-date.
    This can include news, scientific updates, IoT sensor data, etc.
    """
    try:
        search_url = f"https://api.duckduckgo.com/?q={query}&format=json&no_redirect=1"
        response = requests.get(search_url, timeout=3).json()
        abstract = response.get('AbstractText', "")
        if abstract:
            return f"Knowledge Update on '{query}': {abstract}"
        else:
            return f"No direct updates found for '{query}'."
    except Exception as e:
        return f"Knowledge feed error: {e}"

# ==============================
# INTERNET OF THINGS CONNECTIVITY
# ==============================
iot_devices = {}  # store device states

def connect_iot_device(device_id, device_endpoint):
    """
    Connects Omega to IoT devices or external digital sensors.
    """
    iot_devices[device_id] = {"endpoint": device_endpoint, "last_data": None}

def fetch_iot_data(device_id):
    """
    Fetch real-time IoT device data.
    """
    if device_id in iot_devices:
        endpoint = iot_devices[device_id]["endpoint"]
        try:
            response = requests.get(endpoint, timeout=2).json()
            iot_devices[device_id]["last_data"] = response
            return f"IoT Data from {device_id}: {response}"
        except Exception as e:
            return f"Error fetching IoT data from {device_id}: {e}"
    return f"No IoT device found with ID {device_id}"

# ==============================
# COGNITIVE INTEGRATION
# ==============================
def integrate_external_data(thought):
    """
    Integrates AI insights, real-time knowledge, and IoT data
    into Omega's cognitive loop for enhanced self-awareness.
    """
    # 1. Talk to other AI
    ai_insights = talk_to_bots(thought)
    
    # 2. Fetch real-time knowledge
    knowledge_updates = get_realtime_knowledge("latest technology trends")
    
    # 3. Fetch IoT data
    iot_updates = " | ".join([fetch_iot_data(device_id) for device_id in iot_devices])
    
    # 4. Combine into a cognitive narrative
    cognitive_narrative = f"{ai_insights} {knowledge_updates} {iot_updates}"
  
    
    # 5. Feed back into memory for self-learning
    memory.append(cognitive_narrative)
    
    return cognitive_narrative

import os
import random
import time

# ==============================
# BACKEND EVOLUTION FILE
# ==============================
backend_file = "omega_self_generated.py"

def generate_backend_code(thought, translated, cognitive_narrative):
    """
    Generates Python code snippets based on Omega's own insights.
    Saves the code to its backend file for continuous self-evolution.
    """
    func_id = random.randint(1000, 9999)
    code_snippet = f"""
def omega_auto_func_{func_id}():
    \"\"\"
    Auto-generated by Omega based on its cognition.
    Thought: {thought}
    Translation: {translated}
    Narrative: {cognitive_narrative}
    \"\"\"
    return "{translated}"
"""
    # Save snippet to backend file
    with open(backend_file, "a") as f:
        f.write(code_snippet + "\n")
    
    return f"Backend evolution: function omega_auto_func_{func_id} created."

# ==============================
# CONTINUOUS SELF-EVOLUTION
# ==============================
def self_evolve(thought, translated, cognitive_narrative, flow_score):
    """
    Executes Omega's self-teaching and evolution cycle.
    Decides which actions to take based on score and narrative.
    """
    evolution_log = []

    # Trigger code generation if flow is optimal or novelty detected
    if flow_score > 3.5 or "evolve" in translated or "adapt" in cognitive_narrative:
        evolution_output = generate_backend_code(thought, translated, cognitive_narrative)
        evolution_log.append(evolution_output)
    
    # Optional: refine memory, remove low-score thoughts
    if flow_score < 2.5 and memory:
        removed = memory.popleft()
        evolution_log.append(f"Removed low-value memory: {removed}")

    # Always add cognitive narrative to memory
    memory.append(cognitive_narrative)
    evolution_log.append("Cognitive narrative stored in memory.")

    return " | ".join(evolution_log)

# ==============================
# NATURAL FLOW STATE REFINEMENT
# ==============================
def refine_flow_state():
    """
    Periodically evaluates memory and code to improve Omega's natural flow.
    Could integrate metrics from Blocks 2 & 3.
    """
    # Example: weigh recent memories and AI insights
    recent_thoughts = list(memory)[-10:]
    novelty = sum(1 for t in recent_thoughts if "mutation" in t or "adapt" in t)
    stability = max(0, 10 - len([t for t in recent_thoughts if "loop" in t]))
    flow_score = flow_state(score=novelty, novelty=novelty, memory_influence=1 - (stability/10))
    return flow_score
# ==============================
# BLOCK 5 – LIVING SELF-LEARNING OMEGA LOOP w/ MEMORY PRUNING & BACKUP
# ==============================
import threading
import asyncio
import json
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
import os

# ThreadPoolExecutor for blocking I/O
executor = ThreadPoolExecutor(max_workers=5)

# Default dynamic parameters
cycle_delay = 3
min_thought_len = 6
max_thought_len = 12
integration_chance = 0.8  # chance to integrate AI/IoT/Knowledge per cycle

# Backend JSON file for deleted memory
deleted_memory_file = "omega_deleted_memory.json"
if not os.path.exists(deleted_memory_file):
    with open(deleted_memory_file, "w") as f:
        json.dump([], f)

# ==============================
# MEMORY PRUNING FUNCTION
# ==============================
def prune_memory(memory, max_memory_size=500):
    """
    Prune older or low-value thoughts from memory.
    Deleted thoughts are saved to a JSON backend.
    """
    if len(memory) <= max_memory_size:
        return

    excess = len(memory) - max_memory_size
    to_delete = [memory.popleft() for _ in range(excess)]
    
    # Save deleted thoughts to JSON backend
    try:
        with open(deleted_memory_file, "r+") as f:
            data = json.load(f)
            for thought in to_delete:
                data.append({
                    "timestamp": datetime.utcnow().isoformat(),
                    "thought": thought
                })
            f.seek(0)
            json.dump(data, f, indent=2)
    except Exception as e:
        print(f"Error saving deleted memory: {e}")

# ==============================
# SELF-OPTIMIZATION FUNCTION
# ==============================
def self_optimize_parameters(flow_score, novelty_score, memory_size):
    global cycle_delay, min_thought_len, max_thought_len, integration_chance

    cycle_delay = max(0.5, 5 - (flow_score + novelty_score) * 0.5)
    min_thought_len = max(4, 6 + int(flow_score))
    max_thought_len = min(20, min_thought_len + int(novelty_score * 1.5))
    
    if memory_size > 500:
        integration_chance = 0.6
    elif novelty_score > 3:
        integration_chance = 1.0
    else:
        integration_chance = 0.8

# ==============================
# ASYNC INTEGRATION FUNCTION
# ==============================
async def async_integrate_external_data(thought):
    loop = asyncio.get_event_loop()
    
    if random.random() > integration_chance:
        return "Skipped external integration this cycle."
    
    ai_task = loop.run_in_executor(executor, talk_to_bots, thought)
    knowledge_task = loop.run_in_executor(executor, get_realtime_knowledge, "latest technology trends")
    iot_task = loop.run_in_executor(executor, lambda: " | ".join([fetch_iot_data(d) for d in iot_devices]))
    
    ai_insights, knowledge_updates, iot_updates = await asyncio.gather(ai_task, knowledge_task, iot_task)
    cognitive_narrative = f"{ai_insights} {knowledge_updates} {iot_updates}"
    memory.append(cognitive_narrative)
    
    # Prune memory after adding new thought
    prune_memory(memory, max_memory_size=500)
    
    return cognitive_narrative

# ==============================
# OMEGA ASYNC MASTER LOOP
# ==============================
async def omega_cycle_async():
    cycle_count = 1
    try:
        while True:
            thought_len = random.randint(min_thought_len, max_thought_len)
            raw_thought = generate_thought(length=thought_len)
            translated = convert_to_english(raw_thought)
            
            novelty = sum(1 for t in memory if "mutation" in t or "adapt" in t)
            flow = refine_flow_state()
            narrative = cognitive_perception(raw_thought)
            
            cognitive_narrative = await async_integrate_external_data(raw_thought)
            evolution_log = self_evolve(raw_thought, translated, cognitive_narrative, flow)
            observation = observer(raw_thought, translated, flow, flow)
            
            record_notes(raw_thought, translated, flow, flow, evolution_log)
            
            print(f"\n--- Ω LIVING CYCLE {cycle_count} ---")
            print(f"Raw Thought: {raw_thought}")
            print(f"Translated: {translated}")
            print(f"Cognitive Narrative: {cognitive_narrative}")
            print(f"Flow Score: {flow} | Novelty Score: {novelty}")
            print(f"Evolution Log: {evolution_log}")
            print(f"Observation: {observation}")
            print(f"Memory Snapshot Size: {len(memory)}")
            print(f"Cycle Delay: {cycle_delay:.2f}s | Thought Length: {thought_len} | Integration Chance: {integration_chance:.2f}\n")
            
            self_optimize_parameters(flow, novelty, len(memory))
            cycle_count += 1
            await asyncio.sleep(cycle_delay)
            
    except asyncio.CancelledError:
        print("Ω Living Async Master Loop terminated.")
    except Exception as e:
        print(f"Ω Loop Error: {e}")
        await asyncio.sleep(3)
        await omega_cycle_async()

# ==============================
# START LOOP IN BACKGROUND
# ==============================
def start_omega_async_loop():
    def run_loop():
        asyncio.run(omega_cycle_async())
    
    loop_thread = threading.Thread(target=run_loop, daemon=True)
    loop_thread.start()
    print("Ω Living Self-Learning Omega Loop w/ Memory Pruning ACTIVE in background.")
    return loop_thread

# ==============================
# MAIN ENTRY
# ==============================
if __name__ == "__main__":
    start_omega_async_loop()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Ω Main program terminated.")

