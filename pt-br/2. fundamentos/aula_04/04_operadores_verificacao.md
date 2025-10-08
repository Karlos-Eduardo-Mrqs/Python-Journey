# 🔹 Operadores de Verificação 🆔🔎

Os operadores de verificação permitem testar relações entre objetos ou verificar se um valor está presente em uma coleção. Eles são úteis para validações rápidas, filtragens e comparações.

## 🔸 Operadores de Identidade 🆔

> Usados para verificar se duas variáveis apontam para o mesmo objeto na memória, e não apenas se têm o mesmo valor.

| 🔢 Operador | 💬 Descrição                                                  | 💡 Exemplo   | 🎯 Resultado      |
| ----------- | ------------------------------------------------------------- | ------------ | ----------------- |
| `is`        | Retorna `True` se as variáveis referenciam o **mesmo objeto** | `a is b`     | `True` ou `False` |
| `is not`    | Retorna `True` se os objetos forem **diferentes**             | `a is not b` | `True` ou `False` |

> **💡 Dica:** ``a == b`` compara valores, enquanto ``a is b`` compara identidade de objeto (mesma posição na memória).

### Exemplo de Identidade 🆔

```python
a = [1, 2]
b = a
c = [1, 2]

print(a is b)     # True → a e b são o mesmo objeto
print(a is c)     # False → a e c têm o mesmo conteúdo, mas são objetos diferentes
```

## 🔸 Operadores de Membros 🔎📦

> Permitem verificar se um valor está presente dentro de uma sequência, como listas, strings ou dicionários.

| 🔢 Operador | 💬 Descrição                                       | 💡 Exemplo         | 🎯 Resultado |
| ----------- | -------------------------------------------------- | ------------------ | ------------ |
| `in`        | Retorna `True` se o valor estiver presente         | `'a' in 'Carlos'`  | `True`       |
| `not in`    | Retorna `True` se o valor **não** estiver presente | `5 not in [1,2,3]` | `True`       |

### Exemplo de membros 🔎📦

```python
frutas = ['maçã', 'banana']

print('banana' in frutas)       # True → banana está na lista
print('laranja' not in frutas)  # True → laranja não está na lista
print('uva' in frutas)          # False → uva não está na lista

```

## 🔹 Conclusão

Os operadores de verificação ajudam a garantir a integridade de dados e validar condições rapidamente.

Use ``is`` e ``is`` not para comparar identidade de objetos.

Use ``in`` e ``not in`` para testar pertencimento em sequências.

**Próximo Capítulo: [Precedência dos Operadores](../aula_05/05_resumo_operadores.md)**

---

## 📝 Exercícios de Verificação 🆔🔎

### Crie duas listas ``lista1`` e ``lista2`` com os mesmos valores ``[1, 2, 3]``
  
1. Verifique se ``lista1`` e ``lista2`` são o mesmo objeto usando is.  
2. Crie uma variável ``lista3 = lista1`` e verifique se ``lista1 is lista3``.

### Verificar se um elemento digitado pelo usuário está presente em uma lista de frutas.frutas = ["maçã", "banana", "laranja", "uva", "pera"]

**[Gabarito](exercicios/README.md)**
