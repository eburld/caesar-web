def alphabet_position(letter):
    letter = letter.lower()
    pos = ord(letter) - 97
    return pos


def rotate_character(char, rot):
    if char.isalpha():
        char_pos = alphabet_position(char)
        if char.islower():
            new_pos = (char_pos + rot) % 26
            new_chr = chr(new_pos + 97)
        else:
            new_pos = (char_pos + rot) % 26
            new_chr = chr(new_pos + 65)
        return new_chr
    else:
        return char


def encrypt(text, rot):
    new_text = []
    for x in range(len(text)):
        new_char = rotate_character(text[x], rot)
        new_text.append(new_char)
    return ''.join(new_text)


#things = [1,2,3,4]
#print(things[100])