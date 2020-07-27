# AI Meets Location

Ever wondered on how we can add AI when it comes to location based services? In this code we upload pass an image to a Python Flask Application and get recommendation based on the food picture you have passed.

#### Sign up for IBM Cloud at https://ibm.biz/HERETechnologies
#### Get your Here Maps API Key at https://developer.here.com

## Architecture 

![Arch](/images/AI_Location_Sol_Arch.png)

1. User passes an image in the python code
1. As we are using the visual recognition service there is a out of the box food model which we are going to use and it detects the name of the food which we have passed
1. The name of the food is then passed to the Here Maps Discover API which then suggests places around a particular location which we have configured within the python application.

### Local Deployment

To implement this code to a location of your choice 

1. Clone this repository 
```bash
git clone https://github.com/vidhanbhonsle/Visual-Recognition-with-IBM-HERE-and-Python
```
2. Add your IBM Cloud Visual Recogntion API Key and Here Maps API Key in ```test.py```

```python
authenticator = IAMAuthenticator('IBM_API_KEY')

visual_recognition = VisualRecognitionV3(
    version='2018-03-19',
    authenticator=authenticator)

visual_recognition.set_service_url('IBM_SERVICE_URL') 

```
3. Enter the templates directory and add the HERE maps API key obtained from developer.here.com and add it to the ```JS_API_KEY``` variable

```javascript
	 var platform = new H.service.Platform({
            apikey: "JS_API_KEY" //HERE MAPS API KEY   
        });
```

4. And scroll to the variables where the ```latitude``` and ```longitude``` are set and replace it with the latitude and longitude of your desired locaiton.
```python
latitude = 12.959111
longitude = 77.732022
```
5. Open a terminal and ```cd``` into the application directory and export the ```FLASK_APP``` variable
```bash
export FLASK_APP=test.py
```

6. You can now run the application by running ```flask run``` in the terminal.


7. ***OPTIONAL*** If you would like to assess another food item just add it to the project folder and in the ```test.py``` file replace the filename ```pizza.jpg``` with the filename of your picture.

```python
with open('./pizza.jpg', 'rb') as images_file:
```

Save the file and re-run ```flask run``` to see the changes.

## Cloud Foundry Deployment 

To host your application online you can also deploy the same application on IBM Cloud's Coud Foundry.

### Cloud Foundry Architecture 

![Arch_CF](/images/AI_LOC_ARCH.png)

### Deploy Application on Cloud Foundry

Install the IBM Cloud CLI 

Mac or Linux

```bash
curl -sL https://ibm.biz/idt-installer | bash
```

Windows (Use Powershell as Adminstrator)
```bash
[Net.ServicePointManager]::SecurityProtocol = "Tls12, Tls11, Tls, Ssl3"; iex(New-Object Net.WebClient).DownloadString('https://ibm.biz/idt-win-installer')
```

1. Login to the IBM Cloud CLI
```bash
ibmcloud login
```

2. Target your IBM Cloud CF Organization & Space
```bash
ibmcloud target --cf 
```

3. Edit the ```manifest.yaml``` and change then ```- name: <your app name>``` to the same name you have entered on IBM Cloud when creating the Cloud Foundry IBM Cloud Service
```yml
  applications:
  - name: allocation 
    random-route: true
    memory: 128M
```

8. Once you have changed the .yml file you can start with pushing your application, making sure that you are in the ```VisualRec-CloudFoundry```  directory enter the command 
```bash
ibmcloud app push
```
And your application will start to deploy on Cloud Foundry and you will be able to access it by seeing the output of the application route on your terminal and also can be access through .

***NOTICE*** You can also make changes to the application if you like as stated in the [local deployment](###Local-Deployment) section within the ```VisualRec-CloudFoundry``` directory and run ```cf psuh``` to see your changes.
