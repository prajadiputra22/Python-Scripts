def hitung_gaji():
    # Meminta input dari pengguna
    jam_kerja = float(input("Masukkan jumlah jam kerja dalam seminggu: "))
    tarif_per_jam = float(input("Masukkan tarif per jam: "))

    # Menentukan gaji
    if jam_kerja > 40:
        jam_lembur = jam_kerja - 40
        gaji_lembur = jam_lembur * tarif_per_jam * 1.5
        gaji_normal = 40 * tarif_per_jam
        total_gaji = gaji_normal + gaji_lembur
        print(f"Gaji normal: {gaji_normal}")
        print(f"Gaji lembur: {gaji_lembur}")
        print(f"Total gaji: {total_gaji}")
    else:
        total_gaji = jam_kerja * tarif_per_jam
        print(f"Total gaji: {total_gaji}")

# Menjalankan fungsi untuk menghitung gaji
hitung_gaji()
