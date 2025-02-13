import os
import variables 
import operators
import conditions

def mainMenu():
    print(
        "--------------------------------------------------------------------------\n"
        "Mini apostila de Python:\n"
        "--------------------------------------------------------------------------\n"
        "(1) - Variáveis\n"
        "(2) - Operadores Matematicos\n"
        "(3) - Operadores Comparativos\n"
        "(4) - Operadores Logicos\n"
        "(5) - If...Else - Condicionais\n"
        "(0) - Sair"
    )

if __name__ == "__main__":
    while True:
        os.system('cls' if os.name == 'nt' else 'clear') 
        mainMenu()
        
        userInput = input("Digite o número correspondente para selecionar: ").strip()
        if userInput:
            os.system('cls' if os.name == 'nt' else 'clear') 
        
        if userInput == "1":
            variables.varTypes() 
        elif userInput == "2":
            operators.mathOperators()
        elif userInput == "3":
            operators.comparisonOperators()
        elif userInput == "4":
            operators.logicalOperators()
        elif userInput == "5":
            conditions.ifStatements()
        elif userInput == "0":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")
            
        input("\nPressione Enter para voltar ao menu...") 