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

    
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            if file_name.endswith(".dat"):
                file_path = os.path.join(root, file_name)
                
                with open(file_path, 'r') as file:
                    try:
                        json_data = json.load(file)
                        
                        file_id = os.path.splitext(file_name)[0]
                        
                        print(f"File ID: {file_id}")
                        print("JSON Data:", json_data)
                    except json.JSONDecodeError as e:
                        print(f"Error {file_name}: {e}")
                        
folder_path = "data"



dat_files(folder_path)
