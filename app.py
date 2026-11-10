import streamlit as st
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.set_page_config(page_title="FAQ Chatbot", page_icon="💬")
st.title("💬 FAQ Chatbot")
st.write("Ask a question about the example topic: a student support service.")

FAQS = [
    ("How do I reset my password?", "Select 'Forgot password' on the sign-in page and follow the reset instructions sent to your registered email."),
    ("How can I contact support?", "Contact the support team using the email address or phone number provided by your organisation."),
    ("What are the support hours?", "Support hours depend on the organisation. Check its official contact page for the latest hours."),
    ("How do I submit an assignment?", "Follow the submission instructions from your institution. Check the required file format, deadline and submission link before submitting."),
    ("Can I upload a PDF?", "If PDF is an accepted format in your submission instructions, upload the PDF and confirm that it opens correctly."),
    ("What should I do if my upload fails?", "Check your internet connection, file size and file format, then try again. Contact support if the issue continues."),
    ("How do I check my application status?", "Sign in to the relevant portal and look for an application or status section. If it is not available, contact the organisation."),
    ("Where can I find the project instructions?", "Check the official project brief or the messages shared by your programme coordinator."),
]

questions = [item[0] for item in FAQS]
answers = [item[1] for item in FAQS]
vectorizer = TfidfVectorizer(lowercase=True, stop_words="english", ngram_range=(1, 2))
question_matrix = vectorizer.fit_transform(questions)

def get_answer(user_question):
    cleaned = re.sub(r"\s+", " ", user_question).strip()
    if not cleaned:
        return None, 0.0
    query_vector = vectorizer.transform([cleaned])
    scores = cosine_similarity(query_vector, question_matrix)[0]
    best_index = scores.argmax()
    return answers[best_index], float(scores[best_index])

if "history" not in st.session_state:
    st.session_state.history = []

for question, answer in st.session_state.history:
    with st.chat_message("user"):
        st.write(question)
    with st.chat_message("assistant"):
        st.write(answer)

user_input = st.chat_input("Type your question...")
if user_input:
    answer, score = get_answer(user_input)
    if answer is None:
        response = "Please type a question so I can help."
    elif score < 0.08:
        response = "I could not find a close FAQ match. Please rephrase your question or contact the relevant support team."
    else:
        response = answer
    st.session_state.history.append((user_input, response))
    st.rerun()

with st.expander("View example FAQs"):
    for question, answer in FAQS:
        st.markdown(f"**Q: {question}**")
        st.write(f"A: {answer}")

st.caption("This demonstration uses TF-IDF and cosine similarity to match questions. Answers are limited to the sample FAQ dataset.")
