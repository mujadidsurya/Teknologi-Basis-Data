import xml.etree.ElementTree as ET

# Membaca file XML
tree = ET.parse('xml/books.xml')
root = tree.getroot()

#XPath: /books/book
books = root.findall('book')

# Menampilkan judul buku
for book in books:
    # Mengakses informasi buku
    title = book.find('title').text
    author = book.find('author').text
    # Menampilkan informasi buku
    print(f"Title: {title}")
    print(f"Author: {author}")
    print()