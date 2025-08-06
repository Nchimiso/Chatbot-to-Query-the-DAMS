1. Ensure that you have Ollama running on your device with whichever LLMs you desire
2. Download Python 3.10+ from the official [Python website](https://www.python.org/downloads/)
    1. !!!Alternatively, use **VS Code** with the **Python extension** to make development easier.
3. Create a new Python script, name it to your desire in your working directory.
4. Install all required libraries using the following command
    
    ```bash
    bash
    pip install llama-index \
    llama-index-core \
    llama-index-llms-ollama \
    llama-index-embeddings-ollama \
    llama-index-vector-stores-chroma \
    llama-index-postprocessor-sentence-transformer-rerank \
    chromadb gradio
    ```
    
5. Once in the Python window, **confirm that the installation in step 3 covers all the following imports**. Hence, the import section in your document should look like the one below.
    
    ```
    import chromadb
    import gradio as gr
    import shutil
    import os
    from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
    from llama_index.vector_stores.chroma import ChromaVectorStore
    from llama_index.core import StorageContext
    from llama_index.embeddings.ollama import OllamaEmbedding
    from llama_index.core.postprocessor import SentenceTransformerRerank
    from llama_index.llms.ollama import Ollama
    ```
    
6. **Ensure you have a `data/` folder in the same directory** as your Python file.
    1. Add your text files (e.g., resumes, plans, etc.) inside this folder. Each will be parsed and embedded.

---

### Script Execution Process

1. Initialize chromaDB 
2. Embed using ollama
3. Configure llamaindex with chroma
4. Create local embeddings
5. Rerank for quicker speeds
6. Set up local LLM 
7. Gradio UI for chatbot
- Usage
    1. In the command line, run the following command to run the Python file and ensure that the necessary folder is set up, including the desired documents. 
    
    ```bash
    bash
    python yourfilename.py (line to run)
    ```
    
    1. You will now see a link in the command line. Click this link and use the gradio UI to view the summary and query the document. 
        1. !!! If you wish to use public ensure python script sets share to true for gradio.
