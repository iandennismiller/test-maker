# -*- coding: utf-8 -*-

import csv, random, os, json
from Version import TestVersion

def UnicodeDictReader(utf8_data, **kwargs):
    csv_reader = csv.DictReader(utf8_data, **kwargs)
    for row in csv_reader:
        yield dict([(key, unicode(value, 'utf-8')) for key, value in row.iteritems()])

class TestMaker(object):
    def __init__(self, filename):
        with open(filename) as f:
            self.cfg = json.load(f)
        self.questions = list()

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

    def create_version(self):
        num_questions = len(self.questions)
        num_options = 4
        mapping = []
        for i in range(0, num_questions):
            choices = range(0, num_options)
            random.shuffle(choices)
            mapping.append(choices)
        numbers = range(0, 50)
        random.shuffle(numbers)
        return zip(numbers, mapping)

    def create_all_versions(self):
        answer_options = ['a', 'b', 'c', 'd']
        answer_file = self.get_filename(os.path.join(self.cfg["output_path"], "key.txt"))
        with open(answer_file, "w") as answers:
            for version in self.cfg['versions']:
                filename = os.path.join(self.cfg["version_path"], "%s.json" % version)
                filename = self.get_filename(filename)
                with open(filename, "wb") as f:
                    mapping = self.create_version()
                    json.dump(mapping, f, indent=4)
                correct_answers = []
                for item in mapping:
                    # which one is the 0?
                    correct_answers.append(answer_options[item[1].index(0)])
                    if not (len(correct_answers)+1) % 6:
                        correct_answers.append("/")
                buf = "%s\n\n" % version + " ".join(correct_answers) + "\n\n"
                answers.write(buf)

    def render_version(self, version):
        v = TestVersion(self, version, key=True)
        v.render()
        v = TestVersion(self, version, key=False)
        v.render()

    def render_all_versions(self):
        for version in self.cfg["versions"]:
            self.render_version(version)
