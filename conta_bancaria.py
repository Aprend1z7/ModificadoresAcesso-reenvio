# Classe ContaBancaria com encapsulamento do saldo
class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.__saldo = saldo_inicial  # atributo privado

    # Getter - retorna o saldo atual
    def get_saldo(self):
        return self.__saldo

    # Setter - atualiza o saldo (garantindo que nunca seja negativo)
    def set_saldo(self, novo_saldo):
        if novo_saldo >= 0:
            self.__saldo = novo_saldo
        else:
            print("Erro: O saldo não pode ser negativo!")

    # Método para depositar dinheiro
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print("Valor de depósito inválido!")

    # Método para sacar dinheiro
    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
        else:
            print("Saldo insuficiente ou valor inválido!")


# Teste da classe
conta = ContaBancaria("Maria", 1000)
print("Saldo inicial:", conta.get_saldo())

conta.depositar(500)
print("Após depósito:", conta.get_saldo())

conta.sacar(300)
print("Após saque:", conta.get_saldo())

conta.set_saldo(-50)  # Teste de valor inválido
