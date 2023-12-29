def main():
    print("MENU")

    print("\nAPPETIZER")
    appetizer = ["Nachos", "Bread", "Chips"]
    hargaappetizer = [27000, 23000, 25000]
    for i, (item, price) in enumerate(zip(appetizer, hargaappetizer), 1):
        print(f"[{i}] {item} : {price}")

    print("\nMAIN COURSE")
    main_course = ["Aglio Olio", "Fetuccine Carbonara", "Nasi Goreng", "Chicken Mentai Rice", "Salmon Mentai Rice"]
    hargamain = [41000, 41000, 37000, 40000, 50000]
    for i, (item, price) in enumerate(zip(main_course, hargamain), 1):
        print(f"[{i}] {item} : {price}")

    print("\nSIDE DISH")
    side_dish = ["French Fries", "Sausage", "Chicken Karage"]
    hargaside = [27000, 30000, 33000]
    for i, (item, price) in enumerate(zip(side_dish, hargaside), 1):
        print(f"[{i}] {item} : {price}")

    print("\nDESSERT")
    dessert = ["Mochi Ice Cream", "Caramel Custard"]
    hargadessert = [21000, 28000]
    for i, (item, price) in enumerate(zip(dessert, hargadessert), 1):
        print(f"[{i}] {item} : {price}")

    print("\nBEVERAGE")
    beverage = ["Ice Tea", "Artisan Tea", "Americano", "Coffee Latte", "Mineral Water"]
    hargabeverage = [18000, 28000, 21000, 27000, 12000]
    for i, (item, price) in enumerate(zip(beverage, hargabeverage), 1):
        print(f"[{i}] {item} : {price}")

    def pesan_appetizer():
        jumlah = 0
        beliappetizer = input("Apakah ada appetizer yang ingin dipesan? (y/n) ")
        if beliappetizer.lower() == "y":
            while True:
                kodeappetizer = int(input("Masukkan kode appetizer: "))
                qty = int(input("Masukkan jumlah: "))
                print(f"Total harga item = {hargaappetizer[kodeappetizer - 1] * qty}")
                jumlah += hargaappetizer[kodeappetizer - 1] * qty
                tambah = input("Apakah ada appetizer lain yang ingin dipesan? (y/n) ")
                if tambah.lower() == "y":
                    continue
                else:
                    break
            print(f"Total harga appetizer = {jumlah}")
        return jumlah

    def pesan_main():
        jumlah = 0
        belimain = input("Apakah ada main course yang ingin dipesan? (y/n) ")
        if belimain.lower() == "y":
            while True:
                kodemain = int(input("Masukkan kode main course: "))
                qty = int(input("Masukkan jumlah: "))
                print(f"Total harga item = {hargamain[kodemain - 1] * qty}")
                jumlah += hargamain[kodemain - 1] * qty
                tambah = input("Apakah ada main course lain yang ingin dipesan? (y/n) ")
                if tambah.lower() == "y":
                    continue
                else:
                    break
            print(f"Total harga main course = {jumlah}")
        return jumlah

    def pesan_side():
        jumlah = 0
        beliside = input("Apakah ada side dish yang ingin dipesan? (y/n) ")
        if beliside.lower() == "y":
            while True:
                kodeside = int(input("Masukkan kode side dish: "))
                qty = int(input("Masukkan jumlah: "))
                print(f"Total harga item = {hargaside[kodeside - 1] * qty}")
                jumlah += hargaside[kodeside - 1] * qty
                tambah = input("Apakah ada side dish lain yang ingin dipesan? (y/n) ")
                if tambah.lower() == "y":
                    continue
                else:
                    break
            print(f"Total harga side dish = {jumlah}")
        return jumlah

    def pesan_dessert():
        jumlah = 0
        belidessert = input("Apakah ada dessert yang ingin dipesan? (y/n) ")
        if belidessert.lower() == "y":
            while True:
                kodedessert = int(input("Masukkan kode dessert: "))
                qty = int(input("Masukkan jumlah: "))
                print(f"Total harga item = {hargadessert[kodedessert - 1] * qty}")
                jumlah += hargadessert[kodedessert - 1] * qty
                tambah = input("Apakah ada dessert lain yang ingin dipesan? (y/n) ")
                if tambah.lower() == "y":
                    continue
                else:
                    break
            print(f"Total harga dessert = {jumlah}")
        return jumlah

    def pesan_beverage():
        jumlah = 0
        belibeverage = input("Apakah ada beverage yang ingin dipesan? (y/n) ")
        if belibeverage.lower() == "y":
            while True:
                kodebeverage = int(input("Masukkan kode beverage: "))
                qty = int(input("Masukkan jumlah: "))
                print(f"Total harga item = {hargabeverage[kodebeverage - 1] * qty}")
                jumlah += hargabeverage[kodebeverage - 1] * qty
                tambah = input("Apakah ada beverage lain yang ingin dipesan? (y/n) ")
                if tambah.lower() == "y":
                    continue
                else:
                    break
            print(f"Total harga beverage = {jumlah}")
        return jumlah

    totalbayar = pesan_appetizer() + pesan_main() + pesan_side() + pesan_dessert() + pesan_beverage()
    print("Total yang harus dibayar: ", totalbayar)

main()
