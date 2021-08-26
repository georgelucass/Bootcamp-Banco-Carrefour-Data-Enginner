# Soluções Aritméticas em Python

## Desafio 1

🔴 Nível: Básico

### Notas de Prova

Norminia é uma professora e pesquisadora renomada de uma famosa Universidade do Brasil, com inúmeras prêmiações e reconhecimento internacional pelo seu trabalho. Recentemente, Norminia foi convidada para ministrar aulas em uma Universidade da Alemanhã. Mesmo falando muito bem a Língua alemã, Norminia ficou um pouco apreensiva com a responsabilidade, mas resolveu aceitar a proposta e encará-la como um bom desafio.

Os estudantes adoraram a metodologia de ensino de Norminia e tudo estava indo super bem, até o momento da aplicação da sua primeira prova. Acostumada a dar notas de 0 (zero) a 100 (cem), ela fez o mesmo na primeira prova da sua turma da Alemanhã. No entanto, os estudante acharam estranho, uma vez que na Alemanhã o sistema de notas é diferente: as notas devem ser dadas como conceitos de A a E. O conceito A é o mais alto, enquanto o conceito E é o mais baixo.

Conversando com outros docentes, ela recebeu a sugestão de utilizar a seguinte tabela, relacionando as notas numéricas com as notas de conceitos:

| Nota     | Conceito |
| -------- | -------- |
| 0        | E        |
| 1 a 35   | D        |
| 36 a 60  | C        |
| 31 a 65  | B        |
| 86 a 100 | A        |

O problema é que Norminia já deu as notas no sistema numérico, e terá que converter as notas para o sistema de letras. No entanto, Norminia precisa preparar as próximas atividades educacionais para os seus alunos, e não tem tempo suficiente para fazer a conversão das notas manualmente.

Você terá o seguinte desafio: escrever um programa que recebe uma nota no sistema numérico e determina o conceito correspondente.

### Entrada

A entrada contém um único conjunto de testes, que deve ser lido do dispositivo de entrada padrão (normalmente o teclado). A entrada contém uma única linha com um número inteiro N (0 ≤ N ≤ 100), representando uma nota de prova no sistema numérico.

### Saída

Seu programa deve imprimir, na saída padrão, uma letra (A, B, C, D, ou E em maiúsculas) representando o conceito correspondente à nota dada na entrada.

| Exemplo de Entrada | Exemplo de Saída |
| ------------------ | ---------------- |
| 12                 | D                |
| 87                 | A                |
| 0                  | E                |

------

## Desafio 2

🔴Nível: Básico

### Preenchimento de vetor I

Você recebeu o desafio de ler um valor e criar um programa que coloque o valor lido na primeira posição de um vetor N[10]. Em cada posição subsequente, coloque o dobro do valor da posição anterior. Por exemplo, se o valor lido for 1, os valores do vetor devem ser 1,2,4,8 e assim sucessivamente. Mostre o vetor em seguida.

### Entrada

A entrada contém um valor inteiro **(V<=50)**.

### Saída

Para cada posição do vetor, escreva "N[**i**] = **X**", onde **i** é a posição do vetor e **X** é o valor armazenado na posição **i**. O primeiro número do vetor N (N[0]) irá receber o valor de V.

| Exemplo de Entrada | Exemplo de Saída               |
| ------------------ | ------------------------------ |
| 1                  | N[0] = 1 N[1] = 2 N[2] = 4 ... |

------

## Desafio 3

🔴Nível: Básico

### Triângulo

Leia 3 valores reais (A, B e C) e verifique se eles formam ou não um triângulo. Em caso positivo, calcule o perímetro do triângulo e apresente a mensagem:

Perimetro = XX.X

Em caso negativo, calcule a área do trapézio que tem A e B como base e C como altura, mostrando a mensagem

Area = XX.X

## Entrada

A entrada contém três valores reais.

## Saída

O resultado deve ser apresentado com uma casa decimal.

| Exemplo de Entrada | Exemplo de Saída |
| ------------------ | ---------------- |
| 6.0 4.0 2.0        | Área = 10.0      |
| 6.0 4.0 2.1        | Perímetro = 12.1 |