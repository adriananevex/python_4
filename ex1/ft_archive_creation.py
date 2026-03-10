def main():
    filename = "new_discovery.txt"

    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ==="
    print("Initializing new storage unit:", filename)

    f = open(filename, "w")
    print("Storage unit created successfully...")
    print("Inscribing preservation data...")

    f.write("[ENTRY 001] New quantum algorithm discovered\n")
    print("[ENTRY 001] New quantum algorithm discovered")

    f.write("[ENTRY 002] Efficiency increased by 347%\n")
    print("[ENTRY 002] Efficiency increased by 347%")

    f.write("[ENTRY 003] Archived by Data Archivist trainee\n")
    print("[ENTRY 003] Archived by Data Archivist trainee")

    f.close()

    print("Data inscription complete. Storage unit sealed.")
    print("Archive '" + filename + "' ready for long-term preservation.")


if __name__ == "__main__":
    main()
