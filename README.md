**Excuses:** ___I apologize for the English used, my language is Spanish.___

# Process Python #

## Content ##

1. [Introduction.](#Introduction "Introduction")
2. [Dependencies.](#Dependencies "Dependencies")
3. [The process html.](#TheProcessHtml "The process html")
4. [The process sql.](#TheProcessSql "The process sql")

<span id="Introduction"></span>
## Introduction ##

This project aims to automate repetitive processes or patterns, using the great Python programming language.

<span id="Dependencies"></span>
## Dependencies ##

- Python (https://www.python.org): Download Python and add it to the path of your operating system.

<span id="TheProcessHtml"></span>
## The process html ##

This command will allow you to create HTML files from others files.

Suppose you downloaded the "processpy" files in the "D:/proyectos/python/processpy/" path and created an "example" folder in the "D:/proyectos/python/example" path. Now you must open a console of your operating system (in this case windows), stand on the "example" folder and run the following command:

**python D:/proyectos/python/processpy/process.py -html (Command #1)**

If all goes well, this command should create a couple of files and folders over the current folder (example). Additionally we must create the folder "pageTemplates" inside "example" and a file "index.html" inside "pageTemplates". With this we already have the entire structure which is explained below.

- "../pages": This folder contains the files that correspond to each page.
- "../pageTemplates": This folder contains the templates that each of the pages will use.
- "../web": This folder contains the production files.

Now we can do a couple of tests to see how it works. Open the file "../example/pageTemplates/index.html" and add the following lines:

**File: ../example/pageTemplates/index.html**

~~~
<!DOCTYPE html>
<html lang="en">
  <head>
    <!--headHTML-->
  </head>
  <body>
    <!--bodyHTML-->
  </body>
</html>
~~~

As you can see we have common and current HTML tags except for "'<!--headHTML-->'" and "'<!--bodyHTML-->'", which we will explain next. But first check the file "../example/web/index.html" and you will see that it is empty, run Command #1 again and check this same file again, if everything goes well, you will see how the code has been copied from the template to the production file.

Now the tags "'<!--headHTML-->'" and "'<!--bodyHTML-->'" tell the template that the tags are in the files "../example/pages/head.html" and "../example/pages/body.html" and to be added respectively. Knowing this, we will modify the following files:

**File: ../example/pages/head.html**

~~~
<title>My Page</title>
~~~

**File: ../example/pages/body.html**

~~~
<h1>Hello World!!!</h1>
~~~

We execute Command #1 repeatedly and if everything goes well, the changes will be detected in the production file "../example/web/index.html".

With all of the above we already know how this command works in general. Now we are going to create a new folder called "page2" in the directory "../example/pages/" and we will execute Command #1 again, this automatically creates two new files inside the new folder, which we will modify like this:

**File: ../example/pages/page2/head.html**

~~~
<title>This is my page number 2.</title>
<script>
	console.log('Hello World!!!');
</script>
~~~

**File: ../example/pages/page2/body.html**

~~~
<h1>Hello, this is my page number 2.</h1>
~~~

Now you can run Command #1 again and if everything goes well you can check the production path "../example/web/", where you can now find two pages with different contents.

Last but not least, we will create a new template. In the path "../example/pageTemplates/" we will add a new file called "temp2.html", which will be a new template and will contain the following tags:

**File: ../example/pageTemplates/temp2.html**

~~~
<!DOCTYPE html>
<html lang="en">
  <head>
    <!--headHTML-->
  </head>
  <body>
  	<div style="background-color: blue; color: white;">
  		<!--bodyHTML-->
  	</div>
  </body>
</html>
~~~

If you don't specify a template for each page you create, Command # 1 defaults to the template "../example/pageTemplates/index.html", but if you want the template "temp2.html" to be taken for the page "page2", the following should be added in the first line of the file "../example/pages/page2/head.html".

**File: ../example/pages/page2/head.html**

~~~
<!--Route: temp2.html-->
<title>This is my page number 2.</title>
<script>
	console.log('Hello World!!!');
</script>
~~~

See how the first line indicates "'<!--Route: temp2.html-->'", which tells this page which template to use, which in this case is "temp2.html". Now we run Command #1 for the last time and if all goes well, we will have two pages using two different templates.

<span id="TheProcessSql"></span>
## The process sql ##

This command allows you to take all the ".sql" files in a folder and convert them into one file.

Suppose you downloaded the "processpy" files in the "D:/proyectos/python/processpy/" path and created an "example" folder in the "D:/proyectos/python/example" path. Now we will create a folder that we will call "sql", which will be in the path "../example/" and will contain the files you want with the extension ".sql".

Everything is ready to execute the following command in which "(FILE)" is the final file that contains all the lines of the other files and "(SQL_FILE_PATH)" is the path of the ".sql" files.

**python D:/proyectos/python/processpy/process.py -sql (FILE) (SQL_FILE_PATH) (Command #2)**

For this example, the command would look like this:

**python D:/proyectos/python/processpy/process.py -sql D:/proyectos/python/example/myfile.sql D:/proyectos/python/example/sql**

If all goes well, you will have a file named "myfile.sql" in the path "D:/proyectos/python/example/", which will contain all the lines of all the files that are in the "sql" folder.