text = "Python is the best language"
words = text.split()
print(words)
longest_word = ''
for word in words:
    if len(word) > len(longest_word):
        longest_word = word
print('The longest word:', longest_word)