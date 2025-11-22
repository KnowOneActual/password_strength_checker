# Contributing to Password Strength Tool

First off, thanks for taking the time to contribute!

## Core Principles

This project prioritizes **Privacy** and **Security** above all else.

- **No external requests:** The tool must remain 100% offline.
- **No insecure randomness:** Do not use the `random` module for password generation; use `secrets`.
- **Fail Safe:** If a feature cannot be executed securely (e.g., missing dictionary), it should fail rather than degrade to an insecure state.

## How to Submit Changes

1.  Fork the repository.
2.  Create a new branch (`git checkout -b feature/amazing-feature`).
3.  Commit your changes.
4.  Push to the branch.
5.  Open a Pull Request.

## Coding Standards

- Please use **Type Hints** for all function arguments.
- Run your code through `black` before submitting to ensure consistent formatting.
