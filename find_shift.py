from shift import decode

# Get a data structure containing a few thousand English words.
from english_words import english_words_set as ENGLISH_WORDS
import re

# Create a program that takes in an encoded string, then try decoding it with all 25 shift values.
def find_shift(string):
    max_finds = 0
    best_shift = None
    for i in range(25):
        text = decode(string, i)
        #Use the dictionary to try to automatically determine which shift is most likely
        
        # getting words seperately for periods. quote,
        words = re.findall(r"[A-z]+", text.lower())
        count = 0
        for text in words:
            # filter forchars
            if text in ENGLISH_WORDS:
                count += 1

        # Because you have to deal with messages with no spaces, you can simply keep a count of how many dictionary words show up in the decoded output. 
        # Occasionally, one or two words might appear by accident, but the correct decoding should have significantly more hits.   
        if count > max_finds:
            max_finds = count
            best_shift = i

    print(f"ciphered text: {string}")
    print(f"word count = {max_finds}")
    print(f"shift {best_shift} is most likely. word: {decode(string, best_shift)}\n")
    
    return best_shift

if __name__ == '__main__':
    find_shift("VDDS")
    find_shift("N QTAJ HTKKJJ")
    find_shift("KJFZHJI BJ DN GDAZ")
    find_shift("P SVCL, NVVK tvyupun Jvmmll")
    find_shift("Hthalbyz Ohjr Zfzaltz Wyvmlzzpvuhsz Ohjr Wlvwsl.")
