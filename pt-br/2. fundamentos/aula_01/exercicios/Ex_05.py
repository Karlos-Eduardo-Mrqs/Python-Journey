# Operadores Bit a Bit 05: Experimente manipular os bits de um número e veja como ele altera o valor.

num = int(input("Digite um número inteiro: "))

print("Número em binário: ", bin(num))

print("\n--- Operações Bit a Bit ---")
print("AND (&) com 1:", num & 1)
print("OR (|) com 1:", num | 1)
print("XOR (^) com 1:", num ^ 1)
print("NOT (~):", ~num)
print("Shift Left (<< 1):", num << 1)  
print("Shift Right (>> 1):", num >> 1)
