from app.database.session import engine
from app.models.request_log import RequestLog
from app.database.session import Base

def init_db():
    print("Creating database tables...")
    Base.metadata.create_all(bind=engine)
    print("Done.")

if __name__ == "__main__":
    init_db()