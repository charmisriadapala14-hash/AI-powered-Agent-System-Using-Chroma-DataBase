import streamlit as st
from agent import AIagent

st.set_page_config(
    page_title="AI Agent System",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Agent System using ChromaDB")

st.write(
    "An intelligent AI agent powered by ChromaDB "
    "for semantic search and information retrieval."
)

if "agent" not in st.session_state:
    st.session_state.agent = AIagent()

query = st.text_input("Ask your question:")

if st.button("Ask Agent"):
    if query:
        with st.spinner("Agent is thinking..."):
            response = st.session_state.agent.run(query)

        st.subheader("Agent Response")
        st.write(response)
    else:
        st.warning("Please enter a question.")
