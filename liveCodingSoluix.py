# Bahasa: Python

# Mapping bc why not
angkaToKata = {
	0: "",
	1: "Satu",
	2: "Dua",
	3: "Tiga",
	4: "Empat",
	5: "Lima",
	6: "Enam",
	7: "Tujuh",
	8: "Delapan",
	9: "Sembilan",
	10: "Sepuluh",
	11: "Sebelas"
}

# Fungsi Konversi
def terbilang(angka):

	if angka == 0:
		return "Nol"
	elif angka <= 11:
		return angkaToKata[angka]
	elif angka <= 20:
		return angkaToKata[angka - 10] + " Belas"
	elif angka < 100:
		return angkaToKata[angka // 10] + " Puluh " + terbilang(angka % 10)
	elif angka < 200:
		return "Seratus " + terbilang(angka - 100)
	elif angka < 1000:
		return angkaToKata[angka // 100] + " Ratus " + terbilang(angka % 100)
	elif angka < 2000:
		return "Seribu " + terbilang(angka - 1000)
	elif angka < 10000:
		return terbilang(angka // 1000) + " Ribu " + terbilang(angka % 1000)
	else:
		return "Angka kebesaran, coba masukkan lebih kecil :)"

# Untuk Excessive Spacing
def formatting(angka):
	return " ".join(terbilang(angka).split())

angka = int(input("Angka (0 - 9999): "))
print(formatting(angka))
	