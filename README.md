#### Excuses: I apologize for the English used, my language is Spanish. ####

# Process Python #

## Content: ##

1. [Introduction.](Introduction "Introduction")
2. [Dependencies.](Dependencies "Dependencies")
3. [The process html.](TheProcessHtml "The process html")

## Introduction: [Introduction] ##

This project aims to automate repetitive processes or patterns, using the great Python programming language.

## Dependencies: [Dependencies] ##

- Python (https://www.python.org): Download Python and add it to the path of your operating system.

## The process html: [TheProcessHtml] ##

This command will allow you to create HTML files from others files.

Suppose you downloaded the "processpy" files in the "D:/proyectos/python/processpy/" path and created an "example" folder in the "D:/proyectos/python/example" path. Now you must open a console of your operating system (in this case windows), stand on the "example" folder and run the following command:

** * python D:/proyectos/python/processpy/process.py -html (Command #1) * **

If all goes well, this command should create a couple of files and folders over the current folder (example). Additionally we must create the folder "pageTemplates" inside "example" and a file "index.html" inside "pageTemplates". With this we already have the entire structure which is explained below.

- "../pages": This folder contains the files that correspond to each page.
- "../pageTemplates": This card contains the templates that each of the pages will use.
- "../web": This folder contains the production files.

Now we can do a couple of tests to see how it works. Open the file "../example/pageTemplates/index.html" and add the following lines:

~~~
<!DOCTYPE html>
<html>
	<head>
		<title>Hola Mundo !!!</title>
	</head>
	<body>
		<h1>Hola Mundo !!!</h1>
	</body>
</html>
~~~