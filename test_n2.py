num = int(input("Digite um número: ")) # O usuário digita um número, que é armazenado na variável num.

fib_ant = 0  # valor anterior da sequência de Fibonacci
fib_atual = 1  # valor atual da sequência de Fibonacci

while fib_atual < num:
    fib_prox = fib_ant + fib_atual
    fib_ant = fib_atual
    fib_atual = fib_prox

if fib_atual == num:
    print(f"O número {num} pertence à sequência de Fibonacci.")
else:
    print(f"O número {num} não pertence à sequência de Fibonacci.")
