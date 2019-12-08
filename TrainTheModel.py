# import modules
import requests

# Request headers set Subscription key which provides access to this API. Found in your Cognitive Services accounts.
headers = {
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': '6b83d43d62544a8a90b837b8be390a87',
}

personGroupId="friends"

#Request Body
body = dict()

#Request URL
FaceApiTrain = 'https://facedetectioniotgarrage.cognitiveservices.azure.com/face/v1.0/persongroups/'+personGroupId+'/train'

try:
    # REST Call
    response = requests.post(FaceApiTrain, data=body, headers=headers)
    print("RESPONSE:" + str(response.status_code))

except Exception as e:
    print(e)
