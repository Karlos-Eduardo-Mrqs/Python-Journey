valor_celsius = [38.5,15.6,36.8,37.0]

valor_farenheit = list(map(lambda celsius:(celsius * 9/5) + 32, valor_celsius))

print(valor_farenheit)