import json
from pprint import pprint
import random

def process_transcript(transcript_id):

    with open(f'transcripts/{transcript_id}.json', 'r') as file:
        data = json.load(file)

    # sentiment analysis
    moves = ["Brillant", "Great", "Blunder", "Mistake","Inaccuracy", "Dubious","Book","Interesting"]

    logs = []
    for sentence in data["data"]["transcript"]["sentences"]:
        output_move = random.choice(moves)
        sentence_copy = sentence.copy()
        sentiment = sentence_copy.pop("ai_filters")["sentiment"]
        logs.append(sentence_copy | {
            "move": output_move,
            "sentiment": sentiment
        })

    with open(f'processed_transcripts/{transcript_id}.json', 'w') as json_file:
        json.dump(logs, json_file, indent=2)

