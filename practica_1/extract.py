from bs4 import BeautifulSoup
import os

def get_keywords(soup):
    keywords = soup.find('keywords')
    if keywords is not None:
        return "### Keywords:\n" + keywords.text
    else:
        return "### No keywords found.\n"

def get_figures(soup):
    figures = soup.find_all('figure')
    if figures is not None:
        return "### Number of figures found: " + str(len(figures)) + "\n"
    else:
       return "### No figures found.\n\n"
    

def get_links(soup):
    links = soup.find_all("ptr")
    res = ""
    if str(len(links)) != 0:
        res += "### Links found (" + str(len(links)) + "):\n"
        for link in links:
            res += "- " + link["target"] + "\n"
    else:
        res= "### No links found.\n"
    return res

output_path = '../pdfs/output/'
output_file = '../rationale.md'

if os.path.exists(output_file):
    os.remove(output_file)

with open(output_file, 'w') as file:
    for root, dirs, files in os.walk(output_path):
        for file_name in files + dirs:
            file_path = os.path.join(root, file_name)

            with open(file_path, 'r', encoding="utf-8") as tei:
                soup = BeautifulSoup(tei, 'xml')
                keywords = get_keywords(soup)
                figures = get_figures(soup)
                links = get_links(soup)

                file.write("# For file: " + str(file_path).removeprefix("../pdfs/output/") + "\n")
                
                file.write(get_keywords(soup))
                file.write(get_figures(soup))

                file.write(get_links(soup))

                file.write("---\n")