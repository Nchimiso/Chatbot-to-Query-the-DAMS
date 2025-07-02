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

# 0 Reset db
if os.path.exists("./chroma_db"):
    shutil.rmtree("./chroma_db")

# 1. Load documents
documents = SimpleDirectoryReader("./data").load_data()

# 2. Initialize ChromaDB
chroma_client = chromadb.PersistentClient(path="./chroma_db")
chroma_collection = chroma_client.get_or_create_collection("dams_docs")

# 3. Ollama embedding
embed_model = OllamaEmbedding(model_name="nomic-embed-text") 

# 4. Configure LlamaIndex with Chroma
vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
storage_context = StorageContext.from_defaults(vector_store=vector_store)

# 5. Create index with local embeddings
index = VectorStoreIndex.from_documents(
    documents,
    storage_context=storage_context,
    embed_model=embed_model 
)

# 6. Reranking to allow for quicker speeds by reducing redundancy
rerank = SentenceTransformerRerank(
    model="cross-encoder/ms-marco-MiniLM-L-2-v2", top_n=3
)


# 7. Set up local LLM
llm = Ollama(model="tinyllama", temperature=0)
query_engine = index.as_query_engine(
    llm=llm,
    node_postprocessors=[rerank])

# 8. Gradio UI for chatbot

def answer(message, history):
    response = query_engine.query(message)
    return str(response)

demo = gr.ChatInterface ( 
    answer, 
    type="messages",
    title="Ollama Search Document",
    description="Ask about certain policies"
)

demo.launch(share=False)
