import os
import json

class Auto:
    def __init__(self, file_id, data):
        self.id = file_id
        self.type = data.get("type", "")
        self.ajtok_szama = data.get("ajtok_szama", 0)
        self.marka = data.get("marka", "")

class Bicikli:
    def __init__(self, file_id, data):
        self.id = file_id
        self.type = data.get("type", "")
        self.terhelhetoseg = data.get("terhelhetoseg", 0)
        self.marka = data.get("marka", "")

def dat_files(folder_path):
    objects = []
    count = 0
    print("Program elindult.")
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            if file_name.endswith(".dat"):
                file_path = os.path.join(root, file_name)
                print(f"{file_name} fájl megtalálva.")
                count += 1
                
                with open(file_path, 'r') as file:
                    try:
                        json_data = json.load(file)
                        
                        file_id = os.path.splitext(file_name)[0]
                        
                        if json_data.get("type") == "bicikli":
                            obj = Bicikli(file_id, json_data)
                            objects.append(obj)
                        elif json_data.get("type") == "auto":
                            obj = Auto(file_id, json_data)
                            objects.append(obj)
                        else:
                            print(f"Unknown type{file_name}")
                        
                    except json.JSONDecodeError as e:
                        print(f"Error {file_name}: {e}")
    if count >= 1:
        print()
        print("Talált elemek listázása")
        print()
    else:
        print(f"{count} találat",f"Mappa:'{folder_path}'")
    return objects

def print_objects(obj):
    if isinstance(obj, Bicikli):
        print(f"ID: {obj.id}", "|", f"Type: {obj.type}", "|", f"Terhelhetoseg: {obj.terhelhetoseg}", "|", f"Marka: {obj.marka}" )
        print("---------------------------------------------------------")
    elif isinstance(obj, Auto):
        print(f"ID: {obj.id}", "|", f"Type: {obj.type}", "|", f"Ajtok Szama: {obj.ajtok_szama}", "|", f"Marka: {obj.marka}")
        print("---------------------------------------------------------")
    else: pass
    
folder_path = "data"
objects = dat_files(folder_path)

biciklik_printed = False
autok_printed = False

for obj in objects:
    if isinstance(obj, Auto):
        if not autok_printed:
            print("Autok:")
            autok_printed = True
        print_objects(obj)

for obj in objects:
    if isinstance(obj, Bicikli):
        if not biciklik_printed:
            print("Biciklik:")
            biciklik_printed = True
        print_objects(obj)


input("")