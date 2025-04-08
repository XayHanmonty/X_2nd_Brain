from langchain_huggingface import HuggingFaceEmbeddings
import os
from pathlib import Path

def get_embedding_model(
    model_id: str,
    device: str = "cpu",
) -> HuggingFaceEmbeddings:
    """Gets an instance of the HuggingFace embedding model.

    Args:
        model_id (str): The ID/name of the HuggingFace embedding model to use
        device (str, optional): The device to use for the embedding model. Defaults to "cpu"

    Returns:
        HuggingFaceEmbeddings: A HuggingFace embedding model instance
    """
    # Set cache directory to a location within the project where we definitely have write permissions
    current_dir = Path(__file__).parent.parent.parent  
    cache_dir = current_dir / "data" / "model_cache"
    os.makedirs(cache_dir, exist_ok=True)
    
    return HuggingFaceEmbeddings(
        model_name=model_id,
        cache_folder=str(cache_dir),
        model_kwargs={"device": device},
        encode_kwargs={"normalize_embeddings": True},
    )
