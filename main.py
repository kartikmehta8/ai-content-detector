import json
import requests
from utils import return_column_csv

# Getting all the responses from the csv file
responses_prompt = return_column_csv('FILE_NAME.csv', 12)

# Configuration for the EdenAI API
headers = {"Authorization": "Bearer YOUR_EDEN_AI_TOKEN"}
url ="https://api.edenai.run/v2/text/ai_detection"

# Omitting the first response as it is the question.
responses_prompt = responses_prompt[1:]

index = 0
for response in responses_prompt:
    index += 1
    
    # Setting the payload to be sent to the API & Model
    payload={"providers": "sapling", "text": str(response)}

    res = requests.post(url, json=payload, headers=headers)
    result = json.loads(res.text)

    # For storing the metrics.
    total_rows = 0
    ai_generated = 0
    human_generated = 0

    for row in result['sapling']['items']:
        total_rows += 1
        if row['prediction'] == 'ai-generated':
            ai_generated += 1
        else:
            human_generated += 1

    percentage = ai_generated/total_rows * 100
    print(f"{index}. Percentage of AI generated responses: {percentage}%")
    print(f"Total rows: {total_rows} | AI generated: {ai_generated} | Human generated: {human_generated}")
    with open('OUTPUT.txt', 'a') as f:
        f.write(f"{percentage}\n")