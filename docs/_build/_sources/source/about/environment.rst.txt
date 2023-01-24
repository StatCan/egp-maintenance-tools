***********
Environment
***********

.. contents:: Contents:
   :depth: 4


Software
========

Data Editing and Tool Implementation
------------------------------------

- `QGIS <https://www.qgis.org/en/site/forusers/download.html>`_: Open source GIS application.

Repository Management and Script Usage
--------------------------------------

- `Git <https://git-scm.com/downloads>`_: Version control system for tracking code changes and collaborative
  development.
- `conda <https://docs.anaconda.com/anaconda/install/>`_: Virtual environment and package manager.

.. admonition:: conda setup

    ``conda`` installation may require the following additions to the ``Path`` environment variable in order for
    ``conda`` to be recognized as a valid command:

    - C:\\ProgramData\\Anaconda3
    - C:\\ProgramData\\Anaconda3\\Library\\bin
    - C:\\ProgramData\\Anaconda3\\Scripts

Repository
==========

The repository is the root directory containing all files and code for a project. This project's repository is named
``egp-maintenance-tools``.

``Git`` is used for repository management. ``Git`` allows you to fetch content from a remote repository (GitHub in this
case) and integrate the differences into your local repository.

Installation
------------

1. Change directory to the desired installation location::

    cd /d C:/

2. Install the repository::

    git clone https://github.com/StatCan/egp-maintenance-tools.git

Updates
-------

1. Change directory to the repository root::

    cd /d C:/egp-maintenance-tools

2. Fetch and integrate updates::

    git pull

Virtual Environment
===================

All scripts within the ``egp-maintenance-tools`` repository are intended to be executed within a ``conda`` virtual
environment. The ``conda`` environment is defined within an ``environment.yml`` file within the
``egp-maintenance-tools`` repository.

``conda`` is an environment and package manager and is used by the ``egp-maintenance-tools`` repository to provide an
isolated processing environment and effective dependency management. The ``conda`` environment must be activated before
executing any scripts in order to make use of the contained dependencies.

Installation
------------

Install the ``conda`` environment via::

    conda env create -f C:/egp-maintenance-tools/environment.yml

Activation
----------

Activate the ``conda`` environment via::

    conda activate egp-maintenance-tools

Updates
-------

Update the ``conda`` environment via (only required if dependencies change)::

    conda env update -f C:/egp-maintenance-tools/environment.yml --prune

Documentation
=============

Documentation is written in reStructuredText (RST), a markup language developed for technical documentation
(specifically Python projects), and rendered as HTML via ``sphinx``. Updates to documentation requires a rebuild with
the ``sphinx-build`` command-line tool using the following parameters::

    sphinx-build -b html egp-crn/docs egp-crn/docs/_build

.. admonition:: Note

    Various warnings and errors may be logged during the documentation build. These are not always an indication of
    true errors and can largely be ignored so long as the resulting documentation actually gets built correctly.
