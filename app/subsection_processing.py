from embedding_utils import embed_text

def embed_sections(sections):
    """
    Takes a list of section dictionaries, each containing a 'text' key.
    Returns a list of (section_dict, embedding) tuples.
    """
    embeddings = []
    for sec in sections:
        text = sec.get('text', None)
        if not text:
            print(f"Warning: Section missing text or empty: {sec}")
            continue
        emb = embed_text(text)
        embeddings.append((sec, emb))
    return embeddings

def split_into_subsections(sections):
    """
    Splits each section's text into smaller logical subsections.
    Useful for improving granularity before embedding.
    """
    subsections = []
    for sec in sections:
        lines = sec['text'].split("\n\n")  # Simple heuristic
        for line in lines:
            if line.strip():
                subsections.append({'text': line.strip()})
    return subsections


def summarize_ranked_sections(ranked_sections):
    """
    Takes top-k ranked sections and returns trimmed document info.
    """
    refined = []
    for section, score in ranked_sections:
        refined.append({
            "document": section["doc"],
            "page_number": section["page"],
            "snippet": section["text"][:300] + "..."  # first 300 characters
        })
    return refined

