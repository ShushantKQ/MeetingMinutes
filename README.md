# Meeting_minutes_generator
Generate minutes of a meeting

## Directory Structure


meeting_summarizer

    └── gpt_indexing      📄 subdirectory for gpt indexing
        └── datasets        dataset for gpt indexing
            └── meeting_corpus.txt  corpus for gpt indexing
    └── models      contains the trained and pretrained word2vec models

    └── generate_meeting_minutes_transformer.py     module to generate meeting minutes using 

    └── generate_meeting_minutes.py module to generate meeting minutes 

    └── gpt_indexing_inferencing.py  inference module to run the GPT indexed model

    └── gpt-neo.ipynb      notebook for finetuning the gpt-j model on medical dataset

    └── gpt_meeting.txt     corpus of the meeting transcription and minutes generated

    └── index.json  json file of the index generated from chatGPT

    └── meeting_minutes_data.csv    csv data of the minutes and meeting transcription

    └── meeting_summary_nltk.py     module to generate minutes using nltk and chatGPT

    └── README.md           README file for the repo

    └── streamlit_app.py        streamlit web application to run the meeting minute generator






## Instructions

### Create a virtual environment
### Install libraries using following command
pip instal -r requirements.txt

## Run the web application
To run the stremalit web application run streamlit run streamlit_app.py

