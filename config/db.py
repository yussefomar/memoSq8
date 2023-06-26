from sqlalchemy import create_engine ,MetaData
engine=create_engine("postgres://root:YAaKfEUJKmPULknsRRuH4Qugjeby0obQ@dpg-cid1q8liuie2ea22e110-a/flutter", isolation_level="AUTOCOMMIT")
meta_data=MetaData()