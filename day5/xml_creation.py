# Author: Victor Ding

try:
    import xml.etree.cElementTree as etree
except ImportError:
    import xml.etree.ElementTree as etree

users_xml = etree.Element("Users")

name = etree.SubElement(users_xml,"User",attrib={"Name":"Victor","enrolled":"yes"})
age = etree.SubElement(name,"age",attrib={"checked":"yes"})
age.text ='44'
sex = etree.SubElement(name,"sex")
sex.text = 'Male'
name2 = etree.SubElement(users_xml,"User",attrib={"Name":"Mary","enrolled":"no"})
sex2 = etree.SubElement(name2,"sex")
sex2.text = 'Female'
age2 = etree.SubElement(name2,"age")
age2.text = '19'

tree = etree.ElementTree(users_xml)
tree.write("xml_creation.xml",encoding='utf-8',xml_declaration=True)


