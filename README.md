# Ask Query with External Website URLs using LangChain Ollama LLMs with Streamlit App

## Overview

This project showcases a Streamlit application integrated with LangChain Ollama LLMs to handle queries related to external website URLs. The application allows users to interact with an AI model that processes and generates responses based on content from specified URLs. The system is designed to provide an interactive and efficient way to query and retrieve information from various web sources.

## Features

- **Query Handling**: Ask questions about external website content.
- **LangChain Integration**: Utilizes LangChain Ollama LLMs for generating responses based on external website data.
- **Streamlit Interface**: Provides a user-friendly web interface for easy interaction and query management.
- **External URL Processing**: Fetches and processes content from specified URLs for querying.

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/PynaPavani/ask-query-external-urls.git
   ```

2. **Navigate to the Project Directory**

   ```bash
   cd ask-query-external-urls
   ```

3. **Install Required Packages**

   It is recommended to use a virtual environment. Install the dependencies using:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the Streamlit App**

   Start the Streamlit application using:

   ```bash
   streamlit run app.py
   ```

2. **Interact with the Application**

   Open your browser and navigate to `http://localhost:8501` to access the Streamlit interface. Enter your queries and provide URLs as needed.


## Dependencies

- **Streamlit**: For building the web interface.
- **LangChain Ollama LLMs**: For processing queries and generating responses.
- **Requests**: For fetching content from external URLs.

Refer to `requirements.txt` for a complete list of dependencies.
