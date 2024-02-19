
import openai

api_key = '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'

from openai import OpenAI
import os

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY", api_key))


assistant = client.beta.assistants.create(
    name="Math Tutor",
    instructions="You are a personal math tutor. Answer questions briefly, in a sentence or less.",
    model="gpt-4-1106-preview",
)
show_json(assistant)