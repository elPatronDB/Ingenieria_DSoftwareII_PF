import unittest
from juego_DB import compararJugada 

class TestJuegoPiedraPapelTijera(unittest.TestCase):
    def test_piedra_vs_piedra(self):
        self.assertEqual(compararJugada("piedra", "piedra"), 1000) 

    def test_piedra_vs_papel(self):
        self.assertEqual(compararJugada("piedra", "papel"), -1)  

    def test_piedra_vs_tijera(self):
        self.assertEqual(compararJugada("piedra", "tijera"), 1) 

    def test_papel_vs_piedra(self):
        self.assertEqual(compararJugada("papel", "piedra"), 1) 
    def test_papel_vs_papel(self):
        self.assertEqual(compararJugada("papel", "papel"), 0)

    def test_papel_vs_tijera(self):
        self.assertEqual(compararJugada("papel", "tijera"), -1) 

    def test_tijera_vs_piedra(self):
        self.assertEqual(compararJugada("tijera", "piedra"), -1) 

    def test_tijera_vs_papel(self):
        self.assertEqual(compararJugada("tijera", "papel"), 1) 

    def test_tijera_vs_tijera(self):
        self.assertEqual(compararJugada("tijera", "tijera"), 0)

if __name__ == '__main__':
    unittest.main()