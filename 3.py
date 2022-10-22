

print("                PROGRAM MENGHITUNG PEMBELIAN ")
print("_____________________________________________________________")

harga=float(input("HARGA SATUAN  :"))
jum=float(input("JUMLAH PEMBELIAN  :"))
discon=harga*0.1
print(" DISKON :",discon)
print("total pembayaran :",harga*jum - discon)