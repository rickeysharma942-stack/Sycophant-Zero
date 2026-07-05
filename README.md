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
