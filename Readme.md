# 📄 Docent: PDF Relevance Extraction Pipeline

**Docent** is a Python-based pipeline that extracts meaningful titles and structured headings from PDFs and filters them based on relevance to a given job description or persona. It leverages semantic similarity to return only the most informative content.

---

## 🚀 Overview

Docent processes collections of PDFs and identifies the most relevant sections using natural language understanding. The pipeline outputs a structured JSON summary that emphasizes meaningful and contextually appropriate content for any given use case (e.g., job-matching, persona targeting).

---

## 🧠 Pipeline Workflow

For each PDF, Docent performs the following steps:

1. **📘 PDF Parsing**
   Extracts hierarchical text data using `PyMuPDF`.

2. **🧬 Embedding Generation**
   Generates sentence-level embeddings via `sentence-transformers` models (e.g., `all-MiniLM-L6-v2`).

3. **🔍 Semantic Similarity**
   Computes cosine similarity between PDF content and the target persona or job description.

4. **✂️ Subsection Filtering**
   Ranks paragraphs and retains only the most relevant ones based on similarity thresholds.

5. **📦 Output Formatting**
   Outputs structured data following a consistent JSON format (compatible with downstream systems or integrations).

---

## 🛠️ Dependencies

Install required libraries using `pip`:

```bash
pip install pymupdf sentence-transformers scikit-learn numpy
```

### Required Packages

* [`sentence-transformers`](https://www.sbert.net/) – Semantic embedding
* `PyMuPDF (fitz)` – PDF parsing and layout detection
* `scikit-learn` – Cosine similarity computation
* Standard libraries: `os`, `glob`, `json`, `re`, `numpy`

---

## 📁 Project Structure

```
DOCENT/
├── app/
│   ├── embedding_utils.py           # Text embedding functions
│   ├── main.py                      # Entry point
│   ├── output_formatter.py          # JSON output formatter
│   ├── pdf_parser.py                # PDF heading extractor
│   ├── pipeline.py                  # Workflow coordinator
│   ├── similarity_ranking.py        # Semantic similarity scoring
│   └── subsection_processing.py     # Subsection refinement
│
├── Collection 1/
│   ├── PDF/                         # Source PDFs
│   ├── challenge1b_input.json       # Persona/Job Description input
│   └── challenge1b_output.json      # Final JSON output (generated)
│
├── Collection 2/
├── Collection 3/
│
├── sentence_transformers/          # (Optional) Local model directory
├── sentence_transformers.py        # SentenceTransformer model wrapper
├── test_sentence_transformer.py    # Model test script
├── output.json                     # Aggregated results (optional)
├── requirements.txt                # Dependencies
├── Dockerfile                      # Container setup
└── .gitignore
```

---

## 📥 Input

* Place PDFs inside the relevant `Collection` folder (e.g., `Collection 1/PDF/`)
* Add a `challenge1b_input.json` file in the collection folder containing the persona/job description

---

## ▶️ Running the Project

### 🐳 Docker (Recommended)

1. **Build Docker Image**

   ```bash
   docker build -t docent:latest .
   ```

2. **Run Container**

   ```bash
   docker run -it --rm docent:latest
   ```

> Customize paths or bind volumes if needed for local file access.

---

## 📌 Output

* A JSON file (e.g., `challenge1b_output.json`) is generated for each collection
* Output includes:

  * Extracted titles/headings
  * Most relevant paragraphs
  * Sectional structure for better readability

---

## ✅ Summary

* 🔍 Smart relevance-based PDF section filtering
* 💬 Semantic understanding using transformer-based models
* 📂 Outputs in clean, structured JSON
* 🔒 Fully offline and customizable


