from sqlalchemy import create_engine ,MetaData
engine=create_engine("mysql+pymysql://root@localhost:3306/flutter", isolation_level="AUTOCOMMIT")

conn=engine.connect()
meta_data=MetaData()