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

# message = "Attack at dawn!!!"
# key = "B"

message = "Python + ciphers are a lot of fun!"
key = "P"

plaintext = get_as_uppercase(message)

ciphertext = encrypt(plaintext, key)
print(ciphertext) # should be BUUBDL BU EBXO!!!

new_plaintext = decrypt(ciphertext, key)
print(new_plaintext)
