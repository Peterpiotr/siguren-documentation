==========
Self-test
==========

.. include:: ../../_img/_image-substitutions.rst

.. note::
     Description refers to software version 8.2.


A self-test is a procedure in which the MotoSuiveur unit tests its health through a sequence of tests. 
The self-test is performed after the initial power-up of the MotoSuiveur system or after a restart from the Reset button on the electrical panel.
Sequence of Self-test operations are displayed on MS controller 7 – segment display.

In table below self-test sequence is shown.

  +------------+-------------------+-----------------------------------------------+
  | Symbol     | Test              |     Description                               |
  +============+===================+===============================================+
  | |image013| | Software          |Checking version of MS controller software     |
  +------------+-------------------+-----------------------------------------------+
  | |image017| | Electrical        |Check for activated commands for movement,     |
  |            |                   |presence of an enabling signal from crane/hoist|
  +------------+-------------------+-----------------------------------------------+
  | |image001| | Home              |Worm positioning in nominal position between   |
  |            |                   |SCRE and USCRE limit switches                  |
  +            +-------------------+-----------------------------------------------+
  |            | Bliocking check   |Check for blocked worm. In the event that the  |
  |            |                   |MS holds the load or for any other reason the  |
  |            |                   |worm cannot exit the hydraulic chamber do not  |
  |            |                   |settle in the nominal position                 |                    
  +            +-------------------+-----------------------------------------------+
  |            | Healthy           |Check for blocked worm. In the event that the  |
  |            |                   |MS holds the load or for any other reason the  |
  |            |                   |worm cannot exit the hydraulic chamber do not  |
  |            |                   |settle in the nominal position                 |                    
  +------------+-------------------+-----------------------------------------------+
  | |image021| | Switch test*      |Functional testing of MS unit limit switches   |
  |            |                   |for operability and correct positioning        |
  +------------+-------------------+-----------------------------------------------+
  | |image025| | Damping test*     |Hydraulic chamber hardness test of MS unit.    |
  |            |                   |Checking for change in hydraulic cartridge     |
  |            |                   |setting and sufficient oil in the hydraulic    |
  |            |                   |chamber.                                       |
  +------------+-------------------+-----------------------------------------------+
  | |image029| | Air test*         |Hydraulic chamber hardness test of MS unit.    |
  |            |                   |Checking for change in hydraulic cartridge     |
  |            |                   |setting and sufficient oil in the hydraulic    |
  |            |                   |chamber.                                       |
  +------------+-------------------+-----------------------------------------------+
  | |image001| | Home              |Worm positioning in nominal position between   |
  |            |                   |SCRE and USCRE limit switches                  |
  +------------+-------------------+-----------------------------------------------+
  | |image033| | Play test         |Check for nominal backlash (worm free play)    | 
  |            |                   |between worm and worm wheel                    |
  +------------+-------------------+-----------------------------------------------+


Sowtware test
--------------

Software test perform check for correct version of MS controller firmware version.
If version is not correct, E28 appears.


Electrical test
---------------

.. csv-table:: Electrical test sequence
   :file: ../../_tables/self-test.csv
   :delim: ;
   :header-rows: 1
   :class: tight-table
   :align: left
   :widths: auto

\*\ *If MotoSuiveur unit is equipped with Recovery system