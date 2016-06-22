import re
import string

infile_kilo = open('Conf_Files/nova-controller1.conf', 'r')
infile_mitaka= open('Conf_Files/nova-mitaka.conf', 'r')
outfile_exclusivo_kilo = open('Result/kilo_ex.txt', 'w')
outfile_mitaka2 = open('Result/mitaka2.txt', 'w')

def GetPart(s,part=0, separator='='):
    out = s.partition(separator)[part].strip()
    return out

def CreateDictionaryFromFile(filein):
    diccionario = {}
    for line in filein:
        if not (re.match("^#",line) or re.match("\n",line)):
            key=GetPart(line,0,"=")
            val=GetPart(line,2,"=")

            diccionario [key] = val

    return diccionario

def CreateListFromFile(filein):
    lista_key = []

    for line in filein:
        if not (re.match("^#",line) or re.match("\n",line)):
            key=GetPart(line,0,"=")
            lista_key.extend([key])

    return lista_key

def StringToFile(line,dict):
    key=GetPart(line,0,"=")
    val=GetPart(line,2,"=")

    string_to_file = "# MITAKA VALUE = " + val + "\n" + key + "\n"

    if not (key.startswith('[') or key.startswith('\n')):
        if key in dict.keys():
            string_to_file = key + "=" + dict[key] + "\n"

    return string_to_file

dict_kilo = CreateDictionaryFromFile (infile_kilo)
list_key_mitaka = CreateListFromFile (infile_mitaka)

infile_kilo = open('Conf_Files/nova-controller1.conf', 'r')
infile_mitaka= open('Conf_Files/nova-mitaka.conf', 'r')

for line in infile_mitaka:
    if not (re.match("^#",line) or re.match("\n",line)):
        outfile_mitaka2.write(StringToFile(line,dict_kilo))

for line in infile_kilo:
    key=GetPart(line,0,"=")
    val=GetPart(line,2,"=")
    if key not in list_key_mitaka:
        if not (re.match("^#",line) or re.match("\n",line)):
            outfile_exclusivo_kilo.write(line)

infile_mitaka.close()
infile_kilo.close()
