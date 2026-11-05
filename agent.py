from openai import OpenAI
from config import OPENAI_API_KEY, LLM_MODEL
from vector_store import VectorStore


class AIagent:

    def __init__(self):
        if not OPENAI_API_KEY:
            raise ValueError("OPENAI_API_KEY is missing.")

        self.client = OpenAI(api_key=OPENAI_API_KEY)
        self.vector_store = VectorStore()

    def run(self, query):

        documents = self.vector_store.search(query)

        context = "\n".join(documents)

        prompt = f"""
        You are an intelligent AI assistant.

        Use the following context to answer
        the user's question.

        Context:
        {context}

        User Question:
        {query}

        Provide a clear and helpful answer.
        """

        response = self.client.chat.completions.create(
            model=LLM_MODEL,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.3
        )

        return response.choices[0].message.content
