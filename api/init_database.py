from sqlmodel import create_engine,Session
import os

# Prefer an external database (e.g. Render Postgres) via DATABASE_URL,
# falling back to a local SQLite file for development.
DATABASE_URL = os.environ.get('DATABASE_URL')
if DATABASE_URL:
    # Render/Heroku style URLs use the 'postgres://' scheme which SQLAlchemy
    # no longer accepts; normalise to 'postgresql://'.
    if DATABASE_URL.startswith('postgres://'):
        DATABASE_URL = DATABASE_URL.replace('postgres://', 'postgresql://', 1)
else:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DB_DIR = os.path.join(BASE_DIR, '..', 'db')
    os.makedirs(DB_DIR, exist_ok=True)
    DATABASE_URL = f"sqlite:///{os.path.join(DB_DIR, 'database.db')}"

# Create the database engine
engine = create_engine(DATABASE_URL,echo=False)