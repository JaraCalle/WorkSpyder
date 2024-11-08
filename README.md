# WorkSpyder

![WorkSpyder Logo](https://cdn-icons-png.freepik.com/512/1301/1301579.png)

**WorkSpyder** es una plataforma que permite a empresas organizar ferias de trabajo y gestionar todos los aspectos relacionados con los registros. Los aspirantes pueden inscribirse en las ferias, marcarlas como favoritas y acceder a otras funcionalidades para mejorar su experiencia en la búsqueda de empleo.

## Características

- **Gestión de Ferias de Trabajo**: Las empresas pueden crear, editar y gestionar eventos.
- **Registro de Aspirantes**: Los usuarios pueden registrarse como aspirantes y marcar eventos como favoritos.
- **Sistema de Autenticación**: Solo los usuarios registrados pueden acceder a ciertas funcionalidades como la creación de ferias.
- **Filtrado de Ferias**: Los aspirantes pueden filtrar ferias de trabajo por ubicación, fecha y tipo de empresa.
- **Interfaz Personalizada**: Estilos personalizados con un diseño minimalista y moderno.

## Tecnologías Utilizadas

- **Backend**: Django 4.x
- **Frontend**: HTML5, CSS3, JavaScript (con Bootstrap)
- **Base de Datos**: SQLite (por defecto) / Soporte para PostgreSQL
- **Autenticación**: Sistema de usuarios de Django
- **Despliegue de Medios**: Manejo de archivos de imagen mediante `ImageField` de Django

## Instalación

1. Clona este repositorio:
   ```bash
   git clone https://github.com/tu_usuario/workspyder.git
   cd workspyder
    ```
2. Crea y activa un entorno virtual
  * Linux - MacOS
      ```bash
      python -m venv venv
      source venv/bin/activate
      ```
  * Windows
      ```bash
      python -m venv venv
      venv\Scripts\activate
      ```
3. Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```
4. Realiza las migraciones de la base de datos:
    ```bash
    python manage.py migrate
    ```
5. Ejecuta el servidor de desarrollo:
    ```bash
    python manage.py runserver
    ```

## Uso
### Crear un evento
1. Accede a la sección Pon tu evento en WorkSpyder desde el navbar.
2. Completa el formulario con los detalles del evento, incluyendo título, fecha, lugar y un ponente destacado.
3. El evento será publicado y accesible a todos los aspirantes.
### Filtrar ferias
  * Ubicacion
  * Fecha del evento
  * Tipo de empresa

### Registro de Aspirantes
1. Los aspirantes pueden registrarse en la plataforma y automáticamente se les creará un perfil con el cual podrán acceder a las funcionalidades exclusivas de usuarios registrados.
