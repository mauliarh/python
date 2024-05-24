menu = {
    "fried Chicken": 15000,
    "Burger Quenn":25000,
    "french Fries":10000,
    "Jasmine Tea":5000,
    "Coca Cola":12000
}
print("====================== Daftar Menu ======================")
for i in menu:
    print("Daftar Menu : ", i,"\t Harga : ",menu[i])
print("pembelian diatas Rp.100.000,00 mendapatkan diskon 15%")
print("============================================")
beli = input("pilih menu : ")
jumlah = int(input("jumlah pesanan : "))
bayar = jumlah * menu[beli]

if bayar > 100000:
    diskon = bayar*15/100
    total = bayar - diskon
else:
    total = bayar

print("====================== Detail Pembayaran ======================")
print("Menu yang dipesan        : ",beli)
print("Jumlah yang dipesan      : ",jumlah)
print("Total Biaya              : ",bayar)
print("Total yang harus dibayar : ",total)

