from fabric.api import env, run, put, open_shell, local
import csv, random, os, string, re, sys
import jinja2
import codecs

def generate_questions():

    def UnicodeDictReader(utf8_data, **kwargs):
        csv_reader = csv.DictReader(utf8_data, **kwargs)
        for row in csv_reader:
            yield dict([(key, unicode(value, 'utf-8')) for key, value in row.iteritems()])

    env = jinja2.Environment(loader=jinja2.FileSystemLoader('.'))
    template = env.get_template('question.tex')

    with open('exam_source.csv', 'rb') as csvfile:
        spamreader = UnicodeDictReader(csvfile, quotechar='"')
        buf = u""
        rows = list(spamreader)
        random.shuffle(rows)
        for row in rows:
            choices = [
                u"\choice {0}".format(row['foil1']),
                u"\choice {0}".format(row['foil2']),
                u"\choice {0}".format(row['foil3']),
                #"\choice {0}".format(row['foil4']),
                u"\CorrectChoice {0}".format(row['correct'])
            ]
            random.shuffle(choices)
            row['question'] = re.sub(r'_+', "\underline{\hspace*{0.5in}}", row['question'])
            choices = u"\t\t" + u"\n\t\t".join(choices)
            buf += template.render(choices=choices, question=row['question'])
    return buf

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
