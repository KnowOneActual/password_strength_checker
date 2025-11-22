# Security Evolution & Decision Log

This document tracks the security philosophy, architectural decisions, and the rationale behind the evolution of the Password Strength Checker. It serves as a guide for future maintainers to understand _why_ certain implementations were chosen over others.

## Core Philosophy

We prioritize **Cryptographically Secure Pseudo-Random Number Generators (CSPRNG)** over standard pseudo-random generators. Accuracy in validation takes precedence over speed. I aim to fail safe—if a word list cannot be found for passphrases, I alert the user rather than generating a weak fallback.

## Implementation Decisions

### 1. Input Handling: `getpass` vs `input`

- **Decision:** Switched from Python's standard `input()` to `getpass.getpass()`.
- **Reasoning:** Standard input echoes characters to the terminal stdout. This creates a "shoulder surfing" vulnerability and leaves the password in the terminal history/scrollback buffers. `getpass` interacts directly with the tty to disable echo, ensuring the password is never displayed.

### 2. Randomness: `secrets` vs `random`

- **Decision:** Strictly use the `secrets` library for all generation logic.
- **Reasoning:** The standard `random` module in Python is deterministic (Mersenne Twister). If an attacker can determine the seed state (e.g., from the time of execution), they can predict future outputs. `secrets` calls the OS's specific true random source (like `/dev/urandom` on \*nix), rendering prediction computationally infeasible.

### 3. Feedback Loop: Aggregated Errors

- **Decision:** Validate all rules simultaneously and return a list of errors, rather than returning on the first failure.
- **Reasoning:** "Fail-fast" validation in password checkers is poor UX and poor security practice. It forces users to guess the policy one rule at a time, often leading to frustration and the creation of "bare minimum" passwords (e.g., adding `1!` to the end of a weak password just to satisfy the rule).

### 4. Passphrase Entropy

- **Decision:** Inject random numbers into dictionary-based passphrases.
- **Reasoning:** While `correct-horse-battery-staple` is memorable, it is susceptible to specific dictionary attacks if the attacker knows the format is "four dictionary words."
  - **Mitigation:** This inject 1 or 2 integers (0-99) at random positions. This exponentially increases the search space for an attacker without significantly impacting the user's ability to memorize the string.

### 5. Dictionary Hygiene

- **Decision:** Filter system word lists for length (3-8 chars) and content (no apostrophes).
- **Reasoning:** System dictionaries often contain unusable entries like single characters (`z`), massive compound words, or proper nouns. Filtering ensures the generated passphrase is typeable and clean.

## Future Considerations

- **Entropy Calculation:** Currently, I use rule-based validation (regex). In the future, I may consider implementing entropy estimation (bits of entropy) to give a mathematical score of strength rather than a boolean "Strong/Weak."
- **Clipboard Integration:** Adding an optional feature to copy the generated password directly to the clipboard would improve security by bypassing the need to display the password on the screen entirely.
