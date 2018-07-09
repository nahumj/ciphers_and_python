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
        if decrypt_position == 26:
            decrypt_position = 0
        decrypt_key = alphabet[decrypt_position]
        decrypt_keyphrase = decrypt_keyphrase + decrypt_key
    return encrypt(ciphertext, decrypt_keyphrase)

def get_percentage_of_real_words(text, english_words):
    only_letters_and_spaces = ""
    for character in text:
        if character in "ABCDEFGHIJKLMNOPQRSTUVWXYZ ":
            only_letters_and_spaces = only_letters_and_spaces + character
    wordy_things = only_letters_and_spaces.split()
    real_word_count = 0
    for wordy_thing in wordy_things:
        if wordy_thing in english_words:
            real_word_count = real_word_count + 1 

    return (real_word_count / len(wordy_things)) * 100

def crack(ciphertext, dictionary_filename, threshold):
    file = open(dictionary_filename)
    english_words = set(file.read().split())
    for word in english_words:
        possible_plaintext = decrypt(ciphertext, word)
        percentage_words = get_percentage_of_real_words(possible_plaintext, english_words)
        if percentage_words > threshold:
            print("Possible match:")
            print("Percentage of real words is", percentage_words)
            print("Keyphrase is", word)
            print("Plaintext is", possible_plaintext)
            print()


plaintext = "Three Rings for the Elven-kings under the sky, Seven for the Dwarf-lords in their halls of stone, Nine for Mortal Men doomed to die, One for the Dark Lord on his dark throne In the Land of Mordor where the Shadows lie. One Ring to rule them all, One Ring to find them, One Ring to bring them all and in the darkness bind them In the Land of Mordor where the Shadows lie."
plaintext = get_as_uppercase(plaintext)
keyphrase = "RING"

ciphertext = "KPEKV EOEOF WWE KPR VTIKE-XOEOF LVQKI GNV FQP, YVDRT NBX BUK LJGIN-RFZQY QA KPROI UGCTF FN YKWAK, AOEM LFZ SFZGGC ZKE QUFURJ BB UQR, WAK NBX BUK LNXB YUIL UE UOJ QGIS ZYZBTV VT BUK TNTU BL UBXUWE NPRXV GNV FNRLBCJ YOV. UEM XZVT KW XLTR KPRS IYR, BTV EOEO ZF SOEL ZYMZ, WAK ZVTX GU JEOEO ZYMZ RTY RVQ ZV ZYM JRZXTVAF SQAJ BUKD VT BUK TNTU BL UBXUWE NPRXV GNV FNRLBCJ YOV."

# ciphertext = encrypt(plaintext, keyphrase)
# print(ciphertext)

# new_plaintext = decrypt(ciphertext, keyphrase)
# print(new_plaintext)
dictionary_filename = "dictionary.txt"
threshold = 50
crack(ciphertext, dictionary_filename, threshold)
print("Done")