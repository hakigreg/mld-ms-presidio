# Best practices

Presidio works best when detection is treated as a configurable step in a larger data-handling workflow. The [official overview](https://github.com/data-privacy-stack/presidio) cautions that automatic detection cannot find every sensitive value. These practices help make its behavior understandable and useful.

## Define the data and the action

Decide which entity types matter and what should happen to each before running the analyzer. An email-only sharing rule should request `EMAIL_ADDRESS`, as this lab does, rather than silently replacing every entity the default registry proposes. For a support-ticket export, you might replace emails and phone numbers while preserving non-sensitive product names. The data's purpose determines the operator: a type label preserves the fact that contact data was present; full redaction removes it; masking preserves selected characters. The [anonymizer documentation](https://github.com/data-privacy-stack/presidio/blob/main/docs/anonymizer/index.md) describes operator choices. Avoid assuming that all operators provide the same privacy properties.

## Use the right recognizers and language

Predefined recognizers are a starting point, not a catalog of every organization's identifiers. Use a [custom recognizer](https://github.com/data-privacy-stack/presidio/blob/main/docs/analyzer/adding_recognizers.md) for a well-defined local format, and prefer a checksum or contextual clue when the format supports one. Choose the correct input language and suitable NLP model. The default configuration focuses on English; adding a language requires recognizers and an NLP engine configured for that language, as the [language guide](https://github.com/data-privacy-stack/presidio/blob/main/docs/analyzer/languages.md) explains. In this lab, both the model and `language="en"` are explicit.

## Evaluate representative examples

Collect safely handled examples that include true sensitive values, harmless lookalikes, edge formats, and text with no target entity. Compare expected spans with actual spans, then inspect false negatives and false positives separately. A missed address can remain in the output; an incorrect match can erase useful data. Tune recognizers, context, and thresholds against that evidence instead of adjusting a threshold until one sample looks right. The [presidio-research repository](https://github.com/data-privacy-stack/presidio-research) supports deeper evaluation. The two synthetic sentences in this lab verify the wiring only; they are not an accuracy benchmark.

## Keep spans and text together

The anonymizer's offsets refer to the exact text analyzed. Pass the same original string to both engines, as `lab.py` does. If you trim, normalize, or concatenate text between analysis and anonymization, an offset can point to the wrong characters. For a larger document, track which field or segment each result belongs to. Inspect overlapping detections and selected operators before treating a transformed document as safe to release.

## Protect data around the pipeline

Analyze or transform text before it reaches a sink that should not receive the original. Avoid logging input text, findings with raw values, or error traces containing sensitive data. Apply access controls, retention limits, and review appropriate to the data; Presidio addresses recognition and transformation, not an entire privacy program. This lab intentionally prints the original and matched address for learning, so its command should be run only with synthetic input. Keep versions pinned and repeat a representative check after upgrades because recognizer and model behavior can change.
