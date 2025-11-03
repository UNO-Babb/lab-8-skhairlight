#ProcessData.py
#Name: Salsabiel Khair Allah
#Date: Nov.2
#Assignment: Lab 8

import random

def main():

  #Open the files we will be using
  inFile = open("names.dat", 'r')
  outFile = open("StudentList.csv", 'w')

  year_map = {
    "Freshman": "FR",
    "Sophomore": "SO",
    "Junior": "JR",
    "Senior": "SR"
  }

  header = inFile.readline()

  for line in inFIle:
    parts = line.strip().split("\t")
    if len(parts) < 7:
      continue

    first = parts[0].strip()
    last = parts[1].strip()
    student_id = parts[3].strip()
    year = parts[5].strip()
    major = parts[6].strip()

    #Create User ID
    user_id = first[0].lower() + last.lower()
    if len(last) < 5:
      user_id += "X"
    user_id += student_id[-3:]

    #Create Major-Year code
    major_code = major[:3].upper()
    year_code = year_map.get(year, "NA")
    major_year = major_code + "-" + year_code

    #Write to output CSV file
    outFile.write(f"{last},{first},{user_id},{major_year}\n")

  #Close files in the end to save and ensure they are not damaged.
  inFile.close()
  outFile.close()

if __name__ == '__main__':
  main()
