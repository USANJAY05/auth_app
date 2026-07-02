from src.core.conf import Base, engine
from src.models.users import User

def init_db():
    Base.metadata.create_all(
        bind=engine
    )
