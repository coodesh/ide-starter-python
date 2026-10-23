import unittest

from app.core import greet


class GreetTest(unittest.TestCase):
    def test_cumprimenta_pelo_nome(self):
        self.assertEqual(greet("Ana"), "Olá, Ana!")


if __name__ == "__main__":
    unittest.main()
