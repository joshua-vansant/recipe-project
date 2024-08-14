import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('postgresql://jmvs_project_storage_user:3CaSFRahhno5g1xINy0mGPrH7Mo2D61T@dpg-cqtqjpjv2p9s73ci779g-a.oregon-postgres.render.com/jmvs_project_storage', 'sqlite:///local.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
