# -*- coding: utf-8 -*-

import os, re, json, codecs
import jinja2

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

        # here replace ___ with TeX underlines
        question_str = re.sub(r'_+', "\underline{\hspace*{0.5in}}", question['question'])
        arranged = u"\t\t" + u"\n\t\t".join(arranged)
        if self.key:
            source = '\\textit{(%s)}' % question['source']
            return template.render(choices=arranged, question=question_str, source=source)
        else:
            return template.render(choices=arranged, question=question_str, source="")

    def render(self):
        questions = u""
        for (original, mapping) in self.mapping:
            question = self.tm.questions[original]
            questions += self.render_question(question, mapping)

        template = self.jinja.get_template('exam.tex')
        assets_latex = '\graphicspath{{%s/}}' % self.tm.get_filename(self.tm.cfg["assets_path"])

        if self.key:
            tex_filename = "%s KEY.tex" % self.version
            version_presentation = "%s KEY" % self.version
            answers = "answers,"
        else:
            tex_filename = "%s.tex" % self.version
            version_presentation = self.version
            answers = ""

        outfile_tex = os.path.join(self.tm.cfg["output_path"], tex_filename)
        outfile_tex = self.tm.get_filename(outfile_tex)
        with codecs.open(outfile_tex, 'w', encoding="utf-8") as texfile:
            rendered = template.render(
                questions=questions, 
                version=version_presentation, 
                answers=answers, 
                assets_path=assets_latex
                )
            texfile.write(rendered)

        cmd = "pdflatex -output-directory=%s '%s'" % \
            (self.tm.get_filename(self.tm.cfg["output_path"]), outfile_tex)
        os.system(cmd)
