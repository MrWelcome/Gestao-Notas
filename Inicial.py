import sys
sys.path.append(".")

from write_read import writeRead
from screen import screen
from ordenacao import ordenacao

cont = 1
nomes = []
notas = []

wr = writeRead
scr = screen
reord = ordenacao

scr.cabecalho()
lerEscr = int(input("Deseja Ler ou Escrever o arquivo? (1->Ler/2->Escrever): "))

def ler():
    notaNome = int(input("Deseja Ordernar por Nome(0) ou Nota(1): "))
    cresDecr = int(input("Deseja Ordenar por ordem Crescente(1) ou Decrescente(2): "))

    reordena = (reord.ordenar(reord, wr.getNomeNota(wr), notaNome, cresDecr))
    wr.writeOrd(wr, reordena)
    print(scr.corpo(reordena))
if(lerEscr == 1):
   ler()
else:
    while(cont == 1):
        nomes.append(input("Nome do aluno: "))
        notas.append(input("Nota do aluno: "))
        cont = int(input("Continuar(1->Sim/2->Não): "))
    else:
        wr.write(wr, nomes, notas)
        act = int(input("Deseja Ler ou Escrever o arquivo? (1->Sim/2->Finalizar): "))

        if(act == 1):
            ler()
scr.rodape(wr.getNomeNota(wr))

