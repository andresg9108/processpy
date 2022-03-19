**Excuses:** ___I apologize for the English used, my language is Spanish.___

# Process Python #

## Content ##

1. [Introduction.](#Introduction "Introduction")
2. [Dependencies.](#Dependencies "Dependencies")
3. [Getting started.](#GettingStarted "Getting started")
4. [The process html.](#TheProcessHtml "The process html")
5. [The process sql.](#TheProcessSql "The process sql")
6. [Replace text string.](#ReplaceTextString "Replace text string")
7. [Calendar.](#Calendar "Calendar")

## Introduction <span name="Introduction"></span> ##

This project aims to automate repetitive processes or patterns using the great Python programming language.

## Dependencies <span name="Dependencies"></span> ##

- Node.js (https://nodejs.org).
- Python (https://www.python.org): Download Python and add it to the path of your operating system.

## Getting started <span name="GettingStarted"></span> ##

We will start by installing the processpy package in the folder where we want to use it as follows.

~~~
npm i processpy
~~~

If all goes well now we can use processpy.

~~~
python node_modules/processpy/process.py -help
~~~

## The process html <span name="TheProcessHtml"></span> ##

This command will allow you to create HTML files from other files. To do this we have the following command.

**Command #1**
~~~
python node_modules/processpy/process.py -html
~~~

This command should create a couple of files and folders on top of the current folder and with this we already have the structure that is explained below.

- "./pages": This folder contains the files that correspond to each page.
- "./pageTemplates": This folder contains the templates that each of the pages will use.
- "./web": This folder contains the production files.

Now we can do a couple of tests to see how it works. Open the file "./pageTemplates/index.html" and add the following lines.

**File: ./pageTemplates/index.html**

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <!--headHTML-->
  </head>
  <body>
    <!--bodyHTML-->
  </body>
</html>
```

As you can see, we have common HTML tags except for "&lt;!&#45;&#45;headHTML&#45;&#45;&gt;" and "&lt;!&#45;&#45;bodyHTML&#45;&#45;&gt;" which we will explain below. But first check the file "./web/index.html" and you will see that it is empty, execute Command # 1 again and check this same file again, if all goes well, you will see how the code has been copied from the template to the production file.

* "&lt;!&#45;&#45;headHTML&#45;&#45;&gt;": You can use this statement so that the unique HTML tags in the page header appear instead when the production files are updated.
* "&lt;!&#45;&#45;bodyHTML&#45;&#45;&gt;": You can use this statement so that the unique HTML tags in the page body appear instead when the production files are updated.

The following tags can also be used.

* "&lt;&lt;ROOT-DIR&gt;&gt;": You can use this declaration so that when the production files are updated, the project root appears instead. So if you put "&lt;&lt;ROOT-DIR&gt;&gt;src/example/main.min.js", something like "../../src/example/main.min.js" will appearaccording to the location in the folder tree.
* "&lt;&lt;DIR&gt;&gt;": This tag does the same as the previous one but places the path one level lower in the file tree.

Understanding the above, we can make the following modification.

**File: ./pages/head.html**

```html
<title>My Page</title>
```

**File: ./pages/body.html**

```html
<h1>Hello World!!!</h1>
```

We execute Command # 1 again and all changes will be detected in the production file "./web/index.html".

With all of the above we already know how this command works in general. Now we are going to create a new folder called "page2" in the directory "./pages/" and we will execute Command #1 again, this automatically creates two new files inside the new folder which we will modify like this.

**File: ./pages/page2/head.html**

```html
<title>This is my page number 2.</title>
<script>
  console.log('Hello World!!!');
</script>
```

**File: ./pages/page2/body.html**

```html
<h1>Hello, this is my page number 2.</h1>
```

Now you can run Command #1 again and if everything goes well you can check the production path "./web/", where you can now find two pages with different contents.

Last but not least, we will create a new template. In the path "./pageTemplates/" we will add a new file called "temp2.html" which will be a new template and will contain the following tags.

**File: ./pageTemplates/temp2.html**

```html
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
```

If you don't specify a template for each page you create, Command #1 defaults to the template "./pageTemplates/index.html", but if you want the template "temp2.html" to be taken for the page "page2" the following should be added in the first line of the file "./pages/page2/head.html".

**File: ./pages/page2/head.html**

```html
<!--Route: temp2.html-->
<title>This is my page number 2.</title>
<script>
  console.log('Hello World!!!');
</script>
```

See how the first line ("&lt;!&#45;&#45;Route: temp2.html&#45;&#45;&gt;") tells this page which template to use and in this case it is "temp2.html". Now we execute Command #1 for the last time and if all goes well we will have two pages using two different templates.

## The process sql <span name="TheProcessSql"></span> ##

This command allows you to take all the ".sql" files in a folder and convert them into one file.

For this example, we will create a new separate directory, install "processpy" for it, and create a folder called "sql" that will contain the files you want with the extension ".sql".

Everything is ready to execute the following command in which "(FILE)" is the final file that contains all the lines of the other files and "(SQL_FILE_PATH)" is the path of the ".sql" files.

**Command #2**

~~~
python node_modules/processpy/process.py -sql (FILE) (SQL_FILE_PATH)
~~~

For this example, the command would look like this.

~~~
python node_modules/processpy/process.py -sql ./myfile.sql ./sql
~~~

If all goes well, you will have a file called "myfile.sql" in the current path that will contain all the lines of all the files that are in the "sql" folder.

## Replace text string <span name="ReplaceTextString"></span> ##

This command will allow you to replace a text string in all files in a directory.

For this example, we will create a new separate directory, install "processpy" for it, and create a folder called "data" that will contain the files we want and include in them the line of text we want to modify.

Everything is ready to execute the following command in which "(FOLDER)" is the directory that contains the files that we want to modify, "(SEARCH)" is the text string that we want to modify and "(REPLACE)" is the new string of text to be added where the previous one was.

**Command #3**

~~~
python node_modules/processpy/process.py -rts (FOLDER) (SEARCH) (REPLACE)
~~~

For this example, the command would look like this.

~~~
python node_modules/processpy/process.py -rts ./data "Old string" "New string"
~~~

If all goes well, the text string will be replaced in all files in the folder.

## Calendar <span name="Calendar"></span> ##

This command will allow us to print a calendar by console defining the month and the year.

For this example, we will create a new separate directory and install "processpy" to it. Now we can execute the following command in which "(DATE)" is a text string that will contain the year and month that we want to print on the console, the string will have the following syntax "2022-03", in this case it should print the month of March 2022.

**Command #4**

~~~
python node_modules/processpy/process.py -cal (DATE)
~~~

For this example, the command would look like this.

~~~
python node_modules/processpy/process.py -cal '2022-03'
~~~

If you run the command without including the text string as shown below, it should print the current month to the console.

~~~
python node_modules/processpy/process.py -cal
~~~