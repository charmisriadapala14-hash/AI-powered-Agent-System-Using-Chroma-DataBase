import chromadb
from config import CHROMA_DB_PATH, COLLECTION_NAME


class VectorStore:

    def __init__(self):

        self.client = chromadb.PersistentClient(
            path=CHROMA_DB_PATH
        )

        self.collection = self.client.get_or_create_collection(
            name=COLLECTION_NAME
        )

    def add_documents(self, documents):

        for index, document in enumerate(documents):

            self.collection.add(
                documents=[document],
                ids=[str(index)]
            )

    def search(self, query):

        results = self.collection.query(
            query_texts=[query],
            n_results=3
        )

        return results["documents"][0] if results["documents"] else []
