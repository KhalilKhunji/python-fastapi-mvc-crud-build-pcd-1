# seed.py

from sqlalchemy.orm import Session, sessionmaker
from models.base import Base
from data.tea_data import teas_list, comments_list
from data.user_data import user_list # Add user list
from config.environment import db_URI
from sqlalchemy import create_engine

engine = create_engine(db_URI)
SessionLocal = sessionmaker(bind=engine)

try:
    print("Recreating database...")
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    print("Seeding database...")
    db = SessionLocal()

    db.add_all(teas_list)
    db.commit()

    db.add_all(comments_list)
    db.commit()

    # add users
    db.add_all(user_list)
    db.commit()

    db.close()

    print("Database seeding complete! 👋")
except Exception as e:
    print("An error occurred:", e)
