# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-11-22

### Added
- Created 'logo' for project and used for readme
- **Passphrase Generator**: New feature to create memorable, comic-style passphrases (e.g., "correct-horse-battery") using system dictionaries.
- **Number Insertion**: Added logic to randomly insert 1 or 2 numbers into passphrases to increase entropy against dictionary attacks.
- **Secure Random Generator**: Added `generate_strong_password` using the `secrets` module for cryptographically strong random strings.
- **Interactive Menu**: Implemented a CLI menu system allowing users to choose between checking a password, generating a random password, or creating a passphrase.
- **Hidden Input**: Integrated `getpass` to mask passwords in the terminal while typing.
- **Type Hints**: Added Python type annotations throughout the codebase for better development support.
- **Project Documentation**: Added `SECURITY_LOG.md` to track architectural decisions and `CONTRIBUTING.md` to set development standards.
- **Repository Hygiene**: Added `.gitignore` to help prevent garbage commits and `LICENSE` to formally adopt the MIT License.

### Changed

- **Refactored Validation**: The `check_password_strength` function now returns a list of errors rather than printing directly, allowing for better integration.
- **Error Aggregation**: Validation now reports _all_ missing criteria (length, digits, special chars) at once, rather than failing on the first error found.
- **Project Structure**: Wrapped the execution logic in a `main()` function and `if __name__ == "__main__":` block to support importing as a module.

### Removed

- Removed plain-text `input()` which exposed passwords on the screen.

## [0.1.0] - Original Release

### Added

- Basic script to check password length and character diversity (uppercase, lowercase, digits, special characters).
