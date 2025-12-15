from app.core.database import engine, Base
from app.core import models  # ensures models are registered

print("Creating database tables...")
Base.metadata.create_all(bind=engine)
print("✅ Tables created successfully!")
