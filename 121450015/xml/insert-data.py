# Insert Data

import xml.etree.ElementTree as ET
# Membaca file XML
tree = ET.parse('xml/mahasiswa.xml') 
root = tree.getroot()

# Membuat elemen untuk mahasiswa baru
mahasiswa_baru = ET.Element('data') 
mahasiswa_baru.set('nim', '121450015')

# Menambahkan sub-elemen untuk mahasiswa baru
nama = ET.SubElement(mahasiswa_baru, 'nama') 
nama.text = 'Mujadid Choirus Surya'

jurusan = ET.SubElement(mahasiswa_baru, 'jurusan') 
jurusan.text = 'Sains Data'

alamat = ET.SubElement(mahasiswa_baru, 'alamat') 
alamat.text = 'Pringsewu'

#Menambahkan mahasiswa baru ke dalam root
root.append(mahasiswa_baru) 
ET.indent(tree, space="\t", level=0)
# Menyimpan perubahan ke dalam file XML 
tree.write('xml/mahasiswa.xml')