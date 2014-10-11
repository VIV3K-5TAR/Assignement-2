__author__ = 'Venkat Nirmal'

from xmlutils.xml2json import xml2json

converter = xml2json("Converted_Student_xml.xml", encoding="utf-8")
fjson = open("Converted_Student_JSON.json","w")
fjson.write(converter.get_json(pretty=True))
fjson.close()