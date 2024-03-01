from sqlalchemy import create_engine
from sqlalchemy import text

engine = create_engine('mysql://root:@localhost/temp')
con = engine.connect()

result = con.execute(text("SELECT * FROM admin"))

for data in result:
    print(data)
