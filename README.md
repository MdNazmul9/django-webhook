# runserver

```
python manage.py runserver 9000

```


# CURL

```
curl -X POST http://127.0.0.1:9000/webhook/ -d '{"Type" : "Notification",
  "MessageId" : "20d48143-6af4-571d-b7cb-d211e6a2ac69",
  "TopicArn" : "arn:aws:sns:ap-southeast-1:354285753755:bpt_01823072645",
  "Message" :
       {
       "dateTime":"20180419122246",
       "debitMSISDN":"8801700000001",
       "creditOrganizationName":"Org 01",
       "creditShortCode":"ORG001",
       "trxID":"4J420ANOXC",
       "transactionStatus":"Completed",
       "transactionType":"1003",
       "amount":"100",
       "currency":"BDT",
       "transactionReference":"User inputed reference value." 
       },
  "Timestamp" : "2018-04-19T12:22:46.236Z",
  "SignatureVersion" : "1",
  "Signature" : "jZBoouSuStaUqYZY+mruc3r3ST58CPkzjOu8i65dDIReWDcNAvPGUpNDSCBBMVLLA6UIJ9KtvTmop+JefiAd/8+YOxR738j0AXDcWc0A4u1EaMWqnmLvFufC0rAkEQuHdzn+XpHSET8Vn9SsnDJMsmdnWIiqH6JDsuPImuzP6V4Fh9/EKOYVOSks5aNChD1fwPQ1Z6DmtpEVaEXKagWXO8yPPAgs5meDArV7qIm93devI3DzfJboF1DOqHL9JkIrj5S9+ZqybCNKl3ay1JkgY9BXPoRe3XCzUSd4zTXa6GDbH7+3KZ3wmsiaa2zfwYCmrFNvzuE5o6OkeNHE/mqyCA==",
  "SigningCertURL" : "https://sns.ap-southeast-1.amazonaws.com/SimpleNotificationService-ac565b8b1a6c5d002d285f9598aa1d9b.pem",
  "UnsubscribeURL" : "https://sns.ap-southeast-1.amazonaws.com/?Action=Unsubscribe&SubscriptionArn=arn:aws:sns:ap-southeast-1:354285753755:bpt_01823072645:ddc1093b-2885-4179-ae8f-961577b564bd"
}' --header 'Acme-Webhook-Token: testToken@654321'

```

# python

```
import requests

url = "http://127.0.0.1:9000/webhook/"

payload = {
    "Type" : "Notification",
  "MessageId" : "20d48143-6af4-571d-b7cb-d211e6a2ac69",
  "TopicArn" : "arn:aws:sns:ap-southeast-1:354285753755:bpt_01823072645",
  "Message" :
       {
       "dateTime":"20180419122246",
       "debitMSISDN":"8801700000001",
       "creditOrganizationName":"Org 01",
       "creditShortCode":"ORG001",
       "trxID":"4J420ANOXC",
       "transactionStatus":"Completed",
       "transactionType":"1003",
       "amount":"100",
       "currency":"BDT",
       "transactionReference":"User inputed reference value." 
       },
  "Timestamp" : "2018-04-19T12:22:46.236Z",
  "SignatureVersion" : "1",
  "Signature" : "jZBoouSuStaUqYZY+mruc3r3ST58CPkzjOu8i65dDIReWDcNAvPGUpNDSCBBMVLLA6UIJ9KtvTmop+JefiAd/8+YOxR738j0AXDcWc0A4u1EaMWqnmLvFufC0rAkEQuHdzn+XpHSET8Vn9SsnDJMsmdnWIiqH6JDsuPImuzP6V4Fh9/EKOYVOSks5aNChD1fwPQ1Z6DmtpEVaEXKagWXO8yPPAgs5meDArV7qIm93devI3DzfJboF1DOqHL9JkIrj5S9+ZqybCNKl3ay1JkgY9BXPoRe3XCzUSd4zTXa6GDbH7+3KZ3wmsiaa2zfwYCmrFNvzuE5o6OkeNHE/mqyCA==",
  "SigningCertURL" : "https://sns.ap-southeast-1.amazonaws.com/SimpleNotificationService-ac565b8b1a6c5d002d285f9598aa1d9b.pem",
  "UnsubscribeURL" : "https://sns.ap-southeast-1.amazonaws.com/?Action=Unsubscribe&SubscriptionArn=arn:aws:sns:ap-southeast-1:354285753755:bpt_01823072645:ddc1093b-2885-4179-ae8f-961577b564bd"
 
}
headers = {
    "Accept": "application/json",
    "Acme-Webhook-Token": "testToken@654321"
}

response = requests.request("POST", url, json=payload, headers=headers)

print(response.text)

```



# curl 
```
curl -X POST http://127.0.0.1:9000/webhook/ -d '{ "yourdata": "Which data you want to send the webhook lister" }' --header 'Acme-Webhook-Token: testToken@654321'

```
# django-webhook


