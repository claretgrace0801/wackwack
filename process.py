import json
from pprint import pprint
import random

with open('transcript1.json', 'r') as file:
    data = json.load(file)

# sentiment analysis
moves = ["Brillant", "Great", "Blunder", "Mistake"]
output_move = random.choice(moves)

logs = []
for sentence in data["data"]["transcript"]["sentences"]:
    sentence_copy = sentence.copy()
    sentiment = sentence_copy.pop("ai_filters")["sentiment"]
    logs.append(sentence_copy | {
        "move": output_move,
        "sentiment": sentiment
    })

with open('processed.json', 'w') as json_file:
    json.dump(logs, json_file, indent=2)

