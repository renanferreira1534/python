numero_placa = input("digite o numero da placa do veiculo:")
match numero_placa:


    case "1" | "2": print("Rodizio na segunda-ferira")
    case "3" | "4": print("Rodizio na terça-ferira")
    case "5" | "6": print("Rodizio na quarta-ferira")
    case "7" | "8": print("Rodizio na quinta-ferira")
    case "9" | "0": print("Rodizio na sexta-ferira")
    case _: print("final de placa invalido")
    