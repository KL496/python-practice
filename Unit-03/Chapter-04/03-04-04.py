input_string = input()
result = ""

for index in range(len(input_string)):
    if input_string[index] == " ":
        if result == "":
            result = str(index)
        else:
            result += ", " + str(index)

if result == "":
    print("no spaces found")
else:
    print(result)