from jsonschema import Draft7Validator
import json
import csv
#import cv2

#for testing only
def validateJsonText(jsonTxt):
    try:
        json.loads(jsonTxt)
    except ValueError as err:
        print(err)
        return False
    return True

#for testing only
def validateJsonFile(jsonFile):
    try:
        json.load(jsonFile)
    except ValueError as err:
        print(err)
        return False
    return True


if __name__ == "__main__":
    
    # opening result file
    with open("result_1.json") as f:
        result = json.load(f)
    
    
    validator = Draft7Validator(result)

    print(list(validator.iter_errors(result)))

    if list(validator.iter_errors(result)) == []:
        print("no errors found")
    else:
        # accessing attributes in result_1
        for sequence in result['Sequence']:
            for objectlabels in sequence['ObjectLabels']:
                for frameobjects in objectlabels['FrameObjectLabels']:
                    for attributes in frameobjects['attributes']:
                        error = validateJsonText(str(attributes))
                        if error == ValueError:
                            #deleting the missing attribute 
                            a_file = open('result_1.json', 'r')
                            a_json = json.load(a_file)
                            json_missing1 = json.dumps(a_json, indent=1)
                            a_file.close()

                            #copying the missing attribute to error file
                            with open("error_result1.txt", "w") as outfile:
                                outfile.write(json_missing1)
    
    
    # opening result2 file and doing the same validation as above
    with open("result_2.json") as f2:
        result2 = json.load(f2)
    
    
    validator2 = Draft7Validator(result2)

    print(list(validator2.iter_errors(result2)))

    if list(validator2.iter_errors(result2)) == []:
        print("no errors found")
    else:
        # accessing attributes in result_2
        for sequence in result2['Sequence']:
            for objectlabels in sequence['ObjectLabels']:
                for frameobjects in objectlabels['FrameObjectLabels']:
                    for attributes in frameobjects['attributes']:
                        error = validateJsonText(str(attributes))
                        if error == ValueError:
                            #deleting the missing attribute 
                            a_file = open('result_2.json', 'r')
                            a_json = json.load(a_file)
                            json_missing1 = json.dumps(a_json, indent=1)
                            a_file.close()

                            #copying the missing attribute to error file
                            with open("error_result2.txt", "w") as outfile:
                                outfile.write(json_missing1)

                       

#visualizing images
image1 = cv2.imread('images/1594065528713003.jpg')
image2 = cv2.imread('images/1594065538663682.jpg')
image3 = cv2.imread('images/1594065548667205.jpg')
image4 = cv2.imread('images/15940065558578166.jpg')
image5 = cv2.imread('images/1594065568681687.jpg')

cv2.imshow('image1', image1)
cv2.imshow('image2', image2)
cv2.imshow('image3', image3)
cv2.imshow('image4', image4)
cv2.imshow('image5', image5)