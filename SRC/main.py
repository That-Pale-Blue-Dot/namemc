import requests
import time
import random

def check_name_availability(name):
    url = f"https://api.mojang.com/users/profiles/minecraft/{name}"
    response = requests.get(url, timeout=10)
    code = response.status_code
    print(f"{name};{code}")
    return code == 204 or code == 404

def generate_minecraft_name():
    alphabet = "abcdefghijklmnopqrstuvwxyz_"
    name = random.choice(alphabet) + random.choice(alphabet) + random.choice(alphabet)
    return name

def save_names_to_file(names, filename):
    with open(filename, "a") as file:
        for name in names:
            file.write(name + "\n")

def main():
    num_names = int(input("How many names to generate? "))
    available_names = []
    failed_names = []

    for _ in range(num_names):
        name = generate_minecraft_name()
        print(f"Checking name: {name}")
        
        if name in failed_names:
            print(f"Skipping name {name} as it was previously owned")
            continue

        try:
            if check_name_availability(name):
                available_names.append(name)
                print(f"Name available: {name}")
                save_names_to_file([name], "available_names.txt")
            else:
                failed_names.append(name)
                save_names_to_file([name], "failed_names.txt")
        except requests.Timeout:
            print("Timeout occurred. Retrying...")
            time.sleep(0.9)  # Pause for 1 second before retrying
        
        time.sleep(0.85)  # Pause for 1 second to comply with the rate limit

    if available_names:
        print("Available names saved to available_names.txt")
    else:
        print("No available names found.")

if __name__ == "__main__":
    main()