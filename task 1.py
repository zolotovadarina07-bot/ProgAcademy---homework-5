text = str(input('Enter a text: '))
text = text.upper()
seen = []
for char in text:
    if text.count(char) > 0 and char == 'B' and char not in seen:
        seen.append(char)
        print('Кількість букв b -', text.count(char))