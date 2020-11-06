class Aluno:
    def __init__(self, nome, sobrenome, nota_bimestre_1, nota_bimestre_2, nota_bimestre_3, nota_bimestre_4):
        self.nome = nome
        self.sobrenome = sobrenome
        self.nota_bimestre_1 = nota_bimestre_1
        self.nota_bimestre_2 = nota_bimestre_2
        self.nota_bimestre_3 = nota_bimestre_3
        self.nota_bimestre_4 = nota_bimestre_4

    def calcula_media(self):
        media = (self.nota_bimestre_1 + self.nota_bimestre_2 + self.nota_bimestre_3 + self.nota_bimestre_4)/4
        if media >= 7:
            return 'Aprovado'
        else:
            return self.calcula_recuperacao(5, media)

    def calcula_recuperacao(self, nota_recuperacao, media):
        if nota_recuperacao + media >= 10:
            return 'Aprovado na Recuperação'
        else:
            return 'Reprovado na Recuperação'

mario = Aluno('Mario', 'Silva', 4, 7, 6, 4)
print(f'{mario.nome} {mario.sobrenome} foi {mario.calcula_media()}')

joao = Aluno('João', 'Souza', 8,6,7,9)
maria = Aluno('Maria', 'Fernandes', 5,7,8,7)