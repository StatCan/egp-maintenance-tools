*********************
Canadian Road Network
*********************

.. contents:: Contents:
   :depth: 3

Diagram
=======

.. figure:: /source/_static/data_models/canadian_road_network/canadian_road_network-primary_datasets.svg
    :alt: Canadian Road Network diagram (primary datasets).

    Figure: Canadian Road Network diagram (primary datasets).

.. figure:: /source/_static/data_models/canadian_road_network/canadian_road_network-lookup_datasets.svg
    :alt: Canadian Road Network diagram (lookup datasets).

    Figure: Canadian Road Network diagram (lookup datasets).

Data Dictionary
===============

acquisition_technique_lookup
----------------------------

**Description:** Codeset lookup dataset for acquisition technique.

*Table: Attribute description and constraints.*

.. csv-table::
   :header: "Attribute", "Nullable", "Unique", "Default", "Description"
   :widths: auto
   :align: left

   "code", False, True, "", "Concise code used in place of a more descriptive value."
   "value_en", False, True, "", "English version of the descriptive value."
   "value_fr", False, True, "", "French version of the descriptive value."

|
| *Table: Codeset domain.*

.. csv-table::
   :header: "code", "value_en", "value_fr", "Description"
   :widths: auto
   :align: left

   -1, "Unknown", "Inconnu", "Value is unknown."
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

**Description:** A set of attributes representing the address of the first and last building located along the side of
the entire road or a portion of it.

*Table: Attribute description and constraints.*

.. csv-table::
   :header: "Attribute", "Nullable", "Unique", "Default", "Description"
   :widths: auto
   :align: left

   "address_range_id", False, True, ``gen_random_uuid()``, "Unique identifier of each record."
   "first_house_number", False, False, -1, "The first house number address."
   "first_house_number_suffix", False, False, "Unknown", "A non-integer value, such as a fraction or a character that
   follows the first house number address."
   "first_house_number_type", False, False, "", "The method used to populate the first house number address."
   "last_house_number", False, False, -1, "The last house number address."
   "last_house_number_suffix", False, False, "Unknown", "A non-integer value, such as a fraction or a character that
   follows the last house number address."
   "last_house_number_type", False, False, "", "The method used to populate the last house number address."
   "house_number_structure", False, False, "", "The numbering structure of the address range."
   "reference_system_indicator", False, False, "", "The particular addressing system of the address range."
   "acquisition_technique", False, False, "", "The type of data source or technique used to populate (create or revise)
   the dataset."
   "provider", False, False, "", "The affiliation of the organization that provided the original or revised dataset
   contents."
   "creation_date", False, False, ``now()``, "The date of data creation."
   "revision_date", False, False, ``now()``, "The date of data revision."

basic_block
-----------

| **Description:** Geographic areas formed by all roads and boundaries in :ref:`segment`.
| **Coordinate reference system:** EPSG:3347
| **Coordinate decimal precision:** 5

*Table: Attribute description and constraints.*

.. csv-table::
   :header: "Attribute", "Nullable", "Unique", "Default", "Description"
   :widths: auto
   :align: left

   "bb_uid", False, True, "", "Unique identifier of each record."
   "cb_uid", False, False, "", "Unique identifier of the corresponding census block."
   "geom", False, True, "", "Geometry column."

*Trigger: Enforcing coordinate decimal precision for new and updated geometries. Refer to:* :ref:`snap_coords`

.. code-block::

   CREATE TRIGGER basic_block_snap_coords
   BEFORE INSERT OR UPDATE ON basic_block
   FOR EACH ROW EXECUTE PROCEDURE snap_coords (5);

blocked_passage
---------------

| **Description:** Indication of a physical barrier on a road built to prevent or control further access.
| **Coordinate reference system:** EPSG:3347
| **Coordinate decimal precision:** 5

*Table: Attribute description and constraints.*

.. csv-table::
   :header: "Attribute", "Nullable", "Unique", "Default", "Description"
   :widths: auto
   :align: left

   "blocked_passage_id", False, True, ``gen_random_uuid()``, "Unique identifier of each record."
   "segment_id", False, False, "", "Unique identifier of the corresponding road."
   "blocked_passage_type", False, False, "", "The type of blocked passage."
   "acquisition_technique", False, False, "", "The type of data source or technique used to populate (create or revise)
   the dataset."
   "planimetric_accuracy", False, False, -1, "The planimetric accuracy expressed in meters as the circular map accuracy
   standard (CMAS)."
   "provider", False, False, "", "The affiliation of the organization that provided the original or revised dataset
   contents."
   "creation_date", False, False, ``now()``, "The date of data creation."
   "revision_date", False, False, ``now()``, "The date of data revision."
   "geom", False, True, "", "Geometry column."

*Trigger: Enforcing coordinate decimal precision for new and updated geometries. Refer to:* :ref:`snap_coords`

.. code-block::

   CREATE TRIGGER blocked_passage_snap_coords
   BEFORE INSERT OR UPDATE ON blocked_passage
   FOR EACH ROW EXECUTE PROCEDURE snap_coords (5);

blocked_passage_type_lookup
---------------------------

**Description:** Codeset lookup dataset for blocked passage type.

*Table: Attribute description and constraints.*

.. csv-table::
   :header: "Attribute", "Nullable", "Unique", "Default", "Description"
   :widths: auto
   :align: left

   "code", False, True, "", "Concise code used in place of a more descriptive value."
   "value_en", False, True, "", "English version of the descriptive value."
   "value_fr", False, True, "", "French version of the descriptive value."

|
| *Table: Codeset domain.*

.. csv-table::
   :header: "code", "value_en", "value_fr", "Description"
   :widths: auto
   :align: left

   -1, "Unknown", "Inconnu", "Value is unknown."
   1, "Permanently Fixed", "Permanente", "The barrier cannot be removed without destroying it and requires heavy
   equipment in order to allow further access. Examples include concrete blocks or a mound of earth."
   2, "Removable", "Amovible", "The barrier is designed to free the entrance to the other side of the road that it is
   blocking and further access is easily allowed when so desired."

closing_period_lookup
---------------------

**Description:** Codeset lookup dataset for closing period.

*Table: Attribute description and constraints.*

.. csv-table::
   :header: "Attribute", "Nullable", "Unique", "Default", "Description"
   :widths: auto
   :align: left

   "code", False, True, "", "Concise code used in place of a more descriptive value."
   "value_en", False, True, "", "English version of the descriptive value."
   "value_fr", False, True, "", "French version of the descriptive value."

|
| *Table: Codeset domain.*

.. csv-table::
   :header: "code", "value_en", "value_fr", "Description"
   :widths: auto
   :align: left

   -1, "Unknown", "Inconnu", "Value is unknown."
   0, "None", "Aucun", "There is no closing period. The road or ferry is open year round."
   1, "Summer", "Été", "Period of the year for which the absence of ice and snow prevent access to the road or ferry."
   2, "Winter", "Hiver", "Period of the year for which ice and snow prevent access to the road or ferry."

.. _crossing:

crossing
--------

| **Description:** All intersection points involving 4 or more roads, used for the identification of grade separated
  intersections (overpasses). This dataset exists for the maintenance of a routable road network whereby roads in the
  completely segmented :ref:`segment` dataset can be dissolved into single features if, in reality, they are contiguous
  and intersect at-grade.
| **Coordinate reference system:** EPSG:3347
| **Coordinate decimal precision:** 5

*Table: Attribute description and constraints.*

.. csv-table::
   :header: "Attribute", "Nullable", "Unique", "Default", "Description"
   :widths: auto
   :align: left

   "crossing_id", False, True, ``gen_random_uuid()``, "Unique identifier of each record."
   "crossing_status", False, False, "", "The type of crossing."
   "crossing_order", False, False, "", "The number of roads connected to the crossing point."
   "creation_date", False, False, ``now()``, "The date of data creation."
   "revision_date", False, False, ``now()``, "The date of data revision."
   "geom", False, True, "", "Geometry column."

*Trigger: Enforcing coordinate decimal precision for new and updated geometries. Refer to:* :ref:`snap_coords`

.. code-block::

   CREATE TRIGGER crossing_snap_coords
   BEFORE INSERT OR UPDATE ON crossing
   FOR EACH ROW EXECUTE PROCEDURE snap_coords (5);

crossing_status_lookup
----------------------

**Description:** Codeset lookup dataset for crossing status.

*Table: Attribute description and constraints.*

.. csv-table::
   :header: "Attribute", "Nullable", "Unique", "Default", "Description"
   :widths: auto
   :align: left

   "code", False, True, "", "Concise code used in place of a more descriptive value."
   "value_en", False, True, "", "English version of the descriptive value."
   "value_fr", False, True, "", "French version of the descriptive value."

|
| *Table: Codeset domain.*

.. csv-table::
   :header: "code", "value_en", "value_fr", "Description"
   :widths: auto
   :align: left

   1, "Overpass", "Viaduc", "Grade separated junction of roads."
   2, "Intersection", "Carrefour", "At-grade junction of roads."

ferry
-----

| **Description:** The average route of a ferryboat which transports vehicles.
| **Coordinate reference system:** EPSG:3347
| **Coordinate decimal precision:** 5

*Table: Attribute description and constraints.*

.. csv-table::
   :header: "Attribute", "Nullable", "Unique", "Default", "Description"
   :widths: auto
   :align: left

   "ferry_id", False, True, ``gen_random_uuid()``, "Unique identifier of each record."
   "closing_period", False, False, "", "The period in which the road or ferry is not available to the public."
   "functional_road_class", False, False, "", "A classification based on the role that the road or ferry performs in
   the connectivity of the road network."
   "province", False, False, "", "Province or Territory where the feature is located."
   "acquisition_technique", False, False, "", "The type of data source or technique used to populate (create or revise)
   the dataset."
   "planimetric_accuracy", False, False, -1, "The planimetric accuracy expressed in meters as the circular map accuracy
   standard (CMAS)."
   "provider", False, False, "", "The affiliation of the organization that provided the original or revised dataset
   contents."
   "creation_date", False, False, ``now()``, "The date of data creation."
   "revision_date", False, False, ``now()``, "The date of data revision."
   "geom", False, True, "", "Geometry column."

*Trigger: Enforcing coordinate decimal precision for new and updated geometries. Refer to:* :ref:`snap_coords`

.. code-block::

   CREATE TRIGGER ferry_snap_coords
   BEFORE INSERT OR UPDATE ON ferry
   FOR EACH ROW EXECUTE PROCEDURE snap_coords (5);

functional_road_class_lookup
----------------------------

**Description:** Codeset lookup dataset for functional road class.

*Table: Attribute description and constraints.*

.. csv-table::
   :header: "Attribute", "Nullable", "Unique", "Default", "Description"
   :widths: auto
   :align: left

   "code", False, True, "", "Concise code used in place of a more descriptive value."
   "value_en", False, True, "", "English version of the descriptive value."
   "value_fr", False, True, "", "French version of the descriptive value."

|
| *Table: Codeset domain.*

.. csv-table::
   :header: "code", "value_en", "value_fr", "Description"
   :widths: auto
   :align: left

   -1, "Unknown", "Inconnu", "Value is unknown."
   0, "None", "Aucun", "Value reserved for boundaries."
   1, "Freeway", "Autoroute", "An unimpeded, high-speed controlled access thoroughfare for through traffic with
   typically no at-grade intersections, usually with no property access or direct access, and which is accessed by a
   ramp. Pedestrians are prohibited."
   2, "Expressway / Highway", "Route express", "A high-speed thoroughfare with a combination of controlled access
   intersections at any grade."
   3, "Arterial", "Artère", "A major thoroughfare with medium to large traffic capacity."
   4, "Collector", "Route collectrice", "A minor thoroughfare mainly used to access properties and to feed traffic with
   right of way."
   5, "Local / Street", "Local / Rue", "A low-speed thoroughfare dedicated to provide full access to the front of
   properties."
   6, "Local / Strata", "Local / Semi-privé", "A low-speed thoroughfare dedicated to provide access to properties with
   potential public restriction such as: trailer parks, First Nations, strata, private estates, seasonal residences."
   7, "Local / Unknown", "Local / Inconnu", "A low-speed thoroughfare dedicated to provide access to the front of
   properties but for which the access regulations are unknown."
   8, "Alleyway / Lane", "Ruelle / Voie", "A low-speed thoroughfare dedicated to provide access to the rear of
   properties."
   9, "Ramp", "Bretelle", "A system of interconnecting roadways providing for the controlled movement between two or
   more roadways."
   10, "Resource / Recreation", "Route d'accès ressources / Site récréatif", "A narrow passage whose primary function
   is to provide access for resource extraction and may also have serve in providing public access to the backcountry."
   11, "Rapid Transit", "Réservée transport commun", "A thoroughfare restricted to public transit buses."
   12, "Service Lane", "Service", "A stretch of road permitting vehicles to come to a stop along a freeway or highway,
   scale, service lane, emergency lane, lookout, and rest area."
   13, "Winter", "Hiver", "A road that is only useable during the winter when conditions allow for passage over lakes,
   rivers, and wetlands."

house_number_structure_lookup
-----------------------------

**Description:** Codeset lookup dataset for house number structure.

*Table: Attribute description and constraints.*

.. csv-table::
   :header: "Attribute", "Nullable", "Unique", "Default", "Description"
   :widths: auto
   :align: left

   "code", False, True, "", "Concise code used in place of a more descriptive value."
   "value_en", False, True, "", "English version of the descriptive value."
   "value_fr", False, True, "", "French version of the descriptive value."

|
| *Table: Codeset domain.*

.. csv-table::
   :header: "code", "value_en", "value_fr", "Description"
   :widths: auto
   :align: left

   -1, "Unknown", "Inconnu", "Value is unknown."
   0, "None", "Aucun", "Absence of a house."
   1, "Even", "Numéros pairs", "The house numbers appear as even numbers in a sequentially sorted order (ascending or
   descending) when moving from one end of the road to the other. A series that has missing numbers but is sequentially
   sorted is valid. An example is the series (2, 4, 8, 18, 22)."
   2, "Odd", "Numéros impairs", "The house numbers appear as odd numbers in a sequentially sorted order (ascending or
   descending) when moving from one end of the road to the other. A series that has missing numbers but is sequentially
   sorted is valid. An example is the series (35, 39, 43, 69, 71, 73, 85)."
   3, "Mixed", "Numéros mixtes", "The house numbers appear as both even and odd numbers in a sequentially sorted order
   (ascending or descending) when moving from one end of the road to the other. A series that has missing numbers but
   is sequentially sorted is valid. Examples are the series (5, 6, 7, 9, 10, 13) and (24, 27, 30, 33, 34, 36)."
   4, "Irregular", "Numéros irréguliers", "The house numbers do not occur in any sorted order."

house_number_type_lookup
------------------------

**Description:** Codeset lookup dataset for house number type.

*Table: Attribute description and constraints.*

.. csv-table::
   :header: "Attribute", "Nullable", "Unique", "Default", "Description"
   :widths: auto
   :align: left

   "code", False, True, "", "Concise code used in place of a more descriptive value."
   "value_en", False, True, "", "English version of the descriptive value."
   "value_fr", False, True, "", "French version of the descriptive value."

|
| *Table: Codeset domain.*

.. csv-table::
   :header: "code", "value_en", "value_fr", "Description"
   :widths: auto
   :align: left

   -1, "Unknown", "Inconnu", "Value is unknown."
   0, "None", "Aucun", "Absence of a house."
   1, "Actual Located", "Localisation réelle", "The house number is located at its true position along the road."
   2, "Actual Unlocated", "Localisation présumée", "The house number is located at one end of the road which may or may
   not be its true position."
   3, "Projected", "Projeté", "The house number is planned, figured or estimated for the future and is located at one
   end of the road."
   4, "Interpolated", "Interpolé", "The house number is calculated from two known house numbers which are located on
   either side."

.. _junction:

junction
--------

| **Description:** A feature bounding one or more roads or ferries. A junction is defined at the intersection of three
  or more roads, at the junction of a road and a ferry, at the end of a dead end road, and at the junction of a road or
  ferry with a provincial, territorial, or national boundary.
| **Coordinate reference system:** EPSG:3347
| **Coordinate decimal precision:** 5

*Table: Attribute description and constraints.*

.. csv-table::
   :header: "Attribute", "Nullable", "Unique", "Default", "Description"
   :widths: auto
   :align: left

   "junction_id", False, True, ``gen_random_uuid()``, "Unique identifier of each record."
   "junction_type", False, False, "", "The classification of the junction."
   "exit_number", False, False, "Unknown", "The identifying number of an exit on a controlled access thoroughfare."
   "province", False, False, "", "Province or Territory where the feature is located."
   "acquisition_technique", False, False, "", "The type of data source or technique used to populate (create or revise)
   the dataset."
   "planimetric_accuracy", False, False, -1, "The planimetric accuracy expressed in meters as the circular map accuracy
   standard (CMAS)."
   "provider", False, False, "", "The affiliation of the organization that provided the original or revised dataset
   contents."
   "creation_date", False, False, ``now()``, "The date of data creation."
   "revision_date", False, False, ``now()``, "The date of data revision."
   "geom", False, False, "", "Geometry column."

*Trigger: Enforcing coordinate decimal precision for new and updated geometries. Refer to:* :ref:`snap_coords`

.. code-block::

   CREATE TRIGGER junction_snap_coords
   BEFORE INSERT OR UPDATE ON junction
   FOR EACH ROW EXECUTE PROCEDURE snap_coords (5);

junction_type_lookup
--------------------

**Description:** Codeset lookup dataset for junction type.

*Table: Attribute description and constraints.*

.. csv-table::
   :header: "Attribute", "Nullable", "Unique", "Default", "Description"
   :widths: auto
   :align: left

   "code", False, True, "", "Concise code used in place of a more descriptive value."
   "value_en", False, True, "", "English version of the descriptive value."
   "value_fr", False, True, "", "French version of the descriptive value."

|
| *Table: Codeset domain.*

.. csv-table::
   :header: "code", "value_en", "value_fr", "Description"
   :widths: auto
   :align: left

   1, "Intersection", "Intersection", "A junction where three or more roads intersect at-grade."
   2, "Dead End", "Cul-de-sac", "A junction that indicates that a road ends and is not connected to any other road or
   ferry."
   3, "Ferry", "Transbordement", "A junction that indicates that a road connects to a ferry."
   4, "NatProvTer", "NatProvTer", "A junction at a provincial, territorial, or national boundary indicating that a road
   or ferry continues into the adjacent province, territory, or country."

language_code_lookup
--------------------

**Description:** Codeset lookup dataset for language code.

*Table: Attribute description and constraints.*

.. csv-table::
   :header: "Attribute", "Nullable", "Unique", "Default", "Description"
   :widths: auto
   :align: left

   "code", False, True, "", "Three-letter code identifying the language in accordance with ISO 639-3."
   "value_en", False, True, "", "English version of the descriptive value."
   "value_fr", False, True, "", "French version of the descriptive value."

|
| *Table: Codeset domain.*

.. csv-table::
   :header: "code", "value_en", "value_fr", "Description"
   :widths: auto
   :align: left

   atj, "Atikamekw", "Atikamekw", ""
   bla, "Blackfoot", "Pied-noir", ""
   chp, "Chipewyan", "Chipewyan", ""
   clc, "Chilcotin", "Chilcotin", ""
   cre, "Cree", "Cri", ""
   crg, "Michif", "Métchif", ""
   crx, "Carrier", "Dakelh", ""
   dak, "Dakota", "Dakota", ""
   dgr, "Dogrib", "Flanc-de-chien", ""
   eng, "English", "Anglais", ""
   fra, "French", "Français", ""
   git, "Gitxsan", "Gitksan", ""
   gwi, "Gwich'in", "Gwich'in", ""
   hai, "Haida", "Haïda", ""
   ikt, "Inuinnaqtun", "Inuinnaqtun", ""
   iku, "Inuktitut", "Inuktitut", ""
   kut, "Kutenai", "Kutenai", ""
   kwk, "Kwak'wala", "Kwak'wala", ""
   mic, "Mi'kmaq", "Micmac", ""
   moe, "Innu-aimun", "Innu-aimun", ""
   moh, "Mohawk", "Mohawk", ""
   ncg, "Nisga'a", "Nisgha", ""
   nsk, "Naskapi", "Naskapi", ""
   oji, "Ojibwe", "Ojibwé", ""
   ojs, "Oji-Cree", "Oji-cri", ""
   scs, "North Slavey", "Esclave du Nord", ""
   sek, "Sekani", "Sekani", ""
   shs, "Shuswap", "Shuswap", ""
   squ, "Squamish", "Squamish", ""
   sto, "Stoney", "Stoney", ""
   tli, "Tlingit", "Tlingit", ""
   xsl, "South Slavey", "Esclave du Sud", ""

provider_lookup
---------------

**Description:** Codeset lookup dataset for provider.

*Table: Attribute description and constraints.*

.. csv-table::
   :header: "Attribute", "Nullable", "Unique", "Default", "Description"
   :widths: auto
   :align: left

   "code", False, True, "", "Concise code used in place of a more descriptive value."
   "value_en", False, True, "", "English version of the descriptive value."
   "value_fr", False, True, "", "French version of the descriptive value."

|
| *Table: Codeset domain.*

.. csv-table::
   :header: "code", "value_en", "value_fr", "Description"
   :widths: auto
   :align: left

   -1, "Unknown", "Inconnu", "Value is unknown."
   1, "Other", "Autre", "Other value."
   2, "Federal", "Fédéral", "Federal departments or agencies."
   3, "Provincial / Territorial", "Provincial / Territorial", "Provincial / territorial departments or agencies."
   4, "Municipal", "Municipal", "Municipal departments or agencies."

province_lookup
---------------

**Description:** Codeset lookup dataset for province.

*Table: Attribute description and constraints.*

.. csv-table::
   :header: "Attribute", "Nullable", "Unique", "Default", "Description"
   :widths: auto
   :align: left

   "code", False, True, "", "Concise code used in place of a more descriptive value."
   "value_en", False, True, "", "English version of the descriptive value."
   "value_fr", False, True, "", "French version of the descriptive value."

|
| *Table: Codeset domain.*

.. csv-table::
   :header: "code", "value_en", "value_fr", "Description"
   :widths: auto
   :align: left

   1, "Newfoundland and Labrador", "Terre-Neuve et Labrador", ""
   2, "Nova Scotia", "Nouvelle-Écosse", ""
   3, "Prince Edward Island", "Île-du-Prince-Édouard", ""
   4, "New Brunswick", "Nouveau-Brunswick", ""
   5, "Quebec", "Québec", ""
   6, "Ontario", "Ontario", ""
   7, "Manitoba", "Manitoba", ""
   8, "Saskatchewan", "Saskatchewan", ""
   9, "Alberta", "Alberta", ""
   10, "British Columbia", "Colombie-Britannique", ""
   11, "Yukon", "Yukon", ""
   12, "Northwest Territories", "Territoires du Nord-Ouest", ""
   13, "Nunavut", "Nunavut", ""

reference_system_indicator_lookup
---------------------------------

**Description:** Codeset lookup dataset for reference system indicator.

*Table: Attribute description and constraints.*

.. csv-table::
   :header: "Attribute", "Nullable", "Unique", "Default", "Description"
   :widths: auto
   :align: left

   "code", False, True, "", "Concise code used in place of a more descriptive value."
   "value_en", False, True, "", "English version of the descriptive value."
   "value_fr", False, True, "", "French version of the descriptive value."

|
| *Table: Codeset domain.*

.. csv-table::
   :header: "code", "value_en", "value_fr", "Description"
   :widths: auto
   :align: left

   -1, "Unknown", "Inconnu", "Value is unknown."
   0, "None", "Aucun", "No reference system indicator."
   1, "Civic", "Civique", "Civic addressing system."
   2, "Lot and Concession", "Lot et concession", "Lot and concession number addressing system."
   3, "911 Measured", "Mesuré 911", "Measured distance 911 addressing system."
   4, "911 Civic", "Civique 911", "Civic 911 addressing system."
   5, "DLS Townships", "DLS", "Dominion Land Survey addressing system dominant in the Prairie provinces."

road_surface_type_lookup
------------------------

**Description:** Codeset lookup dataset for road surface type.

*Table: Attribute description and constraints.*

.. csv-table::
   :header: "Attribute", "Nullable", "Unique", "Default", "Description"
   :widths: auto
   :align: left

   "code", False, True, "", "Concise code used in place of a more descriptive value."
   "value_en", False, True, "", "English version of the descriptive value."
   "value_fr", False, True, "", "French version of the descriptive value."

|
| *Table: Codeset domain.*

.. csv-table::
   :header: "code", "value_en", "value_fr", "Description"
   :widths: auto
   :align: left

   -1, "Unknown", "Inconnu", "Value is unknown."
   0, "None", "Aucun", "There is no permanent surface such as with a winter road or boundaries."
   1, "Rigid", "Rigide", "A paved road with a rigid surface such as concrete or steel decks."
   2, "Flexible", "Souple", "A paved road with a flexible surface such as asphalt or tar gravel."
   3, "Blocks", "Pavés", "A paved road with a surface made of blocks such as cobblestones."
   4, "Gravel", "Gravier", "A dirt road whose surface has been improved by grading with gravel."
   5, "Dirt", "Terre", "Roads whose surface is formed by the removal of vegetation and / or by the transportation
   movements over that road which inhibit further growth of any vegetation."
   6, "Paved unknown", "Revêtue inconnu", "A road with a surface made of hardened material such as concrete, asphalt,
   tar gravel, or steel decks, but for which the actual material is unknown."
   7, "Unpaved unknown", "Non revêtue inconnu", "A road with a surface made of loose material such as gravel or dirt,
   but for which the actual material is unknown."

route_name
----------

**Description:** A set of attributes representing a particular route name in the road network.

*Table: Attribute description and constraints.*

.. csv-table::
   :header: "Attribute", "Nullable", "Unique", "Default", "Description"
   :widths: auto
   :align: left

   "route_name_id", False, True, ``gen_random_uuid()``, "Unique identifier of each record."
   "route_name_en", False, False, "Unknown", "The official English version of the route name."
   "route_name_fr", False, False, "Unknown", "The official French version of the route name."
   "creation_date", False, False, ``now()``, "The date of data creation."
   "revision_date", False, False, ``now()``, "The date of data revision."

route_name_link
---------------

**Description:** A dataset facilitating plural linkages of roads and ferries with a particular route name in the road
network.

*Table: Attribute description and constraints.*

.. csv-table::
   :header: "Attribute", "Nullable", "Unique", "Default", "Description"
   :widths: auto
   :align: left

   "route_name_link_id", False, True, ``gen_random_uuid()``, "Unique identifier of each record."
   "segment_id", False, False, "", "Unique identifier of the corresponding road or ferry."
   "route_name_id", False, False, "", "Unique identifier of the corresponding route name."

route_number
------------

**Description:** A set of attributes representing a particular route number in the road network.

*Table: Attribute description and constraints.*

.. csv-table::
   :header: "Attribute", "Nullable", "Unique", "Default", "Description"
   :widths: auto
   :align: left

   "route_number_id", False, True, ``gen_random_uuid()``, "Unique identifier of each record."
   "route_number", False, False, "Unknown", "The official route number."
   "creation_date", False, False, ``now()``, "The date of data creation."
   "revision_date", False, False, ``now()``, "The date of data revision."

route_number_link
-----------------

**Description:** A dataset facilitating plural linkages of roads and ferries with a particular route number in the road
network.

*Table: Attribute description and constraints.*

.. csv-table::
   :header: "Attribute", "Nullable", "Unique", "Default", "Description"
   :widths: auto
   :align: left

   "route_number_link_id", False, True, ``gen_random_uuid()``, "Unique identifier of each record."
   "segment_id", False, False, "", "Unique identifier of the corresponding road or ferry."
   "route_number_id", False, False, "", "Unique identifier of the corresponding route number."

.. _segment:

segment
-------

| **Description:** A road or boundary feature with uniform characteristics.
| **Coordinate reference system:** EPSG:3347
| **Coordinate decimal precision:** 5

*Table: Attribute description and constraints.*

.. csv-table::
   :header: "Attribute", "Nullable", "Unique", "Default", "Description"
   :widths: auto
   :align: left

   "segment_id", False, True, ``gen_random_uuid()``, "Unique identifier of each record."
   "segment_id_left", False, True, ``gen_random_uuid()``, "Unique identifier of the left side of each feature."
   "segment_id_right", False, True, ``gen_random_uuid()``, "Unique identifier of the right side of each feature."
   "element_id", False, False, "", "Non-unique identifier used to identify contiguous road features between
   :ref:`junction` points which also share an official street name."
   "routable_element_id", False, False, "", "Non-unique identifier used to identify contiguous road features which
   intersect at-grade via :ref:`crossing` points."
   "segment_type", False, False, "", "The classification of the feature."
   "exit_number", False, False, "Unknown", "The identifying number of an exit on a controlled access thoroughfare."
   "speed", False, False, -1, "The maximum speed allowed on the road, expressed in kilometers per hour."
   "number_of_lanes", False, False, -1, "The number of lanes existing on the road."
   "road_jurisdiction", False, False, "Unknown", "The agency with the responsibility / authority to ensure maintenance
   occurs but is not necessarily the one who undertakes the maintenance directly."
   "closing_period", False, False, "", "The period in which the road or ferry is not available to the public."
   "functional_road_class", False, False, "", "A classification based on the role that the road or ferry performs in
   the connectivity of the road network."
   "traffic_direction", False, False, "", "The direction(s) of traffic flow allowed on the road."
   "road_surface_type", False, False, "", "The type of surface covering a road."
   "structure_id", False, False, "", "Unique identifier of the corresponding structure."
   "bb_uid_l", True, False, "", "Unique identifier of the corresponding basic block on the left side of each feature."
   "bb_uid_r", True, False, "", "Unique identifier of the corresponding basic block on the right side of each feature."
   "acquisition_technique", False, False, "", "The type of data source or technique used to populate (create or revise)
   the dataset."
   "planimetric_accuracy", False, False, -1, "The planimetric accuracy expressed in meters as the circular map accuracy
   standard (CMAS)."
   "provider", False, False, "", "The affiliation of the organization that provided the original or revised dataset
   contents."
   "creation_date", False, False, ``now()``, "The date of data creation."
   "revision_date", False, False, ``now()``, "The date of data revision."
   "geom", False, True, "", "Geometry column."

*Trigger: Enforcing coordinate decimal precision for new and updated geometries. Refer to:* :ref:`snap_coords`

.. code-block::

   CREATE TRIGGER segment_snap_coords
   BEFORE INSERT OR UPDATE ON segment
   FOR EACH ROW EXECUTE PROCEDURE snap_coords (5);

segment_type_lookup
-------------------

**Description:** Codeset lookup dataset for segment type.

*Table: Attribute description and constraints.*

.. csv-table::
   :header: "Attribute", "Nullable", "Unique", "Default", "Description"
   :widths: auto
   :align: left

   "code", False, True, "", "Concise code used in place of a more descriptive value."
   "value_en", False, True, "", "English version of the descriptive value."
   "value_fr", False, True, "", "French version of the descriptive value."

|
| *Table: Codeset domain.*

.. csv-table::
   :header: "code", "value_en", "value_fr", "Description"
   :widths: auto
   :align: left

   1, "Road", "Route", "A road is a linear section of the earth designed for or the result of vehicular movement."
   2, "Boundary", "Limite", "A boundary is a non-road forming an administrative, statistical, or non-standard
   geographic area."

street_article_lookup
---------------------

**Description:** Codeset lookup dataset for street article.

*Table: Attribute description and constraints.*

.. csv-table::
   :header: "Attribute", "Nullable", "Unique", "Default", "Description"
   :widths: auto
   :align: left

   "code", False, True, "", "Concise code used in place of a more descriptive value."
   "value_en", False, True, "", "English version of the descriptive value."
   "value_fr", False, True, "", "French version of the descriptive value."

|
| *Table: Codeset domain.*

.. csv-table::
   :header: "code", "value_en", "value_fr", "Description"
   :widths: auto
   :align: left

   -1, "Unknown", "Inconnu", "Value is unknown."
   0, "None", "Aucun", "No article."
   1, "à", "à", ""
   2, "à l'", "à l'", ""
   3, "à la", "à la", ""
   4, "au", "au", ""
   5, "aux", "aux", ""
   6, "by the", "by the", ""
   7, "chez", "chez", ""
   8, "d'", "d'", ""
   9, "de", "de", ""
   10, "de l'", "de l'", ""
   11, "de la", "de la", ""
   12, "des", "des", ""
   13, "du", "du", ""
   14, "l'", "l'", ""
   15, "la", "la", ""
   16, "le", "le", ""
   17, "les", "les", ""
   18, "of the", "of the", ""
   19, "the", "the", ""

street_direction_lookup
-----------------------

**Description:** Codeset lookup dataset for street direction.

*Table: Attribute description and constraints.*

.. csv-table::
   :header: "Attribute", "Nullable", "Unique", "Default", "Description"
   :widths: auto
   :align: left

   "code", False, True, "", "Concise code used in place of a more descriptive value."
   "value_en", False, True, "", "English version of the descriptive value."
   "value_fr", False, True, "", "French version of the descriptive value."

|
| *Table: Codeset domain.*

.. csv-table::
   :header: "code", "value_en", "value_fr", "Description"
   :widths: auto
   :align: left

   -1, "Unknown", "Inconnu", "Value is unknown."
   0, "None", "Aucun", "No direction."
   1, "North", "North", ""
   2, "Nord", "Nord", ""
   3, "South", "South", ""
   4, "Sud", "Sud", ""
   5, "East", "East", ""
   6, "Est", "Est", ""
   7, "West", "West", ""
   8, "Ouest", "Ouest", ""
   9, "Northwest", "Northwest", ""
   10, "Nord-ouest", "Nord-ouest", ""
   11, "Northeast", "Northeast", ""
   12, "Nord-est", "Nord-est", ""
   13, "Southwest", "Southwest", ""
   14, "Sud-ouest", "Sud-ouest", ""
   15, "Southeast", "Southeast", ""
   16, "Sud-est", "Sud-est", ""
   17, "Central", "Central", ""
   18, "Centre", "Centre", ""

street_name
-----------

**Description:** A set of attributes representing a particular street name in the road network.

*Table: Attribute description and constraints.*

.. csv-table::
   :header: "Attribute", "Nullable", "Unique", "Default", "Description"
   :widths: auto
   :align: left

   "street_name_id", False, True, ``gen_random_uuid()``, "Unique identifier of each record."
   "street_name_concatenated", False, False, "Unknown", "The official concatenation of all components of the street
   name."
   "street_direction_prefix", False, False, "", "A geographic direction that is part of the street name and precedes
   the street name body."
   "street_type_prefix", False, False, "", "The portion of the street name identifying the street type and precedes the
   street name body."
   "street_article", False, False, "", "An article that is part of the street name and precedes the street name body."
   "street_name_body", False, False, "Unknown", "The portion of the street name that has the most identifying power,
   excluding the street direction prefix and suffix, street type prefix and suffix, and street article."
   "street_type_suffix", False, False, "", "The portion of the street name identifying the street type and succeeds the
   street name body."
   "street_direction_suffix", False, False, "", "A geographic direction that is part of the street name and succeeds
   the street name body."
   "creation_date", False, False, ``now()``, "The date of data creation."
   "revision_date", False, False, ``now()``, "The date of data revision."

street_name_link
----------------

**Description:** A dataset facilitating plural linkages of roads with a particular street name in the road network.

*Table: Attribute description and constraints.*

.. csv-table::
   :header: "Attribute", "Nullable", "Unique", "Default", "Description"
   :widths: auto
   :align: left

   "street_name_link_id", False, True, ``gen_random_uuid()``, "Unique identifier of each record."
   "segment_id", False, False, "", "Unique identifier of the corresponding road."
   "street_name_id", False, False, "", "Unique identifier of the corresponding street name."

street_name_translation
-----------------------

**Description:** A set of attributes representing a recognized translation of a particular street name in the road
network.

*Table: Attribute description and constraints.*

.. csv-table::
   :header: "Attribute", "Nullable", "Unique", "Default", "Description"
   :widths: auto
   :align: left

   "street_name_translation_id", False, True, ``gen_random_uuid()``, "Unique identifier of each record."
   "street_name_id", False, False, "", "Unique identifier of the corresponding street name."
   "street_name_concatenated", False, False, "Unknown", "The official concatenation of all components of the street
   name."
   "language_code", False, False, "", "Three-letter code identifying the language of the street name translation in
   accordance with ISO 639-3."
   "creation_date", False, False, ``now()``, "The date of data creation."
   "revision_date", False, False, ``now()``, "The date of data revision."

street_type_lookup
------------------

**Description:** Codeset lookup dataset for street type.

*Table: Attribute description and constraints.*

.. csv-table::
   :header: "Attribute", "Nullable", "Unique", "Default", "Description"
   :widths: auto
   :align: left

   "code", False, True, "", "Concise code used in place of a more descriptive value."
   "value_en", False, True, "", "English version of the descriptive value."
   "value_fr", False, True, "", "French version of the descriptive value."

|
| *Table: Codeset domain.*

.. csv-table::
   :header: "code", "value_en", "value_fr", "Description"
   :widths: auto
   :align: left

   -1, "Unknown", "Inconnu", "Value is unknown."
   0, "None", "Aucun", "No type."
   1, "Abbey", "Abbey", ""
   2, "Access", "Access", ""
   3, "Acres", "Acres", ""
   4, "Aire", "Aire", ""
   5, "Allée", "Allée", ""
   6, "Alley", "Alley", ""
   7, "Autoroute", "Autoroute", ""
   8, "Avenue", "Avenue", ""
   9, "Barrage", "Barrage", ""
   10, "Bay", "Bay", ""
   11, "Beach", "Beach", ""
   12, "Bend", "Bend", ""
   13, "Bloc", "Bloc", ""
   14, "Block", "Block", ""
   15, "Boulevard", "Boulevard", ""
   16, "Bourg", "Bourg", ""
   17, "Brook", "Brook", ""
   18, "By-pass", "By-pass", ""
   19, "Byway", "Byway", ""
   20, "Campus", "Campus", ""
   21, "Cape", "Cape", ""
   22, "Carre", "Carre", ""
   23, "Carrefour", "Carrefour", ""
   24, "Centre", "Centre", ""
   25, "Cercle", "Cercle", ""
   26, "Chase", "Chase", ""
   27, "Chemin", "Chemin", ""
   28, "Circle", "Circle", ""
   29, "Circuit", "Circuit", ""
   30, "Close", "Close", ""
   31, "Common", "Common", ""
   32, "Concession", "Concession", ""
   33, "Corners", "Corners", ""
   34, "Côte", "Côte", ""
   35, "Cour", "Cour", ""
   36, "Court", "Court", ""
   37, "Cove", "Cove", ""
   38, "Crescent", "Crescent", ""
   39, "Croft", "Croft", ""
   40, "Croissant", "Croissant", ""
   41, "Crossing", "Crossing", ""
   42, "Crossroads", "Crossroads", ""
   43, "Cul-de-sac", "Cul-de-sac", ""
   44, "Dale", "Dale", ""
   45, "Dell", "Dell", ""
   46, "Desserte", "Desserte", ""
   47, "Diversion", "Diversion", ""
   48, "Downs", "Downs", ""
   49, "Drive", "Drive", ""
   50, "Droit de passage", "Droit de passage", ""
   51, "Échangeur", "Échangeur", ""
   52, "End", "End", ""
   53, "Esplanade", "Esplanade", ""
   54, "Estates", "Estates", ""
   55, "Expressway", "Expressway", ""
   56, "Extension", "Extension", ""
   57, "Farm", "Farm", ""
   58, "Field", "Field", ""
   59, "Forest", "Forest", ""
   60, "Freeway", "Freeway", ""
   61, "Front", "Front", ""
   62, "Gardens", "Gardens", ""
   63, "Gate", "Gate", ""
   64, "Glade", "Glade", ""
   65, "Glen", "Glen", ""
   66, "Green", "Green", ""
   67, "Grounds", "Grounds", ""
   68, "Grove", "Grove", ""
   69, "Harbour", "Harbour", ""
   70, "Haven", "Haven", ""
   71, "Heath", "Heath", ""
   72, "Heights", "Heights", ""
   73, "Highlands", "Highlands", ""
   74, "Highway", "Highway", ""
   75, "Hill", "Hill", ""
   76, "Hollow", "Hollow", ""
   77, "Île", "Île", ""
   78, "Impasse", "Impasse", ""
   79, "Island", "Island", ""
   80, "Key", "Key", ""
   81, "Knoll", "Knoll", ""
   82, "Landing", "Landing", ""
   83, "Lane", "Lane", ""
   84, "Laneway", "Laneway", ""
   85, "Limits", "Limits", ""
   86, "Line", "Line", ""
   87, "Link", "Link", ""
   88, "Lookout", "Lookout", ""
   89, "Loop", "Loop", ""
   90, "Mall", "Mall", ""
   91, "Manor", "Manor", ""
   92, "Maze", "Maze", ""
   93, "Meadow", "Meadow", ""
   94, "Mews", "Mews", ""
   95, "Montée", "Montée", ""
   96, "Moor", "Moor", ""
   97, "Mount", "Mount", ""
   98, "Mountain", "Mountain", ""
   99, "Orchard", "Orchard", ""
   100, "Parade", "Parade", ""
   101, "Parc", "Parc", ""
   102, "Park", "Park", ""
   103, "Parkway", "Parkway", ""
   104, "Passage", "Passage", ""
   105, "Path", "Path", ""
   106, "Pathway", "Pathway", ""
   107, "Peak", "Peak", ""
   108, "Pines", "Pines", ""
   109, "Place", "Place", ""
   110, "Place", "Place", ""
   111, "Plateau", "Plateau", ""
   112, "Plaza", "Plaza", ""
   113, "Point", "Point", ""
   114, "Port", "Port", ""
   115, "Private", "Private", ""
   116, "Promenade", "Promenade", ""
   117, "Quay", "Quay", ""
   118, "Rang", "Rang", ""
   119, "Range", "Range", ""
   120, "Reach", "Reach", ""
   121, "Ridge", "Ridge", ""
   122, "Right of Way", "Right of Way", ""
   123, "Rise", "Rise", ""
   124, "Road", "Road", ""
   125, "Rond Point", "Rond Point", ""
   126, "Route", "Route", ""
   127, "Row", "Row", ""
   128, "Rue", "Rue", ""
   129, "Ruelle", "Ruelle", ""
   130, "Ruisseau", "Ruisseau", ""
   131, "Run", "Run", ""
   132, "Section", "Section", ""
   133, "Sentier", "Sentier", ""
   134, "Sideroad", "Sideroad", ""
   135, "Square", "Square", ""
   136, "Street", "Street", ""
   137, "Stroll", "Stroll", ""
   138, "Subdivision", "Subdivision", ""
   139, "Terrace", "Terrace", ""
   140, "Terrasse", "Terrasse", ""
   141, "Thicket", "Thicket", ""
   142, "Towers", "Towers", ""
   143, "Townline", "Townline", ""
   144, "Trace", "Trace", ""
   145, "Trail", "Trail", ""
   146, "Trunk", "Trunk", ""
   147, "Turnabout", "Turnabout", ""
   148, "Vale", "Vale", ""
   149, "Via", "Via", ""
   150, "View", "View", ""
   151, "Village", "Village", ""
   152, "Vista", "Vista", ""
   153, "Voie", "Voie", ""
   154, "Walk", "Walk", ""
   155, "Way", "Way", ""
   156, "Wharf", "Wharf", ""
   157, "Wood", "Wood", ""
   158, "Woods", "Woods", ""
   159, "Wynd", "Wynd", ""
   160, "Driveway", "Driveway", ""
   161, "Height", "Height", ""
   162, "Roadway", "Roadway", ""
   163, "Strip", "Strip", ""
   164, "Concession Road", "Concession Road", ""
   165, "Corner", "Corner", ""
   166, "County Road", "County Road", ""
   167, "Crossroad", "Crossroad", ""
   168, "Fire Route", "Fire Route", ""
   169, "Garden", "Garden", ""
   170, "Hills", "Hills", ""
   171, "Isle", "Isle", ""
   172, "Lanes", "Lanes", ""
   173, "Pointe", "Pointe", ""
   174, "Regional Road", "Regional Road", ""
   175, "Autoroute à péage", "Autoroute à péage", ""
   176, "Baie", "Baie", ""
   177, "Bluff", "Bluff", ""
   178, "Bocage", "Bocage", ""
   179, "Bois", "Bois", ""
   180, "Boucle", "Boucle", ""
   181, "Bretelle", "Bretelle", ""
   182, "Cap", "Cap", ""
   183, "Causeway", "Causeway", ""
   184, "Chaussée", "Chaussée", ""
   185, "Contournement", "Contournement", ""
   186, "Couloir", "Couloir", ""
   187, "Crête", "Crête", ""
   188, "Croix", "Croix", ""
   189, "Cross", "Cross", ""
   190, "Dead End", "Dead End", ""
   191, "Débarquement", "Débarquement", ""
   192, "Entrance", "Entrance", ""
   193, "Entrée", "Entrée", ""
   194, "Evergreen", "Evergreen", ""
   195, "Exit", "Exit", ""
   196, "Étang", "Étang", ""
   197, "Falaise", "Falaise", ""
   198, "Jardin", "Jardin", ""
   199, "Lawn", "Lawn", ""
   200, "Lien", "Lien", ""
   201, "Ligne", "Ligne", ""
   202, "Manoir", "Manoir", ""
   203, "Pass", "Pass", ""
   204, "Pente", "Pente", ""
   205, "Pond", "Pond", ""
   206, "Quai", "Quai", ""
   207, "Ramp", "Ramp", ""
   208, "Rampe", "Rampe", ""
   209, "Rangée", "Rangée", ""
   210, "Roundabout", "Roundabout", ""
   211, "Route de plaisance", "Route de plaisance", ""
   212, "Route sur élevée", "Route sur élevée", ""
   213, "Side", "Side", ""
   214, "Sortie", "Sortie", ""
   215, "Throughway", "Throughway", ""
   216, "Took", "Took", ""
   217, "Turn", "Turn", ""
   218, "Turnpike", "Turnpike", ""
   219, "Vallée", "Vallée", ""
   220, "Villas", "Villas", ""
   221, "Virage", "Virage", ""
   222, "Voie oust", "Voie oust", ""
   223, "Voie rapide", "Voie rapide", ""
   224, "Vue", "Vue", ""
   225, "Westway", "Westway", ""
   226, "Arm", "Arm", ""
   227, "Baseline", "Baseline", ""
   228, "Bourne", "Bourne", ""
   229, "Branch", "Branch", ""
   230, "Bridge", "Bridge", ""
   231, "Burn", "Burn", ""
   232, "Bypass", "Bypass", ""
   233, "Camp", "Camp", ""
   234, "Chart", "Chart", ""
   235, "Club", "Club", ""
   236, "Copse", "Copse", ""
   237, "Creek", "Creek", ""
   238, "Crest", "Crest", ""
   239, "Curve", "Curve", ""
   240, "Cut", "Cut", ""
   241, "Fairway", "Fairway", ""
   242, "Gateway", "Gateway", ""
   243, "Greenway", "Greenway", ""
   244, "Inamo", "Inamo", ""
   245, "Inlet", "Inlet", ""
   246, "Junction", "Junction", ""
   247, "Keep", "Keep", ""
   248, "Lake", "Lake", ""
   249, "Lakes", "Lakes", ""
   250, "Lakeway", "Lakeway", ""
   251, "Market", "Market", ""
   252, "Millway", "Millway", ""
   253, "Outlook", "Outlook", ""
   254, "Oval", "Oval", ""
   255, "Overpass", "Overpass", ""
   256, "Pier", "Pier", ""
   257, "River", "River", ""
   258, "Service", "Service", ""
   259, "Shore", "Shore", ""
   260, "Shores", "Shores", ""
   261, "Sideline", "Sideline", ""
   262, "Spur", "Spur", ""
   263, "Surf", "Surf", ""
   264, "Track", "Track", ""
   265, "Valley", "Valley", ""
   266, "Walkway", "Walkway", ""
   267, "Wold", "Wold", ""
   268, "Tili", "Tili", ""
   269, "Nook", "Nook", ""
   270, "Drung", "Drung", ""
   271, "Awti", "Awti", ""
   272, "Awti'j", "Awti'j", ""
   273, "Rest", "Rest", ""
   274, "Rotary", "Rotary", ""
   275, "Connection", "Connection", ""
   276, "Estate", "Estate", ""
   277, "Crossover", "Crossover", ""
   278, "Hideaway", "Hideaway", ""
   279, "Linkway", "Linkway", ""

structure
---------

**Description:** A set of attributes representing a particular structure in the road network.

*Table: Attribute description and constraints.*

.. csv-table::
   :header: "Attribute", "Nullable", "Unique", "Default", "Description"
   :widths: auto
   :align: left

   "structure_id", False, True, ``gen_random_uuid()``, "Unique identifier of each record."
   "structure_type", False, False, "", "The classification of the structure."
   "structure_name_en", False, False, "Unknown", "The official English version of the structure name."
   "structure_name_fr", False, False, "Unknown", "The official French version of the structure name."
   "creation_date", False, False, ``now()``, "The date of data creation."
   "revision_date", False, False, ``now()``, "The date of data revision."

structure_type_lookup
---------------------

**Description:** Codeset lookup dataset for structure type.

*Table: Attribute description and constraints.*

.. csv-table::
   :header: "Attribute", "Nullable", "Unique", "Default", "Description"
   :widths: auto
   :align: left

   "code", False, True, "", "Concise code used in place of a more descriptive value."
   "value_en", False, True, "", "English version of the descriptive value."
   "value_fr", False, True, "", "French version of the descriptive value."

|
| *Table: Codeset domain.*

.. csv-table::
   :header: "code", "value_en", "value_fr", "Description"
   :widths: auto
   :align: left

   -1, "Unknown", "Inconnu", "Value is unknown."
   0, "None", "Aucun", "Not a structure."
   1, "Bridge", "Pont", "A man-made construction that supports a road on a raised structure and spans an obstacle,
   river, another road, or railway."
   2, "Bridge covered", "Pont couvert", "A man-made construction that supports a road on a covered raised structure and
   spans an obstacle, river, another road, or railway."
   3, "Bridge moveable", "Pont mobile", "A man-made construction that supports a road on a moveable raised structure
   and spans an obstacle, river, another road, or railway."
   4, "Bridge unknown", "Pont inconnu", "A bridge for which it is currently impossible to determine whether its
   structure is covered, moveable or other."
   5, "Tunnel", "Tunnel", "An enclosed man-made construction built to carry a road through or below a natural feature
   or other obstructions."
   6, "Snowshed", "Paraneige", "A man-made roofed structure built over a road in mountainous areas to prevent snow
   slides from blocking the road."
   7, "Dam", "Barrage", "A man-made linear structure built across a waterway or floodway to control the flow of water
   and supporting a road for motor vehicles."

toll_point
----------

| **Description:** Place where a right-of-way is charged to gain access to a road.
| **Coordinate reference system:** EPSG:3347
| **Coordinate decimal precision:** 5

*Table: Attribute description and constraints.*

.. csv-table::
   :header: "Attribute", "Nullable", "Unique", "Default", "Description"
   :widths: auto
   :align: left

   "toll_point_id", False, True, ``gen_random_uuid()``, "Unique identifier of each record."
   "segment_id", False, False, "", "Unique identifier of the corresponding road."
   "toll_point_type", False, False, "", "The type of toll point."
   "acquisition_technique", False, False, "", "The type of data source or technique used to populate (create or revise)
   the dataset."
   "planimetric_accuracy", False, False, -1, "The planimetric accuracy expressed in meters as the circular map accuracy
   standard (CMAS)."
   "provider", False, False, "", "The affiliation of the organization that provided the original or revised dataset
   contents."
   "creation_date", False, False, ``now()``, "The date of data creation."
   "revision_date", False, False, ``now()``, "The date of data revision."
   "geom", False, True, "", "Geometry column."

*Trigger: Enforcing coordinate decimal precision for new and updated geometries. Refer to:* :ref:`snap_coords`

.. code-block::

   CREATE TRIGGER toll_point_snap_coords
   BEFORE INSERT OR UPDATE ON toll_point
   FOR EACH ROW EXECUTE PROCEDURE snap_coords (5);

toll_point_type_lookup
----------------------

**Description:** Codeset lookup dataset for toll point type.

*Table: Attribute description and constraints.*

.. csv-table::
   :header: "Attribute", "Nullable", "Unique", "Default", "Description"
   :widths: auto
   :align: left

   "code", False, True, "", "Concise code used in place of a more descriptive value."
   "value_en", False, True, "", "English version of the descriptive value."
   "value_fr", False, True, "", "French version of the descriptive value."

|
| *Table: Codeset domain.*

.. csv-table::
   :header: "code", "value_en", "value_fr", "Description"
   :widths: auto
   :align: left

   -1, "Unknown", "Inconnu", "Value is unknown."
   1, "Physical Toll Booth", "Poste de péage", "A construction along or across the road where toll can be paid to
   employees of the organization in charge of collecting the toll, to machines capable of automatically recognizing
   coins or bills or to machines involving electronic methods of payment like credit cards or bank cards."
   2, "Virtual Toll Booth", "Poste de péage virtuel", "A virtual point of toll payment where toll will be charged via
   automatic registration of the passing vehicle by subscription or invoice."
   3, "Hybrid", "Hybride", "A toll booth which is both physical and virtual."

traffic_direction_lookup
------------------------

**Description:** Codeset lookup dataset for traffic direction.

*Table: Attribute description and constraints.*

.. csv-table::
   :header: "Attribute", "Nullable", "Unique", "Default", "Description"
   :widths: auto
   :align: left

   "code", False, True, "", "Concise code used in place of a more descriptive value."
   "value_en", False, True, "", "English version of the descriptive value."
   "value_fr", False, True, "", "French version of the descriptive value."

|
| *Table: Codeset domain.*

.. csv-table::
   :header: "code", "value_en", "value_fr", "Description"
   :widths: auto
   :align: left

   -1, "Unknown", "Inconnu", "Value is unknown."
   0, "None", "Aucun", "Value reserved for boundaries."
   1, "Both directions", "Bi-directionel", "Traffic flow is allowed in both directions."
   2, "Same direction", "Même direction", "The direction of one way traffic flow is the same as the digitizing
   direction of the road."
   3, "Opposite direction", "Direction contraire", "The direction of one way traffic flow is opposite to the
   digitizing direction of the road."

Database Trigger Functions
==========================

Trigger functions must be created prior to creating a trigger on a database table. This section details all trigger
functions used by the CRN data model and the corresponding PostgreSQL syntax to create them.

.. _snap_coords:

snap_coords
-----------

**Description:** Rounds geometry coordinates to a given decimal precision.

.. code-block::

   CREATE OR REPLACE FUNCTION snap_coords ()
   RETURNS TRIGGER AS $$
   BEGIN
       NEW.geom := ST_AsText(ST_ReducePrecision(NEW.geom, 1 / (10 ^ TG_ARGV[0]::float)), TG_ARGV[0]::int);
       RETURN NEW;
   END;
   $$ LANGUAGE plpgsql;
