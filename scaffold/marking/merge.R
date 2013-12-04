# start from scratch
try(clean_env(),TRUE)

library(gdata)
source("marking_helpers.R")

# Stage 0: import the scantron results and the blackboard grade center "offline work" spreadsheet
blackboard = read.delim("blackboard/download.xls", fileEncoding = "UTF-16")
version_a = read.xls("scantron/blah_1.xls")
version_b = read.xls("scantron/blah_2.xls")
version_c = read.xls("scantron/blah_3.xls")

# Stage 1: correct any errors in the exam (such as refunding points for bad questions)
# This must be applied on a per-version basis, because the questions will be different

# Stage 2: combine the versions
scantrons = rbind(version_a, version_b, version_c)

# Stage 3: evaluate the scantron input and set "column_to_replace" and "unique_colnames" below
evaluate(scantrons, blackboard)

# which column number on blackboard needs to be replaced with scantron results?
column_to_replace = 10

# what are the names of the blackboard columns that need to be saved?
unique_colnames = c(
  "Weighted Total [Total Pts: up to 0] |982704",
  "Total [Total Pts: up to 50] |982703",
  "Midterm [Total Pts: 50] |1066282",
  "Final Exam [Total Pts: 50] |1079856",
  "Term Paper [Total Pts: 100] |1079857"
)

# Stage 4: correct student ID entry errors
scantrons = fix_id(scantrons, old_id = 0000, new_id = 00000)

# Stage 5: merge the scantron results, replace the proper column, and export
to_export = merge_exam(scantrons, blackboard, column_to_replace)
export_exam(to_export, unique_colnames)
