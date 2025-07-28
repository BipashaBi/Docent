from embedding_utils import embed_text

from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def rank_sections(query_vec, sections, top_k=5):
    texts = [s['text'] for s in sections]
    doc_vectors = embed_text(texts)
    scores = cosine_similarity([query_vec], doc_vectors)[0]
    ranked = sorted(zip(sections, scores), key=lambda x: x[1], reverse=True)
    return ranked[:top_k]
