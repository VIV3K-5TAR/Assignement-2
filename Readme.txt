The conversion from csv to xml doesnot use XSD..
Instead it is kind of hardcoded.
The code has to be changed for every change in XSD.
Couldnot find a method for incorporating XSD in the flow..!!

File Descriptions:
Written_Student_xml and Written_Student_xsd : Written by me
student_csv.csv : Details of 5 students
csv_to_xml.py : File that converts student_csv.csv into Converted_Student_JSON.json
xml_to_json : File that converts Converted_Student_JSON.json into Converted_Student_xml.xml