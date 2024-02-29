import requests
from requests.auth import AuthBase
from requests.auth import  HTTPBasicAuth

auth = HTTPBasicAuth('nkamat', 'Hopedrive4578#')
r = requests.post(url="https://pp.seismic.com/app?ContentId=769fafff-0118-46ec-b061-f795a0d14e78#/doccenter/19e9ef7e-b5c0-4140-adde-b0603fc5bf3f/profileview-landing", auth=auth)
print(r.text)