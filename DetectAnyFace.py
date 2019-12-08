# import modules
import requests

# Request headers set Subscription key which provides access to this API. Found in your Cognitive Services accounts.
headers = {
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': '6b83d43d62544a8a90b837b8be390a87',
}

body = dict()
body["url"] = "https://upload.wikimedia.org/wikipedia/en/6/6f/David_Schwimmer_as_Ross_Geller.jpg"
body = str(body)

# Request URL
FaceApiDetect = 'https://facedetectioniotgarrage.cognitiveservices.azure.com/face/v1.0/detect?returnFaceId=true'

try:
    # REST Call
    response = requests.post(FaceApiDetect, data=body, headers=headers)
    responseJson = response.json()
    faceId = responseJson[0]["faceId"]

except Exception as e:
    print("Face Id Not Found: Person Not Recognized")

personGroupId="friends"
faceIdsList = [faceId]

# Request Body
body = dict()
body["personGroupId"] = personGroupId
body["faceIds"] = faceIdsList
body["maxNumOfCandidatesReturned"] = 1
body["confidenceThreshold"] = 0.5
body = str(body)

# Request URL
FaceApiIdentify = 'https://facedetectioniotgarrage.cognitiveservices.azure.com/face/v1.0/identify'

try:
    # REST Call
    response = requests.post(FaceApiIdentify, data=body, headers=headers)
    responseJson = response.json()
    personId = responseJson[0]["candidates"][0]["personId"]
    confidence = responseJson[0]["candidates"][0]["confidence"]
    print("PERSON ID: " + str(personId) + ", CONFIDENCE :" + str(confidence))

except Exception as e:
    print("Could not detect")

# Request URL
FaceApiGetPerson = 'https://facedetectioniotgarrage.cognitiveservices.azure.com/face/v1.0/persongroups/' + personGroupId + '/persons/' + personId

try:
    response = requests.get(FaceApiGetPerson, headers=headers)
    responseJson = response.json()
    print("This Is " + str(responseJson["name"]))

except Exception as e:
    print(e)
