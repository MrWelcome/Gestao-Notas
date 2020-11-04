class screen:
    def cabecalho():
        print("#"*60)
        print("#"*21,"Gestor de nostas","#"*21)
        print("#"*60)

    def corpo(nomeNota):
        print("_" * 25)
        print("|NOME                   |NOTA       |")
        new_strings = []

        for string in nomeNota:
            string.insert(0, "|")
            string.insert(-1, "\n")
            new_string = string.replace(",", "|")
            new_strings.append(new_string)

        print(new_strings)
        print("_" * 25)


    def rodape(len_lista):
        len_lista = len(len_lista)
        print(f"Nessa sala tem {len_lista} Alunos") 
        print("#"*14,"NÃO HÁ OUTRAS NOTAS REGISTRADAS","#"*14)