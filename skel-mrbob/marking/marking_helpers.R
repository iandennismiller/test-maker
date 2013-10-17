clean_env = function() {
  items = ls(envir=.GlobalEnv)
  filter = 'clean_env|make'
  filtered = items[grep(filter, items, invert=TRUE)]
  rm(list=filtered, envir=.GlobalEnv)
}

find_student = function(student_id, scantrons, blackboard) {
  first_name = as.character(scantrons[scantrons[["ID"]]==student_id,"First.Name"])
  last_name = as.character(scantrons[scantrons[["ID"]]==student_id,"Last.Name"])
  found = blackboard[toupper(blackboard[["Last.Name"]])==last_name,]
  return(c(last_name, first_name, found[["Student.ID"]]))
}

find_entry_errors = function(scantrons, blackboard) {
  entered_ids = scantrons[["ID"]]
  not_found = entered_ids[!is.element(entered_ids, blackboard[["Student.ID"]])]
  for (student_id in not_found) {
    cat(student_id, find_student(student_id, scantrons, blackboard), "\n")
  }
}

fix_id = function(scantrons, old_id, new_id) {
  scantrons[scantrons[["ID"]]==old_id,"ID"] = new_id
  return(scantrons)
}

merge_exam = function(scantrons, blackboard, column_to_replace) {
  id_and_score = subset(scantrons, select=c(ID, Total.Score))
  names(id_and_score)[1] = "Student.ID"
  
  merged <- merge(blackboard, id_and_score, by="Student.ID", all=T)
  merged = with(merged, {
    merged[order(Last.Name, First.Name),]
  })

  blackboard[column_to_replace] = merged[dim(merged)[2]]
  return(blackboard)
}

export_exam = function(to_export, unique_colnames) {
  blackboard_colnames = c(
    "Last Name",
    "First Name",
    "Username",
    "Student ID",
    "Last Access",
    "Availability"
  )
  
  write.table(to_export, 
              file="blackboard/temp-utf8.csv", 
              sep="\t", 
              quote=TRUE,
              na="",
              row.names=F, 
              col.names=c(blackboard_colnames, unique_colnames),
              fileEncoding = "UTF-8")
  
  cat('\xFF\xFE', file = (con <- file("blackboard/upload.csv", "w"))); close(con)
  system("iconv -f UTF-8 -t UTF-16LE blackboard/temp-utf8.csv >> blackboard/upload.csv && rm blackboard/temp-utf8.csv")
}

evaluate = function(scantrons, blackboard) {
  # figure out who entered a student ID that is not in the spreadsheet from blackboard
  find_entry_errors(scantrons, blackboard)
  
  # determine the column that needs to be replaced on blackboard
  print(names(blackboard))
}
