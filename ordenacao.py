class ordenacao:
    def ordenar(self, list_a, coluna, az): #list_a = DICIONARIO, Coluna = Quais dados o usuario quer ordenar, a = 1 Ordem crescente / A-Z
         #Tem que receber um dicionario dessa maneira: dicionario = {0:["NOME", NOTA], 1:["NOME", NOTA], 2: ["NOME", NOTA]}
        len_lista = len(list_a) - 1
        sorted = False
        while not sorted:
            sorted = True
            for i in range(0, len_lista):

                if az == 1:
                    if list_a.get(i)[coluna] > list_a.get(i+1)[coluna]:
                        sorted = False
                        list_a[i], list_a[i+1] = list_a[i+1], list_a[i]
                    elif az != 1:
                        if list_a.get(i)[coluna] < list_a.get(i+1)[coluna]:
                            sorted = False
                            list_a[i], list_a[i+1] = list_a[i+1], list_a[i]
        return list_a



        

