import os.path

class writeRead:

    def write(self, nomes, notas):
        if(os.path.isfile('databasetxt.txt')):
            f = open("databasetxt.txt", "a")
            f.write(self.__formatar(writeRead, nomes, notas))
            f.close()
        else:
            f = open("databasetxt.txt", "w")
            f.write(self.__formatar(writeRead, nomes, notas))
            f.close()

    def writeOrd(self, list_ord):
        f = open("dataordenadotxt.txt", "w")
        f.write(self.__formatarOrd(writeRead, list_ord))
        f.close()


    def __formatar(self, nomes, notas):
        txt = ""
        for i in range(len(nomes)):
            txt += '\n' + nomes[i] + "," + notas[i]

        return txt

    def __formatarOrd(self, list_ord):
        txt = ""
        for i in range(len(list_ord)):
            txt += list_ord.get(i)[0] + "," + str(list_ord.get(i)[1]) + '\n'

        return txt


    def getNomeNota(self):
        lines = self.__read(writeRead)
        nomes = []
        notas = []
        lista = {}

        for line in lines:
            tspl = line.split(',')
            nomes.append(tspl[0])
            notas.append(tspl[1])

        for i in range(len(nomes)):

            lista[i] = [nomes[i], float(notas[i])]

        return lista

    def __read(self):
        f = open("databasetxt.txt", "r")
        return f.read().splitlines()