def biaya_lauk():
    sum_ = 0

    belilauk = input("Apakah anda ingin membeli lauk? (y/n) : ")

    if belilauk.lower() == 'y':
        while True:
            biaya_lauk = [8000, 12000, 6000, 3000, 15000]

            kodelauk = int(input("\nMasukkan kode lauk yang anda pilih : "))
            jumlah = int(input("Masukkan jumlah lauk yang dipilih : "))

            print(f"Harga Lauk = {biaya_lauk[kodelauk - 1] * jumlah}")

            sum_ += biaya_lauk[kodelauk - 1] * jumlah

            answer = input("Apakah anda ingin menambah lauk lagi? (y/n) : ")

            if answer.lower() == 'y':
                continue
            elif answer.lower() == 'n':
                break
            else:
                print("Kode yang anda masukkan tidak valid!")

    print(f"TOTAL BIAYA LAUK : {sum_}")
    return sum_


def biaya_sayur():
    sum_ = 0

    belisayur = input("\nApakah anda ingin membeli sayur? (y/n) : ")

    if belisayur.lower() == 'y':
        while True:
            biaya_sayur = [3000, 5000, 3000, 4000, 3000]

            kodesayur = int(input("\nMasukkan kode sayur yang anda pilih : "))
            jumlah = int(input("Masukkan jumlah porsi sayur yang dipilih : "))

            print(f"Harga Sayur = {biaya_sayur[kodesayur - 1] * jumlah}")

            sum_ += biaya_sayur[kodesayur - 1] * jumlah

            answer = input("Apakah anda ingin menambah sayur lagi? (y/n) : ")

            if answer.lower() == 'y':
                continue
            elif answer.lower() == 'n':
                break
            else:
                print("Kode yang anda masukkan tidak valid!")

    print(f"TOTAL BIAYA SAYUR : {sum_}")
    return sum_


def biaya_minum():
    sum_ = 0

    beliminum = input("\nApakah anda ingin membeli minum? (y/n) : ")

    if beliminum.lower() == 'y':
        while True:
            biaya_minum = [4000, 5000, 3000]

            kodeminuman = int(input("\nMasukkan kode minuman yang anda pilih : "))
            jumlah = int(input("Masukkan jumlah minuman yang dipilih : "))

            print(f"Harga Minuman = {biaya_minum[kodeminuman - 1] * jumlah}")

            sum_ += biaya_minum[kodeminuman - 1] * jumlah

            answer = input("Apakah anda ingin menambah minuman lagi? (y/n) : ")

            if answer.lower() == 'y':
                continue
            elif answer.lower() == 'n':
                break
            else:
                print("Kode yang anda masukkan tidak valid!")

    print(f"TOTAL BIAYA MINUMAN : {sum_}")
    return sum_


def main():
    print("====================================================")
    print("=                                                  =")
    print("=              WELCOME TO WARTEG MODERN            =")
    print("=                                                  =")
    print("====================================================")

    # Initialization of side dishes menu
    lauk = ["Ayam goreng", "Ayam Bakar", "Lele Goreng", "Telur Dadar", "Rendang"]

    print("---- PILIHAN LAUK ----")
    for i, item in enumerate(lauk, 1):
        print(f"[{i}] : {item}")

    # Initialization of vegetables menu
    sayur = ["Sayur Bayam", "Sayur Sop", "Sayur Lodeh", "Sayur Labu", "Sayur Kangkung"]

    print("\n----  PILIHAN SAYUR ----")
    for i, item in enumerate(sayur, 1):
        print(f"[{i}] : {item}")

    # Initialization of drinks menu
    minum = ["Es Teh", "Es Jeruk", "Air mineral"]

    print("\n---- PILIHAN MINUMAN ----")
    for i, item in enumerate(minum, 1):
        print(f"[{i}] : {item}")

    print("\nINTRUKSI USER\n[kode] : pilihan\n")

    total_pembayaran = biaya_lauk() + biaya_sayur() + biaya_minum()  # Calculate total payment

    print(f"\n\nTOTAL PEMBAYARAN : {total_pembayaran}")

    bayar = int(input("TOTAL UANG YANG DIBAYARKAN : "))  # Input total money paid

    kembalian = bayar - total_pembayaran  # Calculate money changes

    print(f"\nTOTAL SISA UANG DARI PEMBAYARAN : {kembalian}")

    print("====================================================")
    print("=                                                  =")
    print("=        TERIMA KASIH DAN SELAMAT MENIKMATI        =")
    print("=                                                  =")
    print("====================================================")


if __name__ == "__main__":
    main()
