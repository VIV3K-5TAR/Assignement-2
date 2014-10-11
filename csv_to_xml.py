__author__ = 'Venkat Nirmal'


fr = open("student_csv.csv","r")
fw = open("Converted_Student_xml.xml","w")

str = "\""
str1 = ","
fw.write("<Students>" + "\n")


for line in fr:
    line = line.split(str)
    fw.write("<Student>" + "\n")

    words = line[1]
    words = words.split(str1)
    fw.write("<Name>" + "\n")
    if words.__len__() == 2:
        fw.write("<FirstName>")
        fw.write(words[0])
        fw.write("</FirstName>" + "\n")
        fw.write("<LastName>")
        fw.write(words[1])
        fw.write("</LastName>" + "\n")
    elif words.__len__() == 3:
        fw.write("<FirstName>")
        fw.write(words[0])
        fw.write("</FirstName>" + "\n")
        fw.write("<MiddleName>")
        fw.write(words[1])
        fw.write("</MiddleName>" + "\n")
        fw.write("<LastName>")
        fw.write(words[2])
        fw.write("</LastName>" + "\n")
    fw.write("</Name>" + "\n")

    words = line[3]
    words = words.split(str1)
    fw.write("<Id>" + "\n")
    if words.__len__() == 6:
        fw.write("<Year>" + " ")
        fw.write(words[0])
        fw.write("</Year>" + "\n")
        fw.write("<Branch1>" + " ")
        fw.write(words[1])
        fw.write("</Branch1>" + "\n")
        fw.write("<Branch2>" + " ")
        fw.write(words[2])
        fw.write("</Branch2>" + "\n")
        fw.write("<PSTS>" + " ")
        fw.write(words[3])
        fw.write("</PSTS>" + "\n")
        fw.write("<Rank>" + " ")
        fw.write(words[4])
        fw.write("</Rank>" + "\n")
        fw.write("<Place>" + " ")
        fw.write(words[5])
        fw.write("</Place>" + "\n")
    elif words.__len__() == 5:
        fw.write("<Year>" + " ")
        fw.write(words[0])
        fw.write("</Year>" + "\n")
        fw.write("<Branch1>" + " ")
        fw.write(words[1])
        fw.write("</Branch1>" + "\n")
        fw.write("<PSTS>" + " ")
        fw.write(words[2])
        fw.write("</PSTS>" + "\n")
        fw.write("<Rank>" + " ")
        fw.write(words[3])
        fw.write("</Rank>" + "\n")
        fw.write("<Place>" + " ")
        fw.write(words[4])
        fw.write("</Place>" + "\n")
    else:
        print "Incorrect file format"
        fr.close()
        fw.close()
        exit(0)
    fw.write("</Id>" + "\n")

    fw.write("<DOB>" + "\n")
    fw.write(line[5])
    fw.write("\n" + "</DOB>" + "\n")

    words = line[7]
    words = words.split(str1)
    fw.write("<Prereqs>" + "\n")

    fw.write("<CProgramming>" + "\n")
    fw.write("<completion>")
    fw.write(words[0])
    fw.write("</completion>"+"\n")
    fw.write("<grade>")
    fw.write(words[1])
    fw.write("</grade>"+"\n")
    fw.write("</CProgramming>" + "\n")

    fw.write("<OOP>" + "\n")
    fw.write("<completion>")
    fw.write(words[2])
    fw.write("</completion>"+"\n")
    fw.write("<grade>")
    fw.write(words[3])
    fw.write("</grade>"+"\n")
    fw.write("</OOP>" + "\n")

    fw.write("<Databases>" + "\n")
    fw.write("<completion>")
    fw.write(words[4])
    fw.write("</completion>"+"\n")
    fw.write("<grade>")
    fw.write(words[5])
    fw.write("</grade>"+"\n")
    fw.write("</Databases>" + "\n")

    fw.write("<MachineLearning>" + "\n")
    fw.write("<completion>")
    fw.write(words[6])
    fw.write("</completion>"+"\n")
    fw.write("<grade>")
    fw.write(words[7])
    fw.write("</grade>"+"\n")
    fw.write("</MachineLearning>" + "\n")

    fw.write("<DataMining>" + "\n")
    fw.write("<completion>")
    fw.write(words[8])
    fw.write("</completion>"+"\n")
    fw.write("<grade>")
    fw.write(words[9])
    fw.write("</grade>"+"\n")
    fw.write("</DataMining>" + "\n")

    fw.write("<xml>" + "\n")
    fw.write("<completion>")
    fw.write(words[10])
    fw.write("</completion>"+"\n")
    fw.write("<grade>")
    fw.write(words[11])
    fw.write("</grade>"+"\n")
    fw.write("</xml>" + "\n")

    fw.write("</Prereqs>" + "\n")

    words = line[9]
    words = words.split(str1)
    fw.write("<Address>" + "\n")
    fw.write("<DoorNo>")
    fw.write(words[0])
    fw.write("</DoorNo>"+"\n")
    fw.write("<Street>")
    fw.write(words[1])
    fw.write("</Street>"+"\n")
    fw.write("<City>")
    fw.write(words[2])
    fw.write("</City>"+"\n")
    fw.write("<State>")
    fw.write(words[3])
    fw.write("</State>"+"\n")
    fw.write("<Country>")
    fw.write(words[4])
    fw.write("</Country>"+"\n")
    fw.write("<PinCode>")
    fw.write(words[5])
    fw.write("</PinCode>"+"\n")
    fw.write("</Address>" + "\n")

    words = line[11]
    words = words.split(str1)
    fw.write("<Contact>" + "\n")
    fw.write("<Phone>" + "\n")
    if words.__len__() == 2:
        fw.write("<Primary>")
        fw.write(words[0])
        fw.write("</Primary>" + "\n")
        fw.write("<Secondary>")
        fw.write(words[1])
        fw.write("</Secondary>" + "\n")
    elif words.__len__() == 1:
        fw.write("<Primary>")
        fw.write(words[0])
        fw.write("</Primary>" + "\n")
    else:
        print "Incorrect file format"
        fr.close()
        fw.close()
        exit(0)
    fw.write("</Phone>" + "\n")

    words = line[13]
    words = words.split(str1)
    fw.write("<Email>" + "\n")
    if words.__len__() == 2:
        fw.write("<Primary>")
        fw.write(words[0])
        fw.write("</Primary>" + "\n")
        fw.write("<Secondary>")
        fw.write(words[1])
        fw.write("</Secondary>" + "\n")
    elif words.__len__() == 1:
        fw.write("<Primary>")
        fw.write(words[0])
        fw.write("</Primary>" + "\n")
    else:
        print "Incorrect file format"
        fr.close()
        fw.close()
        exit(0)
    fw.write("</Email>" + "\n")

    fw.write("</Contact>" + "\n")

    fw.write("<Cgpa>" + "\n")
    fw.write(line[15])
    fw.write("\n" + "</Cgpa>" + "\n")

    fw.write("<PsSem>" + "\n")
    fw.write(line[17])
    fw.write("\n" + "</PsSem>" + "\n")

    fw.write("</Student>" + "\n" + "\n")

fw.write("</Students>")
fr.close()
fw.close()