"""Detect email addresses with Presidio, then replace detected spans."""

import argparse

from presidio_analyzer import AnalyzerEngine
from presidio_analyzer.nlp_engine import NlpEngineProvider
from presidio_anonymizer import AnonymizerEngine


DEFAULT_TEXT = "Contact Ada at ada@example.com."


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--text", default=DEFAULT_TEXT, help="Synthetic English text to inspect")
    args = parser.parse_args()

    # Presidio normally loads a large English model. The small model is enough
    # for this built-in email pattern recognizer and keeps the local lab light.
    nlp_engine = NlpEngineProvider(
        nlp_configuration={
            "nlp_engine_name": "spacy",
            "models": [{"lang_code": "en", "model_name": "en_core_web_sm"}],
        }
    ).create_engine()
    analyzer = AnalyzerEngine(nlp_engine=nlp_engine, supported_languages=["en"])
    findings = analyzer.analyze(text=args.text, entities=["EMAIL_ADDRESS"], language="en")

    # Analyzer results describe spans; the anonymizer performs the text change.
    anonymized = AnonymizerEngine().anonymize(text=args.text, analyzer_results=findings)
    print(f"Input: {args.text}")
    for finding in findings:
        print(
            f"Detected {finding.entity_type} at [{finding.start}:{finding.end}] "
            f"(score {finding.score:.2f}): {args.text[finding.start:finding.end]}"
        )
    print(f"Output: {anonymized.text}")


if __name__ == "__main__":
    main()
