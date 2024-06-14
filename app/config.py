import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
    TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
    TWILIO_PHONE_NUMBER = os.getenv('TWILIO_PHONE_NUMBER')
    FIREBASE_CREDENTIALS = os.getenv('FIREBASE_CREDENTIALS')
    CORS_ORIGINS = os.getenv('CORS_ORIGINS', 'http://localhost:5173')
    SECRET_KEY = os.getenv('SECRET_KEY')
    SESSION_TYPE = 'filesystem'
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_SAMESITE = 'None'
    SESSION_COOKIE_HTTPONLY = True

    @classmethod
    def validate(cls):
        required_vars = [
            'TWILIO_ACCOUNT_SID',
            'TWILIO_AUTH_TOKEN',
            'TWILIO_PHONE_NUMBER',
            'FIREBASE_CREDENTIALS',
            'SECRET_KEY'
        ]
        for var in required_vars:
            if not getattr(cls, var):
                raise ValueError(f"Environment variable {var} is missing")

Config.validate()