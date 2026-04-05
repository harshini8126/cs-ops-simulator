# 🚀 CS Ops Simulator (OpenEnv)

## Overview
This project implements a customer support operations simulation environment using the OpenEnv interface. It models a realistic workflow where an agent processes incoming customer emails by classifying issues, assigning priorities, and deciding appropriate actions under time constraints.

The environment evaluates decision-making behavior in a controlled and reproducible setting.

---

## Motivation
Customer support systems require balancing accuracy, response quality, and operational efficiency. Agents must make decisions quickly while maintaining customer satisfaction and adhering to service-level expectations.

This project simulates such scenarios to evaluate intelligent agent behavior.

---

## Key Features

- Realistic email-based customer support simulation  
- Multi-step decision-making across tasks  
- Time constraints with SLA-style penalties  
- Customer satisfaction dynamics  
- Deterministic evaluation for reproducibility  
- Structured reward function with partial credit  

---

## Environment Design

### Observation Space
- inbox: list of pending emails  
- processed: list of processed email IDs  
- time_left: remaining steps  
- satisfaction: customer satisfaction score (0.0 to 1.0)  

---

### Action Space
- email_id  
- category: billing, technical, spam, general  
- priority: low, medium, high  
- decision: reply, escalate, refund, ignore  
- reply: optional response text  

---

## Reward Function
- Correct classification  
- Correct prioritization  
- Appropriate decision  
- Reply quality  
- Penalties for incorrect or harmful actions  
- SLA/time constraints  
- Customer satisfaction impact  

All rewards are normalized between 0.0 and 1.0.

---

## Tasks

### Easy
Single email with clear intent.

### Medium
Multiple emails with mixed priorities.

### Hard
Complex inbox with ambiguity, spam detection, and time pressure.

---

## Baseline Agent
A deterministic rule-based agent is implemented in `inference.py`.

It:
- Uses keyword-based heuristics  
- Classifies emails  
- Assigns priority  
- Chooses actions  
- Generates responses  

---

## Usage

Run locally:

```bash
pip install -r requirements.txt
python app.py
