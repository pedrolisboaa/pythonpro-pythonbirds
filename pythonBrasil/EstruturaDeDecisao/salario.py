class Salario:
    def __init__(self, salario):
        self.salario = salario
        self.novo_salario = None
        self.percentual = None
        self.valor_aumento = None

    def realizar_aumento_salarial(self):
        if self.salario < 281:
            self.percentual = 20
            self.valor_aumento = self.salario * 0.2
            self.novo_salario = self.salario + self.valor_aumento
        elif 280 < self.salario <= 700:
            self.percentual = 15
            self.valor_aumento = self.salario * 0.15
            self.novo_salario = self.salario + self.valor_aumento
        elif 700 < self.salario <= 1500:
            self.percentual = 10
            self.valor_aumento = self.salario * 0.10
            self.novo_salario = self.salario + self.valor_aumento
        else:
            self.percentual = 5
            self.valor_aumento = self.salario * 0.05
            self.novo_salario = self.salario + self.valor_aumento

    def imprimir_informacoes(self):
        print(f'Antigo salário R$ {self.salario}')
        print(f'Foi aplicado o aumento de {self.percentual}%')
        print(f'Valor de aumento R$ {self.valor_aumento}')
        print(f'Novo salário R$ {self.novo_salario}')









