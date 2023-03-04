# PDF_Analyzer

PDF information extractor for the course of Artificial Intelligence And Open Science In Research Software Engineering.

## Description

This proyects refers to a PDF extraction and parser using Grobit for the method of parsing the PDF and a python program to extract the desired information.

Currently, the program accepts up to 10 pdf files as an input and will produce a "analysis.html" file that will contain the following:

* For each file:
  * Title.
  * Keyword cloud.
  * List of links.
* Histogram of the numer of figures per each file.

## Requirements

To run this program you will need:

* System with Windows or Linux operating systems.
* Install [Grobid](https://github.com/kermitt2/grobid).
* Install [Docker](https://docs.docker.com/engine/install/).

## Installation instructions

1. Clone the git project:

   ```bash
   git clone https://github.com/YizzaJ/PDF_Analyzer.git
   ```
2. Start the docker server.
3. Build the image: On the PDF_Analyzer directory run:

   ```bash
   docker build -t analyzer .
   ```

   Note: `analyzer` will be the name of the image. You can change it but remember it so you can run it afterwards.

## Execution instructions

1. Run the docker server.
2. Run grobid on **localhost:8070,** its important that the **8070** port is the one that is being used.
3. Go to or create a directory to run the application. (For the instructions we will call this the *app* directory).
4. Inside that directory, create another directory called **input**. Important that it has that name.
5. Inside the **input** directory, store the **(up to 10)** *.pdfs* files you want to extract the information from.
6. Run the container from the *app directory*:

   If you are running this program on a Windows based OS use this code:

   ```bash
   docker run --rm -it -v %cd%/input/:/input --network=host --name=PDFanalyzer analyzer
   ```

   If you are running this program on a Linux based OS use this code:

   ```bash
   docker run --rm -it -v %cd%/input/:/input --network=host --name=PDFanalyzer analyzer
   ```

   Notes: `analyzer` was the name of the image in the example, if you changed it when building the image use the  name you chose. `PDFanalyzer` will be the name of the container,you can choose what you like.
7. Inside the input directory previously created, an *analisys.html* file will be created with the desired information. Also a *figures_histogram.png* file will be created with the image of the number of figures histogram.
8. If you want to run it again just repeat step 6.

   **IMPORTANT**: the previous *analisys.html* and *igures_histogram.png* will be deleted.

## Example

Inside the `example` directory of the project you could see an example of the structure of the directory where the application was runned.

## Contact

Main author and contact: Jesus Hernandez ([jesus.hernandezp@alumnos.upm.es](jesus.hernandezp@alumnos.upm.es)).
