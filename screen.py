class screen:
    def cabecalho():
        print("#"*60)
        print("#"*21,"Gestor de nostas","#"*21)
        print("#"*60)

    def corpo(nomeNota):
        print("_" * 25)
        print("#" * 4,"NOTAS DOS ALUNOS","#"* 3)
        print("_" * 25)
        print("|NOME       |NOTA       |")
        print("-" * 25)


        for i in range(0, len(nomeNota)):

            nomeNota[i]= (f"{i+1}: {nomeNota[i]}")
            nova = nomeNota[i].replace(",","|")
            nova = nova.replace("[","")
            nova = nova.replace("]","")
            nova = nova.replace("'","")
            print(nova)

    def rodape(len_lista):
        len_lista = len(len_lista)
        print(f"Nessa sala tem {len_lista} Alunos") 
        print("#"*14,"NÃO HÁ OUTRAS NOTAS REGISTRADAS","#"*14)