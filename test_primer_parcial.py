import unittest
from primer_parcial_DVL import TDDObetenerAccion


class TestMyCalculator(unittest.TestCase):

    def setUp(self):
        self.tdd = TDDObetenerAccion()

    def test_initial_value(self):
        self.assertEqual(0, self.tdd.value)

    def test_obtenerAccion_method1(self):
        self.tdd.obtenerAccion(esObligatorio="si", esDocente=True, esExterno=False, estadoRegistro="porConfirmar", tipoPersonaDestino="externo")
        self.assertEqual("actualizar", self.tdd.value)

    def test_obtenerAccion_method2(self):
        self.tdd.obtenerAccion(esObligatorio="no", esExterno=True,
                               estadoRegistro="porConfirmar", esDocente=True, tipoPersonaDestino="externo")
        self.assertEqual("registrar", self.tdd.value)


if __name__ == '__main__':
    unittest.main()
