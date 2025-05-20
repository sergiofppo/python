class CalculadoraFinanceira:
    def __init__(self):
        self.menu()
    
    def menu(self):
        while True:
            print("\nCalculadora Financeira")
            print("1. Juros Simples")
            print("2. Juros Compostos")
            print("3. Conversão de Moedas")
            print("4. Simulação de Parcelamento")
            print("5. Sair")
            opcao = input("Escolha uma opção: ")
            
            if opcao == '1':
                self.calcular_juros_simples()
            elif opcao == '2':
                self.calcular_juros_compostos()
            elif opcao == '3':
                self.converter_moeda()
            elif opcao == '4':
                self.simular_parcelamento()
            elif opcao == '5':
                print("Encerrando o programa.")
                break
            else:
                print("Opção inválida, tente novamente.")
    
    def calcular_juros_simples(self):
        capital = float(input("Capital inicial (R$): "))
        taxa = float(input("Taxa de juros (% ao ano): "))
        tempo = float(input("Tempo (em anos): "))
        juros = capital * (taxa / 100) * tempo
        montante = capital + juros
        print(f"Juros Simples: R$ {juros:.2f}")
        print(f"Montante Final: R$ {montante:.2f}")
    
    def calcular_juros_compostos(self):
        capital = float(input("Capital inicial (R$): "))
        taxa = float(input("Taxa de juros (% ao ano): "))
        tempo = int(input("Tempo (em anos): "))
        montante = capital * ((1 + (taxa / 100)) ** tempo)
        print(f"Montante com Juros Compostos: R$ {montante:.2f}")
    
    def converter_moeda(self):
        valor = float(input("Valor em Reais (R$): "))
        taxa_dolar = 5.0
        taxa_euro = 5.5
        print(f"Valor em Dólares: $ {valor / taxa_dolar:.2f}")
        print(f"Valor em Euros: € {valor / taxa_euro:.2f}")
    
    def simular_parcelamento(self):
        valor = float(input("Valor do empréstimo (R$): "))
        parcelas = int(input("Número de parcelas: "))
        taxa = float(input("Taxa de juros mensal (%): "))
        valor_parcela = valor * (1 + taxa / 100) ** parcelas / parcelas
        print(f"Valor de cada parcela: R$ {valor_parcela:.2f}")


if __name__ == "__main__":
    CalculadoraFinanceira()