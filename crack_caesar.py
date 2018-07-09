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

def encrypt(plaintext, key):
    ciphertext = ""
    for character in plaintext:
        ciphertext = ciphertext + encrypt_single_character(character, key)
    return ciphertext

def decrypt(ciphertext, key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key_position = alphabet.index(key)
    decrypt_position = 26 - key_position 
    if decrypt_position == 26:
        decrypt_position = 0
    decrypt_key = alphabet[decrypt_position]
    return encrypt(ciphertext, decrypt_key)

def crack(ciphertext):
    possible_keys = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for possible_key in possible_keys:
        possible_plaintext = decrypt(ciphertext, possible_key)
        print(possible_key, ":", possible_plaintext)


ciphertext = "ENIWDC + RXEWTGH PGT P ADI DU UJC!"
crack(ciphertext)

