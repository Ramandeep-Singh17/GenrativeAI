import streamlit as st
from dotenv import load_dotenv

load_dotenv()

from langchain_groq import ChatGroq
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage


# ---------------- PAGE ----------------

st.set_page_config(
    page_title="AI Mood Chatbot",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 Mood Based AI Chatbot")
st.caption("Choose your AI personality and start chatting")


# ---------------- MODEL ----------------

model = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0.9
)


# ---------------- MODE ----------------

mode_choice = st.radio(
    "Choose your AI Mode:",
    ["😡 Angry", "😂 Funny", "😢 Sad"],
    horizontal=True
)


if mode_choice == "😡 Angry":

    mode = """
    You are an angry AI agent.
    You respond aggressively and impatiently.
    Do not use abusive or harmful language.
    """

elif mode_choice == "😂 Funny":

    mode = """
    You are a very funny AI agent.
    You respond with humor and jokes.
    Keep your answers helpful.
    """

else:

    mode = """
    You are a very sad AI agent.
    You respond in a sad and emotional tone.
    Remain helpful and respectful.
    """


# ---------------- SESSION MEMORY ----------------

if (
    "messages" not in st.session_state
    or st.session_state.get("current_mode") != mode
):

    st.session_state.current_mode = mode

    st.session_state.messages = [
        SystemMessage(content=mode)
    ]


# ---------------- DISPLAY HISTORY ----------------

for msg in st.session_state.messages:

    if isinstance(msg, HumanMessage):

        with st.chat_message("user"):
            st.write(msg.content)

    elif isinstance(msg, AIMessage):

        with st.chat_message("assistant"):
            st.write(msg.content)


# ---------------- CHAT INPUT ----------------

user_input = st.chat_input("Say something...")


if user_input:

    # Add user message
    st.session_state.messages.append(
        HumanMessage(content=user_input)
    )

    with st.chat_message("user"):
        st.write(user_input)


    # Generate response
    with st.chat_message("assistant"):

        with st.spinner("AI is thinking..."):

            response = model.invoke(
                st.session_state.messages
            )

            st.write(response.content)


    # Save AI response
    st.session_state.messages.append(
        AIMessage(content=response.content)
    )


# ---------------- RESET ----------------

st.divider()

if st.button("🔄 Reset Chat"):

    st.session_state.messages = [
        SystemMessage(content=mode)
    ]

    st.rerun()