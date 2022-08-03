import csv
from collections import defaultdict
import json
import os

dir_path = 'out'

os.makedirs(dir_path, exist_ok=True)

def convert_to_bool(str: str):
    return str.lower() == 'true' if str and len(str) > 0 else None

with open('list.csv') as csv_file:
    # Read csv - maybe input as a arg
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0  # For iterating through lines
    manufacturers = dict()  # Initialize manufacturers as a Dict
    models = list()  # Initialize models as a list
    parameters = dict()  # Initialize parameters as a dict

    for row in csv_reader:
        if line_count == 0:
            for param in row:
                parameters[param] = row.index(param)
        if line_count != 0:
            manufacturers[row[0]] = list()
        line_count += 1

    # Reset for second iteration
    line_count = 0
    csv_file.seek(0)

    # Output manufacturers list
    manufacturers_JSON = json.dumps(
        list(manufacturers.keys()), indent=4, sort_keys=True)
    with open(os.path.join(dir_path, 'manufacturers.json'), 'w') as outfile:
        outfile.write(manufacturers_JSON)

    for manufacturers_init in manufacturers:
        manufacturers[manufacturers_init] = list()

    # Second iteration of CSV for two JSON
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
            continue

        manufacturer = row[parameters.get('manufacturer')]
        name = row[parameters.get('name')]
        uas_class = row[parameters.get('class')]
        weight = row[parameters.get('weight')]
        max_takeoff = row[parameters.get('max_takeoff')]
        endurance = row[parameters.get('endurance')]
        has_camera = convert_to_bool(row[parameters.get('has_camera')])
        is_toy = convert_to_bool(row[parameters.get('is_toy')])

        models.append({'manufacturer': manufacturer, 'name': name, 'uas_class': uas_class,
                       "weight": weight, 'max_takeoff': max_takeoff, 'endurance': endurance, 'has_camera': has_camera, 'is_toy': is_toy})
        manufacturers[manufacturer].append({'name': name, 'uas_class': uas_class,
                                            "weight": weight, 'max_takeoff': max_takeoff, 'endurance': endurance, 'has_camera': has_camera, 'is_toy': is_toy})

        line_count += 1

    models_JSON = json.dumps(models, indent=4)
    with open(os.path.join(dir_path, 'models.json'), 'w') as outfile:
        outfile.write(models_JSON)

    manufacturers_JSON = json.dumps(manufacturers, indent=4)
    with open(os.path.join(dir_path, 'manufacturersWithModels.json'), 'w') as outfile:
        outfile.write(manufacturers_JSON)
