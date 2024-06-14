import firebase_admin
from firebase_admin import credentials, firestore
from .config import Config

cred = credentials.Certificate(Config.FIREBASE_CREDENTIALS)
firebase_admin.initialize_app(cred)
db = firestore.client()
