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
    print("Program elindult.")
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            if file_name.endswith(".dat"):
                file_path = os.path.join(root, file_name)
                print(f"{file_name} fálj megtalálva.")
                
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
    
    return objects

def print_object(obj):
    if isinstance(obj, Bicikli):
        print(f"ID: {obj.id}")
        print(f"Type: {obj.type}")
        print(f"Terhelhetoseg: {obj.terhelhetoseg}")
        print(f"Marka: {obj.marka}")
    elif isinstance(obj, Auto):
        print(f"ID: {obj.id}")
        print(f"Type: {obj.type}")
        print(f"Ajtok Szama: {obj.ajtok_szama}")
        print(f"Marka: {obj.marka}")
    print()   

folder_path = "data"
objects = dat_files(folder_path)
for obj in objects:
    print_object(obj)
