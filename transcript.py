import requests
import time
from pprint import pprint
import json
from process_transcript import process_transcript

# Define the URL and headers for the request
url = 'https://api.fireflies.ai/graphql'
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer 83e7e7ae-af14-4c43-8dc0-d2595b55c720'
}


# Function to fetch transcript IDs
def fetch_transcripts():
    data = '{"query": "query Transcripts($userId: String) { transcripts(user_id: $userId) { title id } }"}'
    response = requests.post(url, headers=headers, data=data)
    response_json = response.json()
    transcripts = response_json.get('data', {}).get('transcripts', [])
    return transcripts

def fetch_transcript(transcript_id):
    data = '{ "query": "query Transcript($transcriptId: String!) { transcript(id: $transcriptId) { id title transcript_url duration sentences{index text start_time end_time speaker_name speaker_id ai_filters{sentiment}} } }", "variables": { "transcriptId": "' + transcript_id + '" } }'
    response = requests.post(url, headers=headers, data=data)
    response_json = response.json()
    transcript = response_json.get('data', {}).get('transcript', {})
    return transcript

def dump_transcript(transcript, transcript_id):
    with open(f'transcripts/{transcript_id}.json', 'w') as json_file:
        json.dump({'data':{'transcript': transcript}}, json_file, indent=2)

# Initialize the previous count and IDs
previous_transcripts = fetch_transcripts()[:-1]
previous_count = len(previous_transcripts)

print("Monitoring for new transcriptions...")
while True:
    time.sleep(5)  # Wait for 30 seconds

    # Fetch the current transcripts
    current_transcripts = fetch_transcripts()
    current_count = len(current_transcripts)

    # Check if the number of transcripts has increased
    if current_count > previous_count:
        # Determine new transcripts
        new_transcripts = [t for t in current_transcripts if t not in previous_transcripts]

        # Print the IDs of the new transcripts
        print("New transcripts found:")
        for transcript in new_transcripts:
            print(f"New transcript ID: {transcript['id']} {transcript['title']}")
            new_transcript=fetch_transcript(transcript['id'])
            pprint(new_transcript)
            dump_transcript(new_transcript, transcript['id'])
            process_transcript(transcript['id'])

        # Update previous transcripts and count
        previous_transcripts = current_transcripts
        previous_count = current_count
    else:
        print("No new transcriptions.")

    # Optionally print the current state for debugging
    # print(f"Current count: {current_count}, Previous count: {previous_count}")
