import xml.etree.ElementTree as ET

#Membuat root element
root = ET.Element("books")

#Membuat child elements untuk setiap buku
book1 = ET.SubElement(root, "book") 
book1.set("id", "1")

title1 = ET.SubElement(book1, "title")
title1.text = "The Catcher in the Rye"

author1 = ET.SubElement (book1, "author") 
author1.text = "J.D. Salinger"

genre1 = ET.SubElement(book1, "genre") 
genre1.text = "Fiction"

price1 = ET.SubElement(book1, "price") 
price1.text = "20.00"

book2 = ET.SubElement(root, "book") 
book2.set("id", "2")

title2 = ET.SubElement(book2, "title")
title2.text = "To Kill a Mockingbird"

author2 = ET.SubElement (book2, "author") 
author2.text = "Harper Lee"

genre2 = ET.SubElement(book2, "genre")
genre2.text = "Fiction"

price2 = ET.SubElement (book2, "price") 
price2.text = "18.00"

# Membuat XML tree dari root element
tree = ET. ElementTree(root) 
ET.indent(tree, space="\t", level=0)
# Menyimpan XML ke file
tree.write("xml/new-books.xml")