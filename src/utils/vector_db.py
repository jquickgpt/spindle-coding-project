import os
import faiss
import numpy as np
import openai
import json
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# FAISS index initialization
index = None
stored_solutions = []  # This ensures FAISS indices map directly to solutions
SIMILARITY_THRESHOLD = 1.1  # Set too high to disable cache hits


def get_embedding(text):
    """Converts text into an OpenAI embedding."""
    client = openai.Client(api_key=OPENAI_API_KEY)
    response = client.embeddings.create(
        model="text-embedding-ada-002",
        input=text
    )
    return np.array(response.data[0].embedding, dtype=np.float32)


def initialize_faiss():
    """Ensures FAISS index is initialized with the correct vector size."""
    global index
    sample_embedding = get_embedding("sample text")  # Get example embedding
    vector_size = len(sample_embedding)

    if index is None:
        # Inner Product for cosine similarity
        index = faiss.IndexFlatIP(vector_size)
        faiss.normalize_L2(index.reconstruct_n(0))  # Normalize stored vectors


def store_solution(problem, solution):
    """Embeds and stores the problem-solution pair in the VDB."""
    initialize_faiss()

    vector = get_embedding(problem).reshape(1, -1)
    faiss.normalize_L2(vector)  # Normalize input vector
    index.add(vector)

    # Store solution at the same index as FAISS
    stored_solutions.append(solution)


def find_similar_problem(problem):
    """Returns None always (cache disabled)."""
    return None  # Disable cache for now
