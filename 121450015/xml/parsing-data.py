# Parsing Data

import xml.etree.ElementTree as ET
#Membaca file XML
tree = ET.parse('xml/mahasiswa.xml')
root = tree.getroot()
#Menampilkan informasi tentang setiap
for data in root.findall('data'):
    #Mengakses informasi data
    nim = data.attrib['nim']
    nama = data.find('nama').text
    jurusan = data.find('jurusan').text
    alamat = data.find('alamat').text   
    # Menampilkan informasi data
    print(f"NIM: {nim}")
    print(f"Nama: {nama}")
    print(f"Jurusan: {jurusan}")
    print(f"Alamat: {alamat}")
    print()