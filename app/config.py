class Config:
    # Configuración de Mysql
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = ''
    MYSQL_DB = 'posts'
    MYSQL_CURSORCLASS = 'DictCursor'


    # Additional configuration
    DEBUG = True
    SECRET_KEY = 'your_secret_key'