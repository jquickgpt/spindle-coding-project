# Multi-Agent Math Solver

## Overview
This project implements a **multi-agent system** that solves math problems given in **natural language** using OpenAI's API for parsing and **deterministic local math tools** for computation.

## Installation

### 1. Clone the Repository
```bash
git clone <repository-url>
cd multi-agent-math-solver
```

### 2. Create Virtual Environment
```bash
python -m venv env
source env/Scripts/activate  # Windows
source env/bin/activate      # macOS/Linux
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Up OpenAI API Key
Create a `.env` file in the project root and add:
```plaintext
OPENAI_API_KEY=your_api_key_here
```

## Usage
Run the program:
```bash
python main.py
```
Enter a math problem in natural language (e.g., "three plus four"), and the system will return a structured JSON response.

Type `exit` to quit.

## System Components
- **Planner Agent (`planner.py`)** – Uses OpenAI API to parse user input.
- **Executor Agent (`executor.py`)** – Runs deterministic math tools with redundant computation.
- **Error Handler (`error_handler.py`)** – Detects failures and ensures reliability.
- **Vector Database (`vector_db.py`)** – Currently disabled due to retrieval issues.

## Evaluation
Run `evals.py` to test system performance:
```bash
python evals.py
```

## Known Issues
- **Cache Retrieval Disabled:** The system currently does not retrieve cached results due to incorrect FAISS mapping. This will be fixed in a future version.

## Next Steps / Future Work
- **Fix Cache Retrieval:** Ensure correct FAISS index mapping to properly store and retrieve problem embeddings.
- **Optimize Vector Database:** Improve storage efficiency and retrieval performance.
- **Enable Multi-Step Calculations:** Expand system capabilities beyond single operations.
- **Performance Improvements:** Reduce API calls through better caching and batch processing.
