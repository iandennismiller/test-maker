# -*- coding: utf-8 -*-

import csv, random, os, string, re, sys, json
import jinja2
import codecs
from optparse import OptionParser

def UnicodeDictReader(utf8_data, **kwargs):
    csv_reader = csv.DictReader(utf8_data, **kwargs)
    for row in csv_reader:
        yield dict([(key, unicode(value, 'utf-8')) for key, value in row.iteritems()])

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

        self.questions = []

    def load_question_file(self, filename):
        with open(filename, 'rb') as csvfile:
            spamreader = UnicodeDictReader(csvfile, quotechar='"')
            rows = list(spamreader)
            self.questions.append(rows)

    def load_questions(self):
        for filename in self.cfg.questions:
            self.load_question_file(filename)

    def render_questions(self):
        for row in rows:
            choices = [
                u"\choice {0}".format(row['foil1']),
                u"\choice {0}".format(row['foil2']),
                u"\choice {0}".format(row['foil3']),
                #"\choice {0}".format(row['foil4']),
                u"\CorrectChoice {0}".format(row['correct'])
            ]
            row['question'] = re.sub(r'_+', "\underline{\hspace*{0.5in}}", row['question'])
            choices = u"\t\t" + u"\n\t\t".join(choices)
            buf += template.render(choices=choices, question=row['question'])
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
