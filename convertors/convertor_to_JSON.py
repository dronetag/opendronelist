import csv
from collections import defaultdict
import json


with open('../list.csv') as csv_file:
    # Read csv - maybe input as a arg
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0  # For iterating through lines
    manufacturers = dict()  # Initialize manufacturers as a Dict
    models = list()  # Initialize models as a list
    parameters = dict()  # Initialize parameters as a dict

    # First iteration - gets unique manufacturers
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
    with open('manufacturers.json', 'w') as outfile:
        outfile.write(manufacturers_JSON)

    # Initializes manufacturers to a dictionary where every manufacturer has its own empty list, which is then filled in next steps
    for manufacturers_init in manufacturers:
        manufacturers[manufacturers_init] = list()

    # Second iteration of CSV for two JSON
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
            continue

        # read the values and assign them to variables - searched according to index value of the parameter
        manufacturer = row[parameters.get('manufacturer')]
        name = row[parameters.get('name')]
        type = row[parameters.get('type')]
        uas_class = row[parameters.get('class')]
        weight = row[parameters.get('weight')]
        max_takeoff = row[parameters.get('max_takeoff')]
        endurance = row[parameters.get('endurance')]
        has_camera = row[parameters.get('has_camera')]
        is_toy = row[parameters.get('is_toy')]

        # Append model to the big list
        models.append({'manufacturer': manufacturer, 'name': name, 'type': type, 'uas_class': uas_class,
                       "weight": weight, 'max_takeoff': max_takeoff, 'endurance': endurance, 'has_camera': has_camera, 'is_toy': is_toy})

        # Append drone to the correct manufacturer list
        manufacturers[manufacturer].append({'name': name, 'type': type, 'uas_class': uas_class,
                                            "weight": weight, 'max_takeoff': max_takeoff, 'endurance': endurance, 'has_camera': has_camera, 'is_toy': is_toy})

        line_count += 1

    # Spit out JSON with big list of models
    models_JSON = json.dumps(models, indent=4)
    with open('models.json', 'w') as outfile:
        outfile.write(models_JSON)

    # Spit out JSON with big list of vendors and their models
    manufacturers_JSON = json.dumps(manufacturers, indent=4)
    with open('manufacturersWithModels.json', 'w') as outfile:
        outfile.write(manufacturers_JSON)
