from src.core.conf import Base, engine
from src.models.users import User

def init_db():
    try:
        Base.metadata.create_all(
            bind=engine
        )
    except Exception as e:
        print("Failed to Connect to DB try to run the db and then start the app")
