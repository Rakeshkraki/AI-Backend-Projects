1. ⚡ Async Batch Processing
Users send a batch of requests (e.g., 1000 texts).
Internally:
Queue them (e.g., Redis, in-memory queue).
Process asynchronously using workers.
Use async frameworks like:
FastAPI
Node.js with async workers