class Combustivel:
    __distancia_km: float
    __consumo_veiculo: float

    def __init__(self, distancia_km, consumo_veiculo):
        self.distancia_km = distancia_km
        self.consumo_veiculo = consumo_veiculo
        self.preco_gasolina = 6.59
        self.preco_alcool = 4.99
        self.preco_diesel = 6.25

    @property
    def distancia_km(self):
        return self.__distancia_km
    @property
    def consumo_veiculo(self):
        return self.__consumo_veiculo

    @distancia_km.setter
    def distancia_km(self, distancia_km):
        try:
            self.__distancia_km = float(distancia_km)
        except Exception:
            print('O valor da distância em quilômetros a ser percorrida é inválido.')
            exit()

    @consumo_veiculo.setter
    def consumo_veiculo(self, consumo_veiculo):
        try:
            self.__consumo_veiculo = float(consumo_veiculo)
        except Exception:
            print('O valor de consumo de combustível do veículo é inválido.')
            exit()