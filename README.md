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

## Evaluation
Run `evals.py` to test system performance:
```bash
python evals.py
```

## Future Work
- Optimize vector database for caching previously solved problems.
- Expand agent capabilities to handle multi-step calculations.
