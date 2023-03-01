from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import os


def get_keywords(soup):
    keywords = soup.find('keywords')
    if keywords is not None:
        return "<h3>Keywords: </h3> <p>" + keywords.text + "</p>"
    else:
        return "<h3>Keywords: </h3> <p>No Keywords found.</p>"

def get_figures(soup):
    figures = soup.find_all('figure')
    if figures is not None:
        return len(figures)
    else:
       return 0
    

def get_links(soup):
    links = soup.find_all("ptr")
    res = ""
    if str(len(links)) != 0:
        res += "<h3>Links found (" + str(len(links)) + "):<h3><ul>"
        for link in links:
            res += "<li style=\"font-size:18px\"><a href=\"" + link["target"] + "\">" + link["target"] + "</a></li>"
        res += "</ul>"
    else:
        res= "<h3>No links found.<h3>"
    return res

output_path = '../pdfs/output/'
output_file = '../analysis.html'

if os.path.exists(output_file):
    os.remove(output_file)

num_figures = [] # list to store the number of figures for each file
file_names = [] # list to store the name of each file

with open(output_file, 'w') as file:
    for root, dirs, files in os.walk(output_path):
        for file_name in files + dirs:
            file_path = os.path.join(root, file_name)

            with open(file_path, 'r', encoding="utf-8") as tei:
                soup = BeautifulSoup(tei, 'xml')
                file_display = str(file_path).removeprefix("../pdfs/output/").removesuffix(".tei.xml")
                file.write("<h1> For file: " + file_display + "</h1>")
                
                file.write(get_keywords(soup))
                num_figures.append(get_figures(soup))
                file_names.append(file_display)
                file.write(get_links(soup))

                file.write("<hr></hr>")

    plt.figure()
    plt.bar(num_figures, file_names,align='center') 
    plt.xlabel('File names')
    plt.ylabel('Number of figures')
    plt.xticks(rotation=90)
    plt.savefig('figures_histogram.png')

    file.write("<h1>Number of Figures Histogram:</h1>")
    file.write("<img src=\"figures_histogram.png\">")