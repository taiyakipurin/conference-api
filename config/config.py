import os

base_dir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(base_dir, '../data', 'data.db')

class Config:
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{db_path}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'DH#82#@(DE))WCxnsD#*&823W(dn'
    
    MAX_THREAD_POOL_WORKERS = 10
    MAX_CONCURRENT_BOOKINGS = 5
    THREAD_TIMEOUT_SECONDS = 30
    DB_CONNECTION_POOL_SIZE = 20