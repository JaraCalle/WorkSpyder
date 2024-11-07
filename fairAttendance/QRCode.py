from django.shortcuts import get_object_or_404, render
from fairManagement.models import FairRegistration
from .models import QR
from WorkSpyder.settings import SERVER_IP
from .Memento import Memento

class QRCode():
    def __init__(self):
        self.estado = []
        self.observadores = []

    def setEstado(self, qr, url):
        self.estado = [qr, url]

    def generateQR(self, registration_id):
        registration = get_object_or_404(FairRegistration, id=registration_id)

        # Corrigue el error de que al estar viendo el QR recarguen la página y se generen más QR's
        if QR.objects.filter(registration=registration).exists():        
            qr = get_object_or_404(QR, registration=registration)
        else:
            qr = QR(registration=registration)
            qr.save()

        qr_url = f"http://{ SERVER_IP }/attendance/read-attendance/{ qr.id }"
        self.guardar(qr, qr_url)

        return qr_url
    
    def readQR(self, request, qr_id):
        qr = get_object_or_404(QR, id=qr_id)
        registro = qr.registration
        feria = registro.fair
        organizador = feria.organizer
        
        # Si el usuario logeado no es el creador de la feria no puede marcar la asistencia
        if organizador != request.user:
            return render(request, 'denied-permission.html')

        qr.set_as_read()

        self.notificarObservadores(qr, request)

        return qr
    
    def guardar(self, qr, url):
        self.setEstado(qr, url)
        memento = Memento(self.estado)
        return memento
    
    def restaurar(self, memento):
        estado = memento.getEstado()
        qr = estado[0]
        url = estado[1]
        return qr, url
    
    def agregarObservador(self, observador):
        if observador not in self.observadores:
            self.observadores.append(observador)

    def eliminarObservador(self, observador):
        if observador in self.observadores:
            self.observadores.remove(observador)

    def notificarObservadores(self, qr, request):
        for observador in self.observadores:
            observador.update(qr, request) 
