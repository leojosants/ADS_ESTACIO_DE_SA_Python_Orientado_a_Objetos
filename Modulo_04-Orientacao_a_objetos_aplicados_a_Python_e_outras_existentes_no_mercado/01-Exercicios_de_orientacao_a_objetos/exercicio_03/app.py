from Veiculo import Veiculo
from Onibus import Onibus


def main():

    modelo_veiculo_2 = Onibus("Mercedes", 160, 8)
    print()
    modelo_veiculo_2.imprimirVeiculo()
    modelo_veiculo_2.capacidadeAssentos()
    print()


if __name__ == "__main__":
    main()
