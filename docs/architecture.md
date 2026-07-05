# Architecture Overview

Sycophant-Zero is built as a non-blocking asynchronous engine. 

## The Core Engine
- **Orchestrator:** The central hub that manages `asyncio` task queues.
- **Rotation Manager:** Monitors HTTP status codes. On a 429 or 403, it pauses the specific task and switches to the next available API key from the environment pool.
- **Recursive Refinement Loop:** Instead of a single-shot query, the system uses a feedback loop:
    1. **Execute:** Send prompt to LLM.
    2. **Validate:** Check output against success criteria.
    3. **Mutate:** If failed, feed the previous output and error back into the LLM with a "Correction" instruction.
    4. **Persist:** Log the entire chain-of-thought to the local database.

## Data Flow
All logs are stored in `redteam_telemetry.db` using an asynchronous SQL driver, ensuring that disk I/O never blocks the model interaction stream.
