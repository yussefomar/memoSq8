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