<p float="center">
  <img src="supplementary_files/geosea_logo.png" width="100%" />
  <img src="supplementary_files/vmasc-logo.png" width="100%" /> 
</p>

<img align="centre" src="supplementary_files/geosea_logo.png" width="100%">
<img align="centre" src="supplementary_files/vmasc-logo.png" width="100%">

# Virginia Data Cube Jupyter Notebooks

<img align="left" src="https://img.shields.io/badge/License-Apache%202.0-blue.svg">.


**License:** The code in this repository is licensed under the [Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0). **PLACEHOLDER** data is licensed under the [Creative Commons by Attribution 4.0 license](https://creativecommons.org/licenses/by/4.0/).

**Contact:** If you need assistance with any of the Jupyter Notebooks or Python code in this repository, please post a question on the [Open Data Cube Slack channel](http://slack.opendatacube.org/) or on the [GIS Stack Exchange](https://gis.stackexchange.com/questions/ask?tags=open-data-cube) using the `open-data-cube` tag (you can view `previously asked questions` [here](https://gis.stackexchange.com/questions/tagged/open-data-cube). If you would like to report an issue with this notebook, you can file one on the [Github issues page](https://https://github.com/GeoSEA-ODU/va-datacube/issues)

**PLACEHOLDER FOR CITING:** If you use any of the notebooks, code or tools in this repository in your work, please reference them using the following citation:

    **...CITATION**

---

The Virginia (VA) Data Cube Notebooks repository (`va-datacube`) hosts Jupyter Notebooks, Python scripts and workflows for analysing satellite data and derived products in Virginia. This documentation is designed to provide a guide to getting started with the Virginia Data Cube, and to showcase the wide range of geospatial analyses that can be achieved using VA Data Cube data and open-source software including [Open Data Cube](https://www.opendatacube.org/) and [xarray](http://xarray.pydata.org/en/stable/).

The repository is based around the following directory structure (from simple to increasingly complex applications):

1. [Beginners_guide](https://github.com/GeoSEA-ODU/va-datacube/tree/main/Beginners_guide): *Introductory notebooks aimed at introducing Jupyter Notebooks and how to load, plot and interact with Virginia data*

2. [Datasets](https://github.com/GeoSEA-ODU/va-datacube/tree/main/VA_datasets): *Notebooks introducing Virginia's satellite datasets and derived products, including how to load each dataset and any special features of the data. Some external datasets that are useful for analysing and interpreting Virginia products are also covered.*

3. [Frequently_used_code](https://github.com/GeoSEA-ODU/va-datacube/tree/main/Frequently_used_code): *A recipe book of simple code examples demonstrating how to perform common geospatial analysis tasks using open-source software*

4. [Real_world_examples](https://github.com/GeoSEA-ODU/va-datacube/tree/main/Real_world_examples): *More complex workflows demonstrating how the VA datacube can be used to address real-world problems*

5. [Tests](https://github.com/GeoSEA-ODU/va-datacube/tree/main/Scientific_workflows): *Notebooks in this collection are developed for specific use-cases of the VA datacube platform and may not run as seamlessly as notebooks in the other folders of this repository. Notebooks may contain less descriptive markdown, contain more complicated or bespoke analysis, and may take a long time to run. However, they contain useful analysis procedures and provide further examples for advanced users.*

6. [Scientific_workflows](https://github.com/GeoSEA-ODU/va-datacube/tree/main/Scientific_workflows): *Notebooks in this collection are developed for specific papers involving the VA datacube platform. Notebooks may contain more complicated analysesand may take a long time to run. However, in the interest of open science, these may prove useful for replication purposes.*

The supporting scripts and data for the notebooks are kept in the following directories:

- [Tools](https://github.com/GeoSEA-ODU/va-datacube/tree/main/Tools): *Python functions and algorithms developed to assist in analysing VA data (e.g. loading data, plotting, spatial analysis, machine learning)* 

- [Supplementary_data](https://github.com/GeoSEA-ODU/va-datacube/tree/main/Supplementary_data): *Supplementary files required for the analyses above (e.g. images, rasters, shapefiles, training data)*

---

## Getting started with Virginia Datacube Notebooks


To get started with using `va-datacube-notebooks`, visit the VA Datacube Notebooks [Wiki page](https://github.com/GeoSEA-ODU/va-datacube/wiki). This page includes guides for getting started on the [DE Africa Sandbox](https://github.com/digitalearthafrica/deafrica-sandbox-notebooks/wiki#getting-started-on-the-de-africa-sandbox).

Once you're set up, the main option for interacting with `va-datacube` and contributing back to the repository is through:

* **Virginia Datacube notebooks using Git:** Git is a version-control software designed to help track changes to files and collaborate with multiple users on a project. Using ``git`` is the recommended workflow for working with ``va-datacube`` as it makes it easy to stay up to date with the latest versions of functions and code, and makes it impossible to lose your work. 

  * Refer to the repository's [Guide to using VA Datacube Notebooks with git](https://github.com/digitalearthafrica/deafrica-sandbox-notebooks/wiki/Guide-to-using-DE-Africa-Notebooks-with-git) wiki article. For a more detailed explanation suited to new Git users, see our [Version Control with Git](https://docs.digitalearthafrica.org/en/latest/sandbox/git-howto/index.html) tutorial.
  
* **Set up Git authentication tokens:** Git requires multi-factor authentication when using the command line or API. Set up a personal access token by following instructions from the [GitHub Docs](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token).

---

## Contributing to VA Datacube Notebooks

### Main and working branches

The `va-datacube` repository uses 'branches' to manage individuals' notebooks, and to allow easy publishing of notebooks ready to be shared. There are three main types of branches:

* [Main branch](https://github.com/GeoSEA-ODU/va-datacube/tree/main): The ``main`` branch contains VA's collection of publicly available notebooks. The ``main`` branch is protected, and is only updated after new commits are reviewed and approved by the VA Datacube team.
* [Dev and website branches](https://github.com/GeoSEA-ODU/va-datacube/tree/dev): The ``dev`` branch is a development part of our tree. This is a highly experimental branch and is not recommended to ever fork information from this branch. The ``website`` branch includes content related to future web development on this github.
* [Working branches](https://github.com/GeoSEA-ODU/va-datacube/branches): All other branches in the repository are working spaces for users of ``va-datacube``. They have a unique name (typically named after the user). The notebooks on these branches can be works-in-progress and do not need to be pretty or complete. By using a working branch, it is easy to use scripts and algorithms from ``va-datacube` in your own work, or share and collaborate on a working version of a notebook or code.

--- 
### Publishing notebooks to the main branch


Once you have a notebook that is ready to be published on the ``main`` branch, you can submit a 'pull request' in the [Pull requests tab at the top of the repository](https://github.com/GeoSEA-ODU/va-datacube/pulls). The default pull request template contains a check-list to ensure that all ``main`` branch Jupyter notebooks are consistent and well-documented so they can be understood by future users, and rendered correctly. Please ensure that as many of these checklist items are complete as possible, or leave a comment in the pull request asking for help with any remaining checklist items.

#### Draft pull requests

For pull requests you would like help with or that are a work in progress, consider using Github's [draft pull request](https://github.blog/2019-02-14-introducing-draft-pull-requests/) feature. This indicates that your work is still a draft, allowing you to get feedback from other VA datacube users before it is published on the `main` branch.

---
### DE Africa Notebooks template notebook

A template notebook has been developed to make it easier to create new notebooks that meet all the pull request checklist requirements. The template notebook contains a simple structure and useful general advice on writing and formatting Jupyter notebooks. The template can be found here: [Template_General.ipynb](https://github.com/GeoSEA-ODU/va-datacube/blob/Steiner-VA-Cube-Notebooks/Template_General.ipynb)

Using the template is not required for working branch notebooks, but is *highly recommended* as it will make it much easier to publish any notebooks on ``main`` in the future.

---
### Approving pull requests

Anyone with admin access to the ``va-datacube`` repository can approve 'pull requests'.

If the notebook meets all the checklist requirements, click the green 'Review' button and click 'Approve' (with an optional comment). You can also 'Request changes' here if any of the checklist items are not complete.

Once the pull request has been approved, you can merge it into the ``main`` branch. Select the 'Squash and merge' option from the drop down menu to the right of the green 'merge' button. Once you have merged the new branch in, you need to delete the branch. There is a button on the page that asks you if you would like to delete the now merged branch. Select 'Yes' to delete it.

```
git branch -m master main
git fetch origin
git branch -u origin/main main
git remote set-head origin -a
```
