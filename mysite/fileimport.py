import csv
import re
import django
import datetime
import sys
import argparse
from incidents.models import Incident
import customparser
import defaultparser

g_empty_skip = 0

def emptycheck(row, rowlist, header_row, linenumber):
  global g_empty_skip 

  for rowindex in rowlist:
    if row[rowindex].strip() == '':
      print "!!!!! for line %s, row %s, column %s is blank, skipping" % (linenumber, row[0], header_row[rowindex]) 
      g_empty_skip = g_empty_skip + 1
      return False
  return True

def create_incident(incident_group, row, linenumber, header_row):
      return incident


def readfile(the_input_file, the_incident_group, the_parser_function):
  global g_empty_skip 
  g_empty_skip = 0
  duplicate_skip = 0

  with open(the_input_file, 'rU') as csvfile:
    myreader = csv.reader(csvfile)

    linenumber = 0
    header_row = []

    for row in myreader:
      linenumber = linenumber + 1
      incident_record = ",".join([row[0], row[1], row[2], row[3]])
      print "processing %s" % incident_record

      if linenumber == 1:
        print "skipping header row"
        header_row = row
        continue
  
      results = Incident.objects.filter(identifier=row[0])
      if len(results) > 0:
        print "!!!!! at line %s, duplicate record %s, skipping" % (linenumber, row[0])
        duplicate_skip = duplicate_skip + 1
        continue

      incident = the_parser_function(the_incident_group, row, linenumber, header_row)
      if incident is not None:
        incident.save()

  print
  print "in file %s:" % the_input_file
  print "skipped %d rows due to empty fields" % g_empty_skip
  print "skipped %d rows due to duplicates" % duplicate_skip
  print


def parseargs():
  parser = argparse.ArgumentParser(usage='-i <input_file> -p <custom_parser> -t <common_incident_type>or<None> -erasedb <yes>or<no>', description='testing arg parsing')
  parser.add_argument('-i', required=True, help='input CSV file')
  parser.add_argument('-p', required=True, help='custom parser')
  parser.add_argument('-t', required=True, help='common incident type in this file')
  parser.add_argument('-erasedb', required=True, help='erasedb: yes or no')
  return vars(parser.parse_args())

def dumpdb():
  print
  print "dumping db"
  print
  results = Incident.objects.filter()
  for aresult in results:
      print aresult


if __name__ == "__main__":

  django.setup()


  dd = parseargs()
  #print dd
  if dd['p'] == "default":
    parser_function = defaultparser.parse_default
  else:
    parser_function = getattr(customparser, dd['p'])

  thefile = dd['i']
  thetype = dd["t"] 
  erasedb = dd["erasedb"] 

  print "using parser function %s" % parser_function
  print "using type %s" % thetype
  print "erasing DB : %s" % erasedb

  if erasedb == "yes":
    Incident.objects.all().delete()

  readfile(thefile, thetype, parser_function)

  dumpdb()
