# Contributing Guide

Welcome to the opendronelist contribution guide, we're glad you've decided to join our efforts to make a complete open list of all existing drones.

To learn about how the project works, refer to the [README.md](./README.md) file, where it's briefly described.

---

## Reporting an issue or feature request

If you see an error in the data or the output pipeline, you can open [an issue](https://github.com/dronetag/opendronelist/issues) and describe the problem you see or experience.

The same goes if you have any idea for improvements – issues can be marked as "feature requests".

If you decide to open a new issue, please follow these steps:

* First, check if there is not an issue with the same problem already opened
* State if the issue is related to the data, or code (bugs), or anything else (miss-spells, ...)
* Make sure you describe the issue thoroughly, specify all available details and tell us how to reproduce the problem

Even though reporting an issue is much appreciated, even more helpful action is to try to fix the issue by contributing to the project directly. See the next section for details.

### Example of a correct issue

> Issue Name:  
> Wrong weight specified on Pan-1 drone
> ___
> Description:  
> The drone model Harald Pan-1 has according to the official specifications on the official website has endurance of 35 minutes, not 32 minutes.
> See the source of the information on their website at https://harald-drones.example.com/pan-1/specifications

---

## Contributing to the repository

If you're willing to contribute by making changes to the project, but you're not sure if you recognized the issue correctly or what's the best approach to resolving the issue, it's always the best practice to open the issue first, to start a discussion, and then offer to work on the issue.

The recommended steps for contributing a change on GitHub is following:

- Fork the repository to your account
- Make the changes in your repository
- Submit a pull request from your repository to the opendronelist repository

Learn more about contributing to public open-source project [on the official GitHub Docs](https://docs.github.com/en/get-started/quickstart/contributing-to-projects).

### Opening a pull request

When opening a pull request, please try to keep in mind the following instructions:

- Write a meaningful pull request title so everyone knows what your PR is about
- Always write a short description about the changes you've made. Doesn't have to be long, just sum up what should be expect from your contribution and what's the result.
- If you can, select a reviewer for your PR to get faster attention to your contribution.

### Expanding the drone database

To add new drones, or correct errors in the current data, you can help us by editing the source database.

The data are present in the [**`list.csv`**](./list.csv) file, and it's the source file which is later converted to all the other outputs (such as HTML, JSON, ...)

Keep in mind the following:

- Make sure you keep the CSV valid after your changes.
- When creating the pull request, mention the source of the data.
- Do not add or remove columns from the CSV file (a change in the convertors is needed).

### Making changes to the convertors

You can always create a new output format to be converted from the source CSV file.

Use the `convertors/` directory to create a new conversion script. Don't forget trigger the conversion in GitHub Actions, by making changes to the `.github/workflows/release.yml` workflow.

Keep in mind the following:

- Usually we don't allow changing the current output formats in a non-reverse-compatible way, such as removing columns/fields/properties or renaming them.
- When opening a pull request, please describe the motivation behind creating a new output format.

---

## Final words

Thank you for contributing to the project or even just considering to do so. We're glad there are people willing to help open-source projects!