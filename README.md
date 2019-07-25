# Prettify JSON
The module need for print json-file in readable style.

# Quickstart

To print the json-file in readable form, pass it as a parameter.
For example: 
```bash
pprint_json.py example.json
```

### Example of script launch on Linux, Python 3.5:

```bash

$ python pprint_json.py <path to file>

{
    "features": [
        {
            "geometry": {
                "coordinates": [
                    37.39703804817934,
                    55.740999719549094
                ],
                "type": "Point"
            },
            "properties": {
                "DatasetId": 1854,
                "VersionNumber": 1,
                "ReleaseNumber": 2,
                "RowId": "79742784-9ef3-4543-bc98-a219a8903c18",
                "Attributes": {
                    "global_id": 14371450,
                    "Name": "Ароматный Мир",
                    "IsNetObject": "да",
                    "OperatingCompany": "Ароматный Мир",
                    "TypeService": "реализация продовольственных товаров",
                    "AdmArea": "Западный административный округ",
                    "District": "район Кунцево",
                    "Address": "улица Академика Павлова, дом 10",
                    "PublicPhone": [
                        {
                            "PublicPhone": "(495) 777-51-95"
                        }
                    ],
...

```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
