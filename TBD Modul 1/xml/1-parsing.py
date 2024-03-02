import xml.etree.ElementTree as ET
#Membaca file XML
tree = ET.parse('xml/books.xml')
root = tree.getroot()
#Menampilkan informasi tentang setiap
for book in root.findall('book'):
    #Mengakses informasi buku
    title = book.find('title').text
    author = book.find('author').text
    genre = book.find('genre').text
    price = book.find('price').text
    
    # Menampilkan informasi buku
    print(f"Title: {title}")
    print(f"Author: {author}")
    print(f"Genre: {genre}")
    print(f"Price: {price}")
    print()