from argparse import ArgumentParser
from movie_classifier.utils.load_config import load_config

from movie_classifier.providers.gemini import GeminiProvider

# from movie_classifier.providers.openai import OpenAIProvider
from movie_classifier.classifiers.classifier import DefaultClassifier
from pathlib import Path


if __name__ == "__main__":
    config_path = Path(__file__).parent / "config/config.json"
    config = load_config(config_path)

    parser = ArgumentParser(
        prog="Movie Classifier",
        description="Give a summary of a movie and the tool shall classify the movie main theme.",
    )
    parser.add_argument("summary")
    args = parser.parse_args()

    gemini = GeminiProvider(
        model=config["gemini"]["model"],
    )
    # openai = OpenAIProvider(model=config["openai"]["model"])
    classifier = DefaultClassifier(provider=gemini)
    response = classifier.classify(args.summary)
    print(response)
