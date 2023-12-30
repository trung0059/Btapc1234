import xml.dom.minidom
def main():
    # use the parse() function to load and parse an XML file
    doc = xml.dom.minidom.parse("employee.xml");
    # print out the document node and the name of the first child tag
    print(doc.nodeName)
    print(doc.firstChild.tagName)
    # get a list of XML tags from the document and print each one
    expertise = doc.getElementsByTagName("expertise")
    print("%d expertise:" % expertise.length)
    for skill in expertise:
        print(skill.getAttribute("name"))
if __name__=="__main__":
    main();