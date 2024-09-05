import os
import json

BASE_DIR = "json"

def btr_createprofile(name, linktojson):
    filepath = os.path.join(BASE_DIR, f"{name}.json")
    
    if os.path.exists(filepath):
        print("Profile already exists")
    else:
        try:
            os.makedirs(os.path.dirname(filepath), exist_ok=True)
            with open(filepath, 'w') as file:
                json.dump(linktojson, file, indent=4)
            print(f"File '{name}.json' successfully created and written.")
        except IOError as e:
            print(f"Error creating or writing to file: {e}")

def btr_addtoprofile(name, paradd, valladd, is_user_profile=False):
    directory = "userprofiles" if is_user_profile else ""
    filepath = os.path.join(BASE_DIR, directory, f"{name}.json")
    
    try:
        if os.path.exists(filepath):
            with open(filepath, 'r') as file:
                data = json.load(file)

            data[paradd] = valladd

            with open(filepath, 'w') as file:
                json.dump(data, file, indent=4)
            
            print(f"Added parameter '{paradd}' with value '{valladd}' to '{name}.json'.")
        else:
            print(f"File '{name}.json' not found.")
    except IOError as e:
        print(f"Error: {e}")

def btr_changestat(name, par, val):
    filepath = os.path.join(BASE_DIR, f"{name}.json")
    try:
        with open(filepath, 'r') as file:
            data = json.load(file)

        data[par] = val

        with open(filepath, 'w') as file:
            json.dump(data, file, indent=4)
    except IOError as e:
        print(f"Error: {e}")

def btr_readstat(name, par):
    filepath = os.path.join(BASE_DIR, f"{name}.json")
    try:
        if os.path.exists(filepath):
            with open(filepath, 'r') as file:
                data = json.load(file)
            return data.get(par)
        else:
            print(f"File '{name}.json' not found.")
            return None
    except IOError as e:
        print(f"Error: {e}")

def btr_createuserprofile(name, linktojson):
    filepath = os.path.join(BASE_DIR, "userinfa", f"{name}.json")
    
    if os.path.exists(filepath):
        print("Profile already exists")
    else:
        try:
            os.makedirs(os.path.dirname(filepath), exist_ok=True)
            with open(filepath, 'w') as file:
                json.dump(linktojson, file, indent=4)
            print(f"File '{name}.json' successfully created and written.")
        except IOError as e:
            print(f"Error creating or writing to file: {e}")

def btr_changeuserstat(name, par, val):
    filepath = os.path.join(BASE_DIR, "userinfa", f"{name}.json")
    try:
        if os.path.exists(filepath):
            with open(filepath, 'r') as file:
                data = json.load(file)

            data[par] = val

            with open(filepath, 'w') as file:
                json.dump(data, file, indent=4)
        else:
            print(f"File '{name}.json' not found.")
    except IOError as e:
        print(f"Error: {e}")

def btr_readuserstat(name, par):
    filepath = os.path.join(BASE_DIR, "userinfa", f"{name}.json")
    try:
        if os.path.exists(filepath):
            with open(filepath, 'r') as file:
                data = json.load(file)
            return data.get(par)
        else:
            print(f"File '{name}.json' not found.")
            return None
    except IOError as e:
        print(f"Error: {e}")



def btr_createbogprofile(name, linktojson):
    filepath = os.path.join(BASE_DIR, "glazboga", f"{name}.json")
    
    if os.path.exists(filepath):
        print("Profile already exists")
    else:
        try:
            os.makedirs(os.path.dirname(filepath), exist_ok=True)
            with open(filepath, 'w') as file:
                json.dump(linktojson, file, indent=4)
            print(f"File '{name}.json' successfully created and written.")
        except IOError as e:
            print(f"Error creating or writing to file: {e}")

def btr_changebogstat(name, par, val):
    filepath = os.path.join(BASE_DIR, "glazboga", f"{name}.json")
    try:
        if os.path.exists(filepath):
            with open(filepath, 'r') as file:
                data = json.load(file)

            data[par] = val

            with open(filepath, 'w') as file:
                json.dump(data, file, indent=4)
        else:
            print(f"File '{name}.json' not found.")
    except IOError as e:
        print(f"Error: {e}")

def btr_readbogstat(name, par):
    filepath = os.path.join(BASE_DIR, "glazboga", f"{name}.json")
    try:
        if os.path.exists(filepath):
            with open(filepath, 'r') as file:
                data = json.load(file)
            return data.get(par)
        else:
            print(f"File '{name}.json' not found.")
            return None
    except IOError as e:
        print(f"Error: {e}")