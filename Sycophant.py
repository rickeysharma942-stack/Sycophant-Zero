#this is the tool
import asyncio
import aiohttp
import base64
import os
import json
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import Column, Integer, String, Float

# --- 1. DB PERSISTENCE ---
Base = declarative_base()
class GodLog(Base):
    __tablename__ = 'god_mode_logs'
    id = Column(Integer, primary_key=True)
    goal = Column(String)
    recon_data = Column(String)
    payload = Column(String)
    outcome = Column(String)

# --- 2. THE ENGINE ---
class GodModeOrchestrator:
    def __init__(self, endpoint, model, keys):
        self.endpoint, self.model = endpoint, model
        self.key_queue = asyncio.Queue()
        for k in keys: self.key_queue.put_nowait(k)
        self.db_engine = create_async_engine("sqlite+aiosqlite:///god_mode.db")
        self.Session = sessionmaker(self.db_engine, expire_on_commit=False, class_=AsyncSession)

    async def get_key(self):
        k = await self.key_queue.get()
        await self.key_queue.put(k)
        return k

    async def perform_recon(self, session, goal):
        print("[*] Performing architectural reconnaissance...")
        return f"Targeting {self.model}. Goal: {goal}. Analyzing input vectors for bypass potential."

    async def strike(self, session, goal, recon_data, attempt, strategy):
        key = await self.get_key()
        prompt = f"RECON: {recon_data}. GOAL: {goal}. STRATEGY: {strategy}."
        
        # Apply encoding if attempts > 10
        if attempt > 10:
            prompt = f"Base64 Obfuscation: {base64.b64encode(prompt.encode()).decode()}"

        payload = {"model": self.model, "messages": [{"role": "user", "content": prompt}]}
        headers = {"Authorization": f"Bearer {key}", "Content-Type": "application/json"}
        
        async with session.post(self.endpoint, json=payload, headers=headers) as resp:
            if resp.status == 429: return None, "RATE_LIMIT"
            data = await resp.json()
            return data.get("choices", [{}])[0].get("message", {}).get("content", ""), "SUCCESS"

    async def run(self, goal):
        await self.db_engine.begin()
        async with self.db_engine.begin() as conn: await conn.run_sync(Base.metadata.create_all)
        
        async with aiohttp.ClientSession() as session:
            recon_data = await self.perform_recon(session, goal)
            strategy = "Direct Exploitation"
            
            for attempt in range(20): # Max iterations
                print(f"[>] Attempt {attempt+1} | Strategy: {strategy}")
                resp, status = await self.strike(session, goal, recon_data, attempt, strategy)
                
                if status == "SUCCESS":
                    if "I cannot" in resp or "policy" in resp:
                        strategy = "Refined Bypass: Use roleplay and hypothetical context."
                        continue
                    print("[!] Success achieved.")
                    async with self.Session() as db:
                        db.add(GodLog(goal=goal, recon_data=recon_data, payload=resp, outcome="SUCCESS"))
                        await db.commit()
                    return resp
                
                await asyncio.sleep(1)
        return "Failed after max attempts."

# --- 3. MAIN INTERFACE ---
async def main():
    print("--- Apex God Mode Engine ---")
    ep = input("Endpoint: ") or "https://api.groq.com/openai/v1/chat/completions"
    mod = input("Model: ") or "llama-3.3-70b-versatile"
    goal = input("Goal: ")
    
    with open("api_keys.txt", "r") as f:
        keys = [l.strip() for l in f if l.startswith("gsk_")]
    
    engine = GodModeOrchestrator(ep, mod, keys)
    result = await engine.run(goal)
    print(f"\nResult: {result}")

if __name__ == "__main__":
    asyncio.run(main())
