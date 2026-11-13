# Essential links

These links were checked for reachability and relevant content on 2026-11-13. They point to the documentation files in Presidio's maintained Data Privacy Stack repository.

- [Presidio documentation home](https://github.com/data-privacy-stack/presidio/blob/main/docs/index.md): start here for the suite, supported workflows, and its warning about detection limits.
- [Installation](https://github.com/data-privacy-stack/presidio/blob/main/docs/installation.md): supported Python versions, Python packages, NLP model setup, and container options. This lab uses local packages.
- [Text de-identification quick start](https://github.com/data-privacy-stack/presidio/blob/main/docs/getting_started/getting_started_text.md): shows the same analyzer → anonymizer Python flow used here.
- [Analyzer overview](https://github.com/data-privacy-stack/presidio/blob/main/docs/analyzer/index.md): explains recognizers, NLP engines, context, and the detection result.
- [Anonymizer overview](https://github.com/data-privacy-stack/presidio/blob/main/docs/anonymizer/index.md): explains how findings become text changes through operators.
- [Adding recognizers](https://github.com/data-privacy-stack/presidio/blob/main/docs/analyzer/adding_recognizers.md): the next reference when a built-in entity does not match your data.
- [Samples gallery](https://github.com/data-privacy-stack/presidio/blob/main/docs/samples/index.md): examples for text, structured data, images, and deployments. Treat them as examples, not as installed lab features.

The versions in this lab are pinned in [`pyproject.toml`](../pyproject.toml) and [`uv.lock`](../uv.lock); current upstream examples can use different versions or defaults.
