import os

import openai
from dotenv import load_dotenv
from nltk.tokenize import word_tokenize

load_dotenv()

openai.api_key = os.getenv("api_key")

filename = "sample_meeting.txt"

def count_tokens(filename):
    with open(filename, 'r') as f:
        text = f.read()     
    tokens = word_tokenize(text)
    num_tokens = len(tokens)
    return num_tokens

def break_up_file(tokens, chunk_size, overlap_size):
    if len(tokens) <= chunk_size:
        yield tokens
    else:
        chunk = tokens[:chunk_size]
        yield chunk
        yield from break_up_file(tokens[chunk_size-overlap_size:], chunk_size, overlap_size)

def break_up_file_to_chunks(filename, chunk_size=1000, overlap_size=100):
    with open(filename, 'r') as f:
        text = f.read()
    tokens = word_tokenize(text)
    return list(break_up_file(tokens, chunk_size, overlap_size))

def convert_to_prompt_text(tokenized_text):
    prompt_text = " ".join(tokenized_text)
    prompt_text = prompt_text.replace(" 's", "'s")
    return prompt_text

def generate_summary(filename):
    # token_count = count_tokens(filename)
    chunks = break_up_file_to_chunks(filename)
    response = []
    prompt_response = []

    chunks = break_up_file_to_chunks(filename)
    for i, chunk in enumerate(chunks):
        prompt_request = "Summarize this meeting transcript: " + convert_to_prompt_text(chunks[i])
        
        response = openai.Completion.create(
                model="text-davinci-003",
                prompt=prompt_request,
                temperature=.5,
                max_tokens=500,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
        )
        # breakpoint()
        prompt_response.append(response["choices"][0]["text"])

        # summary = prompt_response
        # # print("Summary",summary)

    
    prompt_request = "Consoloidate these meeting summaries: " + str(prompt_response)

    response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt_request,
            temperature=.5,
            max_tokens=1000,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
    print("Meeting summary",response["choices"][0]["text"])

    return response["choices"][0]["text"]

def generate_action_items(filename):
    action_response = []
    chunks = break_up_file_to_chunks(filename)
    for i, chunk in enumerate(chunks):
        prompt_request = "Provide a list of action items with a due date from the provided meeting transcript text: " + convert_to_prompt_text(chunks[i])

        response = openai.Completion.create(
                model="text-davinci-003",
                prompt=prompt_request,
                temperature=.5,
                max_tokens=500,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
        )
        # breakpoint()
        action_response.append(response["choices"][0]["text"])

    # print("Actions",action_response)

    prompt_request = "Consoloidate these meeting action items: " + str(action_response)
    # prompt_request = "Who is the president of US?"
    response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt_request,
            temperature=.5,
            max_tokens=500,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
    
    meeting_action_items = response["choices"][0]["text"]
    print("Meeting Action Items",meeting_action_items)
    return meeting_action_items

if __name__ == "__main__":
    import time
    start_time = time.time()
    filename = "meeting.txt"
    meeting_summary = generate_summary(filename)
    meeting_action_items = generate_action_items(filename)
    print("Time Taken", time.time() - start_time)
