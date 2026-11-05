from vector_store import VectorStore


class Retriever:

    def __init__(self):
        self.vector_store = VectorStore()

    def retrieve(self, query):

        results = self.vector_store.search(query)

        if not results:
            return ["No relevant information found."]

        return results
