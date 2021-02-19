"""import pandas as pd
df = pd.read_fwf("Client_Address.txt")
df.to_csv("Client_Address.csv")"""
import csv
#txt to CSV file
def txt_to_csv(file):
    with open(f"{file}.txt" , "r") as op:
        stripped =(line.strip() for line in op)
        lines = (line.split(" ") for line in stripped)
        #print(lines)
        with open(f"{file}.csv" , "w") as df:
            writer = csv.writer(df)
            writer.writerow(("ID", "Name","Phone Number","Mail Address"))
            writer.writerows(lines)

def csv_to_txt(file):
    with open(f"{file}1.txt" , "w") as Txt:
        with open(f"{file}.csv", "r") as Csv:
            [Txt.write(" ".join(row)+ "\n") for row in csv.reader(Csv)]
        Txt.close()

