# Relatório do TPC7
## Data: 2024-10-21
## Autor: Renata Bravo

## Resumo
O TPC7 consistiu na realização de uma aplicação Python que permite ao utilizador usar todas as seguintes funcionalidades:
* def medias(t): Calcula a temperatura média de cada dia, dando como resultado uma lista de pares: [(data, temperaturaMédia)];
* def guardaTabMeteo(t, fnome): Guarda uma tabela meteorológica num ficheiro de texto;
* def carregaTabMeteo(fnome): Carrega uma tabela meteorológica a partir de um ficheiro de texto;
* def minMin(t): Calcula a temperatura mínima mais baixa registada na tabela, dando como resultado esse valor;
* def amplTerm(t): Calcula a amplitude térmica (diferença entre a temperatura máxima e a temperatura mínima) de cada dia, dando como resultado uma lista de pares: [(data, amplitude)];
* def maxChuva(t): Calcula o dia em que a precipitação registada teve o seu valor máximo e indica esse valor, dando como resultado o par (data, valor);
* def diasChuvosos(t): Recebe uma tabela meteorológica e um limite p e retorna uma lista de pares [(data, precipitação)] correspondente aos dias em que a precipitação foi superior a p;
* def maxPeriodoCalor(t): Recebe uma tabela meteorológica e um limite p e retorna o maior número consecutivo de dias com precipitação abaixo desse limite;
* def grafTabMeteo(t): Recebe uma tabela meteorológica e desenha os gráficos da temperatura mínima, máxima e de pluviosidade.