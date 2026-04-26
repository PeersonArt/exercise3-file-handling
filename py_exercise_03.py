username = input("Enter username: ").strip()
age = input("Enter age: ")

with open("users.txt", "w") as file:
    file.write(f"{username} - {age}\n")

print("User saved successfully.")

with open("users.txt", "r") as file:
    print("\nSaved Users:")
    print(file.read())