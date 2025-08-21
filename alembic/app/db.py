
#File for connecting to  our db
from sqlalchemy import create_engine,text
from sqlalchemy.engine import URL
from sqlalchemy.orm import declarative_base,sessionmaker


db_credentials={
   "drivername":"postgresql+psycopg",
    "host":"aws-0-ap-south-1.pooler.supabase.com ",
    "username":"postgres.qmtomdynrkhdyyyrdpjs",
    "password":"P4+2ygpUyL+sV7v ",
    "port":5432,
    "database":"postgres"
}

#BUILD URL
DATABASE_URL=URL.create(**db_credentials)

engine=create_engine(DATABASE_URL,echo=True,future=True)


SessionLocal=sessionmaker(bind=engine,autoflush=False,autocommit=False)

#BASE
Base=declarative_base()

 