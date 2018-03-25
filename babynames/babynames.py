#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  the_file = open(filename, 'rU')
  text = the_file.read()
  the_file.close()
  lines = text.split('\n')
  dictionary = {}
  for i in range(len(lines)):
    line = lines[i]
    match = re.search('Popularity in ([\d]+)', line)
    if match:
      dictionary[''] = match.group(1)
      break
  if i == len(lines)-1:
    print 'No string of the form "Popularity in ([\d]+)" in ' + filename
    sys.exit(1)
  for j in range(i+1, len(lines)):
    line = lines[j]
    match = re.search('<td>([\d]+)</td><td>([\w]+)</td><td>([\w]+)</td>', line)
    if match:
      rank = match.group(1)
      name1 = match.group(2)
      name2 = match.group(3)
      if name1 in dictionary:
        if int(rank) < int(dictionary[name1]): dictionary[name1] = rank
      else:
        dictionary[name1] = rank
      if name2 in dictionary:
        if int(rank) < int(dictionary[name2]): dictionary[name2] = rank
      else:
        dictionary[name2] = rank
  result = [dictionary.pop('')]
  for name in sorted(dictionary.keys()):
    string = name + ' ' + dictionary[name]
    result.append(string)
  return result


def get_text(list_of_strings):
  """Returns a formatted string from a list of strings."""
  result = ''
  for a_string in list_of_strings: result += (a_string + '\n')
  return result


def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print 'usage: [--summaryfile] file [file ...]'
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]
    if not args:
      print 'usage: [--summaryfile] file [file ...]'
      sys.exit(1)

  # For each filename, get the names, then either print the text output
  # or write it to a summary file
  list_of_lists_of_strings = []
  for filename in args:
    list_of_lists_of_strings.append(extract_names(filename))
  text = ''
  if summary:
    current_file_ctr = 0
    for filename in args:
      text = get_text(list_of_lists_of_strings[current_file_ctr])
      output_file = open(filename + '.summary', 'w')
      output_file.write(text)
      output_file.close()
      current_file_ctr += 1
  else:
    for list_of_strings in list_of_lists_of_strings:
      text += get_text(list_of_strings)
    print text,

if __name__ == '__main__':
  main()
