import xml.etree.ElementTree as ET

# Membaca file XML
tree = ET.parse('xml/books.xml') 
root = tree.getroot()

# Membuat elemen untuk buku baru
new_book = ET.Element('book') 
new_book.set('id', '4')

# Menambahkan sub-elemen untuk buku baru
title = ET.SubElement(new_book, 'title') 
title.text = 'The Great Gatsby'

author = ET.SubElement(new_book, 'author') 
author.text = 'F. Scott Fitzgerald'

genre = ET.SubElement(new_book, 'genre') 
genre.text = 'Classic'

price = ET.SubElement(new_book, 'price') 
price.text = '25.00'

#Menambahkan buku baru ke dalam root
root.append(new_book) 
ET.indent(tree, space="\t", level=0)
# Menyimpan perubahan ke dalam file XML 
tree.write('xml/books.xml')