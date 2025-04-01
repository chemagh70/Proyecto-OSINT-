# Utilizar una imagen base de Python
FROM python:3.9-slim

# Establecer el directorio de trabajo
WORKDIR /opt/osint-tools

# Copiar los archivos necesarios
COPY ./herramientas/instaladores/sherlock /opt/osint-tools/sherlock

# Instalar las dependencias de Sherlock
RUN pip install -r /opt/osint-tools/sherlock/requirements.txt

# Comando por defecto para ejecutar el contenedor
CMD ["python3"]
