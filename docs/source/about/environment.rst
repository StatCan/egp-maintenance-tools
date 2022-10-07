***********
Environment
***********

.. contents:: Contents:
   :depth: 4


Software
========

Data Editing
------------

- `QGIS <https://www.qgis.org/en/site/forusers/download.html>`_: Open source GIS application.

Repository Management and Script Usage
--------------------------------------

- `Git <https://git-scm.com/downloads>`_: Version control system for tracking code changes and collaborative
  development.
- `conda <https://docs.anaconda.com/anaconda/install/>`_: Virtual environment and package manager.

Repository
==========

The repository is the root directory containing all files and code for a project. This project's repository is named
``egp-editing-tools``.

``Git`` is used for repository management. ``Git`` allows you to fetch content from a remote repository (GitHub in this
case) and integrate the differences into your local repository.

Installation
------------

1. Change directory to the desired installation location::

    cd /d C:/

2. Install the repository::

    git clone https://github.com/StatCan/egp-editing-tools.git

Updates
-------

1. Change directory to the repository root::

    cd /d C:/egp-editing-tools

2. Fetch and integrate updates::

    git pull

Virtual Environment
===================

All scripts within the ``egp-editing-tools`` repository are intended to be executed within a ``conda`` virtual
environment. The ``conda`` environment is defined within an ``environment.yml`` file within the ``egp-editing-tools``
repository.

``conda`` is an environment and package manager and is used by the ``egp-editing-tools`` repository to provide an
isolated processing environment and effective dependency management. The ``conda`` environment must be activated before
executing any scripts in order to make use of the contained dependencies.

Installation
------------

Install the ``conda`` environment via::

    conda env create -f C:/egp-editing-tools/environment.yml

Activation
----------

Activate the ``conda`` environment via::

    conda activate egp-editing-tools

Updates
-------

Update the ``conda`` environment via (only required if dependencies change)::

    conda env update -f C:/egp-editing-tools/environment.yml --prune

