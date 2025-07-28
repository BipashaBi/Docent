from sentence_transformers import SentenceTransformer

# Load the SentenceTransformer model once
model = SentenceTransformer('sentence-transformers/paraphrase-MiniLM-L6-v2')


def embed_text(text):
    """
    Embed a single string or list of strings into vector(s).

    Args:
        text (str or list of str): The input text(s) to embed.

    Returns:
        np.ndarray or list of np.ndarray: Embedding vector(s)
    """
    if isinstance(text, str):
        return model.encode([text])[0]  # Return single vector
    else:
        return model.encode(text)       # Return list of vectors


def get_query_embedding(persona, job):
    """
    Combine embeddings of persona and job-to-be-done descriptions.

    Args:
        persona (str): Persona description.
        job (str): Job-to-be-done description.

    Returns:
        np.ndarray: Combined embedding vector.
    """
    persona_vec = embed_text(persona)
    job_vec = embed_text(job)
    query_vec = (persona_vec + job_vec) / 2  # Simple average; can add weights if needed
    return query_vec
