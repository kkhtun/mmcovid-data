import csv 
import json 

def csv_to_json(csvFilePath, jsonFilePath):
    jsonArray = []
      
    #read csv file
    with open(csvFilePath, encoding='utf8') as csvf: 
        #load csv file data using csv library's dictionary reader
        csvReader = csv.DictReader(csvf) 

        #convert each csv row into python dict
        for row in csvReader: 
            #add this python dict to json array
            row = {'name':row.get('name_mm'),
                    'type':row.get('service'),
                    'address':row.get('address_mm'),
                    'township':row.get('township_mm'),
                    'phone':[row.get('phone1'), row.get('phone2'), row.get('phone3'),row.get('phone4'),row.get('phone5')]
            }
            jsonArray.append(row)
  
    #convert python jsonArray to JSON String and write to file
    with open(jsonFilePath, 'w', encoding='utf8') as jsonf: 
        jsonString = json.dumps(jsonArray, indent=4, ensure_ascii=False)
        jsonf.write(jsonString)
          
csvFilePath = r'mmCOVID - Services.csv'
jsonFilePath = r'mmCovid.json'
csv_to_json(csvFilePath, jsonFilePath)

def get_unique_service_types(csvFilePath, jsonFilePath):
    jsonArray = []
    with open(csvFilePath, encoding='utf8') as csvf:
        csvReader = csv.DictReader(csvf)
        for row in csvReader:
            row = row.get('Services')
            jsonArray.append(row)
    with open(jsonFilePath, 'w', encoding='utf8') as jsonf: 
        jsonString = json.dumps(jsonArray, indent=4, ensure_ascii=False)
        jsonf.write(jsonString)

validationCsvFilePath = r'mmCOVID - Validation.csv'
validationJsonFilePath = r'validation.json'
get_unique_service_types(validationCsvFilePath, validationJsonFilePath)
    