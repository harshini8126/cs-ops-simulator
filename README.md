
# CS Ops Simulator (OpenEnv)

## Overview

CS Ops Simulator is a customer support operations environment developed using the OpenEnv framework. It models a realistic workflow in which an agent processes incoming customer emails by performing classification, prioritization, and decision-making under time constraints.

The environment is designed to support the evaluation and benchmarking of intelligent agents in structured, multi-step decision scenarios.

---

## Motivation

Modern customer support systems require agents to balance accuracy, response quality, and operational efficiency. Agents must interpret user intent, assign appropriate priorities, and take timely actions while maintaining customer satisfaction.

This project simulates such conditions in a controlled and reproducible environment to facilitate evaluation of agent behavior.

---

## Environment Design

### Observation Space

Each observation includes:

* `inbox`: List of pending emails
* `processed`: List of processed email identifiers
* `time_left`: Remaining steps before episode termination
* `satisfaction`: Customer satisfaction score (range: 0.0–1.0)

---

### Action Space

Each action consists of:

* `email_id`: Identifier of the selected email
* `category`: One of {billing, technical, spam, general}
* `priority`: One of {low, medium, high}
* `decision`: One of {reply, escalate, refund, ignore}
* `reply`: Optional response text

---

## Reward Function

The reward function evaluates the quality of agent decisions based on:

* Correct classification (category)
* Correct prioritization
* Appropriateness of the chosen action

Additional considerations include:

* Penalties for incorrect or harmful decisions
* Time constraints and SLA-like penalties
* Impact on customer satisfaction

All rewards and task-level scores are strictly bounded within the range (0, 1) to ensure stable and consistent evaluation.

---

## Tasks

### Easy

* Limited number of emails
* Clearly defined intent
* Basic classification and decision-making

### Medium

* Multiple emails with mixed priorities
* Requires consistent and accurate handling

### Hard

* Increased number of emails
* Ambiguity in classification
* Requires prioritization under time constraints

---

## Baseline Agent

A baseline agent is implemented in `inference.py`. It processes emails sequentially, assigns categories and priorities, and selects actions based on deterministic logic or LLM-based inference.

The implementation supports integration with an OpenAI-compatible API for dynamic decision-making.

---

## API Endpoints

The environment is exposed through the following endpoints:

* `/reset` — Initializes the environment
* `/step` — Executes an action
* `/state` — Returns the current state

---

## Execution

To run the project locally:

```bash
pip install -r requirements.txt
python app.py
```

---

## Output Format

The system produces structured logs for evaluation:

* `[START]` — Task initialization
* `[STEP]` — Action execution with corresponding reward
* `[END]` — Final task score

---

## Applications

This environment can be used for:

* Training and evaluating AI-based customer support agents
* Benchmarking large language models in decision-making tasks
* Studying prioritization and response strategies in constrained settings

---

## Status

* Phase 1: Completed
* Phase 2: Completed
* Ready for Phase 3 evaluation
