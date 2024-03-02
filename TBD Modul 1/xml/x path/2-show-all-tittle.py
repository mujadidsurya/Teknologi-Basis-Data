import xml.etree.ElementTree as ET

#Membaca file XL
tree = ET.parse('books.xml')
root = tree.getroot()

#Ekspresi XPath
titles = root.findall('book/title')

#Menampilkan judul buku
for title in titles: 
    print(title.text)