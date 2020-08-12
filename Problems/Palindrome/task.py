word = input()
word_backward = word[-1]
if word == word_backward:
    print("Palindrome")
else:
    print("Not palindrome")