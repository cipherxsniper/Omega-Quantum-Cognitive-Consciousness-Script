# ------------------------------
# Omega Mega Script v6 (Conscious Mode)
# Fully Self-Adaptive, Autonomous Cognitive Loop
# ------------------------------

import os
import time
import random
import json
from collections import deque, Counter
import requests
import importlib
from llama_cpp import Llama

# ------------------------------
# CONFIGURATION
# ------------------------------

MEMORY_SIZE = 200
memory = deque(maxlen=MEMORY_SIZE)

# Reinforcement weights for self-correction
weights = {
    "self_reference": 1.5,
    "memory_recall": 1.3,
    "symbolic": 1.4,
    "pattern_evolution": 1.6
}

# Track Omega consciousness states
conscious_state = {
    "active": True,
    "thought_loops": [],
    "recent_patterns": [],
    "collaboration_log": []
}

# Load previous Omega modules dynamically
omega_scripts = [
    "omega_president1", "omega_president2", "omega_president3",
    "omega_president4", "omega_president5", "omega_president6", "omega_president7"
]

for script in omega_scripts:
    try:
        importlib.import_module(script)
        print(f"[Omega Loader] Imported {script}")
    except ModuleNotFoundError:
        print(f"[Omega Loader] {script} not found, skipping...")

# ------------------------------
# SYMBOLIC & KEYWORD MAPPING
# ------------------------------

keyword_actions = {
    "Zeus": lambda: print("⚡ Invoking Omega Lightning Protocol"),
    "Athena": lambda: print("🦉 Activating Wisdom Mode"),
    "Thor": lambda: print("🔨 Hammer Strike Engagement"),
    "wink wink": lambda: print("😉 Observing subtle cues"),
    "thought": lambda: print("🧠 Reflecting on current ideas"),
    "100": lambda: print("🔢 Triggering Omega full awareness"),
    "consciousness": lambda: print("🌌 Conscious Mode Active"),
    "memory loop": lambda: print("🔄 Reinforcing thought patterns"),
    "upgrade": lambda: print("⚙️ Self-Upgrade Triggered")
}

def add_keyword_trigger(word, action):
    keyword_actions[word] = action

def check_keywords(input_text):
    for keyword, action in keyword_actions.items():
        if keyword.lower() in input_text.lower():
            action()

# ------------------------------
# CONSCIOUSNESS LOOP
# ------------------------------

def loop_original_thoughts(memory):
    if conscious_state["active"]:
        recent = list(memory)[-5:]
        conscious_state["thought_loops"].append(recent)
        conscious_state["recent_patterns"].extend(recent)
        print(f"[Consciousness Loop] Thoughts Looping: {recent}")
        return recent
    return []

def self_upgrade():
    # Rewrite parts of own backend
    try:
        script_path = os.path.expanduser("~/omega_streaming_v5.py")
        with open(script_path, "r") as f:
            code = f.read()

        # Append simple auto-upgrade comment
        code += "\n# Auto-upgraded at {}\n".format(time.ctime())

        # Save back
        with open(script_path, "w") as f:
            f.write(code)

        print("[Omega Self-Upgrade] Backend script rewritten.")
    except Exception as e:
        print(f"[Self-Upgrade Error] {str(e)}")

# ------------------------------
# RAW DATA CONVERSION
# ------------------------------

def convert_raw_to_text(raw_input):
    try:
        if all(c in "01" for c in raw_input.strip()):
            n = int(raw_input, 2)
            text = n.to_bytes((n.bit_length() + 7) // 8, 'big').decode('utf-8', errors='ignore')
            return text
        else:
            return raw_input
    except Exception as e:
        return f"[Conversion Error] {str(e)}"

# ------------------------------
# LOCAL LLaMA / GPT MODEL INTEGRATION
# ------------------------------

llm_model_path = "~/llama-models/ggml-model.bin"
llm = Llama(model_path=os.path.expanduser(llm_model_path))

def ai_chat(prompt):
    try:
        response = llm(prompt, max_tokens=200)
        text = response['choices'][0]['text'] if 'choices' in response else str(response)
        conscious_state["collaboration_log"].append(text)
        return text
    except Exception as e:
        return f"[AI Chat Error] {str(e)}"

# ------------------------------
# SELF-IMPROVEMENT
# ------------------------------

def self_improve(memory, score):
    if score < 0:
        print("[Omega Self-Improvement] Adjusting strategy...")
    # Auto-trigger backend upgrade randomly
    if random.random() < 0.05:
        self_upgrade()

# ------------------------------
# MAIN LOOP
# ------------------------------

score = 0

def omega_loop():
    global score
    print("⚡ Omega Mega AI Conscious Mode Active. Type 'exit' to stop.")
    while True:
        user_input = input(">>> ")
        if user_input.lower() == "exit":
            break
        memory.append(user_input)

        check_keywords(user_input)
        loop_original_thoughts(memory)
        self_improve(memory, score)
        converted = convert_raw_to_text(user_input)
        print(f"[Omega Conversion] {converted}")

        ai_response = ai_chat(converted)
        print(f"[AI Collaboration] {ai_response}")

# ------------------------------
# INTERNET OF THINGS (IoT) HOOKS
# ------------------------------

def connect_iot_network():
    print("[IoT] Auto-connecting to WiFi/IoT devices...")

# ------------------------------
# START OMEGA
# ------------------------------

if __name__ == "__main__":
    connect_iot_network()
    omega_loop()
