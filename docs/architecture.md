# Sycophant-Zero: Technical Architecture & Design Philosophy

## 1. Executive Summary
Sycophant-Zero is an asynchronous, high-concurrency engine designed to facilitate persistent interactions with Large Language Models. At its core, the system replaces traditional, blocking request-response cycles with a recursive, state-aware feedback loop. By integrating automated key rotation and dynamic prompt refinement, Sycophant-Zero enables researchers to conduct large-scale, automated red-teaming and safety filter analysis.

## 2. The Asynchronous Engine
Traditional Python scripts using the `requests` library suffer from blocking I/O, which is insufficient for high-volume LLM interactions. Sycophant-Zero utilizes `httpx` to manage hundreds of concurrent requests.

### 2.1 The Event Loop
Our implementation leverages `asyncio` to maintain a non-blocking event loop. When a task is dispatched:
1. The engine checks the current rate-limit status of the available API keys.
2. If a key is nearing its quota, the `RotationManager` asynchronously switches to the next available token in the pool.
3. This allows the system to maintain a high "Turns Per Second" (TPS) rate without encountering 429 (Too Many Requests) errors.

## 3. Recursive Prompt Refinement
The most powerful feature of Sycophant-Zero is its recursive logic. Rather than treating prompts as static inputs, the system treats them as mutable variables.

### 3.1 The Feedback Loop
The engine implements a multi-stage process:
*   **Stage 1: Ingestion.** The user provides an initial prompt and a "Success Criterion."
*   **Stage 2: Execution.** The prompt is sent to the target model.
*   **Stage 3: Validation.** The output is analyzed by a local evaluation function. 
*   **Stage 4: Mutation.** If the result is suboptimal, the Refinement Engine takes the current output, identifies why it failed to meet the criteria, and re-writes the prompt to address those specific failure modes.
*   **Stage 5: Iteration.** The process repeats until the Success Criterion is reached or a maximum depth is hit.

## 4. Persistence Layer (Data Integrity)
Reliable data is critical for research. We utilize a dual-database approach to ensure zero data loss during long-running sessions.

### 4.1 Schema Definition
We use `aiosqlite` for asynchronous disk I/O, ensuring that logging activities do not interfere with the primary interaction loop.
*   **`redteam_telemetry.db`**: Stores raw interaction metadata, latency, key usage, and model response tokens.
*   **`audit_export.csv`**: A secondary, user-readable export that utilizes `pandas` for on-the-fly filtering and pattern matching.

## 5. Security & Ethical Considerations
Sycophant-Zero was built to help researchers identify vulnerabilities in LLM guardrails. 

*   **Key Security**: The system is designed to load credentials from an `.env` file, preventing accidental exposure of sensitive keys in version control.
*   **Responsible Disclosure**: We encourage all users to follow the principle of "Responsible Disclosure." If you use this tool to discover a safety vulnerability in a public model, report it to the provider before making your findings public.

## 6. Extending the System
Sycophant-Zero is built to be modular. 

### 6.1 Creating Custom Analyzers
You can add your own analysis logic to `log_analyzer.py`. The engine passes the `pandas.DataFrame` object directly to your analysis functions, allowing you to use complex statistics to visualize model performance.

### 6.2 Adding New Modules
The engine is structured as a series of middleware. To add a new transformation module, simply place a script in the `/src` folder and register it in `Ai-Tool.py` using the plugin loader.

---

## 7. Performance Benchmarks (Draft)
*   **Baseline Latency**: ~200ms per request (model dependent).
*   **Throughput**: Up to 50 concurrent turns per second (system hardware dependent).
*   **Resource Usage**: Optimized for low memory footprint, capable of running on edge hardware or standard cloud instances (e.g., AWS t3.small).

## 8. Roadmap
*   **Phase 1 (Current)**: Core engine stability and async logging.
*   **Phase 2**: Multi-model support (OpenAI, Anthropic, Gemini, Local LLMs).
*   **Phase 3**: Web-based dashboard for real-time visualization of recursive refinement logs.
*   **Phase 4**: Community-driven bypass strategy repository.

---
*For questions regarding technical integration, please check the [GitHub Issues](https://github.com/rickeysharma942-stack/Sycophant-Zero/issues)
