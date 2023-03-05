from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import re
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
    ptrs = soup.find_all("ptr")

    links = []
    for ptr in ptrs:
        links.append(ptr["target"])

    link_pattern = re.compile(r"https?://\S+")
    paragraphs = soup.find_all("p")
    for p in paragraphs:
        link_paragraphs = link_pattern.findall(p.text)
        for link in link_paragraphs:
            print(link)
            links.append(link)
    res = ""
    if str(len(links)) != 0:
        res += "<h3>Links found (" + str(len(links)) + "):<h3><ul>"
        for link in links:
            res += "<li style=\"font-size:18px\"><a href=\"" + link + "\">" + link + "</a></li>"
        res += "</ul>"
    else:
        res= "<h3>No links found.<h3>"
    return res

if __name__ == "__main__":

    def check_structure():
        if not os.path.exists("./input"):
            print("Input directory does not exist.")
            return False
        if not os.path.exists("./output"):
            print("Output directory does not exist.")
            return False
        print("Directory structure is OK.")
        return True

    def check_output():
        if not os.path.exists("input/analysis.html"):
            print("analysis.html file was not created.")
            return False
        if not os.path.exists("input/figures_histogram.png"):
            print("figures_histogram.png file was not created.")
            return False
        print("analisys.html file created on the input/ directory.")
        return True


    if check_structure():
        # This code will not be used if this module is imported, this is because of the tests, bcause they fail with the grobid client.
        from grobid_client.grobid_client import GrobidClient

        client = GrobidClient(config_path="config.json")
        client.process("processFulltextDocument", "/input", output="/output", consolidate_citations=True, tei_coordinates=True, force=True)


        output_path = '/output/'
        output_file = 'input/analysis.html'
        output_file_figure = 'input/figures_histogram.png'

        if os.path.exists(output_file):
            os.remove(output_file)

        if os.path.exists(output_file_figure):
            os.remove(output_file_figure)

        num_figures = [] # list to store the number of figures for each file
        file_names = [] # list to store the name of each file

        with open(output_file, 'w') as file:
            for root, dirs, files in os.walk(output_path):
                for file_name in files + dirs:
                    
                    file_path = os.path.join(root, file_name)

                    with open(file_path, 'r', encoding="utf-8") as tei:
                        soup = BeautifulSoup(tei, 'xml')
                        file_display = str(file_path).removeprefix("/output/").removesuffix(".tei.xml")
                        file.write("<h1> For file: " + file_display + "</h1>")
                        
                        file.write(get_keywords(soup))
                        num_figures.append(get_figures(soup))
                        file_names.append(file_display)
                        file.write(get_links(soup))

                        file.write("<hr></hr>")

            plt.figure()
            plt.bar(file_names,num_figures, align='center') 
            plt.xlabel('File names')
            plt.ylabel('Number of figures')
            plt.xticks(rotation=90)
            plt.savefig('input/figures_histogram.png')

            file.write("<h1>Number of Figures Histogram:</h1>")
            file.write("<img src=\"figures_histogram.png\">")
            check_output()