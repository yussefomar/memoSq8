instalar un ambiente 
pip install virtualenv
despues
python3 -m venv nombredelambiente
despues
si es linux source venv/bin/activate
si es windows en cmd: venv\Scripts\activate.bat

despues
pip install fastapi
despues
pip install uvicorn

Finalmente para ejecutarlo
uvicorn main:app --reload

para ver el swagger: 8000 es el puerto por defecto
http://127.0.0.1:8000/docs#/default/

paquetes para la base de datos(mysql)
pip install sqlalchemy pymysql cryptography
