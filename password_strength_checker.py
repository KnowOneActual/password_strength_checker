import re
import getpass
import secrets
import string
import os
from typing import List, Tuple, Optional

def check_password_strength(password: str) -> Tuple[bool, List[str]]:
    """
    Evaluates a password against standard complexity rules.
    """
    feedback = []
    rules = [
        (len(password) < 8, "Must be at least 8 characters long."),
        (not re.search(r"[a-z]", password), "Must contain at least one lowercase letter."),
        (not re.search(r"[A-Z]", password), "Must contain at least one uppercase letter."),
        (not re.search(r"[0-9]", password), "Must contain at least one digit."),
        (not re.search(r'[!@#$%^&*(),.?":{}|<>]', password), "Must contain at least one special character."),
    ]
    
    for failed_condition, message in rules:
        if failed_condition:
            feedback.append(message)

    return len(feedback) == 0, feedback

def get_word_list() -> List[str]:
    """
    Attempts to load a list of words from common system locations or a local file.
    Returns a list of words filtered for length and valid characters.
    """
    locations = [
        'words.txt',                # Local file (user provided)
        '/usr/share/dict/words',    # standard on macOS/Linux
        '/usr/dict/words'           # older Linux
    ]

    for loc in locations:
        if os.path.exists(loc):
            try:
                with open(loc, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read().splitlines()
                    # Filter: keep words 3-8 chars long, all lowercase, no apostrophes
                    words = [w.lower() for w in content if 3 <= len(w) <= 8 and w.isalpha()]
                    if words:
                        return words
            except IOError:
                continue
    
    return []

def generate_strong_password(length: int = 16) -> str:
    """Generates a secure random password string."""
    alphabet = string.ascii_letters + string.digits + string.punctuation
    while True:
        password = ''.join(secrets.choice(alphabet) for _ in range(length))
        is_strong, _ = check_password_strength(password)
        if is_strong:
            return password

def generate_passphrase(num_words: int = 4, separator: str = '-') -> Optional[str]:
    """
    Generates a passphrase like 'correct-horse-25-battery-staple'.
    Mixes in 1 or 2 numbers to increase security.
    """
    words = get_word_list()
    if not words:
        return None
    
    # 1. Select the words
    # secure.choice is safer than random.choice
    chosen_parts = [secrets.choice(words) for _ in range(num_words)]
    
    # 2. Mix in numbers
    # We will add 1 or 2 numbers
    count_numbers = secrets.choice([1, 2])
    
    for _ in range(count_numbers):
        # Generate a number between 0 and 99
        number = str(secrets.randbelow(100))
        
        # Insert it at a random position in the list
        # len(chosen_parts) + 1 allows inserting at the very end too
        position = secrets.randbelow(len(chosen_parts) + 1)
        chosen_parts.insert(position, number)

    return separator.join(chosen_parts)

def main():
    print("--- Password & Passphrase Tool ---")
    print("1. Check a password")
    print("2. Generate a secure password (e.g. Tr7&b%1x)")
    print("3. Generate a passphrase (e.g. correct-horse-25-battery)")
    
    choice = input("Select an option (1-3): ").strip()

    if choice == '1':
        user_password = getpass.getpass("Enter password to check: ")
        is_strong, messages = check_password_strength(user_password)
        if is_strong:
            print("\n✅ Strong: Password is strong!")
        else:
            print("\n❌ Weak: Improvements needed:")
            for msg in messages:
                print(f"  - {msg}")

    elif choice == '2':
        print(f"\n✨ Generated Password: {generate_strong_password()}")

    elif choice == '3':
        passphrase = generate_passphrase()
        if passphrase:
            print(f"\n✨ Generated Passphrase: {passphrase}")
        else:
            print("\n⚠️  Error: Could not find a dictionary file.")
            print("Please create a 'words.txt' file in this folder or ensure '/usr/share/dict/words' exists.")
    
    else:
        print("Invalid selection.")

if __name__ == "__main__":
    main()