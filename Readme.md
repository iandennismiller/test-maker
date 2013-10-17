# Installation

Just download the repo and install it globally.

    git clone https://github.com/iandennismiller/test-maker.git
    cd test-maker
    make install

# Usage

Once installed, each exam will sit in its own folder.  Start by copying the `skel` directory.

    workon mrbob
    mrbob ~/Work/test-maker/skel-mrbob -O {{{ project_path }}}

### config file

Edit config file (config.json) that will control how your exam is built.

    {
        "root_path": "/tmp/new-exam",
        "assets_path": "assets",
        "questions": [
            "questions/source1.csv",
            "questions/source2.csv"
        ],
        "template_path": "templates",
        "templates": {
            "question": "question.tex",
            "exam": "exam.tex"
        },
        "versions": [
            "Version A",
            "Version B",
            "Version C",
            "Makeup Version A",
            "Makeup Version B"
        ],
        "version_path": "versions",
        "output_path": "output"
    }

### running it

    make

# Conclusion

The end result is that a bunch of PDFs now exist, along with the key for marking the exam.
