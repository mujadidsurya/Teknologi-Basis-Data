# Show by Jurusan

import xml.etree.ElementTree as ET
# Membaca file XML
tree = ET.parse('xml/mahasiswa.xml')
root = tree.getroot()

#Mencari semua mahasiswa dengan Jurusan Arsitektur
jurusan_dicari = root.findall("data[jurusan='Arsitektur']")

# Cek apakah ada data dengan jurusan yang dicari
if jurusan_dicari:
    print("Mahasiswa dengan jurusan Arsitektur:")

    # Menampilkan informasi buku
    for data in jurusan_dicari:
        nim = data.attrib['nim']
        nama = data.find('nama').text
        alamat = data.find('alamat').text
        print(f"NIM: {nim}, Nama: {nama}, Alamat: {alamat}")
else:
    print("Tidak ada mahasiswa dengan jurusan Arsitektur")