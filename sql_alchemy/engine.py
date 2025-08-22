from sql_alchemy import create_engine,text
from sql_alchemy.engine import URL
db_credentials={
    "drivername":"postgresql+psycopg",
    "host":"aws-0-ap-south-1.pooler.supabase.com ",
    "username":"postgres.qmtomdynrkhdyyyrdpjs",
    "password":"P4+2ygpUyL+sV7v ",
    "port":5432,
    "database":"postgres"
}

#Build DB URL
#kwags of database cridentials
DATABASE_URL=URL.create(**db_credentials)

#create engine
#the echo  tells sql alchemy to log all the generated sql to the console

engine=create_engine(DATABASE_URL,echo=True,future=True)

with engine.connect() as conn:
    result=conn.execute(text("SELECT * FROM employee"))
    rows=result.fetchall()

    for row in rows:
        print(row)