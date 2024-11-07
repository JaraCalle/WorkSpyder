from .QRCode import QRCode

class Cuidador():
    def __init__(self):
        self.originador = QRCode()
        self.memento = None

    def guardarEstado(self, qr, url):
        memento = self.originador.guardar(qr, url)
        self.memento = memento

    def deshacer(self):
        if self.memento:
            memento = self.memento
            qr, url = self.originador.restaurar(memento)
            return qr, url
        return None