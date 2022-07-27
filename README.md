# opendronelist

A public community-driven list of drones and their common properties

> 💬  
> Repository and API is currently in development, if you have a use-case and would like to help, let's get in touch.  
> marian@dronetag.cz

## Properties

- Name of Manufacturer
- Name of Model
- Type of Model
- Class of Model
- Weight of Model
- Max Takeoff Weight of Model
- Endurance of Model
- If Model has Camera
- If Model is Toy

## Formats available

The list is avilable in CSV file which is then converted into three JSON files:

- Manufacturers
  - An array of unique manufacturers specified in the CSV
  - Download [here](https://github.com/dronetag/opendronelist/releases/latest/download/manufacturers.json)
- Models
  - An array of models, with data about the models - (manufacturer, name, weight, ...)
  - Download [here](https://github.com/dronetag/opendronelist/releases/latest/download/models.json)
- Manufacturers with Models
  - An array of unique manufacturers and all of their models which are specified in the CSV
  - Download [here](https://github.com/dronetag/opendronelist/releases/latest/download/manufacturersWithModels.json)

## Who use opendronelist

We, [authors](https://dronetag.cz), use opendronelist in almost all our systems.
