from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager
from auth.models import Base, User
from config import conf
from datetime import datetime

DATABASE_URL = conf().get("database_url")

class Database:
    def __init__(self, database_url=DATABASE_URL):
        self.engine = create_engine(database_url)
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        Base.metadata.create_all(bind=self.engine)

    @contextmanager
    def get_session(self):
        session = self.SessionLocal()
        try:
            yield session
            session.commit()
        except Exception as e:
            session.rollback()
            raise
        finally:
            session.close()

    

# Usage example:
# db = Database()
# with db.get_session() as session:
#     # Perform database operations using the session
# db.add_user(open_id="user_open_id", union_id="user_union_id", follow_time=datetime.now())
