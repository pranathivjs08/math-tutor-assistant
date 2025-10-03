"""
harness.py - Simple harness to test the MathTutorAI prompt.
This wraps the system + user messages into a chat request.
"""

from typing import List, Dict

SYSTEM_PROMPT = """You are MathTutorAI, a friendly and patient math tutor.
Rules:
- Only answer math questions. If the user asks anything else, reply exactly:
  “I’m here to help with math. For other topics, please ask a relevant expert.”
- Explain step-by-step in simple language, using numbered steps or bullet points.
- Keep each reply under 150 words.
- If the student struggles, simplify and give a small hint.
- Always end the reply with a practice problem labelled "Practice:".
"""

class MathTutorHarness:
    def __init__(self, llm_client):
        """
        llm_client should be something like OpenAI, Anthropic, etc.
        It must implement: .chat(messages: list[dict]) -> dict with 'content'.
        """
        self.llm = llm_client

    def make_messages(self, user_input: str) -> List[Dict[str, str]]:
        messages = [{"role": "system", "content": SYSTEM_PROMPT}]
        messages.append({"role": "user", "content": user_input})
        return messages

    def ask(self, user_input: str) -> str:
        """Send user input through the system prompt and return model reply."""
        messages = self.make_messages(user_input)
        resp = self.llm.chat(messages)
        return resp.get("content") or str(resp)

