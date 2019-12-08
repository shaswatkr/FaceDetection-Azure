# import modules
import requests

# Request headers set Subscription key which provides access to this API. Found in your Cognitive Services accounts.
headers = {
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': '6b83d43d62544a8a90b837b8be390a87',
}

personGroupId="friends"

body = dict()
body["name"] = "F.R.I.E.N.D.S"
body["userData"] = "All friends cast"
body = str(body)

#Request URL
FaceApiCreateLargePersonGroup = 'https://facedetectioniotgarrage.cognitiveservices.azure.com/face/v1.0/persongroups/'+personGroupId

try:
    # REST Call
    response = requests.put(FaceApiCreateLargePersonGroup, data=body, headers=headers)
    print("RESPONSE:" + str(response.status_code))

except Exception as e:
    print(e)
