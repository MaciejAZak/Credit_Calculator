word = input()
result = ""

for letter in word:
    check = str.isupper(letter)
    if check is True:
        result = result + "_" + letter.lower()
    else:
        result = result + letter

print(result)