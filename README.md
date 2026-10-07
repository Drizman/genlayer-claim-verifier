# GenLayer Claim Verifier

A GenLayer Intelligent Contract for decentralized verification of real-world claims using web evidence and validator consensus.

## Overview

The GenLayer Claim Verifier is designed to evaluate factual claims against publicly available web information.

A user submits a claim and a source URL. The Intelligent Contract retrieves the source, analyzes the available evidence, and produces a structured verification result.

The important part is the consensus process: validators independently evaluate the same evidence and verify the leader's decision before the result is accepted.

## Why It Matters

Information on the internet changes quickly, while traditional smart contracts cannot natively reason about unstructured web information.

This project explores how GenLayer Intelligent Contracts can make web-based verification a reusable on-chain primitive.

Potential applications include:

- Verification of public announcements
- Checking project claims
- Monitoring published events
- Evidence-based Web3 research
- Decentralized information verification

## How Consensus Is Used

The contract uses GenLayer's non-deterministic execution and validator consensus.

The leader:

1. Retrieves information from the supplied web source.
2. Analyzes the evidence.
3. Produces a structured verification result.

Validators independently repeat the evaluation and compare the important decision fields.

The result is only accepted when the validator consensus agrees with the required decision criteria.

## Design Principles

- Evidence must come from the supplied source.
- Validators must independently verify the leader's result.
- The contract should reject unsupported conclusions.
- Consensus results are stored only after agreement.
- The design avoids trusting a single AI response.

## Project Structure

```text
genlayer-claim-verifier/
├── contracts/
│   └── claim_verifier.py
├── tests/
│   └── test_claim_verifier.py
└── README.md
