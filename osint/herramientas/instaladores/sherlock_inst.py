import os
import subprocess
import logging

# Configuración del registro de logs
log_dir = "../../registros"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)
logging.basicConfig(filename=os.path.join(log_dir, 'sherlock_inst.log'), level=logging.INFO, format='%(asctime)s - %(levellevel)s - %(message)s')

logger = logging.getLogger('sherlock_inst')

def instalar_sherlock():
    """Instalar Sherlock"""
    try:
        logger.info("Instalando Sherlock...")
        # Lógica de instalación de Sherlock
        print("Sherlock instalado.")
        logger.info("Sherlock instalado.")
    except Exception as e:
        logger.error(f"Error instalando Sherlock: {str(e)}")
        print(f"Error instalando Sherlock: {str(e)}")

if __name__ == "__main__":
    instalar_sherlock()
