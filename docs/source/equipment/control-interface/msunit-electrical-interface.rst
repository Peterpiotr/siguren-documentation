==============================
MS Unit Electrical Interface
==============================

Principle location of electrical components on MS Unit are shown on figure below.

.. _Electrical connections of MS Unit:
.. figure:: /_img/controls-installation/MS-unit.PNG
	:figwidth: 100 %
	:class: instructionimg

	Electrical connection of MS Unit

.. csv-table:: MS Unit electrical components
   :file: /_tables/ms-unit-electrical-connection.csv
   :delim: ;
   :header-rows: 1
   :align: left
   :widths: auto

.. replace with circled numbers


MS servo motor - C6 & C7
===========================

Connectors C6 and C7 should be made according following specification:

.. why C6, C7?

-	For C6 connector should be used screened cable, 4 core, 1.5 mm². Ground the shield of the feedback should be connected to GND.

.. figure:: /_img/controls-installation/C6.png
	:figwidth: 100 %
	:class: instructionimg

	Connector C6


- For C7 connector screened cable with 4 twisted pairs, 0.25 mm² should be used. Ground the shield of the feedback should be connected to GND.

.. figure:: /_img/controls-installation/C7.png
	:figwidth: 100 %
	:class: instructionimg

	Connector C7

Signal arrangement of connector on motor side for motor type S1. 

.. figure:: /_img/controls-installation/S1-power.PNG
	:figwidth: 100 %
	:class: instructionimg

	Power connector type S1 (C6)

.. figure:: /_img/controls-installation/S1-resolver.PNG
	:figwidth: 100 %
	:class: instructionimg

	Resolver connector type S1 (C7)



Signal arrangement of connector on motor side for motor type S2. 


.. figure:: /_img/controls-installation/S2-power.PNG
	:figwidth: 100 %
	:class: instructionimg

	Power connector type S2 (C6)


.. figure:: /_img/controls-installation/S2-resolver.PNG
	:figwidth: 100 %
	:class: instructionimg

	Resolver connector type S2 (C7)



Oil and temperature sensors
=============================

Oil level sensor (S1) and Temperature sensor (S2) are standard 4 male pin M12 connector type PNP or NPN type. 
Figure below shows M12 connector specification and present information which type should be used. 

.. figure:: /_img/controls-installation/oil-and-temp.png
	:figwidth: 100 %
	:class: instructionimg

	M12 connector layout


.. figure:: /_img/controls-installation/oil-sensors-connection.png
	:figwidth: 100 %
	:class: instructionimg

	Oil and temperature sensors connection


Proximity sensors / limit switches
=====================================

.. rename this to reflect the purpose of the equipment, not its nature.

Position proximity sensors/switches are used for allowing or disallowing hoist movement. Position sensors/switches are using in active state output signal. 

.. figure:: /_img/controls-installation/scr-uscr.PNG
	:figwidth: 100 %
	:class: instructionimg

	Movement table

The figure below shows an example of the installation of the limit switches. 
NC contacts are used for connection. Signal from switches is active when they are not pressed.

.. figure:: /_img/controls-installation/limit-switches.png
	:figwidth: 100 %
	:class: instructionimg

	Limit switches

.. typos on the illustration. that is why we should use circled numbers + translation purpose
.. are the labels SCRE UNSCRE and RES on the actual swtiches? it could be a good thing even though their positions define them
.. illustrate with AND without recovery for sensors AND switches. at least say which is which below the images.

In case proxy position sensors are used, sensors are with NO output and are active when worm is in correct position. 

.. figure:: /_img/controls-installation/position-sensors.png
	:figwidth: 100 %
	:class: instructionimg

	Proximity sensors


Recovery motor connections
============================

Recovery systems are two types with same functionality:

  - AC asynchronous motor controlled by variable speed drive.
  - DC motor controlled by Siguren Motor Controller MSRM4514.

.. depends on MS Size? 

.. variable speed drive is schneider drive?

AC asynchronous motor is controlled by 230VAC or 400VAC variable speed drive. 
Windings of motor are connected in STAR (Y) configuration.

.. figure:: /_img/controls-installation/motor-star-connection.png
	:figwidth: 100 %
	:class: instructionimg

	Star connection schematic

.. figure:: /_img/controls-installation/recovery-motor-connection-star.jpg
	:figwidth: 100 %
	:class: instructionimg

	AC motor connection

DC motor is controlled by MSRM4514 motor controller operating on 48VDC voltage.

.. figure:: /_img/controls-installation/recovery-motor-dc.jpg
	:figwidth: 100 %
	:class: instructionimg

	DC motor connection
