# Sistema-Sorteios
Um sistema de sorteios desenvolvido em Python (para meu local de trabalho e posteriormente adaptado para publicação aqui, pode ser utilizado, modificado e distribuído livremente).

Possui as seguintes funções:

- Sorteio por inserção manual de nomes;
- Sorteio via arquivo CSV.

**** ***** ***** **** **** **** **** ****


SEM ARQUIVO CSV:

Pode ser utilizado inserindo nomes de forma manual, através da opção "Adição manual de nomes", onde será aberta uma janela para cada nome informado,
após todos os nomes desejados serem informados, o campo deve ser deixado vazio e clicado em OK, onde levará para a tela de sorteio.


COM ARQUIVO CSV:

Utilizando um arquivo em formato CSV, é necessário que arquivo tenha pelo menos duas colunas separadas por virgula, a segunda não importando a informação,
a única exigência é que a primeira coluna seja nomeada 'nome', portanto, pode ser preciso manipular arquivos CSV para este padrão, conforme o 
"Arquivo_Exemplo" contido na pasta do programa.

Se houver o mesmo nome mais de uma vez, o programa irá considerar apenas 1, ou seja, não há problemas em existir nomes repetidos no arquivo.

**** ***** ***** **** **** **** **** ****

O SORTEIO:

Na tela de sorteio, existe uma visão central, onde correrão os nomes para o sorteio, o botão de 'INICIAR' e o botão 'PARAR';

Ao clicar em 'INICIAR', os nomes começarão a correr a visão central (roleta), aguardando o clique no botão 'PARAR', onde o nome central destacado em vermelho
é o vencedor. O processo pode se repetir quantas vezes forem necessárias;

Cada vencedor é exportado para um arquivo, que será criado em tempo de execução, nomeado 'Vencedores.txt' para posterior consulta;

É possível visualizar os vencedores através do botão 'VENCEDORES' que irá consultar os registros no arquivo texto gerado, também, é possível limpar o
histórico de vencedores através do botão 'LIMPAR VENCEDORES' que irá efetuar a exclusão do arquivo para dar lugar a um novo, zerando as rodadas;

Também, é possível reinicializar as rodadas sem limpar os vencedores através do botão 'REINICIAR RODADAS', que irá zerar as rodadas da partida, sem
excluir qualquer informação.

No botão 'IMPRIMIR VENCEDORES' a lista de vencedores será enviada para impressão na impressora padrão da estação.

******

Importante 'PARAR' a roleta antes de realizar estas operações, pois qualquer operação (ex: reinicializar rodadas, limpar vencedores) durante a roleta em
operação, será considerada como rodada 0! (a não ser que este seja o efeito desejado).

