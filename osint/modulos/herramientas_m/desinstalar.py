import sys
import os
import logging

# Configuración del registro de logs
log_dir = "../../registros"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)
logging.basicConfig(filename=os.path.join(log_dir, 'desinstalar.log'), level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

logger = logging.getLogger('desinstalar')

class ToolUninstaller:
    def uninstall_menu(self):
        print("\n" + "="*50)
        print(" DESINSTALAR HERRAMIENTAS ".center(50))
        print("="*50)
        print("\n1. Desinstalar Sherlock")
        print("\n2. Desinstalar GHunt")
        print("\n3. Volver")
        
        opcion = input("\nSelección: ").strip()
        
        if opcion == "1":
            self.uninstall_sherlock()
        elif opcion == "2":
            self.uninstall_ghunt()
        elif opcion == "3":
            return
        else:
            print("\n¡Opción no válida!")

    def uninstall_sherlock(self):
        logger.info("Desinstalando Sherlock...")
        # Lógica de desinstalación de Sherlock
        print("Sherlock desinstalado.")
        logger.info("Sherlock desinstalado.")

    def uninstall_ghunt(self):
        logger.info("Desinstalando GHunt...")
        # Lógica de desinstalación de GHunt
        print("GHunt desinstalado.")
        logger.info("GHunt desinstalado.")

if __name__ == "__main__":
    uninstaller = ToolUninstaller()
    if len(sys.argv) > 1:
        herramienta = sys.argv[1]
        if herramienta == "Sherlock":
            uninstaller.uninstall_sherlock()
        elif herramienta == "GHunt":
            uninstaller.uninstall_ghunt()
        else:
            print(f"Herramienta desconocida: {herramienta}")
            logger.error(f"Herramienta desconocida: {herramienta}")
    else:
        uninstaller.uninstall_menu()
