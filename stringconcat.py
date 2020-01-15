# nama = " ".join(["Erick","Kurniawan","Python"])
# print(nama)

# firstname,separator,lastname = "Erick-Kurniawan".partition("-")

# print(firstname)
# print(lastname)

data = "belajar menggunakan bahasa python dan django".split()

data.remove('python')
hasil = ' '.join(data)
print(hasil)

stocks = {"TLKM":800,"BBRI":988,"SOCI":878}
stocks.update({"TLKM":999})
print(stocks)
