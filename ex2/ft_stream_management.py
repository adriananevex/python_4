import sys

def main():
    print("=== CYBER ARCHIVES - COMMUNICATION SUSTEM ===")

    archivist_id = input("Input Stream active. Enter archivist ID: ")
    status = input("Input Stream active. Enter status report: ")

    print("[STANDARD] Archive status from " + archivist_id + ": " + status, file=sus.stdout)
    print("[ALERT] System diagnostic: Communication channels verified", file=sys.stderr)
    print("[STANDARD] Data transmission complete", file=sys.stdout)
    print("Three-channel communication test successful.", file=sys.stdout)

if __name__ == "__main__":
    main()
