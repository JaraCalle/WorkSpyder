from django.test import TestCase
from fairAttendance.QRCode import QRCode
from fairAttendance.models import QR
from fairAttendance.Publicador import Publicador
from auth.models import CustomUser
from fairManagement.models import FairRegistration, JobFair, Aspirant
from datetime import date
from django.contrib.messages import get_messages
from django.urls import reverse

class QRCodeTestCase(TestCase):

    def setUp(self):
        # Crear un usuario de prueba
        self.user = CustomUser.objects.create_user(email='test@mail.com')

        # Crear un JobFair de prueba
        self.job_fair = JobFair.objects.create(
            title="Test Job Fair",
            start_event_date=date.today(),
            end_event_date=date.today(),
            direction="Test direction",
            keynote_speaker="Test Speaker",
            image=None,  # Si no necesitas una imagen, pon None o usa una imagen ficticia
            organizer=self.user
        )
        
        # Crear un Aspirant y asociarlo con el usuario
        self.aspirant = Aspirant.objects.create(
            firstName="John", secondName="Doe", lastName="Smith", phone="1234567890", user=self.user
        )

        # Crear una inscripción de prueba en la feria
        self.fair_registration = FairRegistration.objects.create(
            aspirant=self.aspirant, fair=self.job_fair, registrationDate=date.today()
        )

        # Crear un objeto QR que esté asociado con esta inscripción
        self.qr = QR.objects.create(registration=self.fair_registration)

        # Crear un QRCode y establecer su estado
        self.qr_code = QRCode()
        self.qr_code.setEstado(self.qr, "http://some-url.com")

        # Crear el observador y agregarlo al QR
        self.observador = Publicador()
        self.qr_code.agregarObservador(self.observador)

    def test_notify_user_on_qr_read(self):
        # Usamos reverse para obtener la URL de la vista 'successful_attendance' con el qr_id
        url = reverse('successful_attendance', kwargs={'qr_id': self.qr.id})

        # Simulamos una solicitud usando self.client.get, lo que automáticamente maneja los middlewares
        self.client.force_login(self.user)
        response = self.client.get(url)

        # Verificamos si la respuesta fue exitosa (200 OK)
        self.assertEqual(response.status_code, 200)

        # Verificar si el mensaje se ha agregado
        messages = list(get_messages(response.wsgi_request))
        print("Mensajes: ", messages)  # Depuración: Ver los mensajes

        # Si el mensaje está presente, verificamos si es el correcto
        if messages:
            print("Primer mensaje: ", str(messages[0]))  # Depuración: Imprimir el primer mensaje
            self.assertEqual(str(messages[0]), 'Tu QR ha sido leído con éxito!')
        else:
            self.fail("No se generaron mensajes.")

    def test_memento_save_and_restore(self):
        # Guardamos el estado inicial del QR
        estado_inicial = self.qr_code.estado
        print(f"Estado inicial: {estado_inicial}")  # Imprimir el estado inicial
        memento = self.qr_code.guardar(self.qr, "http://some-url.com")
        
        # Modificamos el estado del QR
        self.qr_code.setEstado(self.qr, "http://new-url.com")
        print(f"Nuevo estado: {self.qr_code.estado}")  # Imprimir el nuevo estado
        
        # Aseguramos que el estado actual sea diferente
        self.assertNotEqual(self.qr_code.estado, estado_inicial, "El estado no debería ser el mismo después de cambiarlo.")
        
        # Restauramos el estado desde el Memento
        restored_qr, restored_url = self.qr_code.restaurar(memento)
        print(f"Estado restaurado: {restored_qr}, {restored_url}")  # Imprimir el estado restaurado
        
        # Verificamos que el estado restaurado sea el mismo que el estado guardado
        self.assertEqual(restored_qr, self.qr, "El QR restaurado no es el mismo.")
        self.assertEqual(restored_url, "http://some-url.com", "La URL restaurada no es la misma.")

        
    def test_memento_not_overwrite_changes(self):
        # Guardamos el estado inicial
        memento = self.qr_code.guardar(self.qr, "http://some-url.com")
        
        # Cambiamos el estado del QR
        self.qr_code.setEstado(self.qr, "http://new-url.com")
        
        # Aseguramos que el estado actual del QR es diferente
        self.assertEqual(self.qr_code.estado[1], "http://new-url.com", "La URL no se actualizó correctamente.")
        
        # Restauramos el estado desde el Memento
        restored_qr, restored_url = self.qr_code.restaurar(memento)
        
        # Verificamos que el estado restaurado no sobrescriba los cambios no guardados
        self.assertNotEqual(self.qr_code.estado[1], restored_url, "El estado restaurado no debería sobrescribir el estado actual.")
