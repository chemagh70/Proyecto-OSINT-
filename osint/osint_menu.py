#!/usr/bin/env python3
import os
import sys
import subprocess
import logging
from time import sleep

# Añadir el directorio del proyecto al PATH
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from investigacion.sherlock import Sherlock
from investigacion.ghunt import GHunt
from modulos.herramientas_m.instalar import ToolInstaller
from modulos.herramientas_m.desinstalar import ToolUninstaller
from herramientas.osint_framework import actualizar_osint_framework

# Configuración del registro de logs
log_dir = "./registros"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)
logging.basicConfig(filename=os.path.join(log_dir, 'menu_osint.log'), level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

logger = logging.getLogger('menu_osint')

# Función para leer descripciones de herramientas desde un archivo
def leer_descripciones_herramientas(file_path):
    descripciones = {}
    try:
        with open(file_path, 'r') as file:
            for line in file:
                nombre, descripcion = line.strip().split(': ', 1)
                descripciones[nombre] = descripcion
    except Exception as e:
        logger.error(f"Error leyendo el archivo de descripciones: {str(e)}")
    return descripciones

# Leer descripciones desde el archivo "descripciones_herramientas.txt"
descripciones_herramientas = leer_descripciones_herramientas('descripciones_herramientas.txt')

class MenuOSINT:
    def __init__(self):
        self.installer = ToolInstaller()
        self.uninstaller = ToolUninstaller()
        self.sherlock = Sherlock()
        self.ghunt = GHunt()
        self.herramientas_instaladas = self.verificar_herramientas_instaladas()
        logger.info("Sistema OSINT inicializado")
        actualizar_osint_framework()

    def verificar_herramientas_instaladas(self):
        """Verificar herramientas instaladas"""
        herramientas = []
        if self._verificar_herramienta("herramientas/instaladores/sherlock_inst.py"):
            herramientas.append("Sherlock")
        if self._verificar_herramienta("herramientas/instaladores/ghunt_inst.py"):
            herramientas.append("GHunt")
        if self._verificar_herramienta("herramientas/instaladores/maltego_inst.py"):
            herramientas.append("Maltego")
        if self._verificar_herramienta("herramientas/instaladores/recon_ng_inst.py"):
            herramientas.append("Recon-ng")
        if self._verificar_herramienta("herramientas/instaladores/theharvester_inst.py"):
            herramientas.append("theHarvester")
        if self._verificar_herramienta("herramientas/instaladores/spiderfoot_inst.py"):
            herramientas.append("SpiderFoot")
        if self._verificar_herramienta("herramientas/instaladores/shodan_inst.py"):
            herramientas.append("Shodan")
        if self._verificar_herramienta("herramientas/instaladores/censys_inst.py"):
            herramientas.append("Censys")
        if self._verificar_herramienta("herramientas/instaladores/amass_inst.py"):
            herramientas.append("Amass")
        if self._verificar_herramienta("herramientas/instaladores/metagoofil_inst.py"):
            herramientas.append("Metagoofil")
        logger.info(f"Herramientas instaladas: {', '.join(herramientas)}")
        return herramientas

    def _verificar_herramienta(self, ruta_script):
        """Verificar si una herramienta está instalada"""
        return os.path.exists(ruta_script)

    def mostrar_herramientas_instaladas(self):
        """Mostrar herramientas instaladas"""
        print("\n" + "="*50)
        print(" HERRAMIENTAS INSTALADAS ".center(50))
        print("="*50)
        if self.herramientas_instaladas:
            for herramienta in self.herramientas_instaladas:
                descripcion = descripciones_herramientas.get(herramienta, "Descripción no disponible.")
                print(f"- {herramienta}: {descripcion}")
        else:
            print("No hay herramientas instaladas.")
        print("="*50)

    def mostrar_menu_principal(self):
        """Menú principal robusto"""
        while True:
            self.mostrar_herramientas_instaladas()
            print("\n" + "="*50)
            print(" SISTEMA OSINT ".center(50))
            print("="*50)
            print("\n1. Gestión de Herramientas")
            print("2. Investigación")
            print("0. Salir")
            
            opcion = input("\nSelección: ").strip()
            
            if opcion == "1":
                self.menu_herramientas()
            elif opcion == "2":
                self.menu_investigacion()
            elif opcion == "0":
                logger.info("Aplicación finalizada")
                print("\nSaliendo del sistema...")
                self.limpiar()
                sys.exit(0)
            else:
                print("\n¡Opción no válida!")

    def menu_herramientas(self):
        """Menú de herramientas completo"""
        while True:
            print("\n" + "="*50)
            print(" GESTIÓN DE HERRAMIENTAS ".center(50))
            print("="*50)
            print("\n1. Instalar herramientas")
            print("2. Desinstalar herramientas")
            print("3. Verificar estado")
            print("4. Volver")
            
            opcion = input("\nSelección: ").strip()
            
            if opcion == "1":
                self.instalar_herramientas()
            elif opcion == "2":
                self.desinstalar_herramientas()
            elif opcion == "3":
                self.verificar_estado_herramientas()
            elif opcion == "4":
                break
            else:
                print("\n¡Opción no válida!")

    def instalar_herramientas(self):
        """Instalar herramientas"""
        while True:
            print("\n" + "="*50)
            print(" INSTALAR HERRAMIENTAS ".center(50))
            print("="*50)
            print("\n1. Instalar Sherlock")
            print("2. Instalar GHunt")
            print("3. Instalar Maltego")
            print("4. Instalar Recon-ng")
            print("5. Instalar theHarvester")
            print("6. Instalar SpiderFoot")
            print("7. Instalar Shodan")
            print("8. Instalar Censys")
            print("9. Instalar Amass")
            print("10. Instalar Metagoofil")
            print("11. Volver")
            
            opcion = input("\nSelección: ").strip()
            
            if opcion == "1":
                self.ejecutar_instalacion("herramientas/instaladores/sherlock_inst.py", "Sherlock")
            elif opcion == "2":
                self.ejecutar_instalacion("herramientas/instaladores/ghunt_inst.py", "GHunt")
            elif opcion == "3":
                self.ejecutar_instalacion("herramientas/instaladores/maltego_inst.py", "Maltego")
            elif opcion == "4":
                self.ejecutar_instalacion("herramientas/instaladores/recon_ng_inst.py", "Recon-ng")
            elif opcion == "5":
                self.ejecutar_instalacion("herramientas/instaladores/theharvester_inst.py", "theHarvester")
            elif opcion == "6":
                self.ejecutar_instalacion("herramientas/instaladores/spiderfoot_inst.py", "SpiderFoot")
            elif opcion == "7":
                self.ejecutar_instalacion("herramientas/instaladores/shodan_inst.py", "Shodan")
            elif opcion == "8":
                self.ejecutar_instalacion("herramientas/instaladores/censys_inst.py", "Censys")
            elif opcion == "9":
                self.ejecutar_instalacion("herramientas/instaladores/amass_inst.py", "Amass")
            elif opcion == "10":
                self.ejecutar_instalacion("herramientas/instaladores/metagoofil_inst.py", "Metagoofil")
            elif opcion == "11":
                return
            else:
                print("\n¡Opción no válida!")

    def ejecutar_instalacion(self, ruta_script, nombre_herramienta):
        """Ejecutar instalación y mostrar progreso"""
        print(f"\nInstalando {nombre_herramienta}...")
        logger.info(f"Instalando {nombre_herramienta}...")
        proceso = subprocess.Popen(["sudo", "python3", ruta_script], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        while proceso.poll() is None:
            salida = proceso.stdout.readline().decode()
            if salida:
                print(salida.strip())
                logger.info(salida.strip())
            sleep(0.1)
        salida, error = proceso.communicate()
        if proceso.returncode == 0:
            print(f"{nombre_herramienta} instalado correctamente.")
            logger.info(f"{nombre_herramienta} instalado correctamente.")
            if nombre_herramienta not in self.herramientas_instaladas:
                self.herramientas_instaladas.append(nombre_herramienta)
                logger.info(f"{nombre_herramienta} instalado y añadido a la lista de herramientas instaladas.")
        else:
            print(f"Error instalando {nombre_herramienta}: {error.decode()}")
            logger.error(f"Error instalando {nombre_herramienta}: {error.decode()}")

    def desinstalar_herramientas(self):
        """Desinstalar herramientas"""
        while True:
            print("\n" + "="*50)
            print(" DESINSTALAR HERRAMIENTAS ".center(50))
            print("="*50)
            print("\n1. Desinstalar Sherlock")
            print("\n2. Desinstalar GHunt")
            print("\n3. Desinstalar Maltego")
            print("\n4. Desinstalar Recon-ng")
            print("\n5. Desinstalar theHarvester")
            print("\n6. Desinstalar SpiderFoot")
            print("\n7. Desinstalar Shodan")
            print("\n8. Desinstalar Censys")
            print("\n9. Desinstalar Amass")
            print("\n10. Desinstalar Metagoofil")
            print("\n11. Volver")
            
            opcion = input("\nSelección: ").strip()
            
            if opcion == "1":
                self.ejecutar_desinstalacion("modulos/herramientas_m/desinstalar.py", "Sherlock")
            elif opcion == "2":
                self.ejecutar_desinstalacion("modulos/herramientas_m/desinstalar.py", "GHunt")
            elif opcion == "3":
                self.ejecutar_desinstalacion("modulos/herramientas_m/desinstalar.py", "Maltego")
            elif opcion == "4":
                self.ejecutar_desinstalacion("modulos/herramientas_m/desinstalar.py", "Recon-ng")
            elif opcion == "5":
                self.ejecutar_desinstalacion("modulos/herramientas_m/desinstalar.py", "theHarvester")
            elif opcion == "6":
                self.ejecutar_desinstalacion("modulos/herramientas_m/desinstalar.py", "SpiderFoot")
            elif opcion == "7":
                self.ejecutar_desinstalacion("modulos/herramientas_m/desinstalar.py", "Shodan")
            elif opcion == "8":
                self.ejecutar_desinstalacion("modulos/herramientas_m/desinstalar.py", "Censys")
            elif opcion == "9":
                self.ejecutar_desinstalacion("modulos/herramientas_m/desinstalar.py", "Amass")
            elif opcion == "10":
                self.ejecutar_desinstalacion("modulos/herramientas_m/desinstalar.py", "Metagoofil")
            elif opcion == "11":
                return
            else:
                print("\n¡Opción no válida!")

    def ejecutar_desinstalacion(self, ruta_script, nombre_herramienta):
        """Ejecutar desinstalación y mostrar progreso"""
        print(f"\nDesinstalando {nombre_herramienta}...")
        logger.info(f"Desinstalando {nombre_herramienta}...")
        proceso = subprocess.Popen(["sudo", "python3", ruta_script, nombre_herramienta], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        while proceso.poll() is None:
            salida = proceso.stdout.readline().decode()
            if salida:
                print(salida.strip())
                logger.info(salida.strip())
            sleep(0.1)
        salida, error = proceso.communicate()
        if proceso.returncode == 0:
            print(f"{nombre_herramienta} desinstalado correctamente.")
            logger.info(f"{nombre_herramienta} desinstalado correctamente.")
            if nombre_herramienta in self.herramientas_instaladas:
                self.herramientas_instaladas.remove(nombre_herramienta)
                logger.info(f"{nombre_herramienta} desinstalado y eliminado de la lista de herramientas instaladas.")
        else:
            print(f"Error desinstalando {nombre_herramienta}: {error.decode()}")
            logger.error(f"Error desinstalando {nombre_herramienta}: {error.decode()}")

    def verificar_estado_herramientas(self):
        """Verificar estado de las herramientas"""
        print("\n" + "="*50)
        print(" ESTADO DE LAS HERRAMIENTAS ".center(50))
        print("="*50)
        print("Verificando estado de las herramientas instaladas...")
        logger.info("Verificando estado de las herramientas instaladas...")
        self.mostrar_herramientas_instaladas()
        print("Estado verificado.")
        logger.info("Estado verificado.")

    def menu_investigacion(self):
        """Menú de investigación funcional"""
        while True:
            print("\n" + "="*50)
            print(" INVESTIGACIÓN ".center(50))
            print("="*50)
            print("\n1. Usar Sherlock")
            print("2. Usar GHunt")
            print("3. Volver")
            
            opcion = input("\nSelección: ").strip()
            
            if opcion == "1":
                self.ejecutar_herramienta(self.sherlock, "herramientas/instaladores/sherlock_inst.py")
            elif opcion == "2":
                self.ejecutar_herramienta(self.ghunt, "herramientas/instaladores/ghunt_inst.py")
            elif opcion == "3":
                break
            else:
                print("\n¡Opción no válida!")

    def ejecutar_herramienta(self, herramienta, ruta_script):
        """Ejecutar herramienta y gestionar contenedor Docker"""
        try:
            logger.info(f"Ejecutando herramienta: {herramienta.__class__.__name__}")
            if not self._verificar_imagen_docker("imagen_osint"):
                print("La imagen Docker 'imagen_osint' no existe. Construyendo la imagen...")
                self._construir_imagen_docker("compartido/Dockerfile", "imagen_osint")
            if not self._verificar_contenedor():
                self._crear_contenedor()
            # Ejecutar herramienta específica
            subprocess.run(["sudo", "python3", ruta_script], check=True)
            herramienta.run()
        except subprocess.CalledProcessError as e:
            logger.error(f"Error ejecutando {herramienta.__class__.__name__}: {str(e)}")
            print(f"Error ejecutando {herramienta.__class__.__name__}: {str(e)}")
        except RuntimeError as e:
            logger.error(str(e))
            print(str(e))
        finally:
            # Limpiar contenedor Docker al finalizar
            self.limpiar()

    def _construir_imagen_docker(self, dockerfile_path, image_name):
        """Construir la imagen Docker"""
        try:
            logger.info(f"Construyendo la imagen Docker '{image_name}' desde '{dockerfile_path}'...")
            resultado = subprocess.run(["docker", "build", "-t", image_name, "-f", dockerfile_path, "."], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            if resultado.returncode != 0:
                raise RuntimeError(f"Error construyendo la imagen Docker: {resultado.stderr.decode().strip()}")
            logger.info(f"Imagen Docker '{image_name}' construida correctamente.")
        except Exception as e:
            logger.error(f"Error construyendo la imagen Docker:
#!/usr/bin/env python3
import os
import sys
import subprocess
import logging
from time import sleep

# Añadir el directorio del proyecto al PATH
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from investigacion.sherlock import Sherlock
from investigacion.ghunt import GHunt
from modulos.herramientas_m.instalar import ToolInstaller
from modulos.herramientas_m.desinstalar import ToolUninstaller
from herramientas.osint_framework import actualizar_osint_framework

# Configuración del registro de logs
log_dir = "./registros"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)
logging.basicConfig(filename=os.path.join(log_dir, 'menu_osint.log'), level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

logger = logging.getLogger('menu_osint')

# Función para leer descripciones de herramientas desde un archivo
def leer_descripciones_herramientas(file_path):
    descripciones = {}
    try:
        with open(file_path, 'r') as file:
            for line in file:
                nombre, descripcion = line.strip().split(': ', 1)
                descripciones[nombre] = descripcion
    except Exception as e:
        logger.error(f"Error leyendo el archivo de descripciones: {str(e)}")
    return descripciones

# Leer descripciones desde el archivo "descripciones_herramientas.txt"
descripciones_herramientas = leer_descripciones_herramientas('descripciones_herramientas.txt')

class MenuOSINT:
    def __init__(self):
        self.installer = ToolInstaller()
        self.uninstaller = ToolUninstaller()
        self.sherlock = Sherlock()
        self.ghunt = GHunt()
        self.herramientas_instaladas = self.verificar_herramientas_instaladas()
        logger.info("Sistema OSINT inicializado")
        actualizar_osint_framework()

    def verificar_herramientas_instaladas(self):
        """Verificar herramientas instaladas"""
        herramientas = []
        if self._verificar_herramienta("herramientas/instaladores/sherlock_inst.py"):
            herramientas.append("Sherlock")
        if self._verificar_herramienta("herramientas/instaladores/ghunt_inst.py"):
            herramientas.append("GHunt")
        if self._verificar_herramienta("herramientas/instaladores/maltego_inst.py"):
            herramientas.append("Maltego")
        if self._verificar_herramienta("herramientas/instaladores/recon_ng_inst.py"):
            herramientas.append("Recon-ng")
        if self._verificar_herramienta("herramientas/instaladores/theharvester_inst.py"):
            herramientas.append("theHarvester")
        if self._verificar_herramienta("herramientas/instaladores/spiderfoot_inst.py"):
            herramientas.append("SpiderFoot")
        if self._verificar_herramienta("herramientas/instaladores/shodan_inst.py"):
            herramientas.append("Shodan")
        if self._verificar_herramienta("herramientas/instaladores/censys_inst.py"):
            herramientas.append("Censys")
        if self._verificar_herramienta("herramientas/instaladores/amass_inst.py"):
            herramientas.append("Amass")
        if self._verificar_herramienta("herramientas/instaladores/metagoofil_inst.py"):
            herramientas.append("Metagoofil")
        logger.info(f"Herramientas instaladas: {', '.join(herramientas)}")
        return herramientas

    def _verificar_herramienta(self, ruta_script):
        """Verificar si una herramienta está instalada"""
        return os.path.exists(ruta_script)

    def mostrar_herramientas_instaladas(self):
        """Mostrar herramientas instaladas"""
        print("\n" + "="*50)
        print(" HERRAMIENTAS INSTALADAS ".center(50))
        print("="*50)
        if self.herramientas_instaladas:
            for herramienta in self.herramientas_instaladas:
                descripcion = descripciones_herramientas.get(herramienta, "Descripción no disponible.")
                print(f"- {herramienta}: {descripcion}")
        else:
            print("No hay herramientas instaladas.")
        print("="*50)

    def mostrar_menu_principal(self):
        """Menú principal robusto"""
        while True:
            self.mostrar_herramientas_instaladas()
            print("\n" + "="*50)
            print(" SISTEMA OSINT ".center(50))
            print("="*50)
            print("\n1. Gestión de Herramientas")
            print("2. Investigación")
            print("0. Salir")
            
            opcion = input("\nSelección: ").strip()
            
            if opcion == "1":
                self.menu_herramientas()
            elif opcion == "2":
                self.menu_investigacion()
            elif opcion == "0":
                logger.info("Aplicación finalizada")
                print("\nSaliendo del sistema...")
                self.limpiar()
                sys.exit(0)
            else:
                print("\n¡Opción no válida!")

    def menu_herramientas(self):
        """Menú de herramientas completo"""
        while True:
            print("\n" + "="*50)
            print(" GESTIÓN DE HERRAMIENTAS ".center(50))
            print("="*50)
            print("\n1. Instalar herramientas")
            print("2. Desinstalar herramientas")
            print("3. Verificar estado")
            print("4. Volver")
            
            opcion = input("\nSelección: ").strip()
            
            if opcion == "1":
                self.instalar_herramientas()
            elif opcion == "2":
                self.desinstalar_herramientas()
            elif opcion == "3":
                self.verificar_estado_herramientas()
            elif opcion == "4":
                break
            else:
                print("\n¡Opción no válida!")

    def instalar_herramientas(self):
        """Instalar herramientas"""
        while True:
            print("\n" + "="*50)
            print(" INSTALAR HERRAMIENTAS ".center(50))
            print("="*50)
            print("\n1. Instalar Sherlock")
            print("2. Instalar GHunt")
            print("3. Instalar Maltego")
            print("4. Instalar Recon-ng")
            print("5. Instalar theHarvester")
            print("6. Instalar SpiderFoot")
            print("7. Instalar Shodan")
            print("8. Instalar Censys")
            print("9. Instalar Amass")
            print("10. Instalar Metagoofil")
            print("11. Volver")
            
            opcion = input("\nSelección: ").strip()
            
            if opcion == "1":
                self.ejecutar_instalacion("herramientas/instaladores/sherlock_inst.py", "Sherlock")
            elif opcion == "2":
                self.ejecutar_instalacion("herramientas/instaladores/ghunt_inst.py", "GHunt")
            elif opcion == "3":
                self.ejecutar_instalacion("herramientas/instaladores/maltego_inst.py", "Maltego")
            elif opcion == "4":
                self.ejecutar_instalacion("herramientas/instaladores/recon_ng_inst.py", "Recon-ng")
            elif opcion == "5":
                self.ejecutar_instalacion("herramientas/instaladores/theharvester_inst.py", "theHarvester")
            elif opcion == "6":
                self.ejecutar_instalacion("herramientas/instaladores/spiderfoot_inst.py", "SpiderFoot")
            elif opcion == "7":
                self.ejecutar_instalacion("herramientas/instaladores/shodan_inst.py", "Shodan")
            elif opcion == "8":
                self.ejecutar_instalacion("herramientas/instaladores/censys_inst.py", "Censys")
            elif opcion == "9":
                self.ejecutar_instalacion("herramientas/instaladores/amass_inst.py", "Amass")
            elif opcion == "10":
                self.ejecutar_instalacion("herramientas/instaladores/metagoofil_inst.py", "Metagoofil")
            elif opcion == "11":
                return
            else:
                print("\n¡Opción no válida!")

    def ejecutar_instalacion(self, ruta_script, nombre_herramienta):
        """Ejecutar instalación y mostrar progreso"""
        print(f"\nInstalando {nombre_herramienta}...")
        logger.info(f"Instalando {nombre_herramienta}...")
        proceso = subprocess.Popen(["sudo", "python3", ruta_script], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        while proceso.poll() is None:
            salida = proceso.stdout.readline().decode()
            if salida:
                print(salida.strip())
                logger.info(salida.strip())
            sleep(0.1)
        salida, error = proceso.communicate()
        if proceso.returncode == 0:
            print(f"{nombre_herramienta} instalado correctamente.")
            logger.info(f"{nombre_herramienta} instalado correctamente.")
            if nombre_herramienta not in self.herramientas_instaladas:
                self.herramientas_instaladas.append(nombre_herramienta)
                logger.info(f"{nombre_herramienta} instalado y añadido a la lista de herramientas instaladas.")
        else:
            print(f"Error instalando {nombre_herramienta}: {error.decode()}")
            logger.error(f"Error instalando {nombre_herramienta}: {error.decode()}")

    def desinstalar_herramientas(self):
        """Desinstalar herramientas"""
        while True:
            print("\n" + "="*50)
            print(" DESINSTALAR HERRAMIENTAS ".center(50))
            print("="*50)
            print("\n1. Desinstalar Sherlock")
            print("\n2. Desinstalar GHunt")
            print("\n3. Desinstalar Maltego")
            print("\n4. Desinstalar Recon-ng")
            print("\n5. Desinstalar theHarvester")
            print("\n6. Desinstalar SpiderFoot")
            print("\n7. Desinstalar Shodan")
            print("\n8. Desinstalar Censys")
            print("\n9. Desinstalar Amass")
            print("\n10. Desinstalar Metagoofil")
            print("\n11. Volver")
            
            opcion = input("\nSelección: ").strip()
            
            if opcion == "1":
                self.ejecutar_desinstalacion("modulos/herramientas_m/desinstalar.py", "Sherlock")
            elif opcion == "2":
                self.ejecutar_desinstalacion("modulos/herramientas_m/desinstalar.py", "GHunt")
            elif opcion == "3":
                self.ejecutar_desinstalacion("modulos/herramientas_m/desinstalar.py", "Maltego")
            elif opcion == "4":
                self.ejecutar_desinstalacion("modulos/herramientas_m/desinstalar.py", "Recon-ng")
            elif opcion == "5":
                self.ejecutar_desinstalacion("modulos/herramientas_m/desinstalar.py", "theHarvester")
            elif opcion == "6":
                self.ejecutar_desinstalacion("modulos/herramientas_m/desinstalar.py", "SpiderFoot")
            elif opcion == "7":
                self.ejecutar_desinstalacion("modulos/herramientas_m/desinstalar.py", "Shodan")
            elif opcion == "8":
                self.ejecutar_desinstalacion("modulos/herramientas_m/desinstalar.py", "Censys")
            elif opcion == "9":
                self.ejecutar_desinstalacion("modulos/herramientas_m/desinstalar.py", "Amass")
            elif opcion == "10":
                self.ejecutar_desinstalacion("modulos/herramientas_m/desinstalar.py", "Metagoofil")
            elif opcion == "11":
                return
            else:
                print("\n¡Opción no válida!")

    def ejecutar_desinstalacion(self, ruta_script, nombre_herramienta):
        """Ejecutar desinstalación y mostrar progreso"""
        print(f"\nDesinstalando {nombre_herramienta}...")
        logger.info(f"Desinstalando {nombre_herramienta}...")
        proceso = subprocess.Popen(["sudo", "python3", ruta_script, nombre_herramienta], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        while proceso.poll() is None:
            salida = proceso.stdout.readline().decode()
            if salida:
                print(salida.strip())
                logger.info(salida.strip())
            sleep(0.1)
        salida, error = proceso.communicate()
        if proceso.returncode == 0:
            print(f"{nombre_herramienta} desinstalado correctamente.")
            logger.info(f"{nombre_herramienta} desinstalado correctamente.")
            if nombre_herramienta in self.herramientas_instaladas:
                self.herramientas_instaladas.remove(nombre_herramienta)
                logger.info(f"{nombre_herramienta} desinstalado y eliminado de la lista de herramientas instaladas.")
        else:
            print(f"Error desinstalando {nombre_herramienta}: {error.decode()}")
            logger.error(f"Error desinstalando {nombre_herramienta}: {error.decode()}")

    def verificar_estado_herramientas(self):
        """Verificar estado de las herramientas"""
        print("\n" + "="*50)
        print(" ESTADO DE LAS HERRAMIENTAS ".center(50))
        print("="*50)
        print("Verificando estado de las herramientas instaladas...")
        logger.info("Verificando estado de las herramientas instaladas...")
        self.mostrar_herramientas_instaladas()
        print("Estado verificado.")
        logger.info("Estado verificado.")

    def menu_investigacion(self):
        """Menú de investigación funcional"""
        while True:
            print("\n" + "="*50)
            print(" INVESTIGACIÓN ".center(50))
            print("="*50)
            print("\n1. Usar Sherlock")
            print("2. Usar GHunt")
            print("3. Volver")
            
            opcion = input("\nSelección: ").strip()
            
            if opcion == "1":
                self.ejecutar_herramienta(self.sherlock, "herramientas/instaladores/sherlock_inst.py")
            elif opcion == "2":
                self.ejecutar_herramienta(self.ghunt, "herramientas/instaladores/ghunt_inst.py")
            elif opcion == "3":
                break
            else:
                print("\n¡Opción no válida!")

    def ejecutar_herramienta(self, herramienta, ruta_script):
        """Ejecutar herramienta y gestionar contenedor Docker"""
        try:
            logger.info(f"Ejecutando herramienta: {herramienta.__class__.__name__}")
            if not self._verificar_imagen_docker("imagen_osint"):
                print("La imagen Docker 'imagen_osint' no existe. Construyendo la imagen...")
                self._construir_imagen_docker("compartido/Dockerfile", "imagen_osint")
            if not self._verificar_contenedor():
                self._crear_contenedor()
            # Ejecutar herramienta específica
            subprocess.run(["sudo", "python3", ruta_script], check=True)
            herramienta.run()
        except subprocess.CalledProcessError as e:
            logger.error(f"Error ejecutando {herramienta.__class__.__name__}: {str(e)}")
            print(f"Error ejecutando {herramienta.__class__.__name__}: {str(e)}")
        except RuntimeError as e:
            logger.error(str(e))
            print(str(e))
        finally:
            # Limpiar contenedor Docker al finalizar
            self.limpiar()

    def _construir_imagen_docker(self, dockerfile_path, image_name):
        """Construir la imagen Docker"""
        try:
            logger.info(f"Construyendo la imagen Docker '{image_name}' desde '{dockerfile_path}'...")
            resultado = subprocess.run(["docker", "build", "-t", image_name, "-f", dockerfile_path, "."], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            if resultado.returncode != 0:
                raise RuntimeError(f"Error construyendo la imagen Docker: {resultado.stderr.decode().strip()}")
            logger.info(f"Imagen Docker '{image_name}' construida correctamente.")
        except Exception as e:
            logger.error(f"Error construyendo la imagen Docker: {str(e)}")
            print(f"Error construyendo la imagen Docker: {str(e)}")

    def _verificar_imagen_docker(self, nombre_imagen):
        """Verificar si la imagen Docker existe"""
        resultado = subprocess.run(["docker", "images", "-q", nombre_imagen], stdout=subprocess.PIPE)
        return bool(resultado.stdout.decode().strip())

    def _verificar_contenedor(self):
        """Verificar si el contenedor Docker existe"""
        resultado = subprocess.run(["docker", "ps", "-a", "-f", "name=osint_tools_container"], stdout=subprocess.PIPE)
        return "osint_tools_container" in resultado.stdout.decode()

    def _crear_contenedor(self):
        """Crear el contenedor Docker"""
        try:
            logger.info("Creando contenedor Docker...")
            resultado = subprocess.run(["docker", "run", "-d", "--name", "osint_tools_container", "imagen_osint"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            if resultado.returncode != 0:
                raise RuntimeError(f"Error creando el contenedor Docker: {resultado.stderr.decode().strip()}")
            logger.info("Contenedor Docker creado.")
        except Exception as e:
            logger.error(f"Error creando el contenedor Docker: {str(e)}")
            print(f"Error creando el contenedor Docker: {str(e)}")

    def limpiar(self):
        """Detener y eliminar el contenedor Docker"""
        try:
            logger.info("Deteniendo y eliminando el contenedor Docker")
            subprocess.run(["docker", "stop", "osint_tools_container"])
            subprocess.run(["docker", "rm", "osint_tools_container"])
        except subprocess.CalledProcessError as e:
            logger.error(f"Error durante la limpieza: {str(e)}")
            print(f"Error durante la limpieza: {str(e)}")
