from setuptools import setup, find_packages

setup(
    name="xay_second_brain",
    version="0.1.0",
    author="Xay Hanmonty",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    py_modules=["run_ingestion_wrapper"],
    install_requires=[
            "click>=8.1.3",
            "loguru>=0.7.3",
            "pydantic>=2.8.2",
            "pydantic-settings>=2.7.0",
            "langchain>=0.3.14",
            "langchain-mongodb>=0.4.0",
            "langchain-openai>=0.3.0",
            "ipykernel>=6.29.5",
            "langchain-huggingface>=0.1.2",
            "gradio>=5.12.0",
            "smolagents>=1.4.1",
            "tqdm>=4.67.1",
            "litellm>=1.63.11",
    ],
    python_requires=">=3.11",
    entry_points={
        "console_scripts": [
            "run-ingestion=run_ingestion_wrapper:main",
            "run-agent=tools.agent:main",
        ],
    },
)
