your_name = input('Enter your name: ')
if your_name.istitle() and your_name.isalpha():
    print('Correct name')
else:
    print('Incorrect name')