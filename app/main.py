import os
import json
from pdf_parser import parse_pdf
from embedding_utils import get_query_embedding
from similarity_ranking import rank_sections
from app.subsection_processing import summarize_ranked_sections  # Corrected import
from app.output_formatter import build_output

def process_collections():
    COLLECTION_FOLDERS = ["Collection 1", "Collection 2", "Collection 3"]

    for collection in COLLECTION_FOLDERS:
        print(f"\n--- Processing: {collection} ---")

        # Define paths
        base_path = os.path.join(os.getcwd(), collection)
        pdf_dir = os.path.join(base_path, "PDF")
        input_json_path = os.path.join(base_path, "challenge1b_input.json")
        output_json_path = os.path.join(base_path, "challenge1b_output.json")

        # Sanity check
        if not os.path.exists(input_json_path) or not os.path.isdir(pdf_dir):
            print(f"⚠ Skipping {collection}: Missing input.json or PDF folder")
            continue

        # Load input JSON
        with open(input_json_path, "r", encoding="utf-8") as f:
            metadata = json.load(f)

        # Parse PDFs
        file_list = [os.path.join(pdf_dir, f) for f in os.listdir(pdf_dir) if f.endswith(".pdf")]
        all_sections = []
        for pdf_path in file_list:
            sections = parse_pdf(pdf_path)
            for section in sections:
                section["doc"] = os.path.basename(pdf_path)
            all_sections.extend(sections)

        if not all_sections:
            print(f"⚠ No valid sections found in {collection}")
            continue

        # Embed and rank
        print("Embedding persona and job-to-be-done...")
        query_vec = get_query_embedding(metadata["persona"], metadata["job"])
        print(f"Embedding {len(all_sections)} document sections...")
        ranked_sections = rank_sections(query_vec, all_sections, top_k=5)

        # Refine for output
        refined_subsections = summarize_ranked_sections(ranked_sections)

        # Build output
        output_data = build_output(metadata, ranked_sections, refined_subsections)

        # Save output JSON
        with open(output_json_path, "w", encoding="utf-8") as f:
            json.dump(output_data, f, indent=2)

        print(f"✅ Output written to: {output_json_path}")

if __name__ == "__main__":
    process_collections()
