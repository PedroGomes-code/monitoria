def soma_nat(n):
    
    if n == 00:
        return 0
    
    else:
        return n + soma_nat(n - 1)


def main():
    try:
        
        n = int(input("Informe até qual número natural você quer somar: "))
        
       
        if n < 0:
            print("Por favor, insira um número natural (não negativo).")
        else:
            
            resultado = soma_nat(n)
            print(f"A soma dos números naturais até {n} é: {resultado}")
    
    except ValueError:
        print("Por favor, insira um número válido.")


if __name__ == "__main__":
    main()
