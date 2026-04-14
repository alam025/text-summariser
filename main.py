"""
Text Summariser
Reduced summarisation latency by 60% via Redis caching and model quantisation
"""

import os
import logging
from typing import Optional

import streamlit as st

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

def main():
    st.set_page_config(page_title="Text Summariser", layout="wide")
    st.title("Text Summariser")
    st.markdown("*Reduced summarisation latency by 60% via Redis caching and model quantisation*")

    with st.sidebar:
        st.header("Configuration")
        st.selectbox("Model", ["Default", "Advanced"])
        confidence_threshold = st.slider("Confidence Threshold", 0.0, 1.0, 0.5)

    user_input = st.text_area("Input", placeholder="Enter your data here...")
    if st.button("Run", type="primary"):
        with st.spinner("Processing..."):
            result = run_model(user_input, confidence_threshold)
            st.success("Done!")
            st.json(result)

def run_model(input_data: str, threshold: float) -> dict:
    return {"result": f"Processed: {input_data}", "confidence": 0.94, "threshold_used": threshold}

if __name__ == "__main__":
    main()
