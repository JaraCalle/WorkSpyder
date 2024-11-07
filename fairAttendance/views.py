from django.shortcuts import render, redirect
from .QRCode import QRCode
from .Cuidador import Cuidador
from .Publicador import Publicador
from django.contrib.auth.decorators import user_passes_test
from fairManagement.models import FairRegistration
from WorkSpyder.settings import SERVER_IP
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import Flow
from django.conf import settings
import uuid
from googleapiclient.discovery import build

@user_passes_test(lambda u: u.is_authenticated, login_url='auth:login')
def generateQR(request, registration_id, fair_title):
    qr = QRCode()
    qr_url = qr.generateQR(registration_id)
    cuidador = Cuidador()
    cuidador.guardarEstado(qr.estado[0], qr.estado[1])
    return render(request, 'successful-inscription.html', {'registration_id': registration_id, 'fair_title': fair_title, 'qr_url': qr_url})

@user_passes_test(lambda u: u.is_authenticated, login_url='auth:login')
def readQR(request, qr_id):
    qr = QRCode()
    observador = Publicador()
    qr.agregarObservador(observador)
    qr_code = qr.readQR(request, qr_id)
    return render(request, 'read-attendance.html', {'qr': qr_code})

def google_calendar_init(request):
    state = str(uuid.uuid4())
    request.session['state'] = state

    flow = Flow.from_client_secrets_file(
        settings.GOOGLE_CLIENT_SECRETS_FILE,
        scopes=settings.GOOGLE_API_SCOPES,
        redirect_uri=settings.REDIRECT_URI
    )

    authorization_url, _ = flow.authorization_url(
        access_type='offline',
        include_granted_scopes='true',
        state=state
    )
    
    return redirect(authorization_url)


def google_calendar_redirect(request):
    state = request.session.get('state')

    flow = Flow.from_client_secrets_file(
        settings.GOOGLE_CLIENT_SECRETS_FILE,
        scopes=settings.GOOGLE_API_SCOPES,
        state=state,
        redirect_uri=settings.REDIRECT_URI
    )

    flow.fetch_token(authorization_response=request.build_absolute_uri())

    credentials = flow.credentials
    
    request.session['credentials'] = credentials_to_dict(credentials)

    return redirect('view_fairs')


def credentials_to_dict(credentials):
    return {'token': credentials.token,
            'refresh_token': credentials.refresh_token,
            'token_uri': credentials.token_uri,
            'client_id': credentials.client_id,
            'client_secret': credentials.client_secret,
            'scopes': credentials.scopes}


def schedule_fair(request, registration_id):
    try:
        credentials = Credentials(**request.session['credentials'])
    
        if credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
            request.session['credentials'] = credentials_to_dict(credentials)
    

        service = build('calendar', 'v3', credentials=credentials)

        fair = FairRegistration.objects.get(pk=registration_id).fair

        event = {
            'summary': fair.title,
            'location': fair.city,
            'description': fair.description,
            'start': {
                'dateTime': f"{fair.start_event_date}T{fair.start_hour}",
                'timeZone': 'America/Bogota',
            },
            'end': {
                'dateTime': f"{fair.end_event_date}T{fair.end_hour}",
                'timeZone': 'America/Bogota',
            },
        }

        event = service.events().insert(calendarId='primary', body=event).execute()
        
        return render(request, 'schedule-fair.html', {'fair': fair})
    
    except Exception as e:
        print(f"Error: {e}")
        return render(request, 'schedule-error.html')