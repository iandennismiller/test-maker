# -*- coding: utf-8 -*-

import csv, random, os, string, re, sys, json
import jinja2
import codecs

class TestVersion(object):
    def __init__(self, testmaker, version_name, key=False):
        self.version = version_name
        self.tm = testmaker
        self.key = key

        loader = jinja2.FileSystemLoader(self.tm.get_filename(self.tm.cfg["template_path"]))
        self.jinja = jinja2.Environment(loader=loader)

        self.mapping = self.get_mapping()

    def get_mapping(self):
        filename = os.path.join(self.tm.cfg["version_path"], "%s.json" % self.version)
        filename = self.tm.get_filename(filename)
        with open(filename, "r") as f:
            mapping = json.load(f)
        return mapping

    def render_question(self, question, mapping):
        template = self.jinja.get_template(self.tm.cfg["templates"]["question"])
        choices = [
            u"\CorrectChoice {0}".format(question['correct']),
            u"\choice {0}".format(question['foil1']),
            u"\choice {0}".format(question['foil2']),
            u"\choice {0}".format(question['foil3']),
        ]
        
        # place the choices in the order specified by the mapping
        arranged = [
            choices[mapping[0]],
            choices[mapping[1]],
            choices[mapping[2]],
            choices[mapping[3]],
        ]

        source = '\\textbf{(Source: %s)}' % question['source']
        # here replace ___ with TeX underlines
        question_str = re.sub(r'_+', "\underline{\hspace*{0.5in}}", question['question'])
        arranged = u"\t\t" + u"\n\t\t".join(arranged)
        return template.render(choices=arranged, question=question_str, source=source)

    def render(self):
        questions = u""
        for (original, mapping) in self.mapping:
            question = self.tm.questions[original]
            questions += self.render_question(question, mapping)

        template = self.jinja.get_template('exam.tex')
        assets_latex = '\graphicspath{{%s/}}' % self.tm.get_filename(self.tm.cfg["assets_path"])

        if self.key:
            outfile_tex = os.path.join(self.tm.cfg["output_path"], "%s KEY.tex" % self.version)
        else:
            outfile_tex = os.path.join(self.tm.cfg["output_path"], "%s.tex" % self.version)
        outfile_tex = self.tm.get_filename(outfile_tex)
        with codecs.open(outfile_tex, 'w', encoding="utf-8") as texfile:
            if self.key:
                rendered = template.render(questions=questions, version="%s KEY" % self.version, answers="answers,", assets_path=assets_latex)
            else:
                rendered = template.render(questions=questions, version=self.version, answers="", assets_path=assets_latex)
            texfile.write(rendered)

        cmd = "pdflatex -output-directory=%s '%s'" % \
            (self.tm.get_filename(self.tm.cfg["output_path"]), outfile_tex)
        os.system(cmd)

