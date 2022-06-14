import os

class Config():
    SECRET_KEY = os.environ.get('SECRET_KEY')

class DesarrolloConfig(Config):
    DEBUG = True


config = {
    'Desarrollo':DesarrolloConfig,
    'produccion':Config
}
