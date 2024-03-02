# Find by NIM

import xml.etree.ElementTree as ET
# Membaca file XML
tree = ET.parse('xml/mahasiswa.xml')
root = tree.getroot()

# Tentukan NIM yang ingin dicari
nim_dicari = "777888999"

# XPath: /mahasiswa/data
mahasiswa = root.findall('data')

# Menampilkan informasi mahasiswa berdasarkan NIM
for data in mahasiswa:
    # Mengakses atribut NIM
    nim = data.attrib['nim']
    
    # Cek apakah NIM cocok dengan yang dicari
    if nim == nim_dicari:
        # Mengakses informasi mahasiswa
        nama = data.find('nama').text
        jurusan = data.find('jurusan').text
        alamat = data.find('alamat').text  
        # Menampilkan informasi mahasiswa
        print("Data Mahasiswa: ")
        print(f"NIM: {nim}")
        print(f"Nama: {nama}")
        print(f"Jurusan: {jurusan}")
        print(f"Alamat: {alamat}")
        break  # Hentikan pencarian setelah menemukan NIM yang cocok
else:
    print("Mahasiswa dengan NIM tersebut tidak ditemukan.")
