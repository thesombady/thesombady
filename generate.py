import os
import datetime
line = '_______'
newline = "\n"
space = ' '

birthDate = datetime.date(1998, 10, 13)
today = datetime.date.today()

def wrap(txt: str):
    return "'" + txt + "'"

def calculateDate():
    years = today.year - birthDate.year
    return str(years)

name = os.environ['LOGNAME']
INFO = [
    '{}@{}'.format(name, today),
    line,
    'Info:',
    "Name: 'Andreas Evensen'",
    "Age: {} years".format(calculateDate()),
    "        ~~~~~ Undefined",
    "Language.Spoken: [Swedish, English]",
    "Language.Coding: [C++, C, V, Python, Go]",
    "Editor: 'Helix'",
    '',
    line,
    "Country: Sweden",
    "City: Västerås",
    "University: Lund University -> Stockholm University",
    "                           ~~~~ Not a pointer",
    "Employment: 50% Amanuens",
    '',
    line,
    "Focus:",
    "Focus.Software: ['Language Creation', 'Scripting']",
    "Focus.Others: ['Gym', 'Outdoors']",
    "Focus.Hardware: null",
    '',
    line,
    "Projects:",
    "Zeta.readme: 'Next generation scientific language'",
    "Zeta.status: {active: true, status: Hidden}",
    "vTikz.readme: 'Generate standalone tikz figures'",
    "vTikz.status: {active: false, reoccupy: true}",
    "cleanr.readme: 'Simply remove unwanted files'",
    "cleanr.status: {active: true, status: Hidden}",
    "templ.readme: 'Generate quick templates for latex'",
    "templ.status: {active: true, status: Hidden}",
    '',
    line,
    "Contacts:",
    "Discord: 'Aristotes'",
    "mail: null"
]

imagePath = 'image.txt'
markdown = "```v\n>>> info\n"
with open(imagePath, 'r') as file:
    lines = file.readlines()
    combined = zip(lines, INFO)
    for info in combined:
        markdown += wrap(info[0][:-1]) + space + info[1] + newline

# markdown = markdown[:-1] # Remove last line
with open('readme.md', 'w') as file:
    file.write(markdown + "\n```")