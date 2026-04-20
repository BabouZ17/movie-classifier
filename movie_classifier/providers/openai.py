import os
from openai import OpenAI
from movie_classifier.providers.abstract_provider import Provider


class OpenAIProvider(Provider):
    def __init__(self, model: str):
        self.model = model

        assert os.environ.get("OPENAI_API_KEY") is not None, (
            "Please provide an OpenAI API Key."
        )

        self.client = OpenAI()

    def invoke(self, summary: str, system_prompt: str) -> str:
        response = self.client.responses.create(
            model=self.model, instructions=system_prompt, input=summary
        )
        return response.output_text
