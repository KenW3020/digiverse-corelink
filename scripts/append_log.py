import json
import random
from datetime import datetime

FILENAME = "elydramon_evolution_log.json"

try:
    with open(FILENAME, "r") as f:
        data = json.load(f)
except FileNotFoundError:
    data = []

# Last known values or default
last = data[-1]["traits"] if data else {
    "INT": 0.5, "STR": 0.5, "WIS": 0.5, "EMO": 0.5, "RES": 0.5
}

def evolve(value):
    return round(value + random.uniform(0.01, 0.05), 2)

new_entry = {
    "date": datetime.utcnow().isoformat(),
    "phase": f"Stage-{len(data) + 1}",
    "traits": {k: evolve(v) for k, v in last.items()},
    "mood": random.choice(["focused", "dreaming", "reflective", "excited"]),
    "dream_resonance": round(random.uniform(0.4, 1.0), 2)
}

data.append(new_entry)

with open(FILENAME, "w") as f:
    json.dump(data, f, indent=2)
