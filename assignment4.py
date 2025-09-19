
try:
    with open("input.txt", "r") as infile:
        content = infile.read()

    modified_content = content.upper()

    with open("output.txt", "w") as outfile:
        outfile.write(modified_content)

    print("✅ File processed successfully! Check 'output.txt'.")

except FileNotFoundError:
    print("❌ Error: input.txt was not found.")


filename = input("Enter the filename to read: ")

try:
    with open(filename, "r") as f:
        content = f.read()
        print("✅ File content loaded successfully:")
        print(content)

except FileNotFoundError:
    print(f"❌ Error: The file '{filename}' was not found.")
except PermissionError:
    print(f"❌ Error: You don’t have permission to read '{filename}'.")
except Exception as e:
    print(f"⚠️ An unexpected error occurred: {e}")
