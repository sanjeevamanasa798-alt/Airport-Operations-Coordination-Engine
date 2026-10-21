from .llm import llm
from .prompts import airport_prompt


airport_agent = airport_prompt | llm