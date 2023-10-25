# PROCESSING JSON WITH PYTHON
import json
data = """{
    "name": "Chuck",
    "phone": {
        "type": "intl",
        "number": "+1 734 303 4456"
    },
    "email": {
        "hide": "yes"
    }
}"""

info = json.loads(data)
print(info['name'])
print(info['email']['hide'])

