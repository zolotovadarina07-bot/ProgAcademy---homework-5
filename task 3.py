text = str(input('Enter a text: '))
summa = 0
for letter in text:
 summa = summa + ord(letter)
print("Sum of codes is :", summa)