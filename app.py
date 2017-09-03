#!/usr/bin/env python

import urllib
import json
import os
import random

from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

    print("Request:")
    print(json.dumps(req, indent=4))

    res = makeWebhookResult(req)

    res = json.dumps(res, indent=4)
    print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

def makeWebhookResult(req):
    if req.get("result").get("action") != "action.marketfacts":
        return {}
    result = req.get("result")
    parameters = result.get("parameters")
    supplier = parameters.get("v-supplier")
    infosys_fact = ["Infosys Fact1","Infosys Fact 2", "InfosysFact 3", "Infosys Fact 4","Infosys Fact 5"]
    cognizant_fact = ["Cognizant Fact 1","Cognizant Fact 2", "Cognizant Fact 3", "Cognizant Fact 4","Cognizant Fact 5"]
    ibm_fact = ["IBM Fact 1","IBM Fact 2", "IBM Fact 3", "IBM Fact 4","IBM Fact 4"]
    # Select the Supplier 
    if supplier == "Infosys":
        fact = random.choice(infosys_fact)            
    elif supplier =="Cognizant":
        fact = random.choice(cognizant_fact)
        # select a random fact from Cognizant List
    elif supplier == "IBM":
        fact = random.choice(ibm_fact)
        #select a random fact from IBM list
    else:
        fact = "No supplier fact available"
 
    speech = fact

    print("Response:")
    print(speech)

    return {
        "speech": speech,
        "displayText": speech,
        #"data": {},
        # "contextOut": [],
        "source": "apiai-vendor-market-facts"
    }


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

   # print "Starting app on port %d" % port

    app.run(debug=True, port=port, host='0.0.0.0')
