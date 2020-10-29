class ordenacao:
    def ordenar(self, list_a, coluna = 0, a = 1): #list_a = DICIONARIO, Coluna = Quais dados o usuario quer ordenar, a = 1 Ordem crescente / A-Z
         #Tem que receber um dicionario dessa maneira: dicionario = {0:["NOME", NOTA], 1:["NOME", NOTA], 2: ["NOME", NOTA]}
        len_lista = len(list_a) - 1
        sorted = False
        while not sorted:
            sorted = True
            for i in range(0, len_lista):

                if a == 1:
                    if list_a.get(i)[coluna] > list_a.get(i+1)[coluna]:
                        sorted = False
                        list_a[i], list_a[i+1] = list_a[i+1], list_a[i]
                    elif a != 1:
                        if list_a.get(i)[coluna] < list_a.get(i+1)[coluna]:
                            sorted = False
                            list_a[i], list_a[i+1] = list_a[i+1], list_a[i]
        return list_a

# Exemplo para testar o codigo, nesse caso, está ordenando por NOME, para ordenar por nota, no lugar de 0 coloque 1
# dicionario = {0:["Marco", 10], 1:["Aellingotn", 2], 2: ["Barisnda", 5]}

# print(ordenar(dicionario, 0))



    #Versão com SELF que não consegui fazer funcionar
    # def ordenar(self, list_a, coluna, a = 1): #list_a = DICIONARIO, Coluna = Quais dados o usuario quer ordenar, a = 1 Ordem crescente / A-Z
    #      #Tem que receber um dicionario dessa maneira: dicionario = {0:["NOME", NOTA], 1:["NOME", NOTA], 2: ["NOME", NOTA]}
    #     len_lista = len(list_a, ) - 1
    #     sorted = False
    #     while not sorted:
    #         sorted = True
    #         for i in range(0, len_lista):

    #             if a == 1:
    #                 if list_a.get(i)[coluna] > list_a.get(i+1)[coluna]:
    #                     sorted = False
    #                     list_a[i], list_a[i+1] = list_a[i+1], list_a[i]
    #                 elif a != 1:
    #                     if list_a.get(i)[coluna] < list_a.get(i+1)[coluna]:
    #                         sorted = False
    #                         list_a[i], list_a[i+1] = list_a[i+1], list_a[i]
    #     return list_a


    #Comentei essa parte pois acho que ela não vai ser mais necessaria, já que a nossa função retorna o propio dicionario.
    """ def reordNomes(self, dicionario):
        lista = list(dicionario.keys())
        listaOrdenada = self.ordenar(lista)

        return {k: dicionario[k] for k in listaOrdenada}

    def reordNotas(self, dicionario):
        lista = list(dicionario.values())
        listaOrdenada = self.ordenar(lista)

        return listaOrdenada
 """



        

