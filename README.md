# AI Second Brain RAG System

My personal knowledge management system powered by MongoDB and RAG (Retrieval Augmented Generation).

## Overview

This system allows you to ingest, process, and retrieve knowledge from your personal documents using advanced NLP techniques. It creates vector embeddings of your documents and stores them in MongoDB for semantic search and retrieval.

## Features

- **Document Ingestion Pipeline**: Process JSON documents from a specified directory
- **Quality Assessment**: Filter documents using both heuristic and LLM-based approaches
- **Vector Embeddings**: Generate document embeddings using Hugging Face models
- **MongoDB Integration**: Store and index documents and embeddings for efficient retrieval
- **CLI Interface**: Easy-to-use command line tool for data ingestion

## Installation

1. Clone the repository:
   ```bash
   git clone <your-repository-url>
   cd xay_second_brain
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the package:
   ```bash
   pip install -e .
   ```

4. Set up environment variables by creating a `.env` file with:
   ```
   MONGODB_URI=your_mongodb_connection_string
   OPENAI_API_KEY=your_openai_api_key
   ```

## Usage

### Running the Data Ingestion Pipeline

Process documents using the CLI tool:

```bash
# Using the installed command
run-ingestion

# Or using the Python script directly
python tools/run_data_ingestion_pipeline.py
```

By default, the pipeline will look for documents in the `data/rag` directory relative to the project root. You can specify a different directory:

### Document Format

Input documents should be JSON files with the following structure:

```json
{
  "content": "Your document text content",
  "metadata": {
    "source": "source_identifier",
    "title": "Document Title",
    "url": "https://original-source-url.com"
  },
  "child_urls": ["https://related-url-1.com", "https://related-url-2.com"]
}
```

## Configuration

Key configuration settings can be found in `src/rag/config.py`:

- Embedding model selection
- MongoDB connection settings
- Quality assessment thresholds
- Device settings (CPU/GPU)

## Requirements

- Python 3.9+
- MongoDB Atlas account for vector search capabilities
- Dependencies as listed in setup.py:
  - sentence-transformers >= 2.7.0
  - transformers == 4.51.1
  - tokenizers < 0.22, >= 0.21
  - Other dependencies as specified in setup.py

## Dependency Notes

The project requires specific versions of certain packages to ensure compatibility:
- `transformers` version 4.51.1 is required for compatibility with the latest `sentence-transformers`
- `tokenizers` must be between versions 0.21 and 0.22

These dependencies are automatically installed when you run `pip install -e .`

## License

[Xay Hanmonty]

## Acknowledgments

- This project uses the [LangChain](https://github.com/hwchase17/langchain) framework
- Hugging Face for embedding models
- MongoDB Atlas for vector database capabilities
