import requests
import json
import pandas as pd

def send_request(message, conversation_history):
    url = 'https://api.openai.com/v1/chat/completions'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer sk-proj-zJ0Vbf0Anl71NJStFVRnT3BlbkFJi0NvA7H9uL38p1CCBspf',
        'Cookie': '_cf_bm=._2PiCg6r70HaAMKhUiJ5dlHLrEZz5tlktuWSPg.AUU-1713291200-1.0.1.1-1CyYTJdv9zE3o_VOqq6Sd2mSBZSKasD0me5B9q9acgoHWgiEj9Myk39tYXZVpk_ocxME_sCaMFO.54k83aV.w; _cfuvid=zvZH1myTHbuWjsdD_fWv.YtHHOnZW3Ct_FJpK8z34a0-1713291200157-0.0.1.1-604800000'
    }
    data = {
        "model": "gpt-3.5-turbo",
        "messages": conversation_history + [{"role": "user", "content": message}],
        "temperature": 1,
        "max_tokens": 533,
        "top_p": 1,
        "frequency_penalty": 0,
        "presence_penalty": 0
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    return response.json()

def send_csv_rows(csv_path):
    # Read the CSV file
    df = pd.read_csv(csv_path)

    # Initialize an empty list to store the responses
    responses = []

    # Initialize the conversation history
    conversation_history = [
        {
            "role": "user",
            "content": "Please write a commentary for frames  of tetris game..."
        },
        {
            "role": "assistant",
            "content": "As we enter the Tetris game, we see Player_name_L and Player_name_R ready to take on the challenge..."
        },
        {
            "role": "user",
            "content":" make the commentary sound natural and don't mention frames think of it as a live video instead, i will provide you 5 frames at a time giving you 5 secons of video footage."
        }
    ]

    # Loop through the DataFrame in chunks of 5 rows
    for i in range(0, len(df), 5):
        # Select the chunk of rows
        chunk = df.iloc[i:i+5]

        # Convert the chunk to a string
        message = chunk.to_string(index=False)

        # Send the message to the API
        response = send_request(message, conversation_history)

        # Append the 'content' of the response to the list
        responses.append(response['choices'][0]['message']['content'])

        # Update the conversation history
        conversation_history.append({
            "role": "assistant",
            "content": response['choices'][0]['message']['content']+"summarise this in 50 words."
        })

    # Join the responses together into a single string
    result = ' next 15 secs \n'.join(responses)
    print(responses)
    response = send_request(result+"Now that you have input of all the frames as well as summary of all the frames, create a natural live commentary, for the previous 60 seconds at the rate of 150 words per minute. Decide your words according to frames descriptions and what word number it is. Also output only commentary nothing else. Keep the output limited to 150 words.", conversation_history)
    result=response['choices'][0]['message']['content']
    print(result)
    return result

# Example usage
def requester():
    # print(send_csv_rows('extracted_data.csv'))
    return send_csv_rows('extracted_data.csv')