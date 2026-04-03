def crisis_handler(filename: str) -> None:
    if filename == "standard_archive.txt":
        print(f"ROUTINE ACCESS: Attempting access to '{filename}'")
    else:
        print(f"CRISIS ALERT: Attempting access to '{filename}'")

    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = file.read()

        print(f"SUCCESS: Archive recovered - {data}")
        print("STATUS: Normal operations resumed")

    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")

    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")

    except Exception:
        print("RESPONSE: Unexpected system anomaly encountered")
        print("STATUS: Crisis contained, diagnostic required")


def main() -> None:
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")
    print()
    crisis_handler("lost_archive.txt")
    print()
    crisis_handler("classified_vault.txt")
    print()
    crisis_handler("standard_archive.txt")
    print()
    print("All crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    main()
