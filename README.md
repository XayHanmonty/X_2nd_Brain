# AI Second Brain RAG System

My personal knowledge management system powered by MongoDB and RAG (Retrieval Augmented Generation).

## Overview

This system allows you to ingest, process, and retrieve knowledge from your personal documents using advanced NLP techniques. It creates vector embeddings of your documents and stores them in MongoDB for semantic search and retrieval.

## Features

- **Document Ingestion Pipeline**: Process JSON documents from a specified directory
- **Quality Assessment**: Filter documents using both heuristic and LLM-based approaches
- **Vector Embeddings**: Generate document embeddings using Hugging Face models
- **MongoDB Integration**: Store and index documents and embeddings for efficient retrieval
- **RAG Generation**: Answer questions using retrieved documents as context
- **CLI Interface**: Easy-to-use command line tools for data ingestion and generation

## System Requirements

- **Python**: Version 3.11+ (required for compatibility with dependencies)
- **MongoDB Atlas**: Account with vector search capabilities
- **OpenAI API Key**: For LLM-based document filtering and generation

## Installation

1. Clone the repository:
   ```bash
   git clone <your-repository-url>
   cd xay_second_brain
   ```

2. Ensure you have Python 3.11+ installed:
   ```bash
   python --version
   ```
   
   If you need to install Python 3.11+, you can use pyenv:
   ```bash
   # Install Python 3.11+ using pyenv
   pyenv install 3.11.7
   
   # Set local Python version for this project
   pyenv local 3.11.7
   ```

3. Create and activate a virtual environment:
   ```bash
   # Deactivate any existing virtual environments
   deactivate 2>/dev/null || true
   
   # Create a new virtual environment
   python -m venv venv
   
   # Activate the virtual environment
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. Install the package and dependencies:
   ```bash
   pip install -e .
   ```

5. Set up environment variables by creating a `.env` file in the project root:
   ```
   MONGODB_URI=your_mongodb_connection_string
   OPENAI_API_KEY=your_openai_api_key
   ```

## Usage

### Running the Data Ingestion Pipeline

The data ingestion pipeline processes documents, generates embeddings, and stores them in MongoDB.

```bash
# Run the ingestion pipeline
python tools/run_data_ingestion_pipeline.py
```

By default, the pipeline will look for documents in the `data/rag` directory relative to the project root. You can specify a different directory:

```bash
# Specify a custom documents directory
python tools/run_data_ingestion_pipeline.py --documents-dir /path/to/your/documents
```

### Running the Data Generation Pipeline

The data generation pipeline answers questions using the RAG (Retrieval Augmented Generation) approach:

```bash
# Run the generation pipeline
python tools/run_data_generation_pipeline.py
```

This will run the default set of questions. You can modify the questions in the script or create your own interface to interact with the RAG system.

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

- **Embedding Model**: Selection and parameters for text embedding models
- **MongoDB Connection**: URI, database name, and collection settings
- **Quality Assessment**: Thresholds for document filtering
- **Device Settings**: CPU/GPU configuration for model inference

## Project Structure

```
xay_second_brain/
├── data/
│   └── rag/                  # Default directory for JSON documents
├── src/
│   └── rag/
│       ├── config.py         # Configuration settings
│       ├── embedding.py      # Text embedding functionality
│       ├── generation.py     # RAG generation chain
│       ├── ingestion.py      # Document ingestion pipeline
│       ├── mongodb.py        # MongoDB integration
│       ├── retriever.py      # Document retrieval functionality
│       └── splitter.py       # Text splitting utilities
├── tools/
│   ├── run_data_ingestion_pipeline.py    # CLI for document ingestion
│   └── run_data_generation_pipeline.py   # CLI for question answering
├── setup.py                  # Package configuration
└── .env                      # Environment variables (create this file)
```

## Dependency Notes

The project requires specific versions of certain packages to ensure compatibility:
- Python 3.11+ is required for the latest dependencies
- `transformers` version 4.51.1 is required for compatibility with the latest `sentence-transformers`
- `tokenizers` must be between versions 0.21 and 0.22

These dependencies are automatically installed when you run `pip install -e .`

## Troubleshooting

### Common Issues

1. **ModuleNotFoundError: No module named 'rag'**
   - Make sure you're running scripts from the project root directory
   - Ensure the package is installed with `pip install -e .`

2. **Path 'data/rag' does not exist**
   - Create the directory: `mkdir -p data/rag`
   - Or specify a different directory with the `--documents-dir` option

3. **MongoDB Connection Issues**
   - Verify your MongoDB URI in the `.env` file
   - Ensure your IP address is whitelisted in MongoDB Atlas

4. **OpenAI API Key Issues**
   - Check that your OpenAI API key is valid and has sufficient credits
   - Verify the key is correctly set in the `.env` file

## License

[Xay Hanmonty]

## Acknowledgments

- This project uses the [LangChain](https://github.com/hwchase17/langchain) framework
- Hugging Face for embedding models
- MongoDB Atlas for vector database capabilities
- OpenAI for language model capabilities
