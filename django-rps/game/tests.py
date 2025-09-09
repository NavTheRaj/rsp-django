from django.test import SimpleTestCase
from .views import outcome


class OutcomeTests(SimpleTestCase):
def test_tie(self):
self.assertEqual(outcome('rock', 'rock'), 'tie')


def test_wins(self):
self.assertEqual(outcome('rock', 'scissors'), 'win')
self.assertEqual(outcome('paper', 'rock'), 'win')
self.assertEqual(outcome('scissors', 'paper'), 'win')


def test_loses(self):
self.assertEqual(outcome('rock', 'paper'), 'lose')
self.assertEqual(outcome('paper', 'scissors'), 'lose')
self.assertEqual(outcome('scissors', 'rock'), 'lose')


def test_invalid(self):
self.assertEqual(outcome('lizard', 'spock'), 'invalid')