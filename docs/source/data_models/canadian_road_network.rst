*********************
Canadian Road Network
*********************

.. contents:: Contents:
   :depth: 2

Diagram
=======

.. figure:: /source/_static/data_models/canadian_road_network/canadian_road_network-primary_datasets.svg
    :alt: Canadian Road Network diagram (primary datasets).

    Figure: Canadian Road Network diagram (primary datasets).

.. figure:: /source/_static/data_models/canadian_road_network/canadian_road_network-lookup_datasets.svg
    :alt: Canadian Road Network diagram (lookup datasets).

    Figure: Canadian Road Network diagram (lookup datasets).

Constraints
===========

.. figure:: /source/_static/data_models/canadian_road_network/canadian_road_network-constraints.svg
    :alt: Canadian Road Network constraints.

    Figure: Canadian Road Network constraints.

Domains
=======

.. figure:: /source/_static/data_models/canadian_road_network/canadian_road_network-domains.svg
    :alt: Canadian Road Network domains.

    Figure: Canadian Road Network domains.

Data Dictionary
===============

acquisition_technique_lookup
----------------------------

Code-value lookup dataset for acquisition technique.

.. csv-table::
   :header: "Attribute", "Nullable", "Unique", "Default", "Description"
   :widths: auto
   :align: left

   "code", False, True, "", "Concise code used in place of a more descriptive value."
   "value_en", False, True, "", "English version of the descriptive value."
   "value_fr", False, True, "", "French version of the descriptive value."

.. csv-table:: Domains
   :header: "code", "value_en", "value_fr", "Description"
   :widths: auto
   :align: left

   -1, "Unknown", "Inconnu", "Value is unknown."
   0, "None", "Aucun", "No value applies."
   1, "Other", "Autre", "Other value."
   2, "GPS", "GPS", "Data collected using a GPS device."
   3, "Orthoimage", "Ortho-image", "Satellite imagery orthorectified."
   4, "Orthophoto", "Ortho-photo", "Aerial photo orthorectified."
   5, "Vector Data", "Données vectorielles", "Vector digital data."
   6, "Paper Map", "Carte papier", "Conventional sources of information like maps or plans."
   7, "Field Completion", "Complètement terrain", "Information gathered from people directly on the field."
   8, "Raster Data", "Données matricielles", "Data resulting from a scanning process."
   9, "Digital Elevation Model", "Modèle numérique d'élévation", "Data coming from a Digital Elevation Model (DEM)."
   10, "Aerial Photo", "Photographie aérienne", "Aerial photography not orthorectified."
   11, "Raw Imagery Data", "Image satellite brute", "Satellite imagery not orthorectified."
   12, "Computed", "Calculé", "Geometric information that has been computed (not captured)."

address_range
-------------

A set of attributes representing the address of the first and last building located along the side of the entire road
or a portion of it.

.. csv-table::
   :header: "Attribute", "Nullable", "Unique", "Default", "Description"
   :widths: auto
   :align: left

   TODO - add content from constraints and below attribute descriptions, then delete individual attribute sections.

address_range_id
^^^^^^^^^^^^^^^^

Unique identifier of each record.

first_house_number
^^^^^^^^^^^^^^^^^^

The first house number address.

first_house_number_suffix
^^^^^^^^^^^^^^^^^^^^^^^^^

A non-integer value, such as a fraction or a character that follows the first house number address.

first_house_number_type
^^^^^^^^^^^^^^^^^^^^^^^

The method used to populate the first house number address.

last_house_number
^^^^^^^^^^^^^^^^^

The last house number address.

last_house_number_suffix
^^^^^^^^^^^^^^^^^^^^^^^^

A non-integer value, such as a fraction or a character that follows the last house number address.

last_house_number_type
^^^^^^^^^^^^^^^^^^^^^^

The method used to populate the last house number address.

house_number_structure
^^^^^^^^^^^^^^^^^^^^^^

The numbering structure of the address range.

reference_system_indicator
^^^^^^^^^^^^^^^^^^^^^^^^^^

The particular addressing system of the address range.

acquisition_technique
^^^^^^^^^^^^^^^^^^^^^

The type of data source or technique used to populate (create or revise) the dataset.

provider
^^^^^^^^

The affiliation of the organization that provided the original or revised dataset contents.

creation_date
^^^^^^^^^^^^^

The date of data creation.

revision_date
^^^^^^^^^^^^^

The date of data revision.

basic_block
-----------

Geographic areas formed by all roads and boundaries in :ref:`segment`.

.. csv-table::
   :header: "Attribute", "Nullable", "Unique", "Default", "Description"
   :widths: auto
   :align: left

   TODO - add content from constraints and below attribute descriptions, then delete individual attribute sections.

bb_uid
^^^^^^

Unique identifier of each record.

cb_uid
^^^^^^

Unique identifier of the corresponding census block.

blocked_passage
---------------

Indication of a physical barrier on a road built to prevent or control further access.

.. csv-table::
   :header: "Attribute", "Nullable", "Unique", "Default", "Description"
   :widths: auto
   :align: left

   TODO - add content from constraints and below attribute descriptions, then delete individual attribute sections.

blocked_passage_id
^^^^^^^^^^^^^^^^^^

Unique identifier of each record.

segment_id
^^^^^^^^^^

Unique identifier of the corresponding road.

blocked_passage_type
^^^^^^^^^^^^^^^^^^^^

The type of blocked passage.

acquisition_technique
^^^^^^^^^^^^^^^^^^^^^

The type of data source or technique used to populate (create or revise) the dataset.

planimetric_accuracy
^^^^^^^^^^^^^^^^^^^^

The planimetric accuracy expressed in meters as the circular map accuracy standard (CMAS).

provider
^^^^^^^^

The affiliation of the organization that provided the original or revised dataset contents.

creation_date
^^^^^^^^^^^^^

The date of data creation.

revision_date
^^^^^^^^^^^^^

The date of data revision.

blocked_passage_type_lookup
---------------------------

Code-value lookup dataset for blocked passage type.

.. csv-table::
   :header: "Attribute", "Nullable", "Unique", "Default", "Description"
   :widths: auto
   :align: left

   "code", False, True, "", "Concise code used in place of a more descriptive value."
   "value_en", False, True, "", "English version of the descriptive value."
   "value_fr", False, True, "", "French version of the descriptive value."

.. csv-table:: Domains
   :header: "code", "value_en", "value_fr", "Description"
   :widths: auto
   :align: left

   TODO

closing_period_lookup
---------------------

Code-value lookup dataset for closing period.

.. csv-table::
   :header: "Attribute", "Nullable", "Unique", "Default", "Description"
   :widths: auto
   :align: left

   "code", False, True, "", "Concise code used in place of a more descriptive value."
   "value_en", False, True, "", "English version of the descriptive value."
   "value_fr", False, True, "", "French version of the descriptive value."

.. csv-table:: Domains
   :header: "code", "value_en", "value_fr", "Description"
   :widths: auto
   :align: left

   TODO

crossing
--------

All intersection points involving 4 or more roads, used for the identification of grade separated intersections
(overpasses). This dataset exists for the maintenance of a routable road network whereby roads in the completely
segmented :ref:`segment` dataset can be dissolved into single features if, in reality, they are contiguous and
intersect at-grade.

.. csv-table::
   :header: "Attribute", "Nullable", "Unique", "Default", "Description"
   :widths: auto
   :align: left

   TODO - add content from constraints and below attribute descriptions, then delete individual attribute sections.

crossing_id
^^^^^^^^^^^

Unique identifier of each record.

crossing_status
^^^^^^^^^^^^^^^

The type of crossing.

crossing_order
^^^^^^^^^^^^^^

The number of roads connected to the crossing point.

creation_date
^^^^^^^^^^^^^

The date of data creation.

revision_date
^^^^^^^^^^^^^

The date of data revision.

crossing_status_lookup
----------------------

Code-value lookup dataset for crossing status.

.. csv-table::
   :header: "Attribute", "Nullable", "Unique", "Default", "Description"
   :widths: auto
   :align: left

   "code", False, True, "", "Concise code used in place of a more descriptive value."
   "value_en", False, True, "", "English version of the descriptive value."
   "value_fr", False, True, "", "French version of the descriptive value."

.. csv-table:: Domains
   :header: "code", "value_en", "value_fr", "Description"
   :widths: auto
   :align: left

   TODO

ferry
-----

The average route of a ferryboat which transports vehicles.

.. csv-table::
   :header: "Attribute", "Nullable", "Unique", "Default", "Description"
   :widths: auto
   :align: left

   TODO - add content from constraints and below attribute descriptions, then delete individual attribute sections.

ferry_id
^^^^^^^^

Unique identifier of each record.

closing_period
^^^^^^^^^^^^^^

The period in which the road or ferry is not available to the public.

functional_road_class
^^^^^^^^^^^^^^^^^^^^^

A classification based on the role that the road or ferry performs in the connectivity of the road network.

province
^^^^^^^^

Province or Territory where the feature is located.

acquisition_technique
^^^^^^^^^^^^^^^^^^^^^

The type of data source or technique used to populate (create or revise) the dataset.

planimetric_accuracy
^^^^^^^^^^^^^^^^^^^^

The planimetric accuracy expressed in meters as the circular map accuracy standard (CMAS).

provider
^^^^^^^^

The affiliation of the organization that provided the original or revised dataset contents.

creation_date
^^^^^^^^^^^^^

The date of data creation.

revision_date
^^^^^^^^^^^^^

The date of data revision.

functional_road_class_lookup
----------------------------

Code-value lookup dataset for functional road class.

.. csv-table::
   :header: "Attribute", "Nullable", "Unique", "Default", "Description"
   :widths: auto
   :align: left

   "code", False, True, "", "Concise code used in place of a more descriptive value."
   "value_en", False, True, "", "English version of the descriptive value."
   "value_fr", False, True, "", "French version of the descriptive value."

.. csv-table:: Domains
   :header: "code", "value_en", "value_fr", "Description"
   :widths: auto
   :align: left

   TODO

house_number_structure_lookup
-----------------------------

Code-value lookup dataset for house number structure.

.. csv-table::
   :header: "Attribute", "Nullable", "Unique", "Default", "Description"
   :widths: auto
   :align: left

   "code", False, True, "", "Concise code used in place of a more descriptive value."
   "value_en", False, True, "", "English version of the descriptive value."
   "value_fr", False, True, "", "French version of the descriptive value."

.. csv-table:: Domains
   :header: "code", "value_en", "value_fr", "Description"
   :widths: auto
   :align: left

   TODO

house_number_type_lookup
------------------------

Code-value lookup dataset for house number type.

.. csv-table::
   :header: "Attribute", "Nullable", "Unique", "Default", "Description"
   :widths: auto
   :align: left

   "code", False, True, "", "Concise code used in place of a more descriptive value."
   "value_en", False, True, "", "English version of the descriptive value."
   "value_fr", False, True, "", "French version of the descriptive value."

.. csv-table:: Domains
   :header: "code", "value_en", "value_fr", "Description"
   :widths: auto
   :align: left

   TODO

junction
--------

A feature bounding one or more roads or ferries. A junction is defined at the intersection of three or more roads, at
the junction of a road and a ferry, at the end of a dead end road, and at the junction of a road or ferry with a
National, Provincial or Territorial Boundary.

.. csv-table::
   :header: "Attribute", "Nullable", "Unique", "Default", "Description"
   :widths: auto
   :align: left

   TODO - add content from constraints and below attribute descriptions, then delete individual attribute sections.

junction_id
^^^^^^^^^^^

Unique identifier of each record.

junction_type
^^^^^^^^^^^^^

The classification of the junction.

exit_number
^^^^^^^^^^^

The identifying number of an exit on a controlled access thoroughfare.

province
^^^^^^^^

Province or Territory where the feature is located.

acquisition_technique
^^^^^^^^^^^^^^^^^^^^^

The type of data source or technique used to populate (create or revise) the dataset.

planimetric_accuracy
^^^^^^^^^^^^^^^^^^^^

The planimetric accuracy expressed in meters as the circular map accuracy standard (CMAS).

provider
^^^^^^^^

The affiliation of the organization that provided the original or revised dataset contents.

creation_date
^^^^^^^^^^^^^

The date of data creation.

revision_date
^^^^^^^^^^^^^

The date of data revision.

junction_type_lookup
--------------------

Code-value lookup dataset for junction type.

.. csv-table::
   :header: "Attribute", "Nullable", "Unique", "Default", "Description"
   :widths: auto
   :align: left

   "code", False, True, "", "Concise code used in place of a more descriptive value."
   "value_en", False, True, "", "English version of the descriptive value."
   "value_fr", False, True, "", "French version of the descriptive value."

.. csv-table:: Domains
   :header: "code", "value_en", "value_fr", "Description"
   :widths: auto
   :align: left

   TODO

language_code_lookup
--------------------

Code-value lookup dataset for language code.

.. csv-table::
   :header: "Attribute", "Nullable", "Unique", "Default", "Description"
   :widths: auto
   :align: left

   "code", False, True, "", "Concise code used in place of a more descriptive value."
   "value_en", False, True, "", "English version of the descriptive value."
   "value_fr", False, True, "", "French version of the descriptive value."

.. csv-table:: Domains
   :header: "code", "value_en", "value_fr", "Description"
   :widths: auto
   :align: left

   TODO

provider_lookup
---------------

Code-value lookup dataset for provider.

.. csv-table::
   :header: "Attribute", "Nullable", "Unique", "Default", "Description"
   :widths: auto
   :align: left

   "code", False, True, "", "Concise code used in place of a more descriptive value."
   "value_en", False, True, "", "English version of the descriptive value."
   "value_fr", False, True, "", "French version of the descriptive value."

.. csv-table:: Domains
   :header: "code", "value_en", "value_fr", "Description"
   :widths: auto
   :align: left

   TODO

province_lookup
---------------

Code-value lookup dataset for province.

.. csv-table::
   :header: "Attribute", "Nullable", "Unique", "Default", "Description"
   :widths: auto
   :align: left

   "code", False, True, "", "Concise code used in place of a more descriptive value."
   "value_en", False, True, "", "English version of the descriptive value."
   "value_fr", False, True, "", "French version of the descriptive value."

.. csv-table:: Domains
   :header: "code", "value_en", "value_fr", "Description"
   :widths: auto
   :align: left

   TODO

reference_system_indicator_lookup
---------------------------------

Code-value lookup dataset for reference system indicator.

.. csv-table::
   :header: "Attribute", "Nullable", "Unique", "Default", "Description"
   :widths: auto
   :align: left

   "code", False, True, "", "Concise code used in place of a more descriptive value."
   "value_en", False, True, "", "English version of the descriptive value."
   "value_fr", False, True, "", "French version of the descriptive value."

.. csv-table:: Domains
   :header: "code", "value_en", "value_fr", "Description"
   :widths: auto
   :align: left

   TODO

road_surface_type_lookup
------------------------

Code-value lookup dataset for road surface type.

.. csv-table::
   :header: "Attribute", "Nullable", "Unique", "Default", "Description"
   :widths: auto
   :align: left

   "code", False, True, "", "Concise code used in place of a more descriptive value."
   "value_en", False, True, "", "English version of the descriptive value."
   "value_fr", False, True, "", "French version of the descriptive value."

.. csv-table:: Domains
   :header: "code", "value_en", "value_fr", "Description"
   :widths: auto
   :align: left

   TODO

route_name
----------

A set of attributes representing a particular route name in the road network.

.. csv-table::
   :header: "Attribute", "Nullable", "Unique", "Default", "Description"
   :widths: auto
   :align: left

   TODO - add content from constraints and below attribute descriptions, then delete individual attribute sections.

route_name_id
^^^^^^^^^^^^^

Unique identifier of each record.

route_name_en
^^^^^^^^^^^^^

The official English version of the route name.

route_name_fr
^^^^^^^^^^^^^

The official French version of the route name.

creation_date
^^^^^^^^^^^^^

The date of data creation.

revision_date
^^^^^^^^^^^^^

The date of data revision.

route_name_link
---------------

A dataset facilitating plural linkages of roads and ferries with a particular route name in the road network.

.. csv-table::
   :header: "Attribute", "Nullable", "Unique", "Default", "Description"
   :widths: auto
   :align: left

   TODO - add content from constraints and below attribute descriptions, then delete individual attribute sections.

route_name_link_id
^^^^^^^^^^^^^^^^^^

Unique identifier of each record.

segment_id
^^^^^^^^^^

Unique identifier of the corresponding road or ferry.

route_name_id
^^^^^^^^^^^^^

Unique identifier of the corresponding route name.

route_number
------------

A set of attributes representing a particular route number in the road network.

.. csv-table::
   :header: "Attribute", "Nullable", "Unique", "Default", "Description"
   :widths: auto
   :align: left

   TODO - add content from constraints and below attribute descriptions, then delete individual attribute sections.

route_number_id
^^^^^^^^^^^^^^^

Unique identifier of each record.

route_number
^^^^^^^^^^^^

The official route number.

creation_date
^^^^^^^^^^^^^

The date of data creation.

revision_date
^^^^^^^^^^^^^

The date of data revision.

route_number_link
-----------------

A dataset facilitating plural linkages of roads and ferries with a particular route number in the road network.

.. csv-table::
   :header: "Attribute", "Nullable", "Unique", "Default", "Description"
   :widths: auto
   :align: left

   TODO - add content from constraints and below attribute descriptions, then delete individual attribute sections.

route_number_link_id
^^^^^^^^^^^^^^^^^^^^

Unique identifier of each record.

segment_id
^^^^^^^^^^

Unique identifier of the corresponding road or ferry.

route_number_id
^^^^^^^^^^^^^^^

Unique identifier of the corresponding route number.

.. _segment:

segment
-------

A road or boundary feature with uniform characteristics. A road is a linear section of the earth designed for or the
result of vehicular movement. A boundary is a non-road forming an administrative, statistical, or non-standard
geographic area.

.. csv-table::
   :header: "Attribute", "Nullable", "Unique", "Default", "Description"
   :widths: auto
   :align: left

   TODO - add content from constraints and below attribute descriptions, then delete individual attribute sections.

segment_id
^^^^^^^^^^

Unique identifier of each record.

segment_id_left
^^^^^^^^^^^^^^^

Unique identifier of the left side of each feature.

segment_id_right
^^^^^^^^^^^^^^^^

Unique identifier of the right side of each feature.

element_id
^^^^^^^^^^

Non-unique identifier used to identify contiguous road features which share an official street name and municipality.

routable_element_id
^^^^^^^^^^^^^^^^^^^

Non-unique identifier used to identify contiguous road features which intersect at-grade via :ref:`crossing` points.

segment_type
^^^^^^^^^^^^

The classification of the feature.

exit_number
^^^^^^^^^^^

The identifying number of an exit on a controlled access thoroughfare.

speed_restriction
^^^^^^^^^^^^^^^^^

The maximum speed allowed on the road, expressed in kilometers per hour.

number_of_lanes
^^^^^^^^^^^^^^^

The number of lanes existing on the road (combined total from each direction).

road_jurisdiction
^^^^^^^^^^^^^^^^^

The agency with the responsibility / authority to ensure maintenance occurs but is not necessarily the one who
undertakes the maintenance directly.

closing_period
^^^^^^^^^^^^^^

The period in which the road or ferry is not available to the public.

functional_road_class
^^^^^^^^^^^^^^^^^^^^^

A classification based on the role that the road or ferry performs in the connectivity of the road network.

traffic_direction
^^^^^^^^^^^^^^^^^

The direction(s) of traffic flow allowed on the road.

road_surface_type
^^^^^^^^^^^^^^^^^

The type of surface covering a road.

structure_id
^^^^^^^^^^^^

Unique identifier of the corresponding structure.

bb_uid_l
^^^^^^^^

Unique identifier of the corresponding basic block on the left side of each feature.

bb_uid_r
^^^^^^^^

Unique identifier of the corresponding basic block on the right side of each feature.

acquisition_technique
^^^^^^^^^^^^^^^^^^^^^

The type of data source or technique used to populate (create or revise) the dataset.

planimetric_accuracy
^^^^^^^^^^^^^^^^^^^^

The planimetric accuracy expressed in meters as the circular map accuracy standard (CMAS).

provider
^^^^^^^^

The affiliation of the organization that provided the original or revised dataset contents.

creation_date
^^^^^^^^^^^^^

The date of data creation.

revision_date
^^^^^^^^^^^^^

The date of data revision.

segment_type_lookup
-------------------

Code-value lookup dataset for segment type.

.. csv-table::
   :header: "Attribute", "Nullable", "Unique", "Default", "Description"
   :widths: auto
   :align: left

   "code", False, True, "", "Concise code used in place of a more descriptive value."
   "value_en", False, True, "", "English version of the descriptive value."
   "value_fr", False, True, "", "French version of the descriptive value."

.. csv-table:: Domains
   :header: "code", "value_en", "value_fr", "Description"
   :widths: auto
   :align: left

   TODO

street_article_lookup
---------------------

Code-value lookup dataset for street article.

.. csv-table::
   :header: "Attribute", "Nullable", "Unique", "Default", "Description"
   :widths: auto
   :align: left

   "code", False, True, "", "Concise code used in place of a more descriptive value."
   "value_en", False, True, "", "English version of the descriptive value."
   "value_fr", False, True, "", "French version of the descriptive value."

.. csv-table:: Domains
   :header: "code", "value_en", "value_fr", "Description"
   :widths: auto
   :align: left

   TODO

street_direction_lookup
-----------------------

Code-value lookup dataset for street direction.

.. csv-table::
   :header: "Attribute", "Nullable", "Unique", "Default", "Description"
   :widths: auto
   :align: left

   "code", False, True, "", "Concise code used in place of a more descriptive value."
   "value_en", False, True, "", "English version of the descriptive value."
   "value_fr", False, True, "", "French version of the descriptive value."

.. csv-table:: Domains
   :header: "code", "value_en", "value_fr", "Description"
   :widths: auto
   :align: left

   TODO

street_name
-----------

A set of attributes representing a particular street name in the road network.

.. csv-table::
   :header: "Attribute", "Nullable", "Unique", "Default", "Description"
   :widths: auto
   :align: left

   TODO - add content from constraints and below attribute descriptions, then delete individual attribute sections.

street_name_id
^^^^^^^^^^^^^^

Unique identifier of each record.

street_name_concatenated
^^^^^^^^^^^^^^^^^^^^^^^^

The official concatenation of all components of the street name.

.. _street_direction_prefix:

street_direction_prefix
^^^^^^^^^^^^^^^^^^^^^^^

A geographic direction that is part of the street name and precedes the :ref:`street_name_body`.

.. _street_type_prefix:

street_type_prefix
^^^^^^^^^^^^^^^^^^

The portion of the street name identifying the street type and precedes the :ref:`street_name_body`.

.. _street_article:

street_article
^^^^^^^^^^^^^^

An article that is part of the street name and precedes the :ref:`street_name_body`.

.. _street_name_body:

street_name_body
^^^^^^^^^^^^^^^^

The portion of the street name that has the most identifying power, excluding the :ref:`street_direction_prefix`,
:ref:`street_direction_suffix`, :ref:`street_type_prefix`, :ref:`street_type_suffix`, and :ref:`street_article`.

.. _street_type_suffix:

street_type_suffix
^^^^^^^^^^^^^^^^^^

The portion of the street name identifying the street type and succeeds the :ref:`street_name_body`.

.. _street_direction_suffix:

street_direction_suffix
^^^^^^^^^^^^^^^^^^^^^^^

A geographic direction that is part of the street name and succeeds the :ref:`street_name_body`.

creation_date
^^^^^^^^^^^^^

The date of data creation.

revision_date
^^^^^^^^^^^^^

The date of data revision.

street_name_link
----------------

A dataset facilitating plural linkages of roads with a particular street name in the road network.

.. csv-table::
   :header: "Attribute", "Nullable", "Unique", "Default", "Description"
   :widths: auto
   :align: left

   TODO - add content from constraints and below attribute descriptions, then delete individual attribute sections.

street_name_link_id
^^^^^^^^^^^^^^^^^^^

Unique identifier of each record.

segment_id
^^^^^^^^^^

Unique identifier of the corresponding road.

street_name_id
^^^^^^^^^^^^^^

Unique identifier of the corresponding street name.

street_name_translation
-----------------------

A set of attributes representing a recognized translation of a particular street name in the road network.

.. csv-table::
   :header: "Attribute", "Nullable", "Unique", "Default", "Description"
   :widths: auto
   :align: left

   TODO - add content from constraints and below attribute descriptions, then delete individual attribute sections.

street_name_translation_id
^^^^^^^^^^^^^^^^^^^^^^^^^^

Unique identifier of each record.

street_name_id
^^^^^^^^^^^^^^

Unique identifier of the corresponding street name.

street_name_concatenated
^^^^^^^^^^^^^^^^^^^^^^^^

The official concatenation of all components of the street name.

language_code
^^^^^^^^^^^^^

Three-letter code identifying the language of the street name translation in accordance with ISO 639-3.

creation_date
^^^^^^^^^^^^^

The date of data creation.

revision_date
^^^^^^^^^^^^^

The date of data revision.

street_type_lookup
------------------

Code-value lookup dataset for street type.

.. csv-table::
   :header: "Attribute", "Nullable", "Unique", "Default", "Description"
   :widths: auto
   :align: left

   "code", False, True, "", "Concise code used in place of a more descriptive value."
   "value_en", False, True, "", "English version of the descriptive value."
   "value_fr", False, True, "", "French version of the descriptive value."

.. csv-table:: Domains
   :header: "code", "value_en", "value_fr", "Description"
   :widths: auto
   :align: left

   TODO

structure
---------

A set of attributes representing a particular structure in the road network.

.. csv-table::
   :header: "Attribute", "Nullable", "Unique", "Default", "Description"
   :widths: auto
   :align: left

   TODO - add content from constraints and below attribute descriptions, then delete individual attribute sections.

structure_id
^^^^^^^^^^^^

Unique identifier of each record.

structure_type
^^^^^^^^^^^^^^

The classification of a structure.

structure_name_en
^^^^^^^^^^^^^^^^^

The official English version of the structure name.

structure_name_fr
^^^^^^^^^^^^^^^^^

The official French version of the structure name.

creation_date
^^^^^^^^^^^^^

The date of data creation.

revision_date
^^^^^^^^^^^^^

The date of data revision.

structure_type_lookup
---------------------

Code-value lookup dataset for structure type.

.. csv-table::
   :header: "Attribute", "Nullable", "Unique", "Default", "Description"
   :widths: auto
   :align: left

   "code", False, True, "", "Concise code used in place of a more descriptive value."
   "value_en", False, True, "", "English version of the descriptive value."
   "value_fr", False, True, "", "French version of the descriptive value."

.. csv-table:: Domains
   :header: "code", "value_en", "value_fr", "Description"
   :widths: auto
   :align: left

   TODO

toll_point
----------

Place where a right-of-way is charged to gain access to a road.

.. csv-table::
   :header: "Attribute", "Nullable", "Unique", "Default", "Description"
   :widths: auto
   :align: left

   TODO - add content from constraints and below attribute descriptions, then delete individual attribute sections.

toll_point_id
^^^^^^^^^^^^^

Unique identifier of each record.

segment_id
^^^^^^^^^^

Unique identifier of the corresponding road.

toll_point_type
^^^^^^^^^^^^^^^

The type of toll point.

acquisition_technique
^^^^^^^^^^^^^^^^^^^^^

The type of data source or technique used to populate (create or revise) the dataset.

planimetric_accuracy
^^^^^^^^^^^^^^^^^^^^

The planimetric accuracy expressed in meters as the circular map accuracy standard (CMAS).

provider
^^^^^^^^

The affiliation of the organization that provided the original or revised dataset contents.

creation_date
^^^^^^^^^^^^^

The date of data creation.

revision_date
^^^^^^^^^^^^^

The date of data revision.

toll_point_type_lookup
----------------------

Code-value lookup dataset for toll point type.

.. csv-table::
   :header: "Attribute", "Nullable", "Unique", "Default", "Description"
   :widths: auto
   :align: left

   "code", False, True, "", "Concise code used in place of a more descriptive value."
   "value_en", False, True, "", "English version of the descriptive value."
   "value_fr", False, True, "", "French version of the descriptive value."

.. csv-table:: Domains
   :header: "code", "value_en", "value_fr", "Description"
   :widths: auto
   :align: left

   TODO

traffic_direction_lookup
------------------------

Code-value lookup dataset for traffic direction.

.. csv-table::
   :header: "Attribute", "Nullable", "Unique", "Default", "Description"
   :widths: auto
   :align: left

   "code", False, True, "", "Concise code used in place of a more descriptive value."
   "value_en", False, True, "", "English version of the descriptive value."
   "value_fr", False, True, "", "French version of the descriptive value."

.. csv-table:: Domains
   :header: "code", "value_en", "value_fr", "Description"
   :widths: auto
   :align: left

   TODO
