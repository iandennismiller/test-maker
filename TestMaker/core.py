# -*- coding: utf-8 -*-

import csv, random, os, string, re, sys, json
import jinja2
import codecs
from optparse import OptionParser

class TestMaker(object):
    def __init__(self, filename=None):
        if filename:
            with open(filename) as f:
                self.cfg = json.load(f)
        else:
            parser = OptionParser()
            parser.add_option('-c', "--config", dest="cfg_file", help="configuration file")
            (options, args) = parser.parse_args()

            if options.cfg_file:
                with open(options.cfg_file) as f:
                    self.cfg = json.load(f)
            else:
                print "--config is a required option"
                sys.exit()

        self.questions = list()
        loader = jinja2.FileSystemLoader(self.get_filename(self.cfg["template_path"]))
        self.jinja = jinja2.Environment(loader=loader)

    def get_filename(self, bare_filename):
        if "root_path" in self.cfg:
            return os.path.join(self.cfg["root_path"], bare_filename)
        else:
            return bare_filename

    def load_question_file(self, filename):
        with open(filename, 'rb') as csvfile:
            questionreader = csv.DictReader(csvfile, quotechar='"')
            rows = list(questionreader)
        self.questions += rows

    def load_questions(self):
        for filename in self.cfg["questions"]:
            self.load_question_file(self.get_filename(filename))

    def make_version(self):
        num_questions = len(self.questions)
        num_options = 4
        mapping = []
        for i in range(0, num_questions):
            choices = range(0, num_options)
            random.shuffle(choices)
            mapping.append(choices)
        return mapping

    def make_versions(self):
        for version in self.cfg['versions']:
            filename = os.path.join(self.cfg["version_path"], "%s.json" % version)
            filename = self.get_filename(filename)
            with open(filename, "wb") as f:
                json.dump(self.make_version(), f)

    def render_question(self, question):
        template = self.jinja.get_template(self.cfg["templates"]["question"])
        print question

        choices = [
            u"\choice {0}".format(question['foil1']),
            u"\choice {0}".format(question['foil2']),
            u"\choice {0}".format(question['foil3']),
            u"\CorrectChoice {0}".format(question['correct'])
        ]
        # here replace ___ with TeX underlines
        question = re.sub(r'_+', "\underline{\hspace*{0.5in}}", question['question'])
        choices = u"\t\t" + u"\n\t\t".join(choices)
        return template.render(choices=choices, question=question)

    def render_questions(self):
        buf = u""
        for question in self.questions:
            buf += self.render_question(question)
        return buf

def generate_questions():

    env = jinja2.Environment(loader=jinja2.FileSystemLoader('.'))
    template = env.get_template('question.tex')


def generate_version(version, early=False):
    env = jinja2.Environment(loader=jinja2.FileSystemLoader('.'))
    template = env.get_template('exam_template.tex')

    buf = generate_questions()

    with codecs.open('latex/exam_%s_key.tex' % version, 'w', encoding="utf-8") as texfile:
        rendered = template.render(questions=buf, version="%s KEY" % version, answers="answers,")
        texfile.write(rendered)
    os.system("pdflatex -output-directory=latex %s" % 'latex/exam_%s_key.tex' % version)

    if early:
        sys.exit()

    with codecs.open('latex/exam_%s.tex' % version, 'w', encoding="utf-8") as texfile:
        rendered = template.render(questions=buf, version=version, answers="")
        texfile.write(rendered)
    os.system("pdflatex -output-directory=latex %s" % 'latex/exam_%s.tex' % version)

def exam():
    generate_version("A")
    generate_version("B")
    os.system("rm latex/exam_*.aux latex/exam_*.log")
    os.system("mv latex/exam_*.pdf exams")

def one():
    generate_version("A", early=True)
