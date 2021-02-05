import os
filedir = os.getcwd()
filenames = os.listdir(filedir)
table_1 = []
dic_1 = {}
dic_2 = {}
dic_3 = {}
dic_4 = {}
outputfile_1 = open("try.txt", "w")
outputfile_2 = open("try_1.txt", "w")
inputfile_1 = open("annotation.txt", "r")
for line_1 in inputfile_1:
    table_1.append(line_1.split())
for a in table_1:
    Chr = a[0]
    c = str(int(a[2])-1)
    d = a[3]
    gene = a[4] + "&" + a[5]
    number = c + "-" + d
    if gene not in dic_1:
        dic_1[gene] = []
    dic_1[gene].append(number)
    if Chr not in dic_3:
        dic_3[Chr] = []
    dic_3[Chr].append(gene)
for aa in dic_3:
    list_1 = list(set(dic_3[aa]))
    dic_4[aa] = list_1
for zhangwei in dic_4:
    print(zhangwei + " " + str(len(dic_4[zhangwei])))
outputfile_1.write(str(dic_4) + "\n" + str(dic_1) + "\n")

def delete_sequence(inputfile_2, outputfile):
    seq = ''
    head = ''
    for line_2 in inputfile_2:
        if line_2[0] == ">" and seq == "":
            head = line_2.strip().split()[0]
        elif line_2[0] != ">":
            seq = seq + line_2.strip()
        elif line_2[0] == ">" and seq != '':
            dic_2[head.replace(">", "")] = list(seq)
            seq = ''
            head = line_2.strip().split()[0]
                
    for j in dic_2:
        if j in dic_4:
            sequence = dic_2[j]
            ab = dic_4[j]
            for ac in ab:
                ad = dic_1[ac]
                seq_1 = []
                az = ac.split("&")[1]
                if az == "+":
                    for ae in ad:
                        af = ae.split("-")
                        ag = int(af[0])
                        ah = int(af[1])
                        seq_2 = sequence[ag:ah]
                        seq_1.append(seq_2)
                    seq_1 = str(seq_1).upper()
                    seq_1 = seq_1.replace("'", "")
                    seq_1 = seq_1.replace("[", "")
                    seq_1 = seq_1.replace("]", "")
                    seq_1 = seq_1.replace(",", "")
                    seq_1 = seq_1.replace(" ", "")
                    outputfile.write(">" + str(ac) + " " + str(j) + " " + str(len(seq_1)) + "\n" + str(seq_1) + "\n")
                if az == "-":
                    ay = reversed(ad)
                    for ax in ay:
                        aw = ax.split("-")
                        au = int(aw[0])
                        av = int(aw[1])
                        seq_2 = sequence[au:av]
                        seq_1.append(seq_2)
                    seq_1 = str(seq_1).upper()
                    seq_1 = seq_1.replace("'", "")
                    seq_1 = seq_1.replace("[", "")
                    seq_1 = seq_1.replace("]", "")
                    seq_1 = seq_1.replace(",", "")
                    seq_1 = seq_1.replace(" ", "")
                    outputfile.write(">" + str(ac) + " " + str(j) + " " + str(len(seq_1)) + "\n" + str(seq_1) + "\n")

for p in filenames:
    if os.path.splitext(p)[1] == '.fasta':
        seq = ''
        head = ''
        inputfile_2 = open(p, "r")
        outputfile = open(p.replace(".fasta", "") + ".txt", "w")
        delete_sequence(inputfile_2, outputfile)
