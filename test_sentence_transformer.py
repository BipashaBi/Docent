from sentence_transformers import SentenceTransformer

# Load the pretrained model. This will download the model if not present locally.
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

# Example to confirm it works:
sentences = [
    "PhD Researcher in Computational Biology",
    "Prepare a comprehensive literature review focusing on methodologies, datasets, and benchmarks"
]
embeddings = model.encode(sentences)
print("Embeddings shape:", embeddings.shape)
print("First vector (truncated):", embeddings[0][:5])
