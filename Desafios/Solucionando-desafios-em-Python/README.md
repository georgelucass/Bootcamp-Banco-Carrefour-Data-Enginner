# Solucionando Desafios em Python



## Desafio 1

🔴  Nível: Intermediário

### Média 3

Leia quatro números (N1, N2, N3, N4), cada um deles com uma casa decimal, correspondente às quatro notas de um aluno. Calcule a média com pesos 2, 3, 4 e 1, respectivamente, para cada uma destas notas e mostre esta média acompanhada pela mensagem *"Media: "*. Se esta média for maior ou igual a 7.0, imprima a mensagem *"Aluno aprovado."*. Se a média calculada for inferior a 5.0, imprima a mensagem *"Aluno reprovado."*. Se a média calculada for um valor entre 5.0 e 6.9, inclusive estas, o programa deve imprimir a mensagem *"Aluno em exame."*.

No caso do aluno estar em exame, leia um valor correspondente à nota do exame obtida pelo aluno. Imprima então a mensagem *"Nota do exame: "* acompanhada pela nota digitada. Recalcule a média (some a pontuação do exame com a média anteriormente calculada e divida por 2). e imprima a mensagem *"Aluno aprovado."* (caso a média final seja 5.0 ou mais ) ou *"Aluno reprovado."*, (caso a média tenha ficado 4.9 ou menos). Para estes dois casos (aprovado ou reprovado após ter pego exame) apresente na última linha uma mensagem *"Media final: "* seguido da média final para esse aluno.

### Entrada

A entrada contém quatro números de ponto flutuante correspendentes as notas dos alunos.

### Saída

Todas as respostas devem ser apresentadas com uma casa decimal. As mensagens devem ser impressas conforme a descrição do problema. Não esqueça de imprimir o *enter* após o final de cada linha, caso contrário obterá "Presentation Error".



| Exemplo de Entrada       | Exemplo de Saída                                             |
| ------------------------ | ------------------------------------------------------------ |
| 2.0 4.0 7.5 8.0<br />6.4 | Media: 5.4<br />Aluno em exame.<br />Nota do exame: 6.4<br />Aluno Aprovado.<br />Media final: 5.9 |
| 2.0 6.5 4.0 9.0          | Media: 4.8<br />Aluno reprovado.                             |
| 9.0 4.0 8.5 9.0          | Media: 7.3<br />Aluno aprovado.                              |



-------------------



## Desafio 2

:red_circle:Nível: Intermediário

### Folha de pagamento

Precisamos saber quanto uma determinada empresa deve pagar para seus colaboradores, porém temos apenas a quantidade de horas trabalhadas e o valor hora. Escreva um programa que leia o número de um colaborador, seu número de horas trabalhadas, o valor que recebe por hora e calcula o salário desse colaborador. Em seguida, apresente o número e o salário do colaborador, com duas casas decimais.

### Entrada

Você receberá 2 números inteiros e 1 número com duas casas decimais, representando o número, quantidade de horas trabalhadas e o valor que o funcionário recebe por hora trabalhada.

### Saída

Exiba o número e o salário do colaborador, conforme exemplo abaixo, com um espaço em branco antes e depois da igualdade. No caso do salário, também deve haver um espaço em branco após o $.

| Exemplo de Entrada    | Exemplo de Saída                    |
| --------------------- | ----------------------------------- |
| 25<br />100<br />5.50 | NUMBER = 25<br />SALARY = U$ 550.00 |
| 1<br />200<br />20.50 | NUMBER = 1<br />SALARY = U$ 4100.00 |
| 6<br />145<br />15.55 | NUMBER = 6<br />SALARY = u$ 2254.75 |

----------------



## Desafio 3

:red_circle:Nível: Intermediário

### Validação de notas

O calendário escolar está passando bem rápido, devido a isso, as professoras de uma escola estão com dificuldade para calcular as notas dos alunos. Visando em resolver a situação, a diretora da escola contratou você para desenvolver um programa que leia as notas da primeira e da segunda avaliação de um aluno. Calcule e imprima a média semestral.

O programa só aceitará notas válidas (uma nota válida deve pertencer ao intervalo [0,10]). Cada nota deve ser validada separadamente.

No final deve ser impressa a mensagem “novo calculo (1-sim 2-nao)”, solicitando as professoras que informe um código (1 ou 2) indicando se ele deseja ou não executar o algoritmo novamente, (aceitar apenas os código 1 ou 2). Se for informado o código 1 deve ser repetida a execução de todo o programa para permitir um novo cálculo, caso contrário o programa deve ser encerrado.

## Entrada

O arquivo de entrada contém vários valores reais, positivos ou negativos. Quando forem lidas duas notas válidas, deve ser lido um valor inteiro **X** . O programa deve parar quando o valor lido para este **X** for igual a 2.

## Saída

Se uma nota inválida for lida, deve ser impressa a mensagem “nota invalida”. Quando duas notas válidas forem lidas, deve ser impressa a mensagem “media = ” seguido do valor do cálculo.

Antes da leitura de **X** deve ser impressa a mensagem "novo calculo (1-sim 2-nao)" e esta mensagem deve ser apresentada novamente se o valor da entrada padrão para **X** for menor do que 1 ou maior do que 2, conforme o exemplo abaixo.

A média deve ser impressa com dois dígitos após o ponto decimal.

| Exemplo de Entrada                                           | Exemplo de Saída                                             |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| -3.5<br />3.5<br />11.0<br />10.0<br />4<br />1<br />8.0<br />9.0<br />2 | nota invalida<br />nota invalida<br />media = 6.75<br />novo calculo (1-sim 2-nao)<br />novo calculo (1-sim 2-nao)<br />media = 8.50<br />novo calculo (1-sim 2-nao) |