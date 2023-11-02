from calculadora import Calculadora
from combustivel import Combustivel

calc = Calculadora()

comb = Combustivel(
    input('Informe a distância em quilômetros a ser percorrida: '),
    input('Informe o consumo de combustível do veículo (km/l): ')
)

print('O valor total gasto será de: \n')

print(
    f'Gasolina: {calc.custo_total_alcool(comb, comb.preco_gasolina):.2f}'
)

print(
    f'Álcool: {calc.custo_total_alcool(comb, comb.preco_alcool):.2f}'
)

print(
    f'Diesel: {calc.custo_total_diesel(comb, comb.preco_diesel):.2f}'
)