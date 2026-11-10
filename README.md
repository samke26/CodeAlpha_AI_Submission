# Task 2: Chatbot for FAQs

**Student:** Samkelisiwe Beverly Khuzwayo  
**Student ID:** CA/DF1/315315

## Description
A simple FAQ chatbot built with Streamlit and scikit-learn. It compares a user's question with a small FAQ dataset using TF-IDF text features and cosine similarity, then displays the closest matching answer.

## Features
- Sample FAQ dataset
- Text preprocessing through TF-IDF vectorization
- Similarity matching using cosine similarity
- Chat-style user interface
- Fallback response when no close match is found

## Requirements
- Python 3.9 or later
- Packages listed in `requirements.txt`

## Run the project
1. Open a terminal in this folder.
2. Create and activate a virtual environment (recommended).
3. Install dependencies: `pip install -r requirements.txt`
4. Start the app: `streamlit run app.py`
5. Open the local address shown in the terminal (usually `http://localhost:8501`).

## Customisation
Edit the `FAQS` list in `app.py` to add questions and answers for your chosen organisation or topic.

## Limitations
This is a small demonstration FAQ bot, not a general-purpose AI assistant. Its answers depend on the FAQ examples supplied in the source code.
