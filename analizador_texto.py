import os
import subprocess


class TextAnalyzer:
    def __init__(self, text: str):
        if not text or not text.strip():
            raise ValueError("El texto no puede estar vacío.")
        self.original_text = text
        self.normalized_text = ""
        self.tokens = []
        self.counts = {}
        self.unique_tokens = set()

    def normalize_text(self, text: str) -> str:
        punctuation = ".,;:!?()[]{}\"'"
        text = text.lower()
        cleaned = "".join(char for char in text if char not in punctuation)
        return " ".join(cleaned.split())

    def tokenize(self, text: str) -> list:
        return text.split()

    def analyze(self):
        self.normalized_text = self.normalize_text(self.original_text)
        self.tokens = self.tokenize(self.normalized_text)

        for token in self.tokens:
            self.counts[token] = self.counts.get(token, 0) + 1

        self.unique_tokens = set(self.tokens)

    def report(self):
        total_tokens = len(self.tokens)
        unique_count = len(self.unique_tokens)

        print("\n===== REPORTE =====")
        print("Total de tokens:", total_tokens)
        print("Tokens únicos:", unique_count)

        print("\nTop 10 tokens más frecuentes:")
        sorted_tokens = sorted(self.counts.items(), key=lambda x: x[1], reverse=True)
        for token, count in sorted_tokens[:10]:
            print(token, "->", count)

        if total_tokens > 0:
            avg_length = sum(len(t) for t in self.tokens) / total_tokens
            print("\nLongitud promedio de palabra:", round(avg_length, 2))

        if self.tokens:
            max_len = max(len(t) for t in self.tokens)
            min_len = min(len(t) for t in self.tokens)

            longest = [t for t in self.unique_tokens if len(t) == max_len]
            shortest = [t for t in self.unique_tokens if len(t) == min_len]

            print("Palabra(s) más larga(s):", longest)
            print("Palabra(s) más corta(s):", shortest)

    def query(self, word: str):
        word = word.lower()
        total = len(self.tokens)

        print("\n===== CONSULTA DE PALABRA =====")

        if word not in self.counts:
            print("Palabra consultada:", word)
            print("La palabra no aparece en el texto.")
            return

        freq = self.counts[word]
        percentage = (freq / total) * 100 if total > 0 else 0

        print("Palabra consultada:", word)
        print("Frecuencia:", freq)
        print("Porcentaje:", round(percentage, 2), "%")

        if freq == 1:
            print("Clasificación: RARA")
        elif freq >= 5:
            print("Clasificación: COMÚN")
        else:
            print("Clasificación: Moderada")


class EntradaTexto:

    def leer_desde_archivo(self):
        ruta = input("Ingrese la ruta del archivo .txt: ").strip()
        try:
            if not os.path.exists(ruta):
                raise FileNotFoundError("La ruta no existe.")
            if not ruta.endswith(".txt"):
                raise ValueError("El archivo debe tener extensión .txt")

            with open(ruta, "r", encoding="utf-8") as archivo:
                contenido = archivo.read()

            if not contenido.strip():
                raise ValueError("El archivo está vacío.")

            return contenido

        except Exception as e:
            print("Error:", e)
            return None

    def leer_desde_consola(self):
        print("Pegue el texto (escriba END para terminar):")
        lineas = []

        while True:
            linea = input()
            if linea.strip() == "END":
                break
            lineas.append(linea)

        texto = "\n".join(lineas)

        if not texto.strip():
            print("Texto vacío.")
            return None

        return texto

    def crear_archivo(self):
        nombre = input("Ingrese el nombre del archivo (sin extensión): ").strip()

        if not nombre:
            print("Nombre vacío.")
            return None

        print("Escriba el contenido (END para terminar):")
        lineas = []
        while True:
            linea = input()
            if linea.strip() == "END":
                break
            lineas.append(linea)

        texto = "\n".join(lineas)

        if not texto.strip():
            print("No se ingresó contenido.")
            return None

        ruta = nombre + ".txt"

        try:
            with open(ruta, "w", encoding="utf-8") as archivo:
                archivo.write(texto)
            print("Archivo creado correctamente.")
        except Exception as e:
            print("Error:", e)

    def editar_archivo(self):
        ruta = input("Ingrese la ruta del archivo (.txt): ").strip()

        if not os.path.exists(ruta) or not ruta.endswith(".txt"):
            print("Archivo inválido.")
            return

        try:
            with open(ruta, "r", encoding="utf-8") as archivo:
                print("\nContenido actual:\n")
                print(archivo.read())

            print("\nNuevo contenido (END para terminar):")
            lineas = []
            while True:
                linea = input()
                if linea.strip() == "END":
                    break
                lineas.append(linea)

            nuevo_texto = "\n".join(lineas)

            with open(ruta, "w", encoding="utf-8") as archivo:
                archivo.write(nuevo_texto)

            print("Archivo sobrescrito correctamente.")

        except Exception as e:
            print("Error:", e)

    def abrir_en_bloc(self):
        ruta = input("Ingrese la ruta del archivo (.txt): ").strip()

        if not os.path.exists(ruta) or not ruta.endswith(".txt"):
            print("Archivo inválido.")
            return

        try:
            subprocess.run(["notepad.exe", ruta])
        except Exception as e:
            print("Error al abrir:", e)

    def eliminar_archivo(self):
        ruta = input("Ingrese la ruta del archivo (.txt): ").strip()

        if not os.path.exists(ruta) or not ruta.endswith(".txt"):
            print("Archivo inválido.")
            return

        confirmacion = input("¿Seguro que desea eliminarlo? (S/N): ").upper()

        if confirmacion == "S":
            try:
                os.remove(ruta)
                print("Archivo eliminado correctamente.")
            except Exception as e:
                print("Error:", e)
        else:
            print("Operación cancelada.")


def run_tests():
    analyzer = TextAnalyzer("Hola, Mundo!! Python 3.")
    assert analyzer.normalize_text("Hola, Mundo!! Python 3.") == "hola mundo python 3"
    assert analyzer.tokenize("hola mundo python 3") == ["hola", "mundo", "python", "3"]
    analyzer2 = TextAnalyzer("hola hola mundo")
    analyzer2.analyze()
    assert analyzer2.counts["hola"] == 2
    assert analyzer2.counts["mundo"] == 1


def menu_principal():
    entrada = EntradaTexto()

    while True:
        print("\n===== ANALIZADOR DE TEXTO =====")
        print("1) Leer archivo y analizar 'txt'")
        print("2) Modo 'consola'")
        print("3) Crear archivo 'text'")
        print("4) Editar archivo 'text'")
        print("5) Abrir archivo en Bloc de notas ' archivo.text'")
        print("6) Eliminar archivo text'")
        print("7) Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "7":
            print("Saliendo del programa...")
            break

        elif opcion == "1":
            texto = entrada.leer_desde_archivo()

        elif opcion == "2":
            texto = entrada.leer_desde_consola()

        elif opcion == "3":
            entrada.crear_archivo()
            continue

        elif opcion == "4":
            entrada.editar_archivo()
            continue

        elif opcion == "5":
            entrada.abrir_en_bloc()
            continue

        elif opcion == "6":
            entrada.eliminar_archivo()
            continue

        else:
            print("Opción inválida.")
            continue

        if texto:
            try:
                analyzer = TextAnalyzer(texto)
                analyzer.analyze()
                analyzer.report()

                while True:
                    palabra = input("Consultar palabra ('exit' para volver): ")
                    if palabra.lower() == "exit":
                        break
                    analyzer.query(palabra)

            except ValueError as e:
                print("Error:", e)


if __name__ == "__main__":
    run_tests()
    menu_principal()