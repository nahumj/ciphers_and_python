import itertools

def get_as_uppercase(message):
    return message.upper()

def encrypt_single_character(character, key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if character not in alphabet:
        return character
    character_position = alphabet.index(character)
    key_position = alphabet.index(key)
    shift_position = character_position + key_position
    if shift_position >= 26:
        shift_position = shift_position - 26
    return alphabet[shift_position]

def encrypt(plaintext, keyphrase):
    ciphertext = ""
    for plaintext_character, key in zip(plaintext, itertools.cycle(keyphrase)):
        ciphertext = ciphertext + encrypt_single_character(plaintext_character, key)
    return ciphertext

def decrypt(ciphertext, keyphrase):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    decrypt_keyphrase = ""
    for key in keyphrase:
        key_position = alphabet.index(key)
        decrypt_position = 26 - key_position
        decrypt_key = alphabet[decrypt_position]
        decrypt_keyphrase = decrypt_keyphrase + decrypt_key
    return encrypt(ciphertext, decrypt_keyphrase)

message = "Attack at dawn!!!"
keyphrase = "LEMON"

plaintext = get_as_uppercase(message)

ciphertext = encrypt(plaintext, keyphrase)
print(ciphertext)

new_plaintext = decrypt(ciphertext, keyphrase)
print(new_plaintext)
