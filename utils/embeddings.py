from sentence_transformers import SentenceTransformer

print("model loaded successfully")


# Load the embedding model only once
model = SentenceTransformer("all-MiniLM-L6-v2")


def generate_embeddings(chunks):
    """
    Generate embeddings for each chunk.

    Args:
        chunks (list): List of chunk dictionaries.

    Returns:
        list: Chunks with embeddings added.
    """

    embedded_chunks = []

    for chunk in chunks:

        embedding = model.encode(chunk["text"])

        embedded_chunks.append({
            "filename": chunk["filename"],
            "title": chunk["title"],
            "text": chunk["text"],
            "embedding": embedding
        })

    return embedded_chunks