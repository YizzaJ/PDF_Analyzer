from bs4 import BeautifulSoup
from practica_1.extract import get_keywords, get_figures, get_links


def get_xml(file):
    with open("tests/xmls/" + file, 'r', encoding="utf-8") as tei:
        return BeautifulSoup(tei, 'xml')

# Test that should find the keywords in the xml.
def test_get_keywords(): 
    soup = get_xml("test1.xml")
    assert get_keywords(soup) == ("<h3>Keywords: </h3> <p>\nKEY1\nKEY2\nKEY3\nKEY4\nKEY5\nKEY6\n</p>")

# Test that should return No Keywords found since ther are none.
def test_get_no_keywords(): 
    soup = get_xml("test2.xml")
    assert get_keywords(soup) == ("<h3>Keywords: </h3> <p>No Keywords found.</p>")

# Test that should find amount of figures in the xml.
def test_get_figures(): 
    soup = get_xml("test2.xml")
    assert get_figures(soup) == 3

# Test that should return No figures found since ther are none.
def test_get_no_figures(): 
    soup = get_xml("test1.xml")
    assert get_figures(soup) == 0

# Test that should show the links in the xml.
def test_get_links(): 
    soup = get_xml("test3.xml")
    assert get_links(soup) == ("<h3>Links found (3):<h3><ul><li style=\"font-size:18px\">" +
                               "<a href=\"http://www.link1.com\">http://www.link1.com</a></li>" +
                               "<li style=\"font-size:18px\"><a href=\"http://www.link2.com\">http://www.link2.com</a>" +
                               "</li><li style=\"font-size:18px\"><a href=\"http://www.link3.com\">http://www.link3.com</a></li></ul>")

# Test that should return No links found since ther are none.
def test_get_no_links(): 
    soup = get_xml("test1.xml")
    assert get_links(soup) == ("<h3>Links found (0):<h3><ul></ul>")

# Test that should show the links in the xml inside paragraphs.
def test_get_links_paragraphs(): 
    soup = get_xml("test4.xml")
    assert get_links(soup) == ("<h3>Links found (3):<h3><ul><li style=\"font-size:18px\">" +
                               "<a href=\"http://www.link1.com\">http://www.link1.com</a></li>" +
                               "<li style=\"font-size:18px\"><a href=\"http://www.link2.com\">http://www.link2.com</a>" +
                               "</li><li style=\"font-size:18px\"><a href=\"http://www.link3.com\">http://www.link3.com</a></li></ul>")

# Test that should show the links in the xml inside paragraphs and ptrs.
def test_get_links_paragraphs_ptrs(): 
    soup = get_xml("test5.xml")
    assert get_links(soup) == ("<h3>Links found (4):<h3><ul>"+
                               "<li style=\"font-size:18px\"><a href=\"http://www.link1.com\">http://www.link1.com</a></li>" +
                               "<li style=\"font-size:18px\"><a href=\"http://www.link2.com\">http://www.link2.com</a></li>" +
                               "<li style=\"font-size:18px\"><a href=\"http://www.link3.com\">http://www.link3.com</a></li>"+
                               "<li style=\"font-size:18px\"><a href=\"http://www.link4.com\">http://www.link4.com</a></li>"+
                               "</ul>")