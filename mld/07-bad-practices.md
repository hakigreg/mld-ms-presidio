# Bad practices and better approaches

## Treating a clean output as proof that no sensitive data remains

Presidio's automatic recognizers can miss formats and context they were not built to handle. A false negative leaves the original value unchanged. For example, a company-specific customer ID will not necessarily match a built-in email or phone recognizer. The better approach is to define the entity types and formats you need, test representative examples, add a custom recognizer when appropriate, and use other controls for high-risk releases. The [project warning](https://github.com/data-privacy-stack/presidio#what-is-presidio) explicitly says detection is not guaranteed. This lab confirms only two synthetic email cases.

## Using a high score as a universal accuracy guarantee

A reported score describes one recognizer's assessment of one span. It is not a calibrated promise that all similar values will be found, and it does not cover categories that were never requested. Raising a threshold may reduce false alarms while increasing missed values. Evaluate both kinds of error on data resembling the intended use, then set thresholds with a specific goal. The lab prints a score so you can see the signal, not to claim complete coverage.

## Passing changed text with old offsets

Analyzer results hold character positions in the analyzed string. If an application analyzes `"Email: ada@example.com"` but anonymizes a prefixed or otherwise edited version, `[start:end]` can identify the wrong characters. Keep the text immutable between the two calls, or recompute findings after a change. The lab passes the same `args.text` to both engines and makes the spans visible.

## Running every recognizer on every field

Broad detection can create unnecessary changes. A numeric order ID might be mistaken for another identifier; a person's name may be important to a permitted workflow. Choose entity filters and recognizers for the field and purpose. This lab asks only for `EMAIL_ADDRESS`, which makes its output easy to explain. Broader detection should be an explicit choice tested with examples, not an accidental default.

## Misusing anonymization operators

Replacement with `<EMAIL_ADDRESS>` is readable but removes the address. Hashing the same low-entropy value consistently may reveal equality across records, and masking can retain more of a value than a recipient should see. Encryption requires key management and permits reversal by someone with the key. Choose an operator based on what the recipient needs and what disclosure it permits; the [operator guide](https://github.com/data-privacy-stack/presidio/blob/main/docs/anonymizer/index.md) describes the mechanics. Do not call every transformed output “anonymous” without considering remaining context and re-identification risk.

## Printing real sensitive input during a demo

The educational script prints the input and matched substring to make offsets obvious. Running it with real personal data can expose that data in terminal scrollback or captured output. Use synthetic values here. In an actual pipeline, avoid such logs and check that exceptions and telemetry do not record the original text. The lab's explicit sample address helps keep the exercise safe and reproducible.
