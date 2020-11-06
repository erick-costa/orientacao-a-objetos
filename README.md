# Projeto introdução a orientação a objetos

> Calcula a média de notas de 4 bimestres e retorna se foi aprovado ou reprovado

Neste projeto existem dois módulos: no primeiro (escola.py), contém uma classe onde suas instâncias recebem um nome,
sobrenome e 4 notas. Dentro dessa classe, há duas funções: a primeira (calcula_media), recebe as notas de uma 
instância, calcula a média das notas e se a média for maior ou igual 7, é retornado "Aprovado", se não, é chamado a
segunda função da classe (calcula_recuperacao). Essa função recebe a média da instância (aluno) e uma nota de recuperação
e retorna "Aprovado na recuperação" se a nota de recuperação somado com a média for maior ou igual a 10, se não alcançado
esse valor, a função retorna "Reprovado na recuperação". 

No segundo (test_escola.py), é feito alguns testes nas funções calcula_media e calcula_recuperacao,
por exemplo, se a mensagem retornada é o esperado.

## Programação Estruturada (PE) x Programação Orientada a Objetos (POO)
A programação estruturada (PE) é uma forma de programação baseada em 3 estruturas (sequência, decisão e repetição)
onde se é mais fácil de compreender e aprender, já a Orientada a Objetos é um tipo de programação feita em camadas
onde se usa objetos de diferentes fontes para fazer parte do código.

* PE pode ser utilizada quando o programa é simples e não integra outros sistemas
* POO pode ser utilizada quando se busca uma melhor organização de código e programas mais complexos

## Como Rodar
### escola.py
```python escola.py```

### test_escola.py
```python -m unittest test_escola.TestEscola```