from django.contrib import messages

class Publicador():
    def update(self, qr, request):
        if qr.isRead:
            messages.success(request, 'Tu QR ha sido leído con éxito!')
