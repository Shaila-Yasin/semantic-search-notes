# Semantic Search over Personal Notes

A semantic search engine built using **Sentence Transformers** that allows users to search their personal Markdown notes using natural language queries instead of exact keyword matching.

Unlike traditional keyword search, this project retrieves notes based on **semantic meaning**, making it possible to find relevant information even when the query uses different words than the original notes.

---

## Features

- Read Markdown (`.md`) notes from a folder
- Split notes into meaningful chunks based on headings
- Generate sentence embeddings using a pretrained transformer model
- Perform semantic search using cosine similarity
- Save embeddings locally to avoid recomputing them every run
- Retrieve the most relevant notes for any natural language query

---

## Project Structure

```
semantic-search-over-notes/
│
├── data/
│   ├── .gitkeep
│   └── embedded_chunks.pkl      # Generated automatically (ignored by Git)
│
├── notes/
│   ├── regex.md
│   ├── text_preprocessing.md
│   └── tokenization.md
│
├── utils/
│   ├── read_notes.py
│   ├── chunking.py
│   ├── embeddings.py
│   ├── similarity.py
│   └── save_load.py
│
├── main.ipynb
├── requirements.txt
├── .gitignore
└── README.md
```

---

# Technologies Used

- Python 3.12+
- Sentence Transformers
- Transformers
- PyTorch
- NumPy
- Scikit-learn
- Jupyter Notebook

---

# How the Project Works

The project follows this pipeline:

```
Markdown Notes
       │
       ▼
Read Notes
       │
       ▼
Chunk Documents
       │
       ▼
Generate Embeddings
       │
       ▼
Save Embeddings (.pkl)
       │
       ▼
User Query
       │
       ▼
Generate Query Embedding
       │
       ▼
Cosine Similarity
       │
       ▼
Top Matching Chunks
```

---

# How to Run the Project

## 1. Clone the repository

```bash
git clone https://github.com/Shaila-Yasin/semantic-search-notes.git
```

Go inside the project folder:

```bash
cd semantic-search-notes
```

---

## 2. Create a Virtual Environment

Windows:

```bash
python -m venv .venv
```

Activate it:

PowerShell

```powershell
.\.venv\Scripts\Activate
```

Command Prompt

```cmd
.\.venv\Scripts\activate.bat
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Add Your Notes

Place your Markdown files inside the **notes/** folder.

Example:

```
notes/

text_preprocessing.md

regex.md

tokenization.md
```

---

## 5. Open the Notebook

Open

```
main.ipynb
```

using VS Code or Jupyter Notebook.

---

## 6. Run All Cells

The first time you run the notebook:

- Notes are loaded.
- Documents are chunked.
- Embeddings are generated.
- Embeddings are saved inside:

```
data/embedded_chunks.pkl
```

The next time you run the notebook, the saved embeddings are loaded automatically, making the search much faster.

---

## 7. Ask Questions

Example queries:

```
What is tokenization?

Explain regex.

Difference between stemming and lemmatization.

Why is text preprocessing important?

How are URLs removed?
```

The project returns the most semantically relevant note sections.

---

# Components

## read_notes.py

Reads all Markdown files from the `notes` folder.

Output:

```python
[
    {
        "filename": "...",
        "content": "..."
    }
]
```

---

## chunking.py

Splits each Markdown document into sections based on headings.

Each chunk contains:

- filename
- section title
- text

---

## embeddings.py

Uses the pretrained Sentence Transformer model:

```
all-MiniLM-L6-v2
```

to convert every chunk into a dense vector embedding.

---

## similarity.py

Generates an embedding for the user's query and compares it against every stored chunk embedding using **Cosine Similarity**.

The chunks are ranked by similarity score, and the most relevant results are returned.

---

## save_load.py

Provides utility functions to:

- Save embeddings to disk
- Load embeddings
- Check whether embeddings already exist

This avoids recomputing embeddings every time the project runs.

---

# Learning Outcomes

This project demonstrates practical implementation of:

- Text preprocessing concepts
- Document chunking
- Sentence embeddings
- Vector representations
- Semantic search
- Cosine similarity
- Embedding persistence
- Project structuring for NLP applications

---

# Contributing

Contributions, suggestions, and improvements are welcome.

Feel free to fork this repository and submit a pull request.

---

## Acknowledgements

The educational notes included in this repository were prepared with the assistance of ChatGPT and then reviewed, edited, and organized as part of my learning process. The project implementation, structure, and experimentation were completed as a hands-on NLP learning project.

---

## Purpose

This project was built as part of my journey to learn Natural Language Processing (NLP) and Retrieval-Augmented Generation (RAG). The goal was to understand the complete semantic search pipeline by implementing each component from scratch rather than relying on existing frameworks.

## Author 
**Shaila Yasin**

## GitHub
https://github.com/Shaila-Yasin
