import string
import random

# Implementacja szyfrowania Cezara
def ceasar_encrypt(text, shift=9):
    alphabet = string.ascii_lowercase + string.ascii_uppercase
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    table = str.maketrans(alphabet, shifted_alphabet)
    return text.translate(table)

# Generator haseł
def password_generator(length=25, use_uppercase=True, use_digits=True, use_special_chars=True):
    chars = string.ascii_lowercase
    if use_uppercase:
        chars += string.ascii_uppercase
    if use_digits:
        chars += string.digits
    if use_special_chars:
        chars += string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

# Generowanie i zapisywanie zaszyfrowanego hasła
def save_encrypted_password(filename, password_length=25, shift=9):
    password = password_generator(password_length)
    encrypted_password = ceasar_encrypt(password, shift)
    # Zapisz plik na dysku C w katalogu dokumenty
    path = 'C:\\Dokumenty\\' + filename
    with open(path, 'w') as f:
        f.write(encrypted_password)
    print("Zapisano hasło do pliku")

save_encrypted_password('password.txt')