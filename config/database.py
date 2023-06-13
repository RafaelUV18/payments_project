import databases
import sqlalchemy

DATABASE_URL = "sqlite:///./test.db"

database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()

payments = sqlalchemy.Table(
    "payments",
    metadata,
    sqlalchemy.Column("Fecha", sqlalchemy.Date),
    sqlalchemy.Column("Cliente", sqlalchemy.String),
    sqlalchemy.Column("Monto ", sqlalchemy.DECIMAL),
    sqlalchemy.Column("Proveedor ", sqlalchemy.String),
)

engine = sqlalchemy.create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

# metadata.create_all(engine)