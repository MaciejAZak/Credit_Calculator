text = input()
vowels = ["a", "e" ,"i", "o" ,"u"]
consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "r", "s", "t", "w", "v", "x", "y", "z"]
for letter in text:
    if letter in vowels:
        print("vowel")
    elif letter in consonants:
        print("consonant")
    else:
        break