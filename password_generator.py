import random
import string

def generate_password(length=12):
    if length < 4:
        return "❌ Password length must be at least 4 characters."

    # Character sets
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    # Make sure password includes at least one letter, digit, and symbol
    password = [
        random.choice(letters),
        random.choice(digits),
        random.choice(symbols),
    ]

    # Fill the rest with random choices from all characters
    all_chars = letters + digits + symbols
    password += random.choices(all_chars, k=length - 3)

    # Shuffle the list to ensure randomness
    random.shuffle(password)

    return ''.join(password)

def main():
    print("🔐 Password Generator")
    try:
        length = int(input("Enter desired password length: "))
        password = generate_password(length)
        print(f"✅ Generated password: {password}")
    except ValueError:
        print("❌ Please enter a valid number.")

if __name__ == "__main__":
    main()
