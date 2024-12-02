from django.shortcuts import redirect
from urllib.parse import urlencode

from django.http import HttpResponseRedirect
from django.urls import reverse
from urllib.parse import urlencode

def user_passes_test_with_param(test_func, param_name, login_url=None):
    """
    Decorador para `user_passes_test` que permite pasar un parámetro adicional en la URL.
    """
    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            if not test_func(request.user):
                # Extraer el parámetro del POST o GET
                param_value = request.POST.get(param_name) or request.GET.get(param_name)

                # Si el parámetro existe, construimos la URL
                if param_value:
                    # Obtener la URL base del login
                    next_url = reverse(login_url)
                    # Si la URL de login ya tiene parámetros, agregamos el parámetro 'fair_id'
                    if '?' in next_url:
                        next_url += f"&next=management:register_fair"
                    else:
                        next_url += f"?next=management:register_fair"

                    if '?' in next_url:
                        next_url += f"&{param_name}={param_value}"
                    else:
                        next_url += f"?{param_name}={param_value}"
                else:
                    # Si no hay parámetro, solo redirigimos al login sin él
                    next_url = reverse(login_url)


                return HttpResponseRedirect(next_url)
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator