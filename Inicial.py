import sys
sys.path.append(".")

from write_read import writeRead

cont = 1
nomes = []
notas = []
wr = writeRead

wour = int(input("Deseja Ler ou Escrever o arquivo? (1->Ler/2->Escrever): "))

if(wour == 1):
    n = wr.getNomes(wr)
    no = wr.getNotas(wr)
    print(n)
    print(no)
else:
    while(cont == 1):
        nomes.append(input("Nome do aluno: "))
        notas.append(input("Nota do aluno: "))
        cont = int(input("Continuar(1->Sim/2->Não)"))

    wr.write(wr, nomes, notas)


