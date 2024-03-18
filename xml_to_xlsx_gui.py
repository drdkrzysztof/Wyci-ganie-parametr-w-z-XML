import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
from xml.etree import ElementTree as ET
from datetime import datetime

def convert_xml_to_xlsx():
    root.withdraw()  # Ukrywa główne okno tkinter
    file_path = filedialog.askopenfilename(filetypes=[("XML files", "*.xml")])
    if not file_path:
        return  # Anulowano wybór pliku

    tree = ET.parse(file_path)
    root_element = tree.getroot()

    products_data = []
    for product in root_element.iter('product'):
        product_data = {
            "ean": product.find('ean').text if product.find('ean') is not None else "",
            "sku": product.find('sku').text if product.find('sku') is not None else "",
            "name": product.find('name').text if product.find('name') is not None else "",
        }
        attributes = product.find('attributes')
        if attributes is not None:
            for attribute in attributes:
                attribute_name = attribute.find('attribute_name').text if attribute.find('attribute_name') is not None else ""
                attribute_value = attribute.find('attribute_value').text if attribute.find('attribute_value') is not None else ""
                product_data[attribute_name] = attribute_value
        
        products_data.append(product_data)

    df = pd.DataFrame(products_data)
    filename = f"parametry_{datetime.now().strftime('%Y-%m-%d')}.xlsx"
    df.to_excel(filename, index=False)
    messagebox.showinfo("Zakończono", f"Plik '{filename}' został zapisany w lokalizacji programu.")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Konwerter XML na XLSX")
    tk.Button(root, text="Wybierz plik XML i konwertuj na XLSX", command=convert_xml_to_xlsx).pack(pady=20)
    root.mainloop()
