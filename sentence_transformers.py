from sentence_transformers import SentenceTransformer

# Load model (make sure weights are local)
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

def embed(text):
    return model.encode([text])[0]  # Returns vector
