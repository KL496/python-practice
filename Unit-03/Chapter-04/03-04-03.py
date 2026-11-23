input_string = input()
result = ""

for index in range(0, len(input_string), 2):
    result += input_string[index]

print(result)