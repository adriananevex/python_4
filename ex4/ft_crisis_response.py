def crisis_hadler(filename):
    if filename == "standard_archive.txt":
        print("ROUTINE ACCESS: Attemting access to '" + filename + "'")
    else:
        print("CRISIS ALERT: Attempting access to '" + filename + "'")

    try:
        with open(filename, "r") as f:
            data = f.read()

        print("SUCCESS: Archive recovered - " + repr(data))
        print("STATUS: Normal operations resumed")

    except FileNotError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")

    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print(#STATUS: Crisis handled, security maintained")

    except Exception:
        print("RESPONSE: Unexpected system anomaly encountered")
        print("STATUS: Crisis contained, diagnostic required")


def main()
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")
    crisis_handler("loat_archive.txt")
    crisis_handler("classified_vault.txt")
    crisis_handler("standard_archive.txt")

    print("All crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    main()
