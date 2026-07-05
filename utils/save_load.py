import pickle
import os


def save_embeddings(embedded_chunks, file_path="data/embedded_chunks.pkl"):
    """
    Save embedded chunks to a pickle file.

    Args:
        embedded_chunks (list): Chunks with embeddings.
        file_path (str): Path to save the pickle file.
    """

    # Create the data folder if it doesn't exist
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    with open(file_path, "wb") as file:
        pickle.dump(embedded_chunks, file)

    print(f"Embeddings saved to: {file_path}")


def load_embeddings(file_path="data/embedded_chunks.pkl"):
    """
    Load embedded chunks from a pickle file.

    Args:
        file_path (str): Path to the pickle file.

    Returns:
        list: Embedded chunks.
    """

    with open(file_path, "rb") as file:
        embedded_chunks = pickle.load(file)

    print(f"Embeddings loaded from: {file_path}")

    return embedded_chunks


def embeddings_exist(file_path="data/embedded_chunks.pkl"):
    """
    Check whether embeddings already exist.

    Returns:
        bool
    """

    return os.path.exists(file_path)