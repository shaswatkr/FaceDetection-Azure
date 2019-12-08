
import requests

# Request headers set Subscription key which provides access to this API. Found in your Cognitive Services accounts.
headers = {
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': '6b83d43d62544a8a90b837b8be390a87',
}

personGroupId="friends"

# Request Body
body = dict()
body["name"] = "Joey"
body["userData"] = "Friends"
body = str(body)

# Request URL
FaceApiCreatePerson = 'https://facedetectioniotgarrage.cognitiveservices.azure.com/face/v1.0/persongroups/' + personGroupId + '/persons'

try:
    # REST Call
    response = requests.post(FaceApiCreatePerson, data=body, headers=headers)
    responseJson = response.json()
    personId = responseJson["personId"]
    print("PERSONID: " + str(personId))

except Exception as e:
    print(e)

# 5 random images of chandler
chandlerImageList = ["https://cdn.newsapi.com.au/image/v1/dd73e8159278db7faa1540bd12389d34",
                     "https://imgix.bustle.com/uploads/image/2018/8/30/540599ec-b13a-428c-8075-6f15bda099d6-joey-tribbianni-best-pickup-lines.png?w=1020&h=574&fit=crop&crop=faces&auto=format&q=70",
                     "https://imgix.elitedaily.com/uploads/image/2018/8/24/1dd02d4f-ca40-4066-9f7d-a0ade78f8b56-maxresdefault.jpg?w=610&fit=max&auto=format&q=70",
                     "https://vignette.wikia.nocookie.net/friends/images/f/f5/JoeyTribbiani.jpg/revision/latest/scale-to-width-down/350?cb=20180424154245",
                     "https://img2.thejournal.ie/inline/3496837/original/?width=630&version=3496837"]

# Request URL
FaceApiCreatePerson = 'https://facedetectioniotgarrage.cognitiveservices.azure.com/face/v1.0/persongroups/' + personGroupId + '/persons/' + personId + '/persistedFaces'

for image in chandlerImageList:
    body = dict()
    body["url"] = image
    body = str(body)

    try:
        # REST Call
        response = requests.post(FaceApiCreatePerson, data=body, headers=headers)
        responseJson = response.json()
        persistedFaceId = responseJson["persistedFaceId"]
        print("PERSISTED FACE ID: " + str(persistedFaceId))

    except Exception as e:
        print(e)
