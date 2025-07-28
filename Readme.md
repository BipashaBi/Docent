# Docent: PDF Relevance Extraction Pipeline

A sincere attempt by team Hack-A-Dobe to extract titles and headings from PDF files, organized in a clear outline. This solution is made to meet the Adobe Hackathon Challenge 1B requirements
---

## Approach

Our pipeline processes each PDF in a collection and performs the following steps:

1. **PDF Parsing**: Extract text content using `PyMuPDF` and organize it into hierarchical sections.
2. **Embedding Generation**: Generate sentence-level embeddings using the `sentence-transformers` model.
3. **Semantic Similarity**: Compute cosine similarity between PDF content and the provided persona/job description.
4. **Subsection Filtering**: Identify and retain the most relevant subsections using a threshold/ranking strategy.
5. **Formatting Output**: Structure the output according to the `challenge1b_output.json` format.

This method ensures only the most relevant and informative text is extracted and returned for each collection.

---

## Models and Libraries Used

- [`sentence-transformers`](https://www.sbert.net/) – For semantic embeddings (e.g., `all-MiniLM-L6-v2`)
- `PyMuPDF (fitz)` – For robust PDF parsing
- `scikit-learn` – For cosine similarity computation
- Standard libraries: `os`, `glob`, `json`, `re`, `numpy`

---

## Build & Run Instructions (For Documentation)

### Directory Structure

DOCENT(1B)/
├── app/
│ ├── embedding_utils.py # Utilities for text embedding using Sentence Transformers
│ ├── main.py # Main entry point for running the pipeline
│ ├── output_formatter.py # Formats output to the required JSON schema
│ ├── pdf_parser.py # Extracts structured content from PDF files
│ ├── pipeline.py # Coordinates the entire workflow
│ ├── similarity_ranking.py # Ranks paragraphs based on similarity
│ └── subsection_processing.py # Refines and groups text subsections
│
├── Collection 1/
│ ├── PDF/ # Folder containing academic PDF files
│ ├── challenge1b_input.json # Input JSON containing persona and job description
│ └── challenge1b_output.json # Final output JSON (generated)
│
├── Collection 2/ # Same format as Collection 1
├── Collection 3/ # Same format as Collection 1
│
├── sentence_transformers/ # (Optional) Pretrained model folder if downloaded manually
│
├── sentence_transformers.py # Handles SentenceTransformer model loading
├── test_sentence_transformer.py # Quick test for verifying model output
├── output.json # Aggregated output file (if used)
├── requirements.txt # Python dependency list
├── Dockerfile # For containerized setup
├── .gitignore # Git ignore file

## Install Dependecies

Install Dependencies

Make sure you have Python 3.7+ and required packages installed:

```bash
pip install pymupdf jsonschema
```

## Place Input PDFs

Put your PDFs into the folder named collection

## **How to run the code project**

docker build -t docent:challenge1b .

docker run -it --rm docent:challenge1b
