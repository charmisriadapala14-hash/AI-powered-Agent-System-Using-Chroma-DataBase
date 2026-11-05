# AI Agent System Using ChromaDB

## Project Overview
An AI-powered agent system that uses ChromaDB as a vector database for storing, searching, and retrieving information efficiently.

## Features
- Intelligent AI Agent
- ChromaDB Vector Database
- Semantic Search
- Document Loading
- Context-Based Question Answering
- Streamlit User Interface
- PDF Document Support

## Technologies Used
- Python
- Streamlit
- ChromaDB
- OpenAI API
- LangChain
- PyPDF

## Project Structure

AI-Agent-System/
│
├── app.py
├── agent.py
├── config.py
├── vector_store.py
├── document_loader.py
├── retriever.py
├── utils.py
├── requirements.txt
└── README.md

## Installation

Install dependencies:

pip install -r requirements.txt

## API Configuration

Create a .env file and add:

OPENAI_API_KEY=your_api_key

## Run Application

streamlit run app.py

## Working Process

1. User enters a question.
2. AI Agent receives the question.
3. ChromaDB searches for relevant information.
4. Retrieved context is sent to the AI model.
5. AI generates a response.

## Author
Developed as a Python AI project.
