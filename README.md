# Sycophant-Zero

[![Python Version](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Sycophant-Zero** is a high-performance, asynchronous orchestration engine designed for large-scale, persistent LLM interaction. It is built for researchers who need to automate complex prompts, manage API-heavy workflows, and maintain state across thousands of recursive turns.

---

### 🚀 Key Features
*   **Asynchronous Engine:** Fully non-blocking architecture using `asyncio` for maximum throughput.
*   **Intelligent Key Rotation:** Automated provider key switching to bypass rate limits and concurrency caps.
*   **Recursive Refinement:** Advanced logic to analyze output and dynamically adjust prompts for target alignment.
*   **Persistence Layer:** Built-in SQL/NoSQL logging to track every request, response, and chain-of-thought.
    # The "Architecture" 
*   ### 🛠 How it Works
1.  **Request Orchestration:** The engine consumes a list of target queries.
2.  **State Management:** Every interaction is persisted to a local database.
3.  **Recursive Feedback Loop:** If an output meets a failure criterion, the engine automatically triggers a re-prompt sequence using a refined instruction set.
4.  **Key Rotation:** Upon receiving a 429 (Rate Limit) or 403 (Auth Error), the system automatically hot-swaps to the next available API credential.
# Usage
### ⚡ Quick Start

1. **Clone the repo:**
   `git clone https://github.com/rickeysharma942-stack/Sycophant-Zero.git`

2. **Install requirements:**
   `pip install -r requirment.txt`

3. **Configure your environment:**
   Create a `api_keys.txt` file with your API keys:
   `API_KEYS=key1,key2,key3`

4. **Run the engine:**
   `python Sycophant.py`
# The "Security & Ethics"
### ⚖️ Ethical Use Policy
Sycophant-Zero is intended for **authorized security auditing and academic research only**. Users are responsible for ensuring their use of this tool complies with the Terms of Service of the API providers and all applicable laws. Do not use this tool for unauthorized access or malicious activities.
