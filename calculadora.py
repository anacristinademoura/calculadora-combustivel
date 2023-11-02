class Calculadora:
    __custo_gasolina: float
    __custo_alcool: float
    __custo_diesel: float

    def custo_total_gasolina(self, comb, preco_gasolina):
        self.__custo_gasolina = (comb.distancia_km / comb.consumo_veiculo) * preco_gasolina
        return self.__custo_gasolina
    def custo_total_alcool(self, comb, preco_alcool):
        self.__custo_alccol = (comb.distancia_km / comb.consumo_veiculo) * preco_alcool
        return self.__custo_alccol
    def custo_total_diesel(self, comb, preco_diesel):
        self.__custo_diesel = (comb.distancia_km / comb.consumo_veiculo) * preco_diesel
        return self.__custo_diesel
