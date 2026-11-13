# Minimum Lab Deployment (MLD)

## Definition

A Minimum Lab Deployment is the smallest working deployment of a technology that lets a learner exercise and observe its essential behavior. It is a learning artifact, not a product. Its purpose is to reach a verifiable, hands-on understanding of the fundamentals as quickly as possible.

The human chooses what to learn and validates the result. The AI coding agent handles most of the implementation and explains the parts that matter. Learning comes from running, changing, observing, and inspecting the deployment, rather than building every piece manually.

## Instructions for the AI coding agent

1. **Start with the ABC.** Identify the technology's core concept, the few components required to demonstrate it, and one simple end-to-end use case. State any necessary assumptions briefly and proceed.
2. **Deploy the smallest real example.** Make it runnable in the requested environment, or locally by default. Include only what is needed to demonstrate the chosen use case. Prefer the technology's normal tools and conventions over custom scaffolding. Do not substitute a mock when the real technology can reasonably run.
3. **Make learning active.** Provide one short exercise in which the learner runs the example, changes one input or setting, and observes the effect. State the expected result and what it demonstrates.
4. **Explain the artifact.** Write a concise project-root README with the basic mental model, prerequisites, exact setup/run/exercise/stop commands, expected output, and a map of the essential files and learning documents. Add brief English comments beside decisions that would otherwise be hard for a beginner to understand. Avoid comments that merely restate the code.
5. **Create the learning guide.** Generate the eight documents specified below in a root-level `mld/` directory. Make them specific to the chosen technology, accurate about the actual deployment, and linked from the project README. Give the five explanatory documents enough depth to teach the technology's general foundations beyond this Lab; keep the remaining reference and iteration guides concise.
6. **Use sound basics.** Keep setup reproducible, declare dependencies and versions where practical, keep secrets out of the repository, and include only the checks needed to verify the core behavior. Avoid premature abstractions, extra services, and production infrastructure unless essential to the learning goal.
7. **Verify and stop.** Run the deployment and exercise when the environment permits. Report what you actually observed, any unverified step, and how to resolve a blocker. Stop when the fundamental use case works; suggest deeper experiments separately rather than implementing them by default.

## Required learning guide

Create these eight Markdown files in the Lab project's root-level `mld/` directory. Use the two-digit prefixes `01` through `08` exactly as listed so the files sort in learning order:

| File | What it should help the learner understand |
| --- | --- |
| `01-concepts-and-fundamentals.md` | A self-contained conceptual foundation for the technology as a whole: its purpose, essential terminology, main components, how they interact, typical workflow, and important boundaries or trade-offs. Explain each concept clearly enough for a beginner to understand the technology in general, then show where the Lab illustrates it. |
| `02-tutorial.md` | A step-by-step introduction that explains the concepts behind each action, walks through the actual deployment and run → change → observe exercise with expected results, and shows how the demonstrated workflow relates to common uses of the technology beyond this Lab. Clearly mark steps that are illustrative rather than verified in the Lab. |
| `03-use-cases.md` | A range of concrete, representative uses of the technology beyond the Lab. Explain the problem each solves, why the technology fits, its relevant limits or trade-offs, and how the Lab's use case relates to the broader set. |
| `04-essential-links.md` | A curated set of authoritative starting points, especially official documentation, with a sentence explaining each link. Verify URLs when access permits; identify any that could not be checked. |
| `05-github-repositories.md` | A small selection of relevant GitHub repositories, prioritizing the official project and useful examples. Give each URL, why it matters, and what to inspect. Verify repository URLs when access permits; identify any that could not be checked. |
| `06-best-practices.md` | Explain the technology's important general practices, why they matter, when to apply them, and concrete examples. Include practices relevant to the Lab without limiting the guide to those used in it. |
| `07-bad-practices.md` | Explain common technology-specific mistakes and anti-patterns across typical uses, why they fail, their consequences, and better approaches. Use concrete examples and identify any mistakes the Lab helps avoid. |
| `08-next-iterations.md` | A short, ordered list of small extensions to this Lab. For each, state the one change to make, the concept it teaches, and the result to observe. Suggest these iterations without implementing them by default. |

The concepts, tutorial, use cases, best practices, and bad practices documents should be substantial enough to give a beginner a broad understanding of the technology's fundamentals without reading the Lab code first. Use the Lab as a concrete example, not as the boundary of those documents. Distinguish what the Lab demonstrates from broader concepts, examples, and recommendations. Keep explanations focused on foundational knowledge rather than trying to cover every advanced feature.

Write for a beginner and prioritize clear explanations over lists of unexplained terms. Avoid generic advice. Support factual claims about the broader technology with authoritative sources where appropriate, and do not present unimplemented examples as verified Lab behavior.

Keep all project instructions, documentation, user-facing text, and explanatory code comments in English.

## Completion criteria

The learner can start the deployment, exercise the core behavior, predict and observe a small change, and find an explanation of why it happened. The five explanatory `mld/` documents also teach the technology's general foundations beyond the Lab, while the other three support further exploration. The agent has verified the path it claims works.
