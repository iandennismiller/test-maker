# Notes

## for next time

- source.csv has a column called "reference" that contains "Ch. X, p. X" or "Lecture X"
- source column is revealed on answer key
- answer key contains question IDs that map question back to original spreadsheet items
- student ID box includes individual boxes for individual numbers (XXX-XXX-XXX)
- generate "pristine" unrandomized version of exam
- generate "version mappings" that contort the pristin exam into the various exam versions
- based on version mappings, export the answer key as a vector that can be compared in Excel
- version mappings can be used to reliably generate .tex and .pdf files from scratch
- "annotated key" could include answer distribution information for that question item (maybe)
- based on auto-generated answer key, perform offline marking in the .xls provided by testing services
- compute per-item (between-version) stats (ditch the item-per-version stats created by testing services)
- each exam version is a single long PDF.
- Each individual exam has a unique ID that appears on both the candidate form and the cover page of the exam
- start sorting exams, versions, keys, scantrons, pdfs, blah in modular exam-packs

## administrative improvements

- the first page of the exam is a tear-off duplicate of the candidate form (also prevents students from knowing which version they have)
- infographic with t-card and scantron explains how to copy student ID: it is 9 digits, and it must match exactly or else the computer will not link your answers to your online grades.  Also explain that Last Name is family name and First Name is given name.
