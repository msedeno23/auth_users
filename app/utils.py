import random

def generate_pin():
    return random.randint(1000, 9999)

def send_pin(phone, pin):
    # Implementa la lógica para enviar el PIN al número de teléfono.
    print(f"Sending PIN {pin} to phone {phone}")

def format_phone_number(phone, country_code="+52"):
    # Asegurarse de que el número de teléfono no tenga espacios ni guiones y que comience con el código del país
    phone = phone.replace(" ", "").replace("-", "")
    if not phone.startswith(country_code):
        phone = country_code + phone
    return phone
