# David Vargas Lastra
# com450 2/2021


class TDDObetenerAccion:

    def __init__(self):
        self.value = 0

    def obtenerAccion(self, esObligatorio, esDocente, esExterno, tipoPersonaDestino, estadoRegistro):
        if (esObligatorio == "si" and esDocente == True):
            self.value = "actualizar"
        if (esObligatorio == "no" and esDocente == True):
            self.value = "matricular"
        if (esExterno == True and estadoRegistro == "porConfirmar"):
            self.value = "actualizar"
        if (esExterno == True and tipoPersonaDestino == "esterno"):
            self.value = "registrar"
        if (esExterno == True and estadoRegistro == "Vigente"):
            self.value = "matricular"
