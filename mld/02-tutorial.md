# Tutorial: detect, then replace an email

This tutorial uses synthetic English text. Presidio's text pipeline has two distinct actions: the analyzer locates sensitive spans, and the anonymizer transforms them. The lab performs both in one local Python process, using the [official Python quick start](https://github.com/data-privacy-stack/presidio/blob/main/docs/getting_started/getting_started_text.md) as its model.

## 1. Prepare the local environment

Install Python 3.11–3.14 and uv, then run from the project root:

```sh
uv sync --locked
```

This creates `.venv/` using `pyproject.toml` and `uv.lock`. The lock includes the Presidio analyzer and anonymizer at version 2.2.366 and spaCy's `en_core_web_sm` model at version 3.8.0. The model is an NLP engine dependency for this analyzer setup; it is not a second anonymizer. The first sync downloads packages and the model, while later runs reuse the local environment. If setup cannot reach PyPI or GitHub, restore network access and run the same command again.

## 2. Run the baseline

```sh
uv run --locked python lab.py
```

Observed output:

```text
Input: Contact Ada at ada@example.com.
Detected EMAIL_ADDRESS at [15:30] (score 1.00): ada@example.com
Output: Contact Ada at <EMAIL_ADDRESS>.
```

The analyzer restricted the search to `EMAIL_ADDRESS`. Its result names the type and positions in the original text: `text[15:30]` is the address. The anonymizer receives that result and uses its default replacement, yielding `<EMAIL_ADDRESS>`. The score is the recognizer's reported confidence for this example, not an estimate of how often it detects all emails.

## 3. Change one input and predict the effect

Before running the next command, predict how many findings there will be and what the final sentence will contain:

```sh
uv run --locked python lab.py --text 'Contact Ada at ada@example.com and Bob at bob@example.org.'
```

Observed result: two email findings, at `[15:30]` and `[42:57]`, and the output is `Contact Ada at <EMAIL_ADDRESS> and Bob at <EMAIL_ADDRESS>.` The added address creates another span. The replacement policy stays the same and is applied to both spans. Try a sentence with no email and predict that the output will be unchanged; this extra variation is illustrative rather than a verified Lab result.

## 4. Inspect the code

Open [`lab.py`](../lab.py). `NlpEngineProvider` loads the pinned small English spaCy model. `AnalyzerEngine.analyze(...)` receives the text, language, and entity filter. `AnonymizerEngine.anonymize(...)` receives the **same original text** and the findings. Supplying different text to the anonymizer would make the offsets refer to the wrong characters. The script prints the original and matched values so a learner can see the relationship; use only synthetic text with this educational command.

## 5. Connect it to wider practice

In an application, the same pattern can run before displaying a document, storing a sanitized copy, or sending a message to another system. The choice of entities, score threshold, recognizers, and anonymization operators should follow the data and privacy goal. Other Presidio paths include structured data and image redaction, described in the [project overview](https://github.com/data-privacy-stack/presidio), but this lab does not install or verify them. The main next step is to evaluate both missed and incorrect detections on representative, safely handled examples before trusting the output.

The script exits after printing; there is no server to stop.
