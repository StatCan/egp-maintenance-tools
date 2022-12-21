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

Acquisistion Technique Lookup
-----------------------------
**UNKNOWN**

Address Range
-------------
A set of attributes representing the address of the first and last building located along the side of the entire Road
Element or a portion of it.

Address Range ID
^^^^^^^^^^^^^^^^

First House Number (left, right)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The first house number address value along a particular side (left or right) of a Road Element. A specific value is
defined for the left and right sides of the Road Element.

First House Number Suffix (left,right)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
A non-integer value, such as a fraction or a character that sometimes follows the house number address value.
A specific value is defined for the left and right sides of the Road Element.

First House Number Type
^^^^^^^^^^^^^^^^^^^^^^^
Method used to populate the address range. A specific value is defined for the left and right sides of the Road Element.

**table**

Last House Number
^^^^^^^^^^^^^^^^^
The last house number address value along a particular side (left or right) of a Road Element. A specific value is
defined for the left and right sides of the Road Element.

Last House Number Suffix
^^^^^^^^^^^^^^^^^^^^^^^^
A non-integer value, such as a fraction or a character that sometimes follows the house number address value.
A specific value is defined for the left and right sides of the Road Element.

Last House Number Type
^^^^^^^^^^^^^^^^^^^^^^
Method used to populate the address range. A specific value is defined for the left and right sides of the Road Element.

**table**

House Number Structure
^^^^^^^^^^^^^^^^^^^^^^
The type of house numbering (or address numbering) method applied to one side of a particular Road Element. A specific
value is defined for the left and right sides of the Road Element.

**table**

Reference System Indicator
^^^^^^^^^^^^^^^^^^^^^^^^^^
An indication of whether the physical address of all or a portion of a Road Element is based on a particular addressing
system. A specific value is defined for the left and right sides of the Road Element.

**table**

Acquisition Technique
^^^^^^^^^^^^^^^^^^^^^
The type of data source or technique used to populate (create or revise) the dataset.

.. _Acquisition Technique:
**table**

Provider
^^^^^^^^
The affiliation of the organization that generated (created or revised) the object.

**table**

Creation Date
^^^^^^^^^^^^^^

revision_date
^^^^^^^^^^^^^
A date in the format YYYYMMDD. If the month or the day is unknown, corresponding characters are left blank. The value
"0" is used when no value applies.

basic_block
-----------

bb_uid
^^^^^^

cb_uid
^^^^^^

blocked_passage
---------------
Indication of a physical barrier on a Road Element built to prevent or control further access.

blocked_passage_id
^^^^^^^^^^^^^^^^^^
**UNKNOWN**

segment_id
^^^^^^^^^^
**UNKNOWN**

blocked_passage_type
^^^^^^^^^^^^^^^^^^^^
The type of blocked passage as an indication of the fact whether it is removable.

.. csv-table::
   :header: "Code", "Label", "Definition"
   :widths: auto
   :align: left

 1, "Permanently Fixed", "The barrier cannot be removed without destroying it. Heavy equipment needed in order to
   allow further access. Examples of permanently fixed blocked passage are concrete blocks or a mound of earth."
   2, "Removable", "The barrier is designed to free the entrance to the (other side of the) Road Element that it is
   blocking. Further access easily allowed when so desired."

acquisition_technique
^^^^^^^^^^^^^^^^^^^^
**Duplicate**


planimetric_accuracy
^^^^^^^^^^^^^^^^^^^^
The planimetric accuracy expressed in meters as the circular map accuracy standard (CMAS)

Provider
^^^^^^^^
**Duplicate**

Creation Date
^^^^^^^^^^^^^
**Duplicate**

revision_date
^^^^^^^^^^^^^^
**Duplicate**

blocked_passage_type_lookup
---------------------------

closing_period_lookup
---------------------

crossing
--------
**UNKNOWN**

crossing_id
^^^^^^^^^^^
**UNKNOWN**

crossing_status
^^^^^^^^^^^^^^^
**UNKNOWN**

crossing_order
^^^^^^^^^^^^^^
**UNKNOWN**

Creation Date
^^^^^^^^^^^^^
**Duplicate**

revision_date
^^^^^^^^^^^^^
**Duplicate**

crossing_status_lookup
----------------------

functional_road_class_lookup
----------------------------

house_number_structure_lookup
-----------------------------

house_number_type_lookup
------------------------

junction
--------
A feature that bounds a Road Element or a Ferry Connection. A Road Element or Ferry Connection always forms a
connection between two Junctions and, a Road Element or Ferry Connection is always bounded by exactly two Junctions. A
Junction Feature represents the physical connection between its adjoining Road Elements or Ferry Connections. A
Junction is defined at the intersection of three or more roads, at the junction of a road and a ferry, at the end of a
dead end road and at the junction of a road or ferry with a National, Provincial or Territorial Boundary.

junction_id
^^^^^^^^^^^

segment_id
^^^^^^^^^^

toll_point_type
^^^^^^^^^^^^^^^
The type of toll point.

acquisistion_type
^^^^^^^^^^^^^^^^^
**Duplicate**

planimetric_accuracy
^^^^^^^^^^^^^^^^^^^^^
**Duplicate**

provider
^^^^^^^^
**Duplicate**

Creation Date
^^^^^^^^^^^^^
**Duplicate**

revision_date
^^^^^^^^^^^^^^
**Duplicate**

junction_type_lookup
--------------------

language_code_lookup
--------------------

provider_lookup
---------------

province_lookup
---------------

reference_system_indicator_lookup
---------------------------------

route_name
--------

route_name_id
^^^^^^^^^^^^^

route_name_en
^^^^^^^^^^^^^
The English version of a name of a particular route in a given road network as attributed by a national or subnational
agency. A particular Road Segment or Ferry Connection Segment can belong to more than one named route. In such cases,
it has multiple route name attributes.

route_name_fr
^^^^^^^^^^^^^
The French version of a name of a particular route in a given road network as attributed by a national or subnational
agency. A particular Road Segment or Ferry Connection Segment can belong to more than one named route. In such cases,
it has multiple route name attributes.

Creation Date
^^^^^^^^^^^^^
**Duplicate**

revision_date
^^^^^^^^^^^^^
**Duplicate**

route_name_link
---------------

route_name_link_id
^^^^^^^^^^^^^^^^^^

segment_id
^^^^^^^^^^

route_name_id
^^^^^^^^^^^^^^

route_number
------------

route_number_id
^^^^^^^^^^^^^^^

route_number
^^^^^^^^^^^^
The ID number of a particular route in a given road network as attributed by a national or subnational agency. A
particular Road Segment or Ferry Connection Segment can belong to more than one numbered route. In such cases, it has
multiple route number attributes.

creation_date
^^^^^^^^^^^^^
**Duplicate**

revision_date
^^^^^^^^^^^^^
**Duplicate**

route_number_link
-----------------

route_number_id
^^^^^^^^^^^^^^^

route_number
^^^^^^^^^^^^
**Duplicate**

Creation Date
^^^^^^^^^^^^^^
**Duplicate**

revision_date
^^^^^^^^^^^^^
**Duplicate**

Segment
------

segment_id
^^^^^^^^^^^

segment_id_left
^^^^^^^^^^^^^^^^

segment_id_right
^^^^^^^^^^^^^^^^

element_id
^^^^^^^^^^^

routable_element_id
^^^^^^^^^^^^^^^^^^^

segment_type
^^^^^^^^^^^

exit_number
^^^^^^^^^^^
The ID number of an exit on a controlled access thoroughfare that has been assigned by an administrating body.

speed
^^^^^
The maximum speed allowed on the road. The value is expressed in kilometers per hour.

number_of_lanes
^^^^^^^^^^^^^^^
The number of lanes existing on a Road Element.

road_jurisdiction
^^^^^^^^^^^^^^^^
The agency with the responsibility/authority to ensure maintenance occurs but is not necessarily the one who undertakes
the maintenance directly.

closing_period
^^^^^^^^^^^^^^
The period in which the road or ferry connection is not available to the public.
**table**

functional_road_class
^^^^^^^^^^^^^^^^^^^^^
A classification based on the importance of the role that the Road Element or Ferry Connection performs in the
connectivity of the total road network.
**table**

traffic_direction
^^^^^^^^^^^^^^^^^
The direction(s) of traffic flow allowed on the road.
**table**

road_surface_type
^^^^^^^^^^^^^^
The type of surface a road element has.
**table**

structure_id
^^^^^^^^^^^^

address_range_id_left
^^^^^^^^^^^^^^^^^^^^^^

address_range_id_right
^^^^^^^^^^^^^^^^^^^^^^

bb_uid_l
^^^^^^^^

bb_uid_r
^^^^^^^^

acquisition_technique
^^^^^^^^^^^^^^^^^^^^^
**Duplicate**


planimetric_accuracy
^^^^^^^^^^^^^^^^^^^^
**Duplicate**

provider
^^^^^^^^
**Duplicate**


Creation Date
^^^^^^^^^^^^^
**Duplicate**

revision_date
^^^^^^^^^^^^^
**Duplicate**

segment_type_lookup
--------------------

street_article_lookup
--------------------

street_direction_lookup
-----------------------

street_name
-----------

street_name_id
^^^^^^^^^^^^^^

street_name_concatenated
^^^^^^^^^^^^^^^^^^^^^^^^
A concatenation of the officially recognized Directional prefix, Street type prefix, Street name article, Street name
body, Street type suffix, Directional suffix and Muni quadrant values.

street_direction_prefix
^^^^^^^^^^^^^^^^^^^^^^^
A geographic direction that is part of the street name and precedes the street name body or, if appropriate, the street
type prefix.
**table**

street_type_prefix
^^^^^^^^^^^^^^^^^^
A part of the street name of a Road Element identifying the street type. A prefix precedes the street name body of a
Road Element.
**table**

street_article
^^^^^^^^^^^^^^
Article(s) that is/are part of the street name and located at the beginning.
**table**

street_name_body
^^^^^^^^^^^^^^^^
The portion of the street name (either official or alternate) that has the most identifying power excluding street type
and directional prefixes or suffixes and street name articles.

street_type_suffix
^^^^^^^^^^^^^^^^^^
A part of the street name of a Road Element identifying the street type. A suffix follows the street name body of a
Road Element.
**table**

street_direction_suffix
^^^^^^^^^^^^^^^^^^^^^^^
A geographic direction that is part of the street name and succeeds the street name body or, if appropriate, the street
type suffix.

**table**

Creation Date
^^^^^^^^^^^^
**Duplicate**

revision_date
^^^^^^^^^^^^^
**Duplicate**

street_name_link
----------------

street_name_link_id
^^^^^^^^^^^^^^^^^^^

segment_id
^^^^^^^^^^

street_name_id
^^^^^^^^^^^^^^

street_name_translation
-----------------------

street_name_translation_id
^^^^^^^^^^^^^^^^^^^^^^^^^^

street_name_id
^^^^^^^^^^^^^^

street_name_concatenated
^^^^^^^^^^^^^^^^^^^^^^^^^
**Duplicate**

language_code
^^^^^^^^^^^^^

Creation Date
^^^^^^^^^^^^^
**Duplicate**

revision_date
^^^^^^^^^^^^^
**Duplicate**

street type lookup
------------------

Structure
---------

structure_id
^^^^^^^^^^^^^
A national unique identifier assigned to the Road Segment or the set of adjoining Road Segments forming a structure.
This identifier allows for the reconstitution of a structure that is fragmented by Junctions.

structure_type
^^^^^^^^^^^^^^^
The classification of a structure.
**table**

structure_name_en
^^^^^^^^^^^^^^^^^
The English version of the name of a road structure as assigned by a national or subnational agency.

structure_name_fr
^^^^^^^^^^^^^^^^^
The French version of the name of a road structure as assigned by a national or subnational agency.

creation_date
^^^^^^^^^^^^^
**Duplicate**

revision_date
^^^^^^^^^^^^^
**Duplicate**

structure type lookup
---------------------

toll point
----------
Place where right-of-way is charged to gain access to a motorway, a bridge, etc.

toll point id
^^^^^^^^^^^^^

segment id
-----------

toll point type
^^^^^^^^^^^^^^^
The type of toll point.
**table**

acquistion_technique
^^^^^^^^^^^^^^^^^^^^
**Duplicate**

planimetric_accuracy
^^^^^^^^^^^^^^^^^^^^
**Duplicate**

provider
^^^^^^^^^
**Duplicate**

Creation Date
^^^^^^^^^^^^^^
**Duplicate**

creation_type
^^^^^^^^^^^^^
**Duplicate**

toll_point_type_lookup
-----------------------

traffic_direction_lookup
------------------------






















Attribute Name
^^^^^^^^^^^^^^

Description of attribute.

.. csv-table::
   :header: "Code", "Label", "Definition"
   :widths: auto
   :align: left

   ...placeholder for table - only populate for attributes with domains...

Dataset Name
------------

Description of dataset.

Attribute Name
^^^^^^^^^^^^^^

Description of attribute.