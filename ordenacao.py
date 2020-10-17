class ordenacao: 

    def ordenar(list_a, a = 1):
        len_lista = len(list_a, ) - 1
        sorted = False
        while not sorted:
            sorted = True
            for i in range(0, len_lista):
                if a == 1:
                    if list_a[i] > list_a[i+1]:
                        sorted = False
                        list_a[i], list_a[i+1] = list_a[i+1], list_a[i]
                else:
                    if list_a[i] < list_a[i+1]:
                        sorted = False
                        list_a[i], list_a[i+1] = list_a[i+1], list_a[i]  
        return list_a


    def reordNomes(self, dicionario):
        lista = list(dicionario.keys())
        listaOrdenada = self.ordenar(lista)

        return {k: dicionario[k] for k in listaOrdenada}

    def reordNotas(self, dicionario):
        lista = list(dicionario.values())
        listaOrdenada = self.ordenar(lista)

        return {k: dicionario[k] for k in listaOrdenada}




        

