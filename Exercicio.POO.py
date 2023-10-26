class Pessoa:
    def __init__(self, N, P, I, comendo=False, falando=False, dormindo=False):
        self.nome = N
        self.peso = P
        self.idade = I
        self.falando = falando
        self.dormindo = dormindo
        self.comendo = comendo

    def falar(self):
        if self.falando == True:
            print(f"{self.nome} esta falando!")
        elif self.dormindo == True:
            print(f"{self.nome} não pode falar pois esta dormindo!")
        elif self.comendo == True:
            print(f"{self.nome} não pode falar pois esta comendo!")
        else:
            self.falando = True
            print(f"{self.nome} começou a falar!")

    def dormir(self):

        if self.dormindo == True:
            print(f"{self.nome} esta  dormindo!")

        elif self.comendo == True:
            print(f"{self.nome} não pode dormir pois esta comendo!")
        elif self.falando == True:
            print(f"{self.nome} não pode dormir pois esta falando!")
        else:
            self.dormindo = True
            print(f"{self.nome} começou a dormir!")

    def comer(self):

        if self.comendo == True:
            print(f"{self.nome} esta comendo!")
        elif self.falando == True:
            print(f"{self.nome} não pode comer pois esta falando!")
        elif self.dormindo == True:
            print(f"{self.nome} não pode comer pois esta dormindo!")
        else:
            comida = input("Digite a comida: ")
            self.comendo = True
            print(f"{self.nome} começou comer {comida}!")

    def pararfalar(self):
        if self.falando == True:
            print(f"{self.nome} parou de falar!")
            self.falando = False
        else:
            print(f"{self.nome} não está falando!")

    def paracomer(self):
        if self.comendo == True:
            print(f"{self.nome} parou de comer!")
            self.comendo = False
        else:
            print(f"{self.nome} não esta comendo!")

    def parardormir(self):
        if self.dormindo == True:
            print(f"{self.nome} parou de dormir!")
            self.dormindo = False
        else:
            print(f"{self.nome} não esta dormindo!")

    def apresentar(self):
        print(f"meu nome é {self.nome} tenho {self.idade} e peso {self.peso}KG")

p1 = Pessoa("Alyff", 73.5, 27)
p1.falar()
p1.dormir()
p1.comer()