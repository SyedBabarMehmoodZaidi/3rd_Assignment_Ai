from agents import Agent, function_tool
from my_config.gemini_config import GEMINI_MODEL


@function_tool
def add(a: int, b: int) -> int:
    """Adds two numbers together"""
    return a + b


@function_tool
def multiply(a: int, b: int) -> int:
    """Multiplies two numbers together"""
    return a * b


math_agent = Agent(
    name="Math Agent",
    instructions="You are a helpful math assistant. Use tools for calculation.",
    model=GEMINI_MODEL,
    tools=[add, multiply],
)
