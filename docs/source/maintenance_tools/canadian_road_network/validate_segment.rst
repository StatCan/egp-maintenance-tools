****************
Validate Segment
****************

.. contents:: Contents:
   :depth: 2

Overview
========

Applies a series of validations against dataset: ``segment``. Once all failed validations have been resolved, the
script will write the following updates to the database:

* Insert records into ``basic_block`` representing polygons newly formed by dataset ``segment``.
* Drop records from ``basic_block`` representing polygons no longer formed by dataset ``segment``.
* Update ``segment`` - ``basic_block`` identifier linkages (``bb_uid_l`` and ``bb_uid_r``) to reflect ``basic_block``
  updates.

Resources
=========

| **Script:** ``validate_segment.py``
| **QGIS File:** ``validate_segment.qgz``

Validations
===========

100 - Construction
------------------

**Description:** Validations pertaining to the construction of individual geometries.

101 - Zero Length
^^^^^^^^^^^^^^^^^

| **Description:** TODO - copy description from corresponding function in python script (just description, not parameter details).
| **Resolution:** TODO - steps to resolve.

102 - Simple
^^^^^^^^^^^^

| **Description:** TODO - copy description from corresponding function in python script (just description, not parameter details).
| **Resolution:** TODO - steps to resolve.

103 - Cluster Tolerance
^^^^^^^^^^^^^^^^^^^^^^^

| **Description:** TODO - copy description from corresponding function in python script (just description, not parameter details).
| **Resolution:** TODO - steps to resolve.

200 - Duplication
-----------------

**Description:** Validations pertaining to the partial or complete duplication of geometries.

201 - Duplicated
^^^^^^^^^^^^^^^^

| **Description:** TODO - copy description from corresponding function in python script (just description, not parameter details).
| **Resolution:** TODO - steps to resolve.

202 - Overlap
^^^^^^^^^^^^^

| **Description:** TODO - copy description from corresponding function in python script (just description, not parameter details).
| **Resolution:** TODO - steps to resolve.

300 - Connectivity
------------------

**Description:** Validations pertaining to the connectivity between different geometries.

301 - Node Intersection
^^^^^^^^^^^^^^^^^^^^^^^

| **Description:** TODO - copy description from corresponding function in python script (just description, not parameter details).
| **Resolution:** TODO - steps to resolve.

302 - Segmentation
^^^^^^^^^^^^^^^^^^

| **Description:** TODO - copy description from corresponding function in python script (just description, not parameter details).
| **Resolution:** TODO - steps to resolve.

400 - Meshblock
---------------

**Description:** Validations pertaining to the polygonization of arcs.

401 - Count
^^^^^^^^^^^

| **Description:** TODO - copy description from corresponding function in python script (just description, not parameter details).
| **Resolution:** TODO - steps to resolve.

402 - Boundary
^^^^^^^^^^^^^^

| **Description:** TODO - copy description from corresponding function in python script (just description, not parameter details).
| **Resolution:** TODO - steps to resolve.
