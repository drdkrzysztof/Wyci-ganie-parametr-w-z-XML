from cx_Freeze import setup, Executable

# Zależności są automatycznie wykrywane, ale niektóre mogą wymagać drobnych dostosowań.
build_exe_options = {
    "packages": ["os", "tkinter"],  # Dodaj tkinter do listy pakietów
    "excludes": [],  # Usuń tkinter z listy wykluczeń, jeśli był wcześniej dodany
    "include_files": []  # Możesz także dołączyć specyficzne pliki, jeśli jest taka potrzeba
}

setup(
    name = "xml_to_xlsx_gui",
    version = "0.1",
    description = "Przykładowa aplikacja GUI",
    options = {"build_exe": build_exe_options},
    executables = [Executable("xml_to_xlsx_gui.py", base="Win32GUI")]  # Użyj "Win32GUI", aby ukryć okno terminala
)
