import math

val = input("Entre com um valor: ")
val = int(val)

valelev = math.pow(val, 3)

if valelev > 100:
    print("O valor é maior que 100")
else:
    print("O valor é menor que 100")

name = "Eric"
age = 74
print(f"Hello, {name}. You are {age}.")
