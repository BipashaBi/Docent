import fitz 
from sentence_transformers import SentenceTransformer

# Load the model globally once
model = SentenceTransformer('sentence-transformers/paraphrase-MiniLM-L6-v2')

def embed_text(text):
    """
    Embed a single string or list of strings into vectors.
    """
    if isinstance(text, str):
        return model.encode([text])[0]
    else:
        return model.encode(text)

def get_query_embedding(persona, job):
    """
    Combine embeddings of persona and job-to-be-done descriptions.
    """
    persona_vec = embed_text(persona)
    job_vec = embed_text(job)
    query_vec = (persona_vec + job_vec) / 2
    return query_vec

def parse_pdf(file_path):
    """
    Parses PDF and returns list of sections (text blocks with page numbers).
    """
    doc = fitz.open(file_path)
    sections = []
    for page_num, page in enumerate(doc, start=1):
        text = page.get_text()
        sections.append({"page": page_num, "text": text})
    return sections
