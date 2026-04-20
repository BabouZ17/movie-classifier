from movie_classifier.providers.abstract_provider import Provider
from enum import Enum


class Theme(str, Enum):
    WESTERN = "Western"
    SCIENCE_FICTION = "Science Fiction"
    HISTORY = "History"
    WAR = "War"
    DRAMA = "Drama"
    ROMANCE = "Romance"
    SURVIVAL = "Survival"
    DARK = "Dark"
    HORROR = "Horror"
    OTHER = "Other"

    @classmethod
    def values(cls) -> list[str]:
        return [member.value for member in cls]


class DefaultClassifier:
    def __init__(self, provider: Provider):
        self.provider = provider

    @property
    def system_prompt(self) -> str:
        return (
            "You are a movie expert. Base on the user summary of"
            "a movie, you will classify the main theme of the movie."
            f"Available labels are as follow: ${','.join(Theme.values())}"
            "When providing an answer, use only one of the label."
            "The user summary:\n{}"
        )

    def classify(self, summary: str) -> Theme:
        response = self.provider.invoke(
            summary=summary, system_prompt=self.system_prompt
        )
        return Theme(response)
