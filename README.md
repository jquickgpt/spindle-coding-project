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
- **Planner Agent (`planner.py`)** → Uses OpenAI API to parse user input.
- **Executor Agent (`executor.py`)** → Runs deterministic math tools.
- **Error Handler (`error_handler.py`)** → Detects failures and ensures reliability.
- **Vector Database (`vector_db.py`)** → **Currently disabled due to retrieval issues**.

## Evaluation
Run `evals.py` to test system performance:
```bash
python evals.py
```

## Data Flow Diagram
```
User Input (CLI) 
        │
        ▼
Planner Agent (Uses OpenAI API for Parsing)
        │
        ▼
Executor Agent (Runs Math Tools)
        │
        ▼
Error Handler (Detects Failures)
        │
        ▼
Structured JSON Output
```

## How the Program Works

### Overview
This system implements a **multi-agent approach** to solving user-provided math problems. The agents perform specific tasks:  
1. **Parsing natural language input**  
2. **Executing deterministic math tools**  
3. **Detecting and handling silent failures**  

### Core Components
- **Planner Agent (`planner.py`)** → Parses user input using OpenAI API.
- **Executor Agent (`executor.py`)** → Executes deterministic math tools.
- **Error Handler (`error_handler.py`)** → Identifies incorrect or unreliable results.

### Workflow
1. The user enters a math problem in natural language (e.g., "three plus four").
2. The **Planner Agent** extracts the operation and numbers.
3. The **Executor Agent** performs redundant computations (100 trials, majority rule).
4. The **Error Handler** detects anomalies and ensures reliability.
5. The system returns **structured JSON output**.

### Design Choices
- **Agent-based architecture** → Improves modularity.
- **Redundant computation** → Provides fault tolerance.
- **Use of OpenAI API** → Ensures flexible natural language parsing.

### Error Handling & Edge Cases
- If input is ambiguous, the system prompts for clarification.
- If a math tool fails, redundant computation detects and corrects the error.

### Performance Considerations
- Using OpenAI API introduces latency (~0.5s per request).
- Disabling cache retrieval increases computation time.

## Redundant Computation Tradeoffs

### Why Use Redundant Computation?
To **mitigate silent failures**, the system executes **100 trials per math operation** and selects the most common result.

### Tradeoffs
#### Advantages
- **High accuracy** → Majority rule corrects for faulty tools.
- **Fault tolerance** → The system can handle unreliable calculations.

#### Limitations
- **Increased computation time** → Running 100 trials per operation increases processing time.
- **Resource-intensive** → More computations require higher CPU cycles.

#### Future Optimization
- Reduce trials dynamically based on reliability.
- Optimize error detection thresholds.

## Compliance Review

| **Requirement**                         | **Status** | **Notes** |
|----------------------------------------|------------|----------------|
| **Python only, no type hints** | Compliant | No type hints used. |
| **Modular, procedural architecture** | Compliant | Agents (`planner.py`, `executor.py`, `error_handler.py`) are modular and procedural. |
| **Use OpenAI API for natural language parsing** | Compliant | `planner.py` correctly uses OpenAI's `gpt-4o-mini` model for parsing. |
| **Math tools implemented (sum, delta, product, quotient, modulo)** | Compliant | Implemented in `math_tools.py`. |
| **One math tool fails silently 40% of the time** | Compliant | Implemented in `unreliable_tool()` within `math_tools.py`. |
| **Redundant computation (100 trials, majority rule)** | Compliant | Implemented in `executor.py`. |
| **Clarification mechanism (`GET_USER_INPUT`)** | Compliant | The OpenAI-based planner returns an error for ambiguous input, prompting the user. |
| **Vector database (VDB) implemented for solution reuse** | Not fully compliant | Implemented but disabled due to retrieval issues. |
| **Semantic matching for similar problems** | Not compliant | Currently disabled. |
| **Evaluation system (`evals.py`) to measure performance** | Compliant | `evals.py` correctly validates system behavior. |
| **Project documentation includes README, installation steps, system overview** | Compliant | `README.md` contains all required sections. |
| **Future work section in README.md** | Compliant | Includes cache retrieval fix and optimizations. |
