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


    def __formatar(self, nomes, notas):
        txt = ""
        for i in range(len(nomes)):
            txt += nomes[i] + "," + notas[i] + ","

        return txt

    def getNomes(self):
        txt = self.__read(writeRead)
        txts = txt.split(',')
        n = []

        for i in range(len(txts)):
            if(i%2 == 0):
                if(txts[i] != ""):
                    n.append(txts[i])
        return n

    def getNotas(self):
        txt = self.__read(writeRead)
        txts = txt.split(',')
        n = []

        for i in range(len(txts)):
            if(i%2 != 0):
                if(txts[i] != ""):
                    n.append(txts[i])
        return n

    def __read(self):
        f = open("databasetxt.txt", "r")
        return f.read()