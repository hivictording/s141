# Author: Victor Ding

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

if __name__ == "__main__":
    tree1 = ET.parse("xml1.xml")
    tree2 = ET.parse("xml2.xml")
    tree3 = ET.parse("xml3.xml")
    root1 = tree1.getroot()
    root2 = tree2.getroot()
    root3 = tree3.getroot()
    print(type(root1))
    print(root1.tag)

    for child in root3:
        # print(child.tag)
        print(child.tag,"Name:",child.attrib["name"])
    # # for country in root3.findall("country"):
    # #     # print(country)
    # #     # 使用find从country节点中查找rank节点
    # #     rank = country.find("rank")
    # #     print(rank.tag, " - ", rank.text)
    # for country in root3.iter("country"):
    #     rank = country.find("rank")
    #     print(country.attrib['name']," rank:",rank.text)
    #
    # for country in root3.iter("country"):
    #     for neighbor in country.findall("neighbor"):
    #         print(country.attrib["name"]," neighbor: ",neighbor.attrib['name']," direction: ",neighbor.attrib['direction'])
    #
    # for movie in root2.iter("movie"):
    #     desc = movie.find("description")
    #     print("Movie name: ",movie.attrib['title']," --- Description: ",desc.text)
    #
    # for year in root2.iter("year"):
    #     year.text = '5000'
    #     year.set("author",'victor')
    #     tree2.write('xml2.xml')
    # #
    # # for rank in root3.iter("rank"):
    # #     rank.text = "mary"
    # #     # rank.set('updated', 'yes')
    # #     tree3.write("xml3.xml")
    #
    # # for country in root3.iter("country"):
    # #     population = ET.Element("population")
    # #     population.text = '10000000'
    # #     country.append(population)
    # #     tree3.write("xml3.xml")
    # #
    # # for country in root3.iter("country"):
    # #     for pop in country.findall("population"):
    # #         country.remove(pop)
    # #     tree3.write("xml3.xml")
    #
    # # for pop in root3.iter("population"):
    # #     print(pop.text)
    # #
    # # for child in root3:
    # #     for child_child in child:
    # #         print(child_child.tag)
    # #         if child_child.tag == "info":
    # #             for third_child in child_child:
    # #                 print(third_child.tag)
    #
    #
    #
