import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python app.py [name]")
        sys.exit(1)
    
    nama = sys.argv[1]
    print("Selamat datang di aplikasi command-line sederhana.")
    print(f"Halo, {nama}! Selamat belajar Jenkins dengan Python.")

if __name__ == "__main__":
    main()
