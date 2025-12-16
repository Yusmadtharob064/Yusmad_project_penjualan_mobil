# Aplikasi Penjualan Mobil

mobil = {
    1: {"merek": "Toyota Avanza", "harga": 300000000},
    2: {"merek": "Honda Brio", "harga": 170000000},
    3: {"merek": "Mitsubishi Xpander", "harga": 320000000},
    4: {"merek": "Suzuki Ertiga", "harga": 280000000},
    5: {"merek": "Daihatsu Terios", "harga": 290000000}
}

def tampilkan_mobil():
    print("===== DAFTAR MOBIL =====")
    for key, value in mobil.items():
        print(f"{key}. {value['merek']} - Rp {value['harga']:,}")
    print("========================")

def beli_mobil():
    total = 0
    while True:
        pilih = int(input("Pilih nomor mobil (0 untuk selesai): "))
        if pilih == 0:
            break
        elif pilih in mobil:
            jumlah = int(input("Jumlah unit: "))
            subtotal = mobil[pilih]["harga"] * jumlah
            total += subtotal
            print(f"Ditambahkan: {mobil[pilih]['merek']} x{jumlah} = Rp {subtotal:,}")
        else:
            print("Pilihan tidak tersedia!")

    print("\n===== RINGKASAN PEMBELIAN =====")
    print(f"Total Harga: Rp {total:,}")
    print("Terima kasih telah membeli mobil di showroom kami!")

# Program utama
tampilkan_mobil()
beli_mobil()
