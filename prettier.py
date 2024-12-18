import os
import subprocess
import importlib.util as lib

INIT_INCLUDE_DIRS = ["src"]
LINT_INCLUDE_DIRS = ["main.py", "prettier.py", "src", "scripts"]


def comprobar_librerias():
    if not lib.find_spec("black"):
        print("ERROR: La librería black no está instalada")
        exit()
    if not lib.find_spec("mypy"):
        print("ERROR: La librería mypy no está instalada")
        exit()


def create_init_files():
    # crear archivo __init__.py en cada directorio de INIT_INCLUDE_DIRS
    for dir in INIT_INCLUDE_DIRS:
        init_file = os.path.join(dir, "__init__.py")
        if not os.path.exists(init_file):
            with open(init_file, "w") as f:
                pass  # Crear archivo vacío


def execute_black():
    for dir in LINT_INCLUDE_DIRS:
        subprocess.run(["black", dir])


def execute_mypy():
    for dir in LINT_INCLUDE_DIRS:
        subprocess.run(["mypy", dir])


def main():
    comprobar_librerias()
    create_init_files()
    execute_black()
    execute_mypy()


# Ruta del proyecto
if __name__ == "__main__":
    main()
