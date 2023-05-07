# Define la imagen base
FROM python:3.10

# Establece el directorio de trabajo en el directorio raíz de la aplicación
WORKDIR /app

# Copia el archivo de requisitos a la imagen
COPY requirements.txt .

# Instala las dependencias de la aplicación
RUN pip install -r requirements.txt

# Copia el resto de la aplicación a la imagen
COPY . .

# Expone el puerto 8000 para que sea accesible desde el exterior
EXPOSE 8000

# Define el comando por defecto que se ejecutará cuando se inicie el contenedor
CMD ["python", "manage.py", "test", "backend.api.tests"]

