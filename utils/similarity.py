from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


# Load the same embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")


def semantic_search(query, embedded_chunks, top_k=3):
    """
    Search the most relevant chunks for a query.

    Args:
        query (str): User question.
        embedded_chunks (list): Chunks with embeddings.
        top_k (int): Number of results to return.

    Returns:
        list: Top matching chunks.
    """

    # Convert the question into an embedding
    query_embedding = model.encode(query)

    results = []

    for chunk in embedded_chunks:

        similarity = cosine_similarity(
            [query_embedding],
            [chunk["embedding"]]
        )[0][0]

        results.append({
            "filename": chunk["filename"],
            "title": chunk["title"],
            "text": chunk["text"],
            "score": similarity
        })

    # Sort by similarity score (highest first)
    results.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return results[:top_k]