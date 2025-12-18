from app.core.database import engine
from app.core.models import Base

print("Creating tables...")
Base.metadata.create_all(bind=engine)
print("Tables created successfully.")
