from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.llms import HuggingFaceHub
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains.question_answering import load_qa_chain
import os
import sys


def load_documents(file_path):
    loader = TextLoader(file_path)
    documents = loader.load()
    return documents


def create_vector_store(docs):
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    texts = text_splitter.split_documents(docs)

    # Updated Embeddings using huggingface
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    vectorstore = FAISS.from_documents(texts, embeddings)
    return vectorstore


def start_rag_chat(query):
    docs = load_documents("rag_engine/data.txt")
    vectorstore = create_vector_store(docs)

    relevant_docs = vectorstore.similarity_search(query)

    # Using HuggingFaceHub model (or replace with any local/custon LLM if needed)
    llm = HuggingFaceHub(repo_id="google/flan-t5-base", model_kwargs={"temperature": 0.5, "max_length": 512})

    chain = load_qa_chain(llm, chain_type="stuff")
    result = chain.run(input_documents=relevant_docs, question=query)

    return result


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide a query as an argument.")
        sys.exit(1)

    user_input = sys.argv[1]
    answer = start_rag_chat(user_input)
    print("\nAnswer:", answer)