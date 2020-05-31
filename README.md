<h4>Excuses: I apologize for the English used, my language is Spanish.</h4>

<h1>Process Python</h1>

<h2>Content:</h2>

<ol>
	<li><a href="#Introduction">Introduction.</a></li>
	<li><a href="#Dependencies">Dependencies.</a></li>
	<li><a href="#ProcessHtml">1) The process html.</a></li>
</ol>

<h2 id="Introduction">Introduction:</h2>

<p>This project aims to automate repetitive processes or patterns, using the great Python programming language.</p>

<h2 id="Dependencies">Dependencies:</h2>

<ol>
	<li>Python (https://www.python.org): Download Python and add it to the path of your operating system.</li>
</ol>

<h2 id="ProcessHtml">1) The process html:</h2>

<p>This command will allow you to create HTML files from others files.</p>

<p>Suppose you downloaded the "processpy" files in the "D:/proyectos/python/processpy/" path and created an "example" folder in the "D:/proyectos/python/example" path. Now you must open a console of your operating system (in this case windows), stand on the "example" folder and run the following command:</p>

<p>python D:/proyectos/python/processpy/process.py -html (Command #1)</p>

<p>If all goes well, this command should create a couple of files and folders over the current folder (example). Additionally we must create the folder "pageTemplates" inside "example" and a file "index.html" inside "pageTemplates". With this we already have the entire structure which is explained below.</p>

<ul>
	<li>"../pages": This folder contains the files that correspond to each page.</li>
	<li>"../pageTemplates": This card contains the templates that each of the pages will use.</li>
	<li>"../web": This folder contains the production files.</li>
</ul>

<p>Now we can do a couple of tests to see how it works. Open the file "../example/pageTemplates/index.html" and add the following lines:</p>

'''
<!DOCTYPE html>
<html>
	<head>
		<title>Hola Mundo !!!</title>
	</head>
	<body>
		<h1>Hola Mundo !!!</h1>
	</body>
</html>
'''