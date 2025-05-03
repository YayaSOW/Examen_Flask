import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app/ges_produits.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = 'cle_secrete'      