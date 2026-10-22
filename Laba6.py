us_input = input("Введите строку: ")
cleaned = ""
for char in us_input:
    if char.isalnum():
        cleaned +=  char.lower()

if cleaned == cleaned [::-1]:
    print(True)
else:
    print(False)