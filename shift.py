# Create a Python program that encodes and decodes messages using the shift cipher. The amount of shift must be configurable.
# ! use encode and decode function 

from string import ascii_lowercase as letters

def _caesar(string, shift, mul):
    result = ""

    for c in string:
        is_upper = False
        if c.isupper():
            is_upper = True

        if c not in letters and not is_upper:
            result += c
            continue

        c = c.lower()

        # get index from letters
        idx = letters.index(c)
        # shift
        new_id = (idx + shift * mul) % 26

        letter = letters[new_id]
        if is_upper:
            letter = letter.upper()
        result += letter

    return result

def encode(string, shift):
    return _caesar(string, shift, 1)

def decode(string, shift):
    return _caesar(string, shift, -1)



if __name__ == '__main__':
    print(f"budots encoded: {encode('budots', 4)} ")
    print(f"fyhsxw decoded: {decode('fyhsxw ', 4)} ")

    print(f"ImBatman encoded: {encode('ImBatman', 24)} ")
    print(f"IkByrkyl decoded: {decode('IkByrkyl', 24)} ")

    # print(decode("Nvvk Tvyupun", 7))