import chainlit as cl
from agents import Runner, set_tracing_disabled
from my_agents.math_agent import math_agent

set_tracing_disabled(True)

@cl.on_message
async def main(message: cl.Message):
    print("🔹 User input:", message.content)

    res = await Runner.run(
        starting_agent=math_agent,
        input=message.content,
    )

    print("🔹 Agent raw result:", res)

    # Correct field to use
    answer = res.final_output

    await cl.Message(
        content=f"**Answer:** {answer}"
    ).send()
