from bs4 import BeautifulSoup
import os

def get_keywords(soup):
   return soup.find('keywords')

def get_figures(soup):
   return soup.find_all('figure')

def get_links(soup):
   return soup.find_all("ptr")

directory_path = '../pdfs/output/'
output_file = 'rationale.md'

if os.path.exists(output_file):
    os.remove(output_file)

with open(output_file, 'w') as file:
    for root, dirs, files in os.walk(directory_path):
        for file_name in files + dirs:
            file_path = os.path.join(root, file_name)

            with open(file_path, 'r', encoding="utf-8") as tei:
                soup = BeautifulSoup(tei, 'xml')
                keywords = get_keywords(soup)
                figures = get_figures(soup)
                links = get_links(soup)

                file.write("## For file: " + str(file_path).removeprefix("../pdfs/output/") + "\n\n")
                
                if keywords is not None:
                    file.write("Keywords:\n\n" + keywords.text + "\n\n")
                else:
                    file.write("No keywords found.\n\n")

                if figures is not None:
                    file.write("Number of figures found " + str(len(figures)) + "\n\n")
                else:
                    file.write("Number of figures found: 0\n\n")

                if links is not None:
                    file.write(str(len(links)) + " Links found:\n\n")
                    for link in links:
                        file.write("- " + link["target"] + "\n")
                    file.write("\n")
                else:
                    file.write("No links found.\n\n")

                file.write("---\n\n")