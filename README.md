# CS Ops Simulator (OpenEnv)

## Overview

This project implements a customer support operations simulation environment using the OpenEnv interface. It models a realistic workflow where an agent must process incoming customer emails by classifying issues, assigning priorities, and deciding appropriate actions under time constraints.

## Motivation

Customer support is a critical real-world task that requires balancing accuracy, response quality, and operational efficiency. Agents must make decisions quickly while maintaining customer satisfaction and adhering to service-level expectations.

This environment is designed to evaluate such decision-making behavior in a controlled and reproducible setting.

## Key Features

- Realistic email-based customer support simulation
- Multi-step decision-making across multiple tasks
- Time constraints with SLA-style penalties
- Customer satisfaction dynamics influencing outcomes
- Deterministic evaluation with reproducible results
- Structured reward function with partial credit

## Environment Design

### Observation Space

Each observation includes:

- `inbox`: list of pending emails
- `processed`: list of processed email IDs
- `time_left`: remaining steps before timeout
- `satisfaction`: customer satisfaction score (0.0 to 1.0)

### Action Space

Each action consists of:

- `email_id`: identifier of the email to process
- `category`: billing, technical, spam, general
- `priority`: low, medium, high
- `decision`: reply, escalate, refund, ignore
- `reply`: optional response text

### Reward Function

The reward function evaluates multiple aspects:

- Correct classification (category)
- Correct prioritization
- Appropriate action decision
- Quality of reply (if provided)

Additional dynamics:

- Penalties for harmful actions (e.g., ignoring high-priority emails)
- Penalties for unnecessary refunds
- SLA penalties if emails remain unprocessed within time limits
- Customer satisfaction decreases for poor decisions and affects rewards

All rewards are bounded within the range [0.0, 1.0].

## Tasks

### Easy
A single email with a clear intent, testing basic classification and action.

### Medium
Multiple emails with mixed categories and priorities, requiring consistent decision-making.

### Hard
Complex scenarios involving:
- Multi-intent emails
- Ambiguity in classification
- Spam detection
- Time pressure and trade-offs between actions

## Baseline Agent

A deterministic rule-based agent is provided in `inference.py`.  
It processes emails sequentially and produces reproducible results across all tasks.

## Usage

Run the environment with the baseline agent:
