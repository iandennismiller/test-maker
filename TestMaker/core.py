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
            questionreader = UnicodeDictReader(csvfile, quotechar='"')
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
            filename = os.path.join(self.cfg["output_path"], "%s.json" % version)
            filename = self.get_filename(filename)
            with open(filename, "wb") as f:
                json.dump(self.make_version(), f)

    def render_question(self, question, mapping):
        template = self.jinja.get_template(self.cfg["templates"]["question"])
        choices = [
            u"\choice {0}".format(question['foil1']),
            u"\choice {0}".format(question['foil2']),
            u"\choice {0}".format(question['foil3']),
            u"\CorrectChoice {0}".format(question['correct'])
        ]
        # here replace ___ with TeX underlines
        question = re.sub(r'_+', "\underline{\hspace*{0.5in}}", question['question'])
        # here shuffle the questions according to the mapping
        choices = u"\t\t" + u"\n\t\t".join(choices)
        return template.render(choices=choices, question=question)

    def get_version_mapping(self, version):
        filename = os.path.join(self.cfg["version_path"], "%s.json" % version)
        filename = self.get_filename(filename)
        with open(filename, "r") as f:
            mapping = json.load(f)
        return mapping

    def render_choices(self, version, version_mapping):
        buf = u""
        this_version = self.questions
        # here, another level of randomization: all the questions orders
        #random.shuffle(this_version)
        for (question, mapping) in zip(this_version, version_mapping):
            buf += self.render_question(question, mapping)
        return buf

    def render_versions(self):
        for version in self.cfg["versions"]:
            self.render_version(version)

    def render_exam(self, choices, template, version, key=False):
        outfile_tex = os.path.join(self.cfg["output_path"], "%s.tex" % version)
        outfile_tex = self.get_filename(outfile_tex)
        assets_latex = '\graphicspath{{%s/}}' % self.get_filename(self.cfg["assets_path"])
        with codecs.open(outfile_tex, 'w', encoding="utf-8") as texfile:
            if key:
                rendered = template.render(questions=choices, version="%s KEY" % version, answers="answers,", assets_path=assets_latex)
            else:
                rendered = template.render(questions=choices, version=version, answers="", assets_path=assets_latex)
            texfile.write(rendered)
        cmd = "pdflatex -output-directory=%s '%s'" % \
            (self.get_filename(self.cfg["output_path"]), outfile_tex)
        print(cmd)
        os.system(cmd)

    def render_version(self, version):
        answer_choices = self.get_version_mapping(version)
        buf = self.render_choices(version, answer_choices)
        template = self.jinja.get_template('exam.tex')
        #self.render_exam(buf, template, version, key=False)
        self.render_exam(buf, template, version, key=True)
