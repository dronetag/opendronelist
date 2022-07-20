# How to contribute

Please follow the instructions according to however you wish to contribute

## Contribute to the drone database

The following instructions are for changes only in the csv file - expansion of the database, expansion of information for listed models, or correcting the information in the models

* Fork the repository
* Make some changes to the csv file
* Submit a pull request to the project owner

### Information in the Pull Request (PR)
* Name of the PR:
  * Choose a category - New manufacturer / New model / New information / Model information
  * In case of more categories present in the PR enumerate all of them and split them with commas
* Description of the PR
  * Briefly introduce the introduced changes
  * If possible, please supply us with some resources, on which the changes are based, this will make the review process much faster

Example:
> Name: New manufacturer, New model
> ___
> Description:
> Added a new manufacturer called Harald and added their new model Pan-1 with its parameters
> 
> The information is based on the specifications found [here](https://damekolu.cz/)

____

## Reporting issues

* Check if there is not an issue with the same problem already opened
* If not open an issue
  * Please choose if issue is with data, code (bugs), or anything else (miss-spells, ...)

In the issue description please tell us about the issue
* If you think that there is a problem with the data, you can either
  * Contribute with the information according to the **Contribute to the drone database** chapter
  * Open an issue with some link on which your assumption that the data is not correct is based upon

Example
> Name: Wrong weight of the 
> ___
> Desription:
> The drone model Harald Pan-1 has according to the [specifications](https://damekolu.cz/) endurance of 35 minutes, not 32 minutes

____

## Contribute to the source code

The following instructions are 

* Fork the repository
* Make your changes to the code
* Submit a pull request to the project owner

### Information in the Pull Request (PR)
* Name of the PR:
  * Choose a category - ci / fix / feat
  * Add a brief description of changes - (3 - 10 words)
* Description of the PR
  * Briefly introduce the introduced changes - Why were they introduced, how do they work, ... 

Example:
> Name: ci: added a cute cat gif to the release
> ___
> Description:
> Added a line in the Github Actions workflow, that adds a random cat gif to every new release. 
> The changes were introduces, because i felt like there was not enough cats in the repository.
