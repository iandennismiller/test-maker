# for next time

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

# administrative improvements

- the first page of the exam is a tear-off duplicate of the candidate form (also prevents students from knowing which version they have)
- infographic with t-card and scantron explains how to copy student ID: it is 9 digits, and it must match exactly or else the computer will not link your answers to your online grades.  Also explain that Last Name is family name and First Name is given name.

# there are a few rules for the exam and a few instructions for getting started

- cellphones must be turned off and stored in bags
- all bags must be placed at the front of the room
- please have your t-card ready to show the invigilator
- do not open the exam booklet until the exam begins

## even before the exam begins, you may do the following

- you may fill out the candidate form before the exam begins
- you may write your name on the answer sheet and fill in the name bubbles before the exam begins
- you may write your student ID on the answer sheet and fill in the bubbles before the exam begins

## once the exam begins:

- turn to the first page of the exam and write your name and student ID in the fields provided
- look at your exam version and write it on the top-right corner of your answer sheet (where the corner has been chopped off)

# future directions

- optical scoring of scanned PDF answer sheets
- automatic sorting of PDF answer sheets based on optical recognition of student ID.
- put the infographic be at the end of the exam.  The pre-cover page is the candidate form only.
- test receipt: the final page is blank except the unique ID number.  A custom ink stamp turns it into a receipt.  This page is removed for the student to keep as proof that they took the exam.

# exam duties

- Checker: collect the candidate forms and put them directly into a "candidate forms" envelope.  The Checker is not the same person as the Collector, because the checker creates one kind of receipt and the collector creates a different kind. The Checker waits until 30 minutes into the exam and then they ask the class if anybody still has their candidate forms. When all have been collected, the checker tells the class the envelope is being sealed, and then the envelope is sealed. Any extra candidate forms need to be logged directly on the envelope, or else it will not count because they are not physically inside the envelope.
- Collector: one person collects exams from students, ensures the version is written on the answer sheet, stamps the receipt and gives it to the student, and passes the collected materials to the counter.  Basically, they are in charge of the stamp and ink, and they are responsible for making the exam receipts.
- Counter: one person sorts the exams by version into separate piles, then keeps a tally of how many exams are in each pile.  They are responsible for the final counts of each exam version.  The tally needs to be written on a separate piece of paper (maybe generate this as a standard exam thing)

# exam materials

- bring up time remaining with http://www.online-stopwatch.com/
- candidate forms envelope
- blank scantron envelope and checkin/checkout count
- receipt stamp
- exam versions tally sheet
- testing services exam metadata sheets: bubble version and human version
- scannable answer keys for testing services
- binder clips for each test version
- a big envelope for answer sheets that will be dropped off at testing services

# audit checklist

- each student ID has a candidate form
- each student ID has an exam book
- each student ID has an answer sheet
- each student ID has an exam ID
- each exam ID has a candidate form
- each exam ID has an exam book
- each exam ID has a stamped exam receipt
- each exam ID must match an ID from the pre-generated database
- each exam ID must be unique
- the blank scantron envelope should contain the correct number of blanks
- the candidate form envelope should contain as many forms as the scantron envelope is missing
- the number of answer sheets should be equal to the number of candidate forms

# timeline

- wait until makeup exam to submit AccessAbility scantrons at the same time

# vectors for cheaters

- stealing an extra exam would enable somebody to claim a unique ID that was actually in the database, then forge a receipt using a scanner/printer or by buying a duplicate stamp.  They could claim that the candidate form, exam book, and answer sheet had all been lost by the invigilators (even though separate individuals handled the candidate forms and answer sheets, at two separate timepoints at the start and at the end of the exam).  Therefore, the only evidence the student has is the receipt; for the examiner's part, there is only evidence of the unaccountable absence of an exam.  In this case, a unique ink could be used that responded to a certain chemical test.  For example: the ink of the exam should be based on toner, and would not run when water is introduced; The ink of the stamp would run.  If the forged receipt were based on a scanned copy, then it's likely both exam and stamp inks would be produced by the same printer, and so they would not behave properly.  If a student went the extra mile to put real ink onto the original exam sheet, then perhaps security ink could have a unique and unpredictable response to a certain chemical test.  Every absence of evidence would constitute a negligence or omission on the invigilators' behalf, but proof positive of a receipt forgery is a crime of commission, and this would clearly constitute academic misconduct.  The ink could also be a distinctive color that is a custom RGB combination (that would be difficult to forge).

