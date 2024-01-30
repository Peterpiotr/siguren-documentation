===================
Running a Self-Test
===================

.. include:: /_img/_image-substitutions.rst

.. note::
     For software version 8.2.


.. what if i interrupt a self-test
.. can i see when was a self test last ran manually/automatically?

Introduction
=============

A Self-Test is a procedure in which the MS Unit tests its health through a sequence of tests. 

The Self-Test is performed either:
    - after the initial power ON of the MotoSuiveur® System 
    - or after a restart from the :guilabel:`🔘 Reset` button on the MS Control Panel.

The steps of Self-Test sequence are displayed on MS Controller 7-segment display (table below).

+------------+-------------------+-----------------------------------------------+--------------------------+
| Symbol     | Test              |Description                                    | Possible warnings/faults |
+============+===================+===============================================+==========================+
| |7s-1|     | Software          |Checking version of MS Controller software     | E28                      |
+------------+-------------------+-----------------------------------------------+--------------------------+
| |7s-2|     | Electrical        |Check for activated commands for movement,     | E64, E65, E05, E04, E02, |
|            |                   |presence of an enabling signal from crane/hoist| E03, E57, E69            |
+------------+-------------------+-----------------------------------------------+--------------------------+
| |7s-H|     | Home              |Worm positioning in nominal position between   |                          |
|            |                   |SCRE and USCRE limit switches                  |                          |
+            +-------------------+-----------------------------------------------+--------------------------+
|            | Blocking check    |Check for blocked worm. In the event that the  | E10                      |
|            |                   |MS holds the load or for any other reason the  |                          |
|            |                   |worm cannot exit the hydraulic chamber do not  |                          |
|            |                   |settle in the nominal position                 |                          |
+            +-------------------+-----------------------------------------------+--------------------------+
|            | Healthy           |Indication on MS Controller 7-segment display  |                          |
|            |                   |for electrical healthy and unblocked worm      |                          |
+------------+-------------------+-----------------------------------------------+--------------------------+
| |7s-3|     | Switch test       |Functional testing of MS Unit limit switches   | E11, E12, E13, E14       |
|            |                   |for operability and correct positioning        |                          |
+------------+-------------------+-----------------------------------------------+--------------------------+
| |7s-4|     | Damping test*     |Hydraulic chamber hardness test of MS Unit.    | F22, F23                 |
|            |                   |Checking for change in hydraulic cartridge     |                          |
|            |                   |setting and sufficient oil in the hydraulic    |                          |
|            |                   |chamber.                                       |                          |
+------------+-------------------+-----------------------------------------------+--------------------------+
| |7s-5|     | Air test*         |Hydraulic chamber hardness test of MS Unit.    | F20                      |
|            |                   |Checking for change in hydraulic cartridge     |                          |
|            |                   |setting and sufficient oil in the hydraulic    |                          |
|            |                   |chamber.                                       |                          |
+------------+-------------------+-----------------------------------------------+--------------------------+
| |7s-H|     | Home              |Worm positioning in nominal position between   | E10                      |
|            |                   |SCRE and USCRE limit switches                  |                          |
+------------+-------------------+-----------------------------------------------+--------------------------+
| |7s-F|   | Play test         |Check for nominal backlash (worm free play)    | F15, F17                 |
|            |                   |between worm and worm wheel                    |                          |
+------------+-------------------+-----------------------------------------------+--------------------------+


\*\ This tests are performed only for **Hydraulic Damping MotoSuiveur® Units**.

Any warnings and faults that occur during MotoSuiveur® System operation are displayed on the HMI screen (if installed) and on the 7-segment display of the MS Controller. 

.. note::
    For the detailed description of warnings and faults, see :doc:`/advanced/controller-faults-warnings`.


Software test
==============

Software test perform check for correct version of MS Controller firmware version.


Electrical test
=================

Electrical test performs sequence of checks listed in table below. 
if some of the checks do not pass, a warning occurs.

.. csv-table:: Electrical test sequence
        :file: /_tables/Self-Test.csv
        :delim: ;
        :header-rows: 1
        :align: left
        :widths: auto

.. this table reverses the information. The user needs to know what happened when a warning is displayed
    NOT which warnings MAY POSSIBLY display if a given thing happens

\*\ *If MS Unit is equipped with Recovery system*


Positioning
==============

Positioning is a sequence of worm movements designed to position the worm in the normal position (between the limit switches/proximity sensors). 


Switch test
===============

A Switch test checks the correct positioning of position limit switches/proximity sensors and their health.

Sequence of switch test is listed in table below.

.. csv-table:: Switch test sequence
   :file: /_tables/switch-test.csv
   :delim: ;
   :header-rows: 1
   :align: left
   :widths: auto


Damping test
==============

Damping test is performed only for hydraulic type MS Units.

It is used to check the hardness of the damping chamber.

Sequence of checks is listed in table below.

.. csv-table:: Damping test sequence
   :file: /_tables/damping-test.csv
   :delim: ;
   :header-rows: 1
   :align: left
   :widths: auto

.. this table reverses the information. The user needs to know what happened when a warning is displayed
    NOT which warnings MAY POSSIBLY display if a given thing happens

Air test
==============

The air test checks for the presence of air in the damping chamber.

The test is performed with three short movements (knocks) in sequence.
-
Test sequence is listed in table below.

.. csv-table:: Air test sequence
   :file: /_tables/air-test.csv
   :delim: ;
   :header-rows: 1
   :align: left
   :widths: auto


Play test
==============

Check for nominal backlash (worm free play) between between pistons () with low torque.

Test sequense is listed below.

.. csv-table:: Play test sequence
   :file: /_tables/play-test.csv
   :delim: ;
   :header-rows: 1
   :align: left
   :widths: auto