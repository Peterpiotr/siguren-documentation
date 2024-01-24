=====================================================================
Connection between MotoSuiveur® control cabinet and MS Unit
=====================================================================

After mechanical assembly of MotoSuiveur® System to hoist is done, electrical connection must be made between MS and control cabinet. 
Figure below shows general view of typical MotoSuiveur®  electrical components that should 
be connected according specific for the project electrical circuit diagram.

.. note::
  All electrical connections are to be made according to electrical circuit diagram of the project!

Electrical connection of the MotoSuiveur® control cabinet
=========================================================


.. _Electrical connections of MotoSuiveur® panel:
.. figure:: /_img/archives/generalViewConnectionsMS-MSCC.png
	:figwidth: 465 px
	:class: instructionimg

	Electrical connection of MotoSuiveur® panel

.. csv-table:: MotoSuiveur® System electrical components
   :file: /_tables/electrical-connection.csv
   :delim: ;
   :header-rows: 1
   
   :align: left
   :widths: auto

Terminals **T1, T2, T4, T4, T6, T7** are mandatory.


In the table below is presented a complete and detailed description of the terminals.
The set of inputs and outputs is defined in advance for each project based on pre-configuration diagram (MS block diagram).


.. csv-table:: Detailed description of terminals
   :file: /_tables/terminasl-description.csv
   :delim: ;
   :header-rows: 1
   
   :align: left
   :widths: auto


\*\ If power supply is separated

\**\ Control voltage from MS control cabinet

\***\ After Reset command MS performs self-test

\****\ Backup and Recovery mode in some models can be combined in common switch Backup/Recovery
 	 
PS – Power Supply

DI – Digital Input

DO – Digital Output/Relay Contact Output

AI – Analog Input

AO – Analog Output

RES – Resolver 

CV – Control Voltage



Electrical connection of the MS Unit
===============================================

Principle location of electrical components on MS Unit are shown on figure below.

.. _Electrical connections of MS Unit:
.. figure:: /_img/controls-installation/MS-unit.PNG
	:figwidth: 465 px
	:class: instructionimg

	Electrical connection of MS Unit

.. csv-table:: MS Unit electrical components
   :file: /_tables/ms-unit-electrical-connection.csv
   :delim: ;
   :header-rows: 1
   
   :align: left
   :widths: auto

How to connect MS servo motor - C6 & C7
----------------------------------------

Connectors C6 and C7 should be made according following specification:

-	For C6 connector should be used screened cable, 4 core, 1.5 mm². Ground the shield of the feedback should be connected to GND.

.. _Connector C6:
.. figure:: /_img/controls-installation/C6.png
	:figwidth: 465 px
	:class: instructionimg

	Connector C6


- For C7 connector screened cable with 4 twisted pairs, 0.25 mm² should be used. Ground the shield of the feedback should be connected to GND.

.. _Connector C7:
.. figure:: /_img/controls-installation/C7.png
	:figwidth: 465 px
	:class: instructionimg

	Connector C7

Signal arrangement of connector on motor side for motor type S1. 

.. _Power connector type S1:
.. figure:: /_img/controls-installation/S1-power.PNG
	:figwidth: 465 px
	:class: instructionimg

	Power connector type S1 (C6)

.. _Resolver connector type S1:
.. figure:: /_img/controls-installation/S1-resolver.PNG
	:figwidth: 465 px
	:class: instructionimg

	Resolver connector type S1 (C7)



Signal arrangement of connector on motor side for motor type S2. 

.. _Power connector type S2:
.. figure:: /_img/controls-installation/S2-power.PNG
	:figwidth: 465 px
	:class: instructionimg

	Power connector type S2 (C6)

.. _Resolver connector type S2:
.. figure:: /_img/controls-installation/S2-resolver.PNG
	:figwidth: 465 px
	:class: instructionimg

	Resolver connector type S2 (C7)



How to connect oil and temperature sensors
------------------------------------------

Oil level sensor (S1) and Temperature sensor (S2) are standard 4 male pin M12 connector type PNP or NPN type. 
Figure below shows M12 connector specification and present information which type should be used. 

.. _M12 connector layout:
.. figure:: /_img/controls-installation/oil-and-temp.png
	:figwidth: 465 px
	:class: instructionimg

	M12 connector layout


.. _Oil and temperature:
.. figure:: /_img/controls-installation/oil-sensors-connection.png
	:figwidth: 465 px
	:class: instructionimg

	Oil and temperature sensors connection


How to connect proximity sensors / limit switches
-------------------------------------------------

Position proximity sensors/switches are used for allowing or prohibits hoist movement. Position sensors/switches are using in active state output signal. 

.. _Movement:
.. figure:: /_img/controls-installation/scr-uscr.PNG
	:figwidth: 465 px
	:class: instructionimg

	Movement table

The figure below shows an example of the installation of the limit switches. 
NC contacts are used for connection. Signal from switches is active when they are not pressed.

.. _Limit switches:
.. figure:: /_img/controls-installation/limit-switches.png
	:figwidth: 465 px
	:class: instructionimg

	Limit switches


In case of proxy position sensors are used, sensors are with NO output and are active when worm is in correct position. 

.. _Proximity sensors:
.. figure:: /_img/controls-installation/position-sensors.png
	:figwidth: 465 px
	:class: instructionimg

	Proximity sensors


How to connect recovery motor
-----------------------------

Recovery systems are two types with same functionallity.:
- AC asynchronous motor controlled by variable speed drive;
- DC motor controlled by Siguren motor controller MSRM4514

AC asynchronous motor is controlled by 230VAC or 400VAC variable speed drive. 
Windings of motor are connected in STAR (Y) configuration.

.. _Star connection schematic:
.. figure:: /_img/controls-installation/motor-star-connection.png
	:figwidth: 465 px
	:class: instructionimg

	Star connection schematic

.. _Star connection:
.. figure:: /_img/controls-installation/recovery-motor-connection-star.jpg
	:figwidth: 465 px
	:class: instructionimg

	AC motor connection

DC motor is controlled by MSRM4514 motor controller operating on 48VDC voltage.

.. _DC motor:
.. figure:: /_img/controls-installation/recovery-motor-dc.jpg
	:figwidth: 465 px
	:class: instructionimg

	DC motor connection
