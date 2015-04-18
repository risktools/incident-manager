import csv
import re
import django
import datetime
import sys
import argparse
from incidents.models import Incident
import fileimport

myregex = re.compile('[ /]')

def parse_default(incident_group, row, linenumber, header_row):
  if fileimport.emptycheck(row, [0, 1, 2, 3], header_row, linenumber):
      date_fields = map(int, myregex.split(row[3]))
      thedate  = datetime.date(date_fields[2], date_fields[0], date_fields[1])
      incident = Incident(identifier = row[0], name = row[2], level=row[1], date = thedate, incident_group = row[4], owner = "none", state = "under investigation")
      return incident
  else:
      return None
