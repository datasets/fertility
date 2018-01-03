from urllib.request import urlopen

with open("../data/fertility.csv", "w") as bumps_file:
    bumps_file.write("season,age,childish-disease,trauma,surgical-intervention,fevers,alcoholic,"
                     "smoking,sitting,output\n")
    for line in urlopen("https://archive.ics.uci.edu/ml/machine-learning-databases/00244/fertility_Diagnosis.txt"):
        decodedLine = line.decode('UTF-8')

        bumps_file.write(decodedLine.strip() + '\n')
    bumps_file.close()
