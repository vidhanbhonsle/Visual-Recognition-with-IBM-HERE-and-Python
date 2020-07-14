# AI Meets Location

Ever wondered on how we can add AI when it comes to location based services? In this code we upload pass an image to a Python Flask Application and get recommendation based on the food picture you have passed.

#### Sign up for IBM Cloud at https://ibm.biz/HERETechnologies
#### Get your Here Maps API Key at https://developer.here.com

## Architecture 

![Arch](/images/ArchLocal.png)

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
visual_recognition = VisualRecognitionV3(
    version='2018-03-19',
    iam_apikey='IBM_API_KEY')
...

api_key = 'HERE_API_KEY' # Acquire from developer.here.com
```

3. And scroll to the variables where the ```latitude``` and ```longitude``` are set and replace it with the latitude and longitude of your desired locaiton.
```python
latitude = 12.959111
longitude = 77.732022
```
4. Open a terminal and ```cd``` into the application directory and export the ```FLASK_APP``` variable
```bash
export FLASK_APP=test.py
```

5. You can now run the application by running ```flask run``` in the terminal.


6. ***OPTIONAL*** If you would like to assess another food item just add it to the project folder and in the ```test.py``` file replace the filename ```pizza.jpg``` with the filename of your picture.

```python
with open('./pizza.jpg', 'rb') as images_file:
```

Save the file and re-run ```flask run``` to see the changes.

## Cloud Foundry Deployment 

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

3. Install the Cloud Clundry CLI and follow the instructions
[Cloud Foundry CLI Installation](https://docs.cloudfoundry.org/cf-cli/install-go-cli.html)

4. Login to the CF CLI
```bash
cf login
```
When logging in make sure to login to [one of the following IBM Cloud Foundry Endpoints](https://cloud.ibm.com/docs/cloud-foundry-public?topic=cloud-foundry-public-endpoints)

5. Deploy the Cloud Foundry Service on IBM Cloud and select the ```python``` runtime

![Cloud_CF](/images/CF_Cloud.png)
![Cloud_Run](/images/CF_Runtime.png)

6. ````cd```` into the ```VisualRec-CloudFoundry```

7. Edit the ```manifest.yaml``` and change then ```- name: <your app name>``` to the same name you have entered on IBM Cloud when creating the Cloud Foundry IBM Cloud Service
```yml
  applications:
  - name: allocation
    random-route: true
    memory: 128M
```
8. Making sure that you are in the ```VisualRec-CloudFoundry``` enter the command 
```bash
cf push
```
And your application will start to deploy on Cloud Foundry and you will be able to access it.

***NOTICE*** You can also make changes to the application if you like as stated in the [local deployment](###Local-Deployment) section within the ```VisualRec-CloudFoundry``` directory and run ```cf psuh``` to see your changes.
