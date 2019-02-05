## nifi-cdsw
Example Apache NiFi to CDSW

### Command line test

curl -H "Content-Type: application/json" -X POST http://cdsw-hdp-3.vpc.cloudera.com/api/altus-ds-1/models/call-model -d '{"accessKey":"mzpu8j7kav775mkrcw0vug6skqxzcvxz","request":{"sentence":"This is great"}}'


### Example Input

{
  "sentence": "This is great"
}

### Sample Response

{
    "result": "positive"
}

### Build Script

cdsw-build.sh


### File

sentiment.py

### Function

sentiment

### Kernel

Python 3

