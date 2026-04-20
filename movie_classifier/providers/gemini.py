import os
from google import genai
from google.genai import types
from movie_classifier.providers.abstract_provider import Provider


class GeminiProvider(Provider):
    def __init__(self, model: str, api_version: str = "v1beta"):
        self.model = model
        self.api_version = api_version

        assert os.environ.get("GEMINI_API_KEY") is not None, (
            "Please provide a Gemini API Key."
        )

        self.client = genai.Client(
            api_key=os.environ["GEMINI_API_KEY"],
            http_options=types.HttpOptions(api_version=self.api_version),
        )

    def invoke(self, summary: str, system_prompt: str) -> str:
        contents = system_prompt.format(summary)
        response = self.client.models.generate_content(
            model=self.model, contents=contents
        )
        return response.text
