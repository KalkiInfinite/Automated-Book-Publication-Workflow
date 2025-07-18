import chromadb
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction

embedding_fn = SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")
client = chromadb.Client()
collection = client.get_or_create_collection("chapters", embedding_function=embedding_fn)

def store_version(chapter_id, version, content, score=0.0):
    collection.add(
        documents=[content],
        metadatas=[{"chapter_id": chapter_id, "version": version, "score": score}],
        ids=[f"{chapter_id}_v{version}"]
    )

def semantic_search(query, n=3):
    return collection.query(query_texts=[query], n_results=n)
