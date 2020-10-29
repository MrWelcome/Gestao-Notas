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

#scr.cabecalho(scr, len(reord.ordenar(reord, wr.getNomeNota(wr))))
wour = int(input("Deseja Ler ou Escrever o arquivo? (1->Ler/2->Escrever): "))

if(wour == 1):
    print(reord.ordenar(reord, wr.getNomeNota(wr), 0))
else:
    while(cont == 1):
        nomes.append(input("Nome do aluno: "))
        notas.append(input("Nota do aluno: "))
        cont = int(input("Continuar(1->Sim/2->Não)"))

    wr.write(wr, nomes, notas)


