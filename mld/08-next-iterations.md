# Next iterations

The current lab stops at one English email recognizer and the default replacement operator. Try these in order, one change at a time; none is implemented or verified in this deployment.

1. **Change the operator.** Pass an `OperatorConfig` for `EMAIL_ADDRESS` that uses `redact`. Learn that recognition and transformation are independent; observe the address disappear instead of becoming `<EMAIL_ADDRESS>`.
2. **Add a second built-in entity.** Include `PHONE_NUMBER` in the analyzer's `entities` list and add a synthetic US phone number to the input. Learn entity filtering and multiple recognizers; observe two different type labels if both are detected.
3. **Try a custom pattern recognizer.** Define a clearly formatted fictional account ID and register a `PatternRecognizer`. Learn how Presidio extends beyond built-in entities; observe the new entity type in the findings and output.
4. **Evaluate a small example set.** Write several synthetic positive, negative, and lookalike sentences with expected spans. Learn the difference between a working pipeline and detection quality; count misses and false alarms before changing thresholds.

Use the [official samples](https://github.com/data-privacy-stack/presidio/blob/main/docs/samples/index.md) and [recognizer guide](https://github.com/data-privacy-stack/presidio/blob/main/docs/analyzer/adding_recognizers.md) for the relevant APIs.
