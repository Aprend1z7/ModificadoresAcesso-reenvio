# Superclasse Veiculo
class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def ligar(self):
        print(f"{self.marca} {self.modelo} está ligando...")

# Subclasse Carro
class Carro(Veiculo):
    def __init__(self, marca, modelo, num_portas):
        super().__init__(marca, modelo)  # chama o construtor da superclasse
        self.num_portas = num_portas

    # Sobrescrevendo o método ligar
    def ligar(self):
        print(f"O carro {self.marca} {self.modelo} com {self.num_portas} portas está pronto para rodar!")

# Subclasse Moto
class Moto(Veiculo):
    def __init__(self, marca, modelo, cilindradas):
        super().__init__(marca, modelo)
        self.cilindradas = cilindradas

    # Sobrescrevendo o método ligar
    def ligar(self):
        print(f"A moto {self.marca} {self.modelo} de {self.cilindradas}cc está acelerando!")


# Testando as classes
carro1 = Carro("Toyota", "Corolla", 4)
moto1 = Moto("Honda", "CB500", 500)

carro1.ligar()
moto1.ligar()
