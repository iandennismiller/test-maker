# Test-Maker

## Pre-requisites

- OS X, Linux, or [Cygwin](http://cygwin.com/)
- LaTeX ([for mac](http://www.tug.org/mactex/) or [for Windows/Linux](http://www.tug.org/texlive/acquire-netinstall.html))
- [Python 2.7.x](https://www.python.org/downloads/)
- [Python 2.7.x source code](https://www.python.org/downloads/source/) (i.e. Python.h)
- Python [virtualenv](https://pypi.python.org/pypi/virtualenv)
- Python [virtualenvwrapper](https://pypi.python.org/pypi/virtualenvwrapper)
- Python [pip](https://pypi.python.org/pypi/pip)
- [Git](http://git-scm.com/)

### OS X pre-requisites installation using [Homebrew](http://brew.sh/)

    brew install python git
    pip install virtualenv virtualenvwrapper

Finally, install [MacTeX](http://www.tug.org/mactex/).

## Test-Maker Installation Process

Before you can generate an exam, you must install the Test-Maker libraries and scripts.  Afterwards, you can generate as many exams as you want.  The installation process assumes:

- you have already installed the pre-requisites
- you are installing the Test-Maker in your User Library path (`~/Library`)

First, download the source code.

    cd ~/Library
    git clone https://github.com/iandennismiller/test-maker.git
    cd test-maker

Create a Python virtual environment and install the Test-Maker.

    mkvirtualenv -a test-maker
    make install

## Creating an Exam

Now that Test-Maker is installed, it is possible to generate new exams using the Test-Maker *scaffold*.  A *scaffold* is a template that can be customized with values that make it into your own exam.

Let's create an exam with the following parameters:

- you store all your exams in your Documents folder
- you are creating an exam for the course number *EDU100*
- this exam is the final exam for the Spring 2015 semester

The following shell commands will create the exam:

    workon test-maker
    cdproject
    mrbob scaffold -w -O ~/Documents/EDU100-2015-Spring-Final

## Customizing your Exam

In the following example, an exam is created with the following parameters:

- there are two sources of questions: book and lecture
- there are five exam versions: A, B, C, and two makeup versions
- the Exam files are stored in */Users/idm/Documents/EDU100-2015-Spring-Final*
- the output PDF filenanes will start with "EDU100 - Spring 2015 - Final Exam"

The following config file (**config.json**) will render an exam with those parameters. Most of the other settings are sensible defaults that probably won't change unless you need to do something exotic.

    {
        "root_path": "/Users/idm/Documents/EDU100-2015-Spring-Final",
        "assets_path": "assets",
        "questions": [
            "questions/lecture.csv",
            "questions/book.csv"
        ],
        "template_path": "templates",
        "templates": {
            "question": "question.tex",
            "exam": "exam.tex"
        },
        "versions": [
            "A",
            "B",
            "C",
            "Makeup A",
            "Makeup B"
        ],
        "version_path": "output/versions",
        "build_path": ".build",
        "output_path": "output",
        "filename_prefix": "EDU100 - Spring 2015 - Final Exam - Version"
    }

### Writing questions for the Exam

The questions, along with answer choices, are contained within Comman Separated Value files (.CSV) that are in the `questions` subdirectory of your exam.  Edit these files with a spreadsheet editor, like Excel or LibreOffice.  For boldface and italics, use the LaTeX commands \textit{} and \textbf{}.  For example, to boldface the "not" in a question prompt:

    Which of the following is \testbf{not} the correct answer:

### Customizing the templates

You probably need to edit `exam.tex` in order to make the Exam match your School's standards.  By following the examples in the `exam.tex` file, you will be able to add your own image logo and create your own instructions.

## Making the Exam PDFs

This is the easiest part.  Ensure you are using the Python virtual environment, switch to your Exam folder, and issue the `make` command.

    workon test-maker
    cd ~/Documents/EDU100-2015-Spring-Final
    make

## Administering the Exam

The end result is that a bunch of PDFs now exist in the output path (`~/Documents/EDU100-2015-Spring-Final/output`).  There are several files that help with test administration:

- exam PDFs for mass duplication
- "Answer Key" PDFs with the answers highlighted for post-exam viewings
- `key.txt`, which is the master key that is used to create optical scan answer keys.
