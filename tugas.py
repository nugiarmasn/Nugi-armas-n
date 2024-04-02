nama_peserta_cpns = str(input('masukan nama peserta : '))
umur = int(input('masukan umur : '))
pendidikan = str(input('masukan pendidikan : '))
kesehatan = str(input('masukan sehat / tidak sehat : '))
nilai = int(input('transkip nilai : '))

min_pendidikan = ['SMA', 'SMK', 'S1', 'D4']
if umur <= 30 and pendidikan in min_pendidikan and kesehatan == "Sehat" and nilai >= 80:
    print("SELAMAT ANDA LOLOS TAHAP INI")
else :
    print("ANDA TIDAK LOLOS DI TAHAP INI")