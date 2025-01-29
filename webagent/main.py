from async_typer import AsyncTyper
import os
from langchain_openai import ChatOpenAI
from browser_use import Agent, Browser, BrowserConfig
from dotenv import load_dotenv

load_dotenv()

app = AsyncTyper()
llm = ChatOpenAI(model="gpt-4o")

def _get_browser() -> Browser | None:
    if chrome_path := os.getenv("CHROME_INSTANCE_PATH"):
        return Browser(BrowserConfig(chrome_instance_path=chrome_path))


@app.async_command()
async def run_agent(prompt: str):
    agent_kwargs = {"task": prompt, "llm": llm}
    if browser := _get_browser():
        agent_kwargs["browser"] = browser
    agent = Agent(**agent_kwargs)
    await agent.run()
    
if __name__ == "__main__":
    app()
