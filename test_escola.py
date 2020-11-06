from escola import Aluno
from unittest import TestCase

class TestEscola(TestCase):
    def test_aprovado_true(self):
        vitor = Aluno ('Vitor', 'Rodrigues', 7,8,9,6)
        res = vitor.calcula_media()
        self.assertEqual(res, 'Aprovado')

    def test_aprovado_false(self):
        vitor = Aluno('Vitor', 'Rodrigues', 7, 8, 9, 6)
        res = vitor.calcula_media()
        self.assertNotEqual(res, 'Reprovado')

    def test_aprovado_rec_true(self):
        vitor = Aluno('Vitor', 'Rodrigues', 7, 8, 6, 6)
        res = vitor.calcula_media()
        self.assertEqual(res, 'Aprovado na Recuperação')

    def test_aprovado_rec_false(self):
        vitor = Aluno('Vitor', 'Rodrigues', 7, 8, 6, 6)
        res = vitor.calcula_media()
        self.assertNotEqual(res, 'Reprovado na Recuperação')

    def test_reprovado_true(self):
        vitor = Aluno('Vitor', 'Rodrigues', 7, 2, 3, 6)
        res = vitor.calcula_media()
        self.assertEqual(res, 'Reprovado na Recuperação')

    def test_reprovado_true(self):
        vitor = Aluno('Vitor', 'Rodrigues', 7, 2, 3, 6)
        res = vitor.calcula_media()
        self.assertNotEqual(res, 'Aprovado na Recuperação')

    def test_type_calcula_media(self):
        vitor = Aluno('Vitor', 'Rodrigues', 7, 8, 9, 6)
        res = vitor.calcula_media()
        self.assertEqual(type(res), str)

    def test_type_calcula_recuperacao(self):
        vitor = Aluno('Vitor', 'Rodrigues', 7, 6, 6, 6)
        res = vitor.calcula_media()
        self.assertEqual(type(res), str)
