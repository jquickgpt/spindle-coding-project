# Spindle Coding Project

## Overview
This project implements a **multi-agent system** that solves math problems given in **natural language** using OpenAI's API for parsing and **deterministic local math tools** for computation.

## Demo Video
Watch the demo video [here](https://www.loom.com/share/8e739cbb2108453297701999ed843e81?sid=abe5739f-abe1-4d6f-adee-6dffed3baae0).

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

## Evaluation
Run `evals.py` to test system performance:
```bash
python evals.py
```

## Project Structure Diagram
```
multi-agent-math-solver/
│── src/
│   ├── agents/
│   │   ├── planner.py
│   │   ├── executor.py
│   │   ├── error_handler.py
│   ├── tools/
│   │   ├── math_tools.py
│   ├── utils/
│   │   ├── vector_db.py
│── tests/
│── docs/
│   ├── architecture.md
│   ├── project_structure.md
│── models/
│── data/
│── notebooks/
│── main.py
│── evals.py
│── requirements.txt
│── README.md
│── .env
│── project_structure.py
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

## Tradeoffs

### Redundant Computation  
#### Why We Use Redundant Computation  
Redundant computation ensures **high reliability** by executing each math operation **100 times** and selecting the most common result. This method reduces the impact of silent failures, particularly with the unreliable tool that fails 40% of the time.  

#### Tradeoffs  
**Advantages**  
- **Fault Tolerance** → Silent failures are mitigated using majority voting.  
- **Increased Accuracy** → The probability of a correct result is over **97%**, even with a faulty tool.  

**Disadvantages**  
- **Performance Overhead** → Executing **100 trials per operation** increases computational load.  
- **Latency Concerns** → The increased processing time can impact real-time use cases.  

#### Future Optimization  
- Implement **adaptive redundancy**, dynamically adjusting the number of trials based on error rate.  
- Explore alternative **error detection mechanisms** to reduce redundant trials when unnecessary.  

---

### Number of Agents  
#### Tradeoffs Between 2, 3, 4, or 5 Agents  
We chose a **three-agent architecture** instead of 2, 4, or 5 agents based on the **optimal balance of modularity and efficiency**.  

#### Why Not 2 Agents?  
- **Less modularity** → A two-agent system would require combining multiple responsibilities, reducing **separation of concerns**.  
- **Increased complexity in error handling** → A single agent would have to manage execution and validation, making debugging more difficult.  

#### Why Not 4 or 5 Agents?  
- **Higher inter-agent communication overhead** → More agents require **additional message-passing logic**, increasing complexity.  
- **Unnecessary duplication** → The core functionality of parsing, execution, and error handling is **efficiently handled with 3 agents**.  

#### Why 3 Agents?  
- **Planner Agent** → Handles natural language parsing with OpenAI API.  
- **Executor Agent** → Runs deterministic math tools and ensures redundant computation.  
- **Error Handler Agent** → Detects and mitigates incorrect or unreliable results.  
- **Balanced Design** → Ensures clarity, efficiency, and maintainability.  

---

### Choosing `gpt-4o-mini` for OpenAI API  
We selected `gpt-4o-mini` as our model due to **its efficiency, cost-effectiveness, and performance** compared to other OpenAI models.  

#### Tradeoffs and Comparison  

| **Model**          | **Latency** | **Cost Efficiency** | **Accuracy** | **Best Use Case** |
|------------------|------------|----------------|------------|----------------|
| **`gpt-4o-mini`** | Low        | High (low cost) | Moderate   | Fast, lightweight parsing tasks |
| **`gpt-4o`**     | Moderate   | Medium         | High       | General AI assistance |
| **`gpt-4-turbo`** | Higher     | Lower         | Very High  | Complex reasoning tasks |

#### Why `gpt-4o-mini`?  
- **Fastest Response Time** → Essential for real-time parsing.  
- **Lower Cost** → Reduces API usage costs while maintaining acceptable accuracy.  
- **Sufficient Accuracy for Parsing** → The model is optimized for extracting structured math expressions from natural language.  

#### Future Considerations  
- We may **upgrade to `gpt-4o`** if parsing quality needs improvement.  
- If advanced reasoning becomes necessary, we could evaluate `gpt-4-turbo` for complex multi-step calculations.  


## Future Work and Product Roadmap

### Phase 1: Foundation Enhancements

**Enhanced Error Recovery**  
- Implement dynamic retry strategies and fallback algorithms.  
- Set adaptive error thresholds to trigger user input when necessary.

**Advanced Tool Functionality**  
- Introduce additional math operations (e.g., integration, differentiation).

**Vector Database Improvements**  
- Transition from in-memory storage to a persistent, lightweight database.  
- Optimize cosine similarity search for improved performance.

---

### Phase 2: Agent and Interface Expansion

**Agent Expansion**  
- Add sub-agents for logging, monitoring, and analytics.  
- Enhance inter-agent communication protocols for smoother collaboration.

**User Interface Enhancements**  
- Develop a dashboard for real-time monitoring of system performance and error recovery.  
- Incorporate visualizations that clearly display tool-call sequences and agent decisions.

---

### Phase 3: Scalability and Security Optimization

**Scalability and Performance**  
- Implement parallel processing and asynchronous tool calls to manage increased load.  
- Evaluate distributed computing options as needed.

**Security and Robustness**  
- Enhance API key management and secure system access.  
- Strengthen input validation and introduce safeguards against malicious inputs.

---

### Phase 4: Domain Expansion and Continuous Improvement

**Broader Domain Applications**  
- Adapt the system architecture to solve problems in areas beyond math.  
- Pilot new tool types and test cross-domain functionalities.

**Continuous Monitoring and Improvement**  
- Refine logging and monitoring strategies based on performance data.  
- Actively solicit user feedback to drive iterative improvements.

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


