# Setting Your Python Stack

Below you can find the tools we'll use throughout the semester to work with Python. To complete exercise #1 you only have
to compelete Task number 1 - "Python Setup". In the second week of the semester I'll show in class how to install
the rest of the tools listed, so you should feel perfectly comfortable with postponing Tasks 2-4 till the second
week of the semester.

## Task 1: Python Setup
1. In the course we'll use Python 3.6. The easiest way to install Python is via 
Anaconda, a popular Python distribution. We'll get to know Anaconda throughout
the course.
2. Download __Miniconda__ from [here](https://conda.io/miniconda.html), for Python 3.6.
3. Setup a new Python environment with the following command: 
`conda create --name my_env python=3.6` (you can change the environment name)
4. Environments are important, since they allow you isolate each project you work on
while increasing reproducibility.
5. After creating the environment activate it by writing in the command line `activate my_env`. 
in Mac\Linux, write `source activate my_env`. 

## Task 2: Editor setup
1. You can write Python code in any text editor, including Notepad, although some
editors are better than others.
2. The three main options are:
    - Spyder
    - PyCharm
    - Visual Studio Code
    - Jupyter Notebook (seen in class)
3. Generally, either PyCharm or Visual Studio Code are the preferred options. Installing
them is pretty straight forward, and we'll discuss the installation process and other considerations for choosing
 one or the other in class #2.
3. If you insist of the familiar MATLAB interface activate your new environment
 and write `conda install spyder` in the command line. Run Spyder by writing
 `spyder` in the command line. Then open the Window menu, and in the window layout submenu 
 choose "MATLAB".

## Task 3: Version Control
Scripts are saved and catalogued using version control. The application we'll use this semester is called `git`, and
as a web interface we'll use GitHub.com. Exercise 1 contains explanations on how to setup version control on
your system.

## Task 4: Jupyter Notebook
The classes are posted in an editable Jupyter Notebook format, which allows for online coding and easy code presentation.
It's also a great tool for "quick-and-dirty" data analyses. Thus I recommend you to install it and use it throughout the semester,
and beyond.

1. Activate your Python environment using `activate my_env`. As always, on Mac\Linux write `source activate my_env`.
2. Write `conda install jupyter notebook`.
3. The notebook is installed! Run it with a simple `jupyter notebook` command. It will open a file browser which you can
use to navigate to the folder containing existing notebooks, or to the folder in which you wish to create a new one.


