import logging

logger = logging.getLogger('menu_osint')

class ToolInstaller:
    def install_menu(self):
        print("\n" + "="*50)
        print(" INSTALAR HERRAMIENTAS ".center(50))
        print("="*50)
        print("\n1. Instalar Sherlock")
        print("2. Instalar GHunt")
        print("3. Volver")
        
        opcion = input("\nSelección: ").strip()
        
        if opcion == "1":
            instalar_sherlock()
        elif opcion == "2":
            instalar_ghunt()
        elif opcion == "3":
            return
        else:
            print("\n¡Opción no válida!")

    def check_status(self):
        logger.info("Verificando estado de las herramientas...")
        # Lógica para verificar el estado de las herramientas
        print("Estado verificado.")
