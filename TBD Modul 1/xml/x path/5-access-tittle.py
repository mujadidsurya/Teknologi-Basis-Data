import xml.etree.ElementTree as ET

# Membaca file XML
tree = ET.parse('books.xml')
root = tree.getroot()

# XPath: /books/book
books = root.findall('book')

#Menampilkan judul buku
for book in books:
    # Mengakses tittle buku yang berada dalam konteks saat ini
    title = book.find('./title').text
    # Menampilkan informasi buku
    print(f"Title: {title}")
    print()