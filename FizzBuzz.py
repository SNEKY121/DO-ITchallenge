n = int(input("N: "))

for i in range(1, n + 1):
    output = ""
    
    if i % 3 == 0:
        output += "Fizz"
    if i % 5 == 0:
        output += "Buzz"
    
    if output == "":
        output = i
    
    print(output)
