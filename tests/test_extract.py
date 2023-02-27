from bs4 import BeautifulSoup
from practica_1 import extract as ext


def get_xml(file):
    with open("tests/xmls/" + file, 'r', encoding="utf-8") as tei:
        return BeautifulSoup(tei, 'xml')

# Test that should find the keywords in the xml.
def test_get_keywords(): 
    soup = get_xml("test1.xml")
    assert ext.get_keywords(soup) == ("### Keywords:\n\nKEY1\nKEY2\nKEY3\nKEY4\nKEY5\nKEY6\n")

# Test that should return No Keywords found since ther are none.
def test_get_no_keywords(): 
    soup = get_xml("test2.xml")
    assert ext.get_keywords(soup) == ("### No keywords found.\n")

# Test that should find amount of figures in the xml.
def test_get_figures(): 
    soup = get_xml("test2.xml")
    assert ext.get_figures(soup) == ("### Number of figures found: 3\n")

# Test that should return No figures found since ther are none.
def test_get_no_figures(): 
    soup = get_xml("test1.xml")
    assert ext.get_figures(soup) == ("### Number of figures found: 0\n")

# Test that should show the links in the xml.
def test_get_links(): 
    soup = get_xml("test3.xml")
    assert ext.get_links(soup) == ("### Links found (3):\n- http://www.link1.com\n- http://www.link2.com\n- http://www.link3.com\n")

# Test that should return No links found since ther are none.
def test_get_no_links(): 
    soup = get_xml("test1.xml")
    assert ext.get_links(soup) == ("### Links found (0):\n")
