
class Config():
    pass

class DesarrolloConfig(Config):
    DEBUG = True


config = {
    'Desarrollo':DesarrolloConfig,
    'produccion':Config
}
