import streamlit as st
from services.gym_assistant.assistant import GymAssistant  

st.set_page_config(page_title="Gym Assistant Chat", layout="wide")

assistant = GymAssistant()

st.title("🏋️ Gym Assistant")

col1, col2 = st.columns([2, 1])

with col2:
    st.markdown(
        """
        ### About this project
        This is an AI-powered assistant connected to a FastApi backend using Clean Architecture concepts.
        
        **Skills shown:**
        - Streamlit UI
        - AI conversational workflow
        - UseCases integration
        - CRUD for gym users
        - Python + FastAPI backend
        """
    )

with col1:
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    user_input = st.chat_input("Write a message…")
    if user_input:
        st.session_state.messages.append({"role": "user", "content": user_input})

        with st.chat_message("assistant"):
            reply = assistant.chat(user_input)
            st.write(reply)

        st.session_state.messages.append({"role": "assistant", "content": reply})