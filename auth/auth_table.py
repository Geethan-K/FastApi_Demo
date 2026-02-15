from auth_database import Base,engine
from auth import models

Base.metadata.create_all(bind=engine)