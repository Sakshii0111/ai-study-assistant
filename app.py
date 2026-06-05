import streamlit as st
from llm import get_explanation, get_notes, get_quiz, ask_question

# Page config
st.set_page_config(page_title="AI Study Assistant", page_icon="📚", layout="centered")

# Title
st.title("📚 Smart AI Study Assistant")
st.markdown("### ✨ Learn Faster with AI")

st.markdown("---")

# Session state for chat
if "messages" not in st.session_state:
    st.session_state.messages = []

# Study Mode
mode = st.selectbox("🎯 Select Learning Mode", ["Beginner", "Intermediate", "Advanced"])

# Topic input
topic = st.text_input("📌 Enter a topic")

st.markdown("---")

# Buttons in columns
col1, col2 = st.columns(2)

with col1:
    if st.button("📖 Explanation"):
        if topic:
            with st.spinner("Generating explanation... 🤔"):
                result = get_explanation(f"{topic} for {mode} level")
                st.write(result)
        else:
            st.warning("Please enter a topic")

with col2:
    if st.button("📝 Notes"):
        if topic:
            with st.spinner("Generating notes... 🧠"):
                result = get_notes(f"{topic} for {mode} level")
                st.write(result)
        else:
            st.warning("Please enter a topic")

# Quiz Section
if st.button("❓ Generate Quiz"):
    if topic:
        with st.spinner("Creating quiz... 🎯"):
            quiz = get_quiz(topic)
            st.write(quiz)
    else:
        st.warning("Please enter a topic")

st.markdown("---")

# Chat Section
st.subheader("💬 Ask Anything")

user_input = st.text_input("Type your question here...")

if st.button("Send"):
    if user_input:
        with st.spinner("Thinking... 🤖"):
            response = ask_question(user_input)
            st.session_state.messages.append(("You", user_input))
            st.session_state.messages.append(("AI", response))
    else:
        st.warning("Please enter a question")

# Display chat history
for role, msg in st.session_state.messages:
    if role == "You":
        st.markdown(f"**🧑 {role}:** {msg}")
    else:
        st.markdown(f"**🤖 {role}:** {msg}")

st.markdown("---")
st.markdown("💡 Built with LLM + Streamlit | Resume Project 🚀")