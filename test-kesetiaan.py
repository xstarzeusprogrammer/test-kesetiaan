print("SOAL KESETIAAN")
print("BY X STAR ZEUS PRIFRAMMER")
print("")
print("CATATAN")
print("JIKA JAWABAN BENAR POIN +1")
print("JIKA JAWABAN SALAH POIN -1")
print("BACA SOAL DENGAN SUNGGUH SUNGGUH!")
print("ADA 2 SOAL, JAWAB DENGAN SUNGGUH SUNGGUH!!")
print("")

print("1. JIKA ORANG LAIN CANTIK/TAMVAN MENEMBAK KAMU, SEDANGKAN KAMU DAH PUNYA DOI, APA YANG AKAN ANDA LAKUKAN?")
print("")
print("a. MENOLAKNYA")
print("b. MENERIMANYA")
print("c. MEMBERITAHU JIKA AKU SUDAH PUNYA DOI")
print("d. TIDAK MENGHIRAUKANNYA")
jawaban1 = input("JAWAB SESUAI a,b,c,d ==> ")

kunci1 = ("c")

if str(jawaban1) == kunci1:
	print("")
	print("JAWABAN ANDA BENAR!")
	print("POIN +1")
	print("")
	poin1 = 1
	
else:
	print("")
	print("JAWABAN ANDA SALAH!")
	print("POIN -1")
	print("")
	poin1 = -1
	
print("2. JIKA KAMU BERTEMU DENGAN CEWE/COWO YANG CANTIK/TAMVAN APA YANG KAMU LAKUKAN, SEDANGKAN KAMU SUDAH MEMPUNYAI PACAR?")
print("")
print("a. MENDEKATINYA")
print("b. PDKT")
print("c. AJAK BICARA")
print("d. ABAIKAN SAJA")
print("")

jawaban2 = input("JAWAB SESUAI a,b,c,d ==> ")

kunci2 = ("c")

if str(jawaban2) == kunci2:
	print("")
	print("JAWABAN ANDA BENAR!")
	print("POIN +1")
	poin2 = 1
	
else:
	print("")
	print("JAWABAN ANDA SALAH!")
	print("POIN -1")
	poin2 = -1

print("POIN TOTAL")
print(poin1 + poin2)
