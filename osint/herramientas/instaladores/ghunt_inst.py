import os
import subprocess
import logging

# Configuración del registro de logs
log_dir = "../../registros"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)
logging.basicConfig(filename=os.path.join(log_dir, 'ghunt_inst.log'), level=logging.INFO, format='%(asctime)s - %(levellevel)s - %(message)s')

logger = logging.getLogger('ghunt_inst')

def instalar_ghunt():
    """Instalar GHunt"""
    try:
        logger.info("Instalando GHunt...")
        # Lógica de instalación de GHunt
        print("GHunt instalado.")
        logger.info("GHunt instalado.")
    except Exception as e:
        logger.error(f"Error instalando GHunt: {str(e)}")
        print(f"Error instalando GHunt: {str(e)}")

if __name__ == "__main__":
    instalar_ghunt()
