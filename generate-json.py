import pandas as pd
sheet = pd.read_excel('/Users/monier/Documents/Jahia/Demo/DSFR/dsfrgouv-pictograms.xlsx')

json_array = [{

        "value": {
            "type": "String",
            "value": row['value']  # Assuming 'value' is the column name in your Excel
        },
        "displayValue": row['displayValue'],  # Assuming 'displayValue' is the column name
        "propertyList": [{
            "name": "image",
            "value": row['propertyList.value']  # Adjust the column name as needed
        }]

} for index, row in sheet.iterrows()]

import json
with open('output_file.json', 'w') as f:
    json.dump(json_array, f, indent=4)
