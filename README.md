# OpenDroneList

OpenDroneList is a public open-source community-driven list of drones and their common properties.

## What is **OpenDroneList** good for?

Thanks to various output formats, including the human-readable HTML table, or computer-readable CSV, JSONs and others, the list can be used for developing your own applications or to use for your data analysis or other projects.

We, [authors](https://dronetag.cz), use opendronelist in many systems and user interfaces requiring the same or similar data — for example when you pick pre-defined drone in our mobile app or when using [Dronald](https://dronald.cz), we always query the latest data from the opendronelist to show a list of known drones and their properties.

## Currently available properties

- **Manufacturer & Model Name**
  - The commercial name of the drone
- **Class**
  - UAV Class label designated for the drone (labels such as C0, C1, ...)
- **Weight**
  - The nominal weight of the drone from the manufacturer specifications
  - in grams
- **Max. takeoff weight**
  - The maximum allowed takeoff weight of the drone
  - Usually used to determine the drone's weight category
  - in grams
- **Endurance**
  - The nominal maximum flight time of the drone
  - in minutes
- **Has Camera?**
  - Determines if the drone is equipped with a camera
- **Is Toy?**
  - Determines if the drone is classified as a toy
  - Drones are regarded as a toy if the drone documentation allows the use of the drone for children below 14 years of age according to Directive 2009/48/ES

## Formats available

The list is avilable in following output formats:

- [CSV Format](./list.csv)
- JSON Format
  - Manufacturers
    - Isolated array of unique manufacturers specified in the CSV
    - Download [here](https://github.com/dronetag/opendronelist/releases/latest/download/manufacturers.json)
  - Models
    - An array of models, with data about the models - (manufacturer, name, weight, ...)
    - Download [here](https://github.com/dronetag/opendronelist/releases/latest/download/models.json)
  - Manufacturers with Models
    - An array of unique manufacturers and all of their models which are specified in the CSV
    - Download [here](https://github.com/dronetag/opendronelist/releases/latest/download/manufacturersWithModels.json)

## Guaranties & Liability

Since this is a community-driven project, we cannot guarantee the correctness and completeness of the data, even though we try to keep the list always up to date and as correct as possible. Refer to our [license](./LICENSE.MD) when in doubt about liability applied when using our list.

---

Opendronelist is maintained by the team behind [Dronetag](https://dronetag.cz)