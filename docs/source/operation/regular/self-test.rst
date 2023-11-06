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

  +------------+-------------------+-----------------------------------------------+--------------------------+
  | Symbol     | Test              |Description                                    | Possible warnings/faults |
  +============+===================+===============================================+==========================+
  | |image013| | Software          |Checking version of MS controller software     | E28                      |
  +------------+-------------------+-----------------------------------------------+--------------------------+
  | |image017| | Electrical        |Check for activated commands for movement,     | E64, E65, E05, E04, E02, |
  |            |                   |presence of an enabling signal from crane/hoist| E03, E57, E69            |
  +------------+-------------------+-----------------------------------------------+--------------------------+
  | |image001| | Home              |Worm positioning in nominal position between   |                          |
  |            |                   |SCRE and USCRE limit switches                  |                          |
  +            +-------------------+-----------------------------------------------+--------------------------+
  |            | Bliocking check   |Check for blocked worm. In the event that the  | E10                      |
  |            |                   |MS holds the load or for any other reason the  |                          |
  |            |                   |worm cannot exit the hydraulic chamber do not  |                          |
  |            |                   |settle in the nominal position                 |                          |
  +            +-------------------+-----------------------------------------------+--------------------------+
  |            | Healthy           |Indication on MS Controller 7-segment display  |                          |
  |            |                   |for electrical healthy and unblocked worm      |                          |
  +------------+-------------------+-----------------------------------------------+--------------------------+
  | |image021| | Switch test*      |Functional testing of MS unit limit switches   | E11, E12, E13, E14       |
  |            |                   |for operability and correct positioning        |                          |
  +------------+-------------------+-----------------------------------------------+--------------------------+
  | |image025| | Damping test*     |Hydraulic chamber hardness test of MS unit.    | F22, F23                 |
  |            |                   |Checking for change in hydraulic cartridge     |                          |
  |            |                   |setting and sufficient oil in the hydraulic    |                          |
  |            |                   |chamber.                                       |                          |
  +------------+-------------------+-----------------------------------------------+--------------------------+
  | |image029| | Air test*         |Hydraulic chamber hardness test of MS unit.    | F20                      |
  |            |                   |Checking for change in hydraulic cartridge     |                          |
  |            |                   |setting and sufficient oil in the hydraulic    |                          |
  |            |                   |chamber.                                       |                          |
  +------------+-------------------+-----------------------------------------------+--------------------------+
  | |image001| | Home              |Worm positioning in nominal position between   | E10                      |
  |            |                   |SCRE and USCRE limit switches                  |                          |
  +------------+-------------------+-----------------------------------------------+--------------------------+
  | |image033| | Play test         |Check for nominal backlash (worm free play)    | F15, F15                 |
  |            |                   |between worm and worm wheel                    |                          |
  +------------+-------------------+-----------------------------------------------+--------------------------+

Any warnings and faults that occur during MotoSuiveur system operation are displayed on the HMI screen (if installed) and on the 7-segment display of the MS controller. 
Each fault is characterized by a number and a description. Faults are divided into two groups - system faults (in result of MS controller internal check) 
and MotoSuiveur system faults. 
System faults are those that are related to the electrical performance of the MS controller or mechanical. 
MotoSuiveur system faults are related to the working process of the MS unit.
Indication of warning or fault on MS Controller 7-segment display is a combination of letter and numbers. 
MS controller internal faults are indicated with blinked combination of |image035| , number and finish with symbol |image039|.
MS faults are displayed with combination of |image036| and number. MS warnings are displayed with combination of |image035| and number. 




Sowtware test
--------------

Software test perform check for correct version of MS controller firmware version.


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