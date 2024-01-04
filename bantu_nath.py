def main():
    print("MENU")

    print("\nAPPETIZER")
    appetizer = ["Nachos", "Bread", "Chips"]
    hargaappetizer = [27000, 23000, 25000]
    for i, (item, price) in enumerate(zip(appetizer, hargaappetizer), 1):
        print("[", i, "]", item, " : ", price)

    print("\nMAIN COURSE")
    main = ["Aglio Olio", "Fetuccine Carbonara", "Nasi Goreng", "Chicken Mentai Rice", "Salmon Mentai Rice"]
    hargamain = [41000, 41000, 37000, 40000, 50000]
    for i, (item, price) in enumerate(zip(main, hargamain), 1):
        print("[", i, "]", item, " : ", price)

    print("\nSIDE DISH")
    side = ["French Fries", "Sausage", "Chicken Karage"]
    hargaside = [27000, 30000, 33000]
    for i, (item, price) in enumerate(zip(side, hargaside), 1):
        print("[", i, "]", item, " : ", price)

    print("\nDESSERT")
    dessert = ["Mochi Ice Cream", "Caramel Custard"]
    hargadessert = [21000, 28000]
    for i, (item, price) in enumerate(zip(dessert, hargadessert), 1):
        print("[", i, "]", item, " : ", price)

    print("\nBEVERAGE")
    beverage = ["Ice Tea", "Artisan Tea", "Americano", "Coffee Latte", "Mineral Water"]
    hargabeverage = [18000, 28000, 21000, 27000, 12000]
    for i, (item, price) in enumerate(zip(beverage, hargabeverage), 1):
        print("[", i, "]", item, " : ", price)

    def pesan_appetizer():
        jumlah = 0
        pesanan = []
        beliappetizer = input("Apakah ada appetizer yang ingin dipesan? (y/n) ")
        if beliappetizer.lower() == "y":
            while True:
                kodeappetizer = int(input("Masukkan kode appetizer: "))
                qty = int(input("Masukkan jumlah: "))
                print("Total harga item = ", hargaappetizer[kodeappetizer - 1] * qty)
                jumlah += hargaappetizer[kodeappetizer - 1] * qty
                pesanan.append((qty, appetizer[kodeappetizer - 1], hargaappetizer[kodeappetizer - 1] * qty))
                tambah = input("Apakah ada appetizer lain yang ingin dipesan? (y/n) ")
                if tambah.lower() == "y":
                    continue
                else:
                    break
            print("Total harga appetizer = ", jumlah)
        return jumlah, pesanan

    def pesan_main():
        jumlah = 0
        pesanan = []
        belimain = input("Apakah ada main course yang ingin dipesan? (y/n) ")
        if belimain.lower() == "y":
            while True:
                kodemain = int(input("Masukkan kode main course: "))
                qty = int(input("Masukkan jumlah: "))
                print("Total harga item = ", hargamain[kodemain - 1] * qty)
                jumlah += hargamain[kodemain - 1] * qty
                pesanan.append((qty, main[kodemain - 1], hargamain[kodemain - 1] * qty))
                tambah = input("Apakah ada main course lain yang ingin dipesan? (y/n) ")
                if tambah.lower() == "y":
                    continue
                else:
                    break
            print("Total harga main course = ", jumlah)
        return jumlah, pesanan

    def pesan_side():
        jumlah = 0
        pesanan = []
        beliside = input("Apakah ada side dish yang ingin dipesan? (y/n) ")
        if beliside.lower() == "y":
            while True:
                kodeside = int(input("Masukkan kode side dish: "))
                qty = int(input("Masukkan jumlah: "))
                print("Total harga item = ", hargaside[kodeside - 1] * qty)
                jumlah += hargaside[kodeside - 1] * qty
                pesanan.append((qty, side[kodeside - 1], hargaside[kodeside - 1] * qty))
                tambah = input("Apakah ada side dish lain yang ingin dipesan? (y/n) ")
                if tambah.lower() == "y":
                    continue
                else:
                    break
            print("Total harga side dish = ", jumlah)
        return jumlah, pesanan

    def pesan_dessert():
        jumlah = 0
        pesanan = []
        belidessert = input("Apakah ada dessert yang ingin dipesan? (y/n) ")
        if belidessert.lower() == "y":
            while True:
                kodedessert = int(input("Masukkan kode dessert: "))
                qty = int(input("Masukkan jumlah: "))
                print("Total harga item = ", hargadessert[kodedessert - 1] * qty)
                jumlah += hargadessert[kodedessert - 1] * qty
                pesanan.append((qty, dessert[kodedessert - 1], hargadessert[kodedessert - 1] * qty))
                tambah = input("Apakah ada dessert lain yang ingin dipesan? (y/n) ")
                if tambah.lower() == "y":
                    continue
                else:
                    break
            print("Total harga dessert = ", jumlah)
        return jumlah, pesanan

    def pesan_beverage():
        jumlah = 0
        pesanan = []
        belibeverage = input("Apakah ada beverage yang ingin dipesan? (y/n) ")
        if belibeverage.lower() == "y":
            while True:
                kodebeverage = int(input("Masukkan kode beverage: "))
                qty = int(input("Masukkan jumlah: "))
                print("Total harga item = ", hargabeverage[kodebeverage - 1] * qty)
                jumlah += hargabeverage[kodebeverage - 1] * qty
                pesanan.append((qty, beverage[kodebeverage - 1], hargabeverage[kodebeverage - 1] * qty))
                tambah = input("Apakah ada beverage lain yang ingin dipesan? (y/n) ")
                if tambah.lower() == "y":
                    continue
                else:
                    break
            print("Total harga beverage = ", jumlah)
        return jumlah, pesanan

    pesanan_appetizer = pesan_appetizer()
    pesanan_main = pesan_main()
    pesanan_side = pesan_side()
    pesanan_dessert = pesan_dessert()
    pesanan_beverage = pesan_beverage()

    totalbayar = (
        pesanan_appetizer[0] + pesanan_main[0] + pesanan_side[0] + pesanan_dessert[0] + pesanan_beverage[0])
    pesanan = pesanan_appetizer[1] + pesanan_main[1] + pesanan_side[1] + pesanan_dessert[1] + pesanan_beverage[1]

    print("Pesanan Anda:")
    for item in pesanan:
        print(f"{item[0]} {item[1]} {item[2]}")

    print("Total yang harus dibayar: ", totalbayar)

main()
