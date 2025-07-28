import os
from pdf_parser import parse_pdf
from embedding_utils import get_query_embedding
from similarity_ranking import rank_sections
from app.subsection_processing import extract_subsections
from app.output_formatter import build_output

def run_pipeline(input_data, pdf_paths):
    # Step 1: Parse all PDFs and extract sections
    all_sections = []
    for pdf_path in pdf_paths:
        sections = parse_pdf(pdf_path)
        for section in sections:
            section["doc"] = os.path.basename(pdf_path)
        all_sections.extend(sections)

    # Step 2: Embed persona + job
    query_vec = get_query_embedding(input_data["persona"], input_data["job"])

    # Step 3: Rank sections by relevance
    ranked_sections = rank_sections(query_vec, all_sections, top_k=5)

    # Step 4: Extract refined subsections
    refined_subsections = extract_subsections(ranked_sections)

    # Step 5: Build the output
    output_data = build_output(input_data, ranked_sections, refined_subsections)

    return output_data
