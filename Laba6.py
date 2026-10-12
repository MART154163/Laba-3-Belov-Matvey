us_input = input("Введите строку: ")
cleaned = "".join(char.lower() for char in us_input if char.isalnum())
if cleaned == cleaned [::-1]:
    print(True)
else:
    print(False)