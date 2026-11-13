# Minimum Lab Deployment: Microsoft Presidio

This local lab demonstrates one fundamental Presidio behavior: detect an email address in English text, then replace the detected span with `<EMAIL_ADDRESS>`.

## Mental model

Presidio's **Analyzer** returns findings such as entity type, character offsets, and confidence score. Its **Anonymizer** takes those findings and changes the text. In this lab, the built-in email recognizer finds addresses; the anonymizer uses its default replacement operator. Detection and replacement are separate steps. Presidio can miss sensitive text or flag harmless text, so review results before relying on them in a real data flow. See the [official text de-identification guide](https://github.com/data-privacy-stack/presidio/blob/main/docs/text_anonymization.md).

## Prerequisites

- Python 3.11–3.14 and [uv](https://docs.astral.sh/uv/getting-started/installation/)
- Internet access for the first `uv sync` (PyPI packages and the pinned spaCy model wheel)

No API key, service, container, or real personal data is needed. The included email addresses are synthetic.

## Set up and run

From the project root:

```sh
uv sync --locked
uv run --locked python lab.py
```

Expected output (the displayed score was observed with the locked dependencies):

```text
Input: Contact Ada at ada@example.com.
Detected EMAIL_ADDRESS at [15:30] (score 1.00): ada@example.com
Output: Contact Ada at <EMAIL_ADDRESS>.
```

The offsets are Python slice positions: `text[15:30]` is `ada@example.com`. The score expresses the recognizer's confidence for this finding; it is not a guarantee that every email will be found.

## Run → change → observe

Run the same program with a second synthetic address:

```sh
uv run --locked python lab.py --text 'Contact Ada at ada@example.com and Bob at bob@example.org.'
```

Expected result: two `EMAIL_ADDRESS` findings, and both addresses become `<EMAIL_ADDRESS>` in the output. This shows that the analyzer returns one finding per matched span and the anonymizer applies the operator to each finding. Try changing one address or removing both to predict the new result. Keep this exercise synthetic: the program intentionally prints its input and findings for learning.

## Stop

The script exits on its own; there is no server to stop. To leave the lab, simply close the terminal. The local `.venv/` can be kept for the next run.

## Files and learning guide

- [`lab.py`](lab.py): one analysis and anonymization pipeline with a small command-line input.
- [`pyproject.toml`](pyproject.toml) and [`uv.lock`](uv.lock): pinned packages and the English spaCy model for repeatable setup.
- [`mld/01-concepts-and-fundamentals.md`](mld/01-concepts-and-fundamentals.md): Presidio's components and boundaries.
- [`mld/02-tutorial.md`](mld/02-tutorial.md): guided run, change, and observation.
- [`mld/03-use-cases.md`](mld/03-use-cases.md): representative applications.
- [`mld/04-essential-links.md`](mld/04-essential-links.md): official documentation.
- [`mld/05-github-repositories.md`](mld/05-github-repositories.md): source repositories and examples.
- [`mld/06-best-practices.md`](mld/06-best-practices.md): reliable use of detection and anonymization.
- [`mld/07-bad-practices.md`](mld/07-bad-practices.md): pitfalls and better approaches.
- [`mld/08-next-iterations.md`](mld/08-next-iterations.md): small follow-on experiments.
