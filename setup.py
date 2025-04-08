from setuptools import setup, find_packages

setup(
    name="xay_second_brain",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "loguru>=0.7.0",
        "pydantic>=2.0.0",
        "pydantic-settings>=2.0.0",
        "langchain-mongodb>=0.1.0",
        "pymongo>=4.0.0",
        "langchain-huggingface>=0.0.2",
        "sentence-transformers>=2.7.0",
        "transformers==4.51.1",
        "tokenizers<0.22,>=0.21",
        "litellm>=1.0.0",
        "click>=8.0.0",
    ],
    python_requires=">=3.9",
    entry_points={
        "console_scripts": [
            "run-ingestion=tools.run_data_ingestion_pipeline:main",
        ],
    },
)
