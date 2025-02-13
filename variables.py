def varTypes():
    print("\n=== VARIAVEIS ===\n"
        "\nVariaveis são responsaveis por armazenar valores.\n"
        "São declaradas por: \n\n"
        "nomeDaVariavel = valor\n"
        )
    nome = "Kayk Caputo"
    idade = 19
    peso = 56.7
    hobbys = ["violão", "videogame", "programação"]
    vivo = True
    print("Exemplos: \n"
        f"string: \nnome = {chr(34)}{nome}{chr(34)}\n"
        "\t+ uma string armazena cadeias de caracteres, basicamente texto\n"
        f"int: \nidade = {idade}\n"
        "\t+ um int armazena numeros inteiros\n"
        f"float: \npeso = {peso}\n"
        "\t+ um float armazena numeros quebrados\n"
        f"list: \nhobbys = {hobbys}\n"
        "\t+ uma lista armazena diversos valores em uma unica variavel\n"
        f"boolean: \nvivo = {vivo}\n"
        "\t+ um boolean armazena condicoes, verdadeiro ou falso"
    )
