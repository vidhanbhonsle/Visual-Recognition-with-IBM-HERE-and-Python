import json
from watson_developer_cloud import VisualRecognitionV3

visual_recognition = VisualRecognitionV3(
    version='2018-03-19',
    iam_apikey='IBM_API_KEY')

with open('./test.jpg', 'rb') as images_file:
    classes = visual_recognition.classify(images_file,threshold='0.6',classifier_ids='food').get_result()
#print(json.dumps(classes, indent=2))

output_query = classes['images'][0]['classifiers'][0]['classes'][0]['class']

print(output_query) #String type data

import requests
from flask import Flask,render_template
URL = "https://discover.search.hereapi.com/v1/discover"
latitude = 12.959111
longitude = 77.732022
api_key = 'HERE_API_KEY' # Acquire from developer.here.com
limit = 5

PARAMS = {
            'apikey':api_key,
            'q':'burger',
            'limit': limit,
            'at':'{},{}'.format(latitude,longitude)
         } 

# sending get request and saving the response as response object 
r = requests.get(url = URL, params = PARAMS) 
data = r.json()
#print(data)

placeOne = data['items'][0]['title']
placeOne_address =  data['items'][0]['address']['label']
placeOne_latitude = data['items'][0]['position']['lat']
placeOne_longitude = data['items'][0]['position']['lng']

print('place 1 -',placeOne)
print(placeOne_address)
print(placeOne_latitude)
print(placeOne_longitude)

placeTwo = data['items'][1]['title']
placeTwo_address =  data['items'][1]['address']['label']
placeTwo_latitude = data['items'][1]['position']['lat']
placeTwo_longitude = data['items'][1]['position']['lng']

#print('place 2 -',placeTwo)
#print(placeTwo_address)
#print(placeTwo_latitude)
#print(placeTwo_longitude)

placeThree = data['items'][2]['title']
placeThree_address =  data['items'][2]['address']['label']
placeThree_latitude = data['items'][2]['position']['lat']
placeThree_longitude = data['items'][2]['position']['lng']

#print('place 3 -',placeThree)
#print(placeThree_address)
#print(placeThree_latitude)
#print(placeThree_longitude)

placeFour = data['items'][3]['title']
placeFour_address =  data['items'][3]['address']['label']
placeFour_latitude = data['items'][3]['position']['lat']
placeFour_longitude = data['items'][3]['position']['lng']

#print('place 4 -',placeFour)
#print(placeFour_address)
#print(placeFour_latitude)
#print(placeFour_longitude)

placeFive = data['items'][4]['title']
placeFive_address =  data['items'][4]['address']['label']
placeFive_latitude = data['items'][4]['position']['lat']
placeFive_longitude = data['items'][4]['position']['lng']

#print('place 5 -',placeFive)
#print(placeFive_address)
#print(placeFive_latitude)
#print(placeFive_longitude)

app = Flask(__name__)
@app.route('/')

def map_func():
	return render_template('map.html',
                            latitude = latitude,
                            longitude = longitude,
                            apikey=api_key,
                            oneName=placeOne,
                            OneAddress=placeOne_address,
                            oneLatitude=placeOne_latitude,
                            oneLongitude=placeOne_longitude,
                            twoName=placeTwo,
                            twoAddress=placeTwo_address,
                            twoLatitude=placeTwo_latitude,
                            twoLongitude=placeTwo_longitude,
                            threeName=placeThree,
                            threeAddress=placeThree_address,
                            threeLatitude=placeThree_latitude,
                            threeLongitude=placeThree_longitude,
                            fourName=placeFour,		
                            fourAddress=placeFour_address,
                            fourLatitude=placeFour_latitude,
                            fourLongitude=placeFour_longitude,
                            fiveName=placeFive,		
                            fiveAddress=placeFive_address,
                            fiveLatitude=placeFive_latitude,
                            fiveLongitude=placeFive_longitude
                            )

if __name__ == '__main__':
	app.run(debug = False)
