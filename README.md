## nifi-cdsw
Example Apache NiFi to CDSW

### Command line test

curl -H "Content-Type: application/json" -X POST http://cdsw-hdp-3.place.com/api/altus-ds-1/models/call-model -d '{"accessKey":"mazpusdfa9dfs0d8f9sadf9s8fd09sa09fda0sd8f09a8sdf","request":{"sentence":"This is great"}}'


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

## source
https://github.com/tspannhw/nlp-utilities

