# Rationale.md

The purpose of this document is to explain the validation of the output of the application. This has been done using a variety of methods:

* **Python tests:** this tests were used to check if the extraction methods from the XMLs were correct. With these, we compared their output with the desired one to see if they were correct.
  * The tests used specific .xml files created for this purpose. They checked if the keywords were correct, the links and the amount of figures with those files. Some tests were made to see what happens if one file doesn't have one element, for example, doesn't have links.
* **Internal checks:** inside the proper application code, some functions like *check_structure()* and *check_output()* were made to see if the initial application structure was correct and if the desired output files were created respectively.
* **Manual checks:** using some example *.pdfs* files, manually I could check if the amount of figures, the keybords and the links were correct.

Using these kinds of validation methods, I assume that the information provided by the application is correct.
