from flask import Blueprint, request, jsonify, session
from .firebase import db
from .twilio_client import client
import random
from datetime import datetime
from .config import Config
import logging

api = Blueprint('api', __name__)
logger = logging.getLogger(__name__)

@api.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok'}), 200

@api.route('/send_pin', methods=['POST'])
def send_pin():
    data = request.json
    phone = data.get('phone')

    if not phone:
        return jsonify({"mensaje": "Número de teléfono no proporcionado", "resultado": False}), 400

    pin = random.randint(1000, 9999)
    db.collection('verifications').document(phone).set({
        'pin': pin,
        'timestamp': datetime.now()
    })

    try:
        message = client.messages.create(
            body=f'Su código de verificación es {pin}',
            from_=Config.TWILIO_PHONE_NUMBER,
            to=phone
        )
        return jsonify({"mensaje": "PIN enviado exitosamente", "resultado": True})
    except Exception as e:
        logger.error("Error al enviar PIN: %s", str(e), exc_info=True)
        return jsonify({"mensaje": "Error al enviar PIN", "resultado": False}), 500

@api.route('/register', methods=['POST'])
def register():
    data = request.json
    phone = data.get('phone')
    pin = data.get('pin')

    if not phone or not pin:
        return jsonify({"mensaje": "Número de teléfono o PIN no proporcionado", "resultado": False}), 400

    doc_ref = db.collection('verifications').document(phone)
    doc = doc_ref.get()

    if doc.exists:
        stored_pin = doc.to_dict().get('pin')
        if int(pin) == stored_pin:
            user_ref = db.collection('users').document(phone)
            user_ref.set({
                'phone': phone,
                'registered': True
            })
            session['user'] = phone
            return jsonify({"mensaje": "Usuario registrado exitosamente", "resultado": True})
        else:
            return jsonify({"mensaje": "PIN incorrecto. Inténtalo de nuevo.", "resultado": False}), 401
    else:
        return jsonify({"mensaje": "No se encontró un PIN para este número de teléfono.", "resultado": False}), 404

@api.route('/logout', methods=['GET'])
def logout():
    session.pop('user', None)
    return jsonify({"mensaje": "Sesión Cerrada", "resultado": True})
