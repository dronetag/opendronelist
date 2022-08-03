import csv
import os
from jinja2 import Environment, PackageLoader
import shutil

env = Environment(loader=PackageLoader('html_convertor', 'templates'))

template = env.get_template("template.html.jinja")

dir_path = 'out'

def convert_to_bool(str: str):
    return str.lower() == 'true' if str and len(str) > 0 else None

os.makedirs(dir_path, exist_ok=True)
with open('list.csv') as csv_file:
    # Read csv - maybe input as a arg
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0  # For iterating through lines
    manufacturers = dict()  # Initialize manufacturers as a Dict
    models = list()  # Initialize models as a list
    parameters = dict()  # Initialize parameters as a dict

    for row in csv_reader:
        for param in row:  # only first row with parameters is necessary
            parameters[param] = row.index(param)
        break

    # Reset for second iteration
    line_count = 0
    csv_file.seek(0)

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

        line_count += 1

    with open(os.path.join(dir_path, 'index.html'), 'w') as outfile:
        outfile.write(template.render(models=models))
    try:  # throws an error of file being in the folder, even in case of empty folder, nevertheless, the files are copied
        shutil.copy('templates/styles.css', 'out/styles.css')
        shutil.copytree('templates/fonts', 'out/fonts')
    except:
        pass
