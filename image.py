from PIL import Image


def get_altered_pixel(old_pixel, letter):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    position = alphabet.index(letter)
    return (position, old_pixel[1], old_pixel[2])

def hide_message(original_image_filename, message, altered_image_filename):
    image = Image.open(original_image_filename)
    pixels = image.load() # create the pixel map

    

    for i in range(len(message)):
        old_pixel = pixels[i, 0]
        letter = message[i]
        new_pixel = get_altered_pixel(old_pixel, letter)
        pixels[i, 0] = new_pixel
    last_pixel = pixels[len(message), 0]
    altered_last_pixel = (100, last_pixel[1], last_pixel[2])
    pixels[len(message), 0] = altered_last_pixel


    image.save(altered_image_filename)


def reveal_message(altered_image_filename):
    image = Image.open(altered_image_filename)
    pixels = image.load() # create the pixel map

    
    message = ""
    for i in range(image.size[0]):
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        pixel = pixels[i, 0]
        possible_letter_pos = pixel[0]
        if possible_letter_pos >= 26:
            break
        letter = alphabet[possible_letter_pos]
        message = message + letter
    return message
    

original_image_filename = "msu.png"
message = "ATTACKATDAWN"
altered_image_filename = "secret.png"
hide_message(original_image_filename, message, altered_image_filename)
found_message = reveal_message(altered_image_filename)
print(found_message)