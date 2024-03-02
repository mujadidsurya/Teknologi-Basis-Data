import xml.etree.ElementTree as ET

# Membaca file XML
tree = ET.parse('books.xml')
root = tree.getroot()

# Ekspresi XPath
titles = root.findall('.//title')

# Menampilkan judul buku
for title in titles: print(title.text)