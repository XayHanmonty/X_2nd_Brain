#!/usr/bin/env python3
"""
Wrapper script to run the data ingestion pipeline with proper imports.
"""
import sys
import os

# Add the project root to the Python path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

# Now import and run the main function
from tools.run_data_ingestion_pipeline import main

if __name__ == "__main__":
    main()
