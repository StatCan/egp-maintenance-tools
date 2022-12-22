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

Acquisition Technique Lookup
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

.. csv-table::
   :header: "Code", "Label", "Definition"
   :widths: auto
   :align: left

   0, "None", "Absence of a house along the Road Element."
   1, "Actual Located", "Qualifier indicating that the house number is located at its ""real world"" position along a
   Road Element."
   2, "Actual Unlocated", "Qualifier indicating that the house number is located at one end of the Road Element. This
   may be or may not be its ""real world"" position."
   3, "Projected", "Qualifier indicating that the house number is planned, figured or estimated for the future and is
   located (at one end) at the beginning or the end of the Road Element."
   4, "Interpolated", "Qualifier indicating that the house number is calculated from two known house numbers which are
   located on either side. By convention, the house is positioned at one end of the Road Element."

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

**Same as first house number type**

House Number Structure
^^^^^^^^^^^^^^^^^^^^^^
The type of house numbering (or address numbering) method applied to one side of a particular Road Element. A specific
value is defined for the left and right sides of the Road Element.

.. csv-table::
   :header: "Code", "Label", "Definition"
   :widths: auto
   :align: left

Reference System Indicator
^^^^^^^^^^^^^^^^^^^^^^^^^^
An indication of whether the physical address of all or a portion of a Road Element is based on a particular addressing
system. A specific value is defined for the left and right sides of the Road Element.

.. csv-table::
   :header: "Code", "Label", "Definition"
   :widths: auto
   :align: left

Acquisition Technique
^^^^^^^^^^^^^^^^^^^^^
The type of data source or technique used to populate (create or revise) the dataset.

.. csv-table::
   :header: "Code", "Label", "Definition"
   :widths: auto
   :align: left

Provider
^^^^^^^^
The affiliation of the organization that generated (created or revised) the object.

.. csv-table::
   :header: "Code", "Label", "Definition"
   :widths: auto
   :align: left

Creation Date
^^^^^^^^^^^^^^
The date of data creation.

Revision Date
^^^^^^^^^^^^^
The date of data revision.

Basic Block
-----------

bb uid
^^^^^^

cb uid
^^^^^^

Blocked Passage
---------------
Indication of a physical barrier on a Road Element built to prevent or control further access.

Blocked Passage id
^^^^^^^^^^^^^^^^^^
**UNKNOWN**

Segment id
^^^^^^^^^^
**UNKNOWN**

Blocked Passage Type
^^^^^^^^^^^^^^^^^^^^
The type of blocked passage as an indication of the fact whether it is removable.

.. csv-table::
   :header: "Code", "Label", "Definition"
   :widths: auto
   :align: left

   1, "Permanently Fixed", "The barrier cannot be removed without destroying it. Heavy equipment needed in order to allow further access. Examples of permanently fixed blocked passage are concrete blocks or a mound of earth."
   2, "Removable", "The barrier is designed to free the entrance to the (other side of the) Road Element that it is blocking. Further access easily allowed when so desired."

Acquisition Technique
^^^^^^^^^^^^^^^^^^^^
**Duplicate**

Planimetric Accuracy
^^^^^^^^^^^^^^^^^^^^
The planimetric accuracy expressed in meters as the circular map accuracy standard (CMAS)

Provider
^^^^^^^^
**Duplicate**

Creation Date
^^^^^^^^^^^^^
**Duplicate**

Revision Date
^^^^^^^^^^^^^^
**Duplicate**

Blocked Passage Type Lookup
---------------------------

Closing Period Lookup
---------------------

crossing
--------
**UNKNOWN**

Crossing id
^^^^^^^^^^^
**UNKNOWN**

Crossing Status
^^^^^^^^^^^^^^^
**UNKNOWN**

Crossing Order
^^^^^^^^^^^^^^
**UNKNOWN**

Creation Date
^^^^^^^^^^^^^
**Duplicate**

Revision Date
^^^^^^^^^^^^^
**Duplicate**

Crossing Status Lookup
----------------------

Functional Road Class lookup
----------------------------

House Number Structure lookup
-----------------------------

House Number Type Lookup
------------------------

Junction
--------
A feature that bounds a Road Element or a Ferry Connection. A Road Element or Ferry Connection always forms a
connection between two Junctions and, a Road Element or Ferry Connection is always bounded by exactly two Junctions. A
Junction Feature represents the physical connection between its adjoining Road Elements or Ferry Connections. A
Junction is defined at the intersection of three or more roads, at the junction of a road and a ferry, at the end of a
dead end road and at the junction of a road or ferry with a National, Provincial or Territorial Boundary.

Junction id
^^^^^^^^^^^

Segment id
^^^^^^^^^^

Toll Point Type
^^^^^^^^^^^^^^^
The type of toll point.

.. csv-table::
   :header: "Code", "Label", "Definition"
   :widths: auto
   :align: left

Acquisition Type
^^^^^^^^^^^^^^^^^

Planimetric Accuracy
^^^^^^^^^^^^^^^^^^^^^
**Duplicate**

Provider
^^^^^^^^
**Duplicate**

Creation Date
^^^^^^^^^^^^^
**Duplicate**

Revision Date
^^^^^^^^^^^^^^
**Duplicate**

Junction Type Lookup
--------------------

Language Code Lookup
--------------------

Provider Lookup
---------------

Province Lookup
---------------

Reference System Indicator lookup
---------------------------------

Route Name
--------

route Name id
^^^^^^^^^^^^^

Route Name (en)
^^^^^^^^^^^^^
The English version of a name of a particular route in a given road network as attributed by a national or subnational
agency. A particular Road Segment or Ferry Connection Segment can belong to more than one named route. In such cases,
it has multiple route name attributes.

Route Name (fr)
^^^^^^^^^^^^^
The French version of a name of a particular route in a given road network as attributed by a national or subnational
agency. A particular Road Segment or Ferry Connection Segment can belong to more than one named route. In such cases,
it has multiple route name attributes.

Creation Date
^^^^^^^^^^^^^
**Duplicate**

Revision Date
^^^^^^^^^^^^^
**Duplicate**

Route Name Link
---------------

Route Name Link id
^^^^^^^^^^^^^^^^^^

Segment id
^^^^^^^^^^

Route Name id
^^^^^^^^^^^^^^

Route Number
------------

Route Number id
^^^^^^^^^^^^^^^

Route Number
^^^^^^^^^^^^
The ID number of a particular route in a given road network as attributed by a national or subnational agency. A
particular Road Segment or Ferry Connection Segment can belong to more than one numbered route. In such cases, it has
multiple route number attributes.

Creation Date
^^^^^^^^^^^^^
**Duplicate**

Revision Date
^^^^^^^^^^^^^
**Duplicate**

Route Number Link
-----------------

Route Number id
^^^^^^^^^^^^^^^

route_number
^^^^^^^^^^^^
**Duplicate**

Creation Date
^^^^^^^^^^^^^^
**Duplicate**

Revision Date
^^^^^^^^^^^^^
**Duplicate**

Segment
------

Segment id
^^^^^^^^^^^

Segment id (left)
^^^^^^^^^^^^^^^^

Segment id (right)
^^^^^^^^^^^^^^^^

Element id
^^^^^^^^^^^

Routable Element id
^^^^^^^^^^^^^^^^^^^

Segment Type
^^^^^^^^^^^

Exit Number
^^^^^^^^^^^
The ID number of an exit on a controlled access thoroughfare that has been assigned by an administrating body.

Speed
^^^^^
The maximum speed allowed on the road. The value is expressed in kilometers per hour.

Number of Lanes
^^^^^^^^^^^^^^^
The number of lanes existing on a Road Element.

Road Jurisdiction
^^^^^^^^^^^^^^^^
The agency with the responsibility/authority to ensure maintenance occurs but is not necessarily the one who undertakes
the maintenance directly.

Closing Period
^^^^^^^^^^^^^^
The period in which the road or ferry connection is not available to the public.

.. csv-table::
   :header: "Code", "Label", "Definition"
   :widths: auto
   :align: left

Functional Road Class
^^^^^^^^^^^^^^^^^^^^^
A classification based on the importance of the role that the Road Element or Ferry Connection performs in the
connectivity of the total road network.

.. csv-table::
   :header: "Code", "Label", "Definition"
   :widths: auto
   :align: left

Traffic Direction
^^^^^^^^^^^^^^^^^
The direction(s) of traffic flow allowed on the road.

.. csv-table::
   :header: "Code", "Label", "Definition"
   :widths: auto
   :align: left

Road Surface Type
^^^^^^^^^^^^^^
The type of surface a road element has.

.. csv-table::
   :header: "Code", "Label", "Definition"
   :widths: auto
   :align: left

Structure id
^^^^^^^^^^^^

Address Range id (left)
^^^^^^^^^^^^^^^^^^^^^^

Address Range id (right)
^^^^^^^^^^^^^^^^^^^^^^

bb uid (l)
^^^^^^^^

bb uid (r)
^^^^^^^^

Acquisition Technique
^^^^^^^^^^^^^^^^^^^^^
**Duplicate**

Planimetric Accuracy
^^^^^^^^^^^^^^^^^^^^
**Duplicate**

Provider
^^^^^^^^
**Duplicate**

Creation Date
^^^^^^^^^^^^^
**Duplicate**

Revision Date
^^^^^^^^^^^^^
**Duplicate**

Segment Type Lookup
--------------------

Street Article Lookup
--------------------

Street Direction Lookup
-----------------------

Street Name
-----------

Street Name id
^^^^^^^^^^^^^^

Street Name Concatenated
^^^^^^^^^^^^^^^^^^^^^^^^
A concatenation of the officially recognized Directional prefix, Street type prefix, Street name article, Street name
body, Street type suffix, Directional suffix and Muni quadrant values.

Street Direction Prefix
^^^^^^^^^^^^^^^^^^^^^^^
A geographic direction that is part of the street name and precedes the street name body or, if appropriate, the street
type prefix.
**table**

Street Type Prefix
^^^^^^^^^^^^^^^^^^
A part of the street name of a Road Element identifying the street type. A prefix precedes the street name body of a
Road Element.

.. csv-table::
   :header: "Code", "Label", "Definition"
   :widths: auto
   :align: left

Street Article
^^^^^^^^^^^^^^
Article(s) that is/are part of the street name and located at the beginning.

.. csv-table::
   :header: "Code", "Label", "Definition"
   :widths: auto
   :align: left

Street Name Body
^^^^^^^^^^^^^^^^
The portion of the street name (either official or alternate) that has the most identifying power excluding street type
and directional prefixes or suffixes and street name articles.

Street Type Suffix
^^^^^^^^^^^^^^^^^^
A part of the street name of a Road Element identifying the street type. A suffix follows the street name body of a
Road Element.

.. csv-table::
   :header: "Code", "Label", "Definition"
   :widths: auto
   :align: left

Street Direction Suffix
^^^^^^^^^^^^^^^^^^^^^^^
A geographic direction that is part of the street name and succeeds the street name body or, if appropriate, the street
type suffix.

.. csv-table::
   :header: "Code", "Label", "Definition"
   :widths: auto
   :align: left

Creation Date
^^^^^^^^^^^^
**Duplicate**

Revision Date
^^^^^^^^^^^^^
**Duplicate**

Street Name Link
----------------

Street Name Link id
^^^^^^^^^^^^^^^^^^^

Segment id
^^^^^^^^^^

Street Name id
^^^^^^^^^^^^^^

Street Name Translation
-----------------------

Street Name Translation id
^^^^^^^^^^^^^^^^^^^^^^^^^^

Street Name id
^^^^^^^^^^^^^^

Street Name Concatenated
^^^^^^^^^^^^^^^^^^^^^^^^^
**Duplicate**

Language Code
^^^^^^^^^^^^^

Creation Date
^^^^^^^^^^^^^
**Duplicate**

Revision Date
^^^^^^^^^^^^^
**Duplicate**

Street Type Lookup
------------------

Structure
---------

Structure id
^^^^^^^^^^^^^
A national unique identifier assigned to the Road Segment or the set of adjoining Road Segments forming a structure.
This identifier allows for the reconstitution of a structure that is fragmented by Junctions.

Structure Type
^^^^^^^^^^^^^^^
The classification of a structure.

.. csv-table::
   :header: "Code", "Label", "Definition"
   :widths: auto
   :align: left

Structure Name (en)
^^^^^^^^^^^^^^^^^^
The English version of the name of a road structure as assigned by a national or subnational agency.

Structure Name (fr)
^^^^^^^^^^^^^^^^^
The French version of the name of a road structure as assigned by a national or subnational agency.

Creation Date
^^^^^^^^^^^^^
**Duplicate**

Revision Date
^^^^^^^^^^^^^
**Duplicate**

Structure Type Lookup
---------------------

Toll Point
----------
Place where right-of-way is charged to gain access to a motorway, a bridge, etc.

Toll Point id
^^^^^^^^^^^^^

Segment id
-----------

Toll Point Type
^^^^^^^^^^^^^^^
The type of toll point.

.. csv-table::
   :header: "Code", "Label", "Definition"
   :widths: auto
   :align: left

   1, "Physical Toll Booth", "A toll booth is a construction along or across the road where toll can be paid to
   employees of the organization in charge of collecting the toll, to machines capable of automatically recognizing
   coins or bills or to machines involving electronic methods of payment like credit cards or bank cards."
   2, "Virtual Toll Booth", "At a virtual point of toll payment, toll will be charged via automatic registration of the
   passing vehicle by subscription or invoice."
   3, "Hybrid", "Hybrid signifies a toll booth which is both physical and virtual."


Acquisition Technique
^^^^^^^^^^^^^^^^^^^^
**Duplicate**

Planimetric Accuracy
^^^^^^^^^^^^^^^^^^^^
**Duplicate**

Provider
^^^^^^^^^
**Duplicate**

Creation Date
^^^^^^^^^^^^^^
**Duplicate**

Creation Type
^^^^^^^^^^^^^

Toll Point Type Lookup
-----------------------

Traffic Direction Lookup
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