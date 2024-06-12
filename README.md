# API RESTful con Flask, Firebase y Twilio

## Descripción

Esta API RESTful permite enviar un PIN de 4 dígitos a un teléfono móvil vía SMS utilizando Firebase y Twilio para validar el inicio de sesión del usuario o registrarlo.

## Requisitos Previos

- Python 3.12
- Una cuenta de Firebase
- Una cuenta de Twilio

## Instalación

1. Clona este repositorio:
   ```bash
   git clone https://github.com/msedeno23/auth_users.git
Navega al directorio del proyecto:
bash
Copiar código
cd tu_repositorio
Crea un entorno virtual (opcional pero recomendado):
bash
Copiar código
python -m venv venv
source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
Instala las dependencias:
bash
Copiar código
pip install -r requirements.txt
Configuración
Configura Firebase:

Ve a la consola de Firebase y crea un proyecto.
Descarga el archivo de credenciales JSON y colócalo en el directorio del proyecto con el nombre firebase_config.json.
Configura Twilio:

Regístrate en Twilio y consigue tu SID de cuenta, tu token de autenticación y tu número de teléfono de Twilio.
Reemplaza los valores de TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN y TWILIO_PHONE_NUMBER en el archivo app.py con los datos de tu cuenta de Twilio.
Ejecución
Ejecuta la aplicación:
bash

python app.py
Endpoints de la API
Enviar PIN
URL: /send_pin
Método: POST
Descripción: Envía un PIN de 4 dígitos al número de teléfono proporcionado.
Parámetros:
phone_number (string, requerido): El número de teléfono al que se enviará el PIN.
Ejemplo de solicitud:
json

{
  "phone_number": "+1234567890"
}

Verificar PIN
URL: /verify_pin
Método: POST
Descripción: Verifica el PIN proporcionado para el número de teléfono.
Parámetros:
phone_number (string, requerido): El número de teléfono que se está verificando.
pin (string, requerido): El PIN que se quiere verificar.
Ejemplo de solicitud:
json

{
  "phone_number": "+1234567890",
  "pin": "1234"
}

Contribución
Si deseas contribuir a este proyecto, por favor sigue los siguientes pasos:

Haz un fork del proyecto
Crea una rama con tu función (git checkout -b feature/nueva-funcion)
Realiza los cambios y haz commit (git commit -am 'Agrega nueva función')
Sube los cambios a tu fork (git push origin feature/nueva-funcion)
Abre un Pull Request

Licencia
Este proyecto está licenciado bajo la MIT License.

