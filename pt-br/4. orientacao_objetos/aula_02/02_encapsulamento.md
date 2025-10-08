# 🟦 Encapsulamento em Python

O encapsulamento é um princípio da programação orientada a objetos que protege os dados de um objeto, controlando como eles são acessados ou modificados. Ele ajuda a evitar alterações indevidas e mantém a integridade do objeto.

## 📌 Conceitos-chave

- *Atributos privados:* São atributos que não devem ser acessados diretamente fora da classe.

- *Métodos de acesso:* Usados para ler ou alterar valores de atributos privados de forma controlada.

- *Proteção vs. privacidade:* Python não impede totalmente o acesso, mas utiliza convenções para indicar atributos “privados”.

## 🔹 Convenções de Atributos

| Prefixo  | Significado                                        |
| -------- | -------------------------------------------------- |
| `_nome`  | Atributo **protegido** (sugerido para uso interno) |
| `__nome` | Atributo **privado** (name mangling)               |
| `nome`   | Atributo **público**                               |

> 💡 Convenções não impedem acesso, mas indicam intenção de proteção.

---

## 🧰 Exemplo de Classe com Encapsulamento

```python
class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular       # atributo público
        self.__saldo = saldo          # atributo privado

    # Método para consultar saldo (getter)
    def consultar_saldo(self):
        return self.__saldo

    # Método para depositar dinheiro (setter controlado)
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de R${valor} realizado com sucesso!")
        else:
            print("Valor inválido para depósito.")

    # Método para sacar dinheiro (setter controlado)
    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
            print(f"Saque de R${valor} realizado com sucesso!")
        else:
            print("Saldo insuficiente ou valor inválido.")
```

### 🔹 Testando Encapsulamento

```python
conta = ContaBancaria("Carlos", 1000)

# Acesso indireto ao saldo
print(conta.consultar_saldo())  # 1000

# Depositando e sacando
conta.depositar(500)
conta.sacar(200)

# Tentativa de acesso direto ao atributo privado
# print(conta.__saldo)  # AttributeError!
```

> ⚠️ O acesso direto a __saldo gera erro, mas ainda é possível acessar usando _ContaBancaria__saldo (não recomendado).

---

## ✅ Vantagens do Encapsulamento

- Protege os dados internos da classe.

- Controla alterações por meio de métodos.

- Facilita manutenção e evita efeitos colaterais inesperados.

- Permite alterar a implementação interna sem afetar o código externo.

### 📝 Desafio

1. Crie uma classe Aluno com atributos privados nome e nota.

2. Adicione métodos para alterar e consultar a nota.

3. Garanta que a nota esteja sempre entre 0 e 10.

4. Teste criando instâncias e alterando valores.

> ➡️ O encapsulamento é essencial para criar objetos seguros e confiáveis. Com ele, você controla o acesso aos atributos e mantém a integridade dos dados.

**[Comentando Desafio](desafios/README.md)**

---

## 📝 Conclusão

O encapsulamento é um pilar da programação orientada a objetos que protege os dados internos de uma classe e garante que eles sejam acessados e modificados de maneira controlada. Ao aplicar o encapsulamento, você consegue:

- Evitar alterações indevidas nos atributos de um objeto.

- Criar métodos que validam ou processam os dados antes de alterá-los.

- Facilitar a manutenção do código e aumentar a confiabilidade do sistema.

> 💡 Dica: Sempre que criar atributos que não devem ser manipulados diretamente, considere torná-los privados e forneça métodos para acesso seguro. Isso torna suas classes mais robustas e profissionais.

**Próximo capítulo: [Herança](../aula_03/03_heranca.md)**
