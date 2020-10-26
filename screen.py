class screen:
    def cabecalho(self):
        print("#"*60)
        print("#"*21,"Gestor de nostas","#"*21)
        print("#"*60)
        print("_"*tamanhoTotal)
        for i in range(1,len_lista ):
            tamanhoNome = len(nome[i])
            tamanhoNota = len(nota[i])
            tamanhoTotal = tamanhoNome + tamanhoNota#pega do tamanho das strings na tabela
            self = self[i].replace(",","|")#substituir as virgulas por barra
            self = self[i].insert(0,"|")#adciona uma barra no inicio da linha

        print("_"*tamanhoTotal) 
        print("#"*14,"NÃO HÁ OUTRAS NOTAS REGISTRADAS","#"*14)

