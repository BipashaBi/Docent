import json
from datetime import datetime

def build_output(metadata, ranked_sections, refined_subsections):
    output = {
        "metadata": {
            "input_documents": metadata.get('docs', []),
            "persona": metadata.get('persona', ''),
            "job_to_be_done": metadata.get('job', ''),
            "timestamp": datetime.now().isoformat()
        },
        "extracted_sections": [],
        "sub_section_analysis": refined_subsections
    }

    for idx, (section, sim_score) in enumerate(ranked_sections):
        output["extracted_sections"].append({
            "document": section["doc"],
            "page_number": section["page"],
            "section_title": section["text"],
            "importance_rank": idx + 1,
            "similarity_score": round(float(sim_score), 4)
        })

    return output
