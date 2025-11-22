<div align="center">
  <img src="assets/img/password_strength_checker_logo.webp" alt="password strength checker logo goes here" width="250">


# Password Strength & Generator Tool

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.6+](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![Privacy](https://img.shields.io/badge/Privacy-100%25%20Offline-brightgreen?style=flat&logo=shield)](https://github.com/knowoneactual/password_strength_checker)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# Password Strength & Generator Tool

**Project Status:** *Refactored Legacy Code*

 **Note:** This repository is a revision of an older project. I revisited the original code to apply my current knowledge of Python security standards. The primary goal was to create a tool that is **verifiably secure and private**, unlike online password checkers.

## Core Philosophy: Privacy First

The problem with most "Password Strength Checkers" is that they require you to type your password into a web browser, potentially sending it to a third-party server.

**This tool is different:**
* **100% Offline:** No data ever leaves your device. There are zero network requests and no API calls.
* **Transparent:** The code is open-source and simple. You can read the Python script yourself to verify that your data remains local.
* **Ephemeral:** Passwords are processed in memory and never stored, logged, or cached.

## Description

This is a Python utility designed to validate password complexity and generate secure credentials locally. Originally a simple linear script, it has been refactored into a modular tool that uses cryptographically secure random number generators (CSPRNG) and provides detailed feedback.

## Features

### Security & Architecture
   **Cryptographically Secure:** Replaced the standard `random` library with `secrets` to prevent prediction attacks.
   **Secure Input:** Implements `getpass` to hide password input in the terminal, preventing "shoulder surfing."
   **Modular Design:** Core logic is decoupled from the CLI, allowing functions to be imported into other projects.

### Functionality
   **Detailed Validation:** Reports *all* missing criteria (length, digits, special characters) simultaneously rather than one by one.
   **Secure Password Generator:** Creates random, high-entropy strings (e.g., `Tr7&b%1x`) guaranteed to pass all security checks.
   **Passphrase Generator:** Creates memorable, XKCD-style passphrases (e.g., `correct-horse-25-battery`) using system dictionaries, with added numeric entropy.

## Requirements

   Python 3.6+

## Usage

1. Run the script:
    ```bash
    python password_strength_checker.py
    ```

2. Select an option from the menu:
       1: Check an existing password (input is hidden).
       2: Generate a strong random password.
       3: Generate a memorable passphrase.

## Code Evolution

### Original vs. Refactored
   **Original:** Used `input()` (insecure), `re` checks that returned on the first failure (poor UX), and global execution scope.
   **Refactored:** Uses `getpass` (secure), aggregates all validation errors for better feedback, and prioritizes local-only execution for privacy.

## License

This project is licensed under the MIT (License)[License].