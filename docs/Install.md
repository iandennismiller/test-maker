# Test-Maker Installation

Test-Maker is a tool for creating perfect Multiple Choice exams with multiple versions.

## Test-Maker Installation Process

Before you can generate an exam, you must install the Test-Maker libraries and scripts.  Afterwards, you can generate as many exams as you want.  The installation process assumes:

- you have already installed the [pre-requisites](https://github.com/iandennismiller/test-maker/blob/master/docs/Install.md#pre-requisites)
- you are installing the Test-Maker in your User Library path (`~/Library`)

First, download the source code from the Project website on GitHub.

    cd ~/Library
    git clone https://github.com/iandennismiller/test-maker.git
    cd test-maker

Create a Python virtual environment and install the Test-Maker.

    mkvirtualenv -a test-maker
    make install

Now Test-Maker is installed.

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

