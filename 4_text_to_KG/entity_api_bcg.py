#-*- coding:utf-8 -*-

import urllib3
import json
 
openApiURL = "http://aiopen.etri.re.kr:8000/WiseNLU"
 
accessKey = "8212eb54-f2fc-4926-a794-136726174880"
analysisCode = "ANALYSIS_CODE"
text = ""
 
text += "\corpus_bcg_toyexam_refined.tok_colab.tsv"
requestJson = {
    "access_key": accessKey,
    "argument": {
        "text": text,
        "analysis_code": analysisCode
    }
}
 
http = urllib3.PoolManager()
response = http.request(
    "POST",
    openApiURL,
    headers={"Content-Type": "application/json; charset=UTF-8"},
    body=json.dumps(requestJson)
)
 
print("[responseCode] " + str(response.status))
print("[responBody]")
print(str(response.data,"utf-8"))