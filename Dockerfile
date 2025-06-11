# Usa imagen oficial de Python
FROM python:3.12

# Setea el directorio de trabajo
WORKDIR /app

# Copia los archivos
COPY . /app

# Instala dependencias
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expone el puerto
EXPOSE 8000

# Ejecuta el servidor
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
