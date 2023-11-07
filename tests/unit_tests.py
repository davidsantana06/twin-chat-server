from os import path
from typing import List
from unittest import TestCase, TestLoader, TestSuite, TextTestRunner
import sys

ROOT_FOLDER = path.abspath(
    path.join(
        path.dirname(__file__), '..'
    )
)
sys.path.append(ROOT_FOLDER)

from app.lib.twin_chatter import TwinChatter


class TwinChatterResponseTests(TestCase):
    def setUp(self):
        self.twin_chatter = TwinChatter()

    def assert_equal(self, statements: List[str], expected_response: str) -> None:
        for statement in statements:
            response = self.twin_chatter.get_response(statement)
            self.assertIn(expected_response, response)

    def test_01_main_exercises(self) -> None:
        self.assert_equal(
            [
                'quais são os principais exercícios de musculação?',
                'quais são os exercícios mais importantes na musculação?'
            ],
            'Os principais exercícios de musculação incluem agachamento, supino, levantamento terra, barra fixa, rosca direta, desenvolvimento com halteres, entre outros.'
        )

    def test_02_best_supplements(self) -> None:
        self.assert_equal(
            [
                'quais suplementos são mais indicados para ganhar músculos?',
                'quais suplementos são recomendados para o ganho de massa muscular?'
            ],
            'Os suplementos mais indicados para ganhar músculos incluem creatina, beta alanina e proteínas em pó (caso haja alguma deficiência na meta de proteína diária). Esses suplementos podem ajudar no aumento da massa muscular, na recuperação e no desempenho durante os treinos. No entanto, é importante consultar um profissional de saúde ou nutricionista antes de adicionar suplementos à sua dieta.'
        )

    def test_03_muscular_group_exercises(self) -> None:
        self.assert_equal(
            ['quais exercícios devo fazer para o bíceps?', 'me indique exercícios para o bíceps'],
            'Para trabalhar o bíceps, você pode incluir exercícios como Rosca Direta, Rosca Alternada, Rosca Martelo, Rosca Concentrada, e Rosca Scott.'
        )

    def test_04_exercise_substitutions(self) -> None:
        self.assert_equal(
            ['qual exercício devo fazer no lugar de supino reto barra?'],
            'Você pode fazer Supino Reto Halteres; Supino Reto Smith.'
        )

    def test_05_training_time(self) -> None:
        self.assert_equal(
            ['qual é o melhor horário para treinar?', 'em qual horário eu devo treinar?'],
            'Quando se trata do horário ideal para treinar, não há uma regra geral. O que importa é o que funciona melhor para você. O ideal é escolher o momento em que você se sinta mais disposto e tenha mais tempo disponível.'
        )

    def test_06_bulking_diet(self) -> None:
        self.assert_equal(
            ['o que devo comer para ganhar músculos?', 'qual é a melhor dieta para ganhar massa muscular?'],
            'Para ganhar massa muscular, é crucial manter uma dieta equilibrada com um superávit calórico. Inicialmente, você pode começar com uma dieta contendo 4g/Kg de carboidratos, 2g/Kg de proteínas e 1g/Kg de gorduras. À medida que progredir, poderá ajustar esses valores, aumentando a ingestão de carboidratos e mantendo os demais macronutrientes.'
        )

    def test_07_illness_handling(self) -> None:
        self.assert_equal(
            ['fiquei doente, o que fazer?', 'como devo agir quando estou doente?'],
            'Se você estiver doente, é melhor não treinar. O corpo precisa de energia para se recuperar e, se você treinar, estará desviando essa energia para o treino. Além disso, você pode transmitir a doença para outras pessoas. Portanto, é melhor ficar em casa e descansar até que esteja totalmente recuperado.'
        )


if __name__ == '__main__':
    test_loader = TestLoader()
    test_suite = TestSuite()
    test_runner = TextTestRunner()

    test_suite.addTest(
        test_loader.loadTestsFromTestCase(TwinChatterResponseTests)
    )

    test_runner.run(test_suite)
