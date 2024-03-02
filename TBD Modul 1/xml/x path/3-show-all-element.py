import xml.etree.ElementTree as ET

# Membaca file XML
tree = ET.parse('xml/books.xml')
root = tree.getroot()

# Mencocokkan semua elemen menggunakan ekspresi XPath //*
all_elements = root.findall('.//*')

#Menampilkan semua elemen yang cocok
for element in all_elements: 
    print(element.tag)