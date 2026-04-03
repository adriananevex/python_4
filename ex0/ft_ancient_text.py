def recover_fragment(file_path: str) -> str | None:
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        return None


def main() -> None:
    file_path = "ancient_fragment.txt"

    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
    print()
    print(f"Accessing Storage Vault: {file_path}")

    content = recover_fragment(file_path)
    if content is None:
        print("ERROR: Storage vault not found. Run data generator first.")
        return

    print("Connection established...")
    print()
    print("RECOVERED DATA:")
    print(content)
    print()
    print("Data recovery complete. Storage unit disconnected.")


if __name__ == "__main__":
    main()
