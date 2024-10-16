=====
MSHMI
=====

.. include:: ../equipment/_img/substitutions.rst


The MotoSuiveur® HMI (MSHMI) is a Schneider Magelis/Harmony HMI STU 655/855 color graphic touchscreen terminal 
programmed with the MotoSuiveur®HMI firmware by Siguren technologies. 
MotoSuiveur® HMI communicates with the MotoSuiveur® controller via MODBUS RTU 485 protocol.

MSHMI significantly expands the capabilities of MotoSuiveur® system by allowing:

- Monitoring of actual MotoSuiveur® system status
- Displayng value of oddometer 
- Displayng value of  brake counter
- Displayng warning and fault messages and guidance on how to solve them
- Displaying log of events. Last 10 events are stored in memory after MSHMI reset or power off
- Change the MotoSuiveur® settings. Configuration has a secure access code at different levels
- Display maintenance information of MotoSuiveur®


.. _MotoSuiveur® HMI view:
.. figure:: ../../_img/Peter/ms-hmi-01.png
	:scale: 100 %
	:align: center

	MotoSuiveur® HMI 

.. note::
    MotoSuiveur®HMI is not part of standard MotoSuiveur® equipment and can be ordered additionally.
    MSHMI can be added/ordered in any stage of project.

MSHMI Touch Screen Operations
=============================
.. Important::
   Presented MSHMI operations are for firmware version 1.3.5 for MSCD controller!


.. note::
 The functions of MSHMI are organized in screens. 
 Each screen has a set of functions and/or indicators and a *Return* button for redirection to the previous screen (one level up).

.. _Menu Screen Components:
.. figure:: ../../_img/HMI/HMI-tree.PNG
	:figwidth: 1200 px


- `Main Screen Components`_
- `Menu Screen`_
- `MS variables Screen`_
- `Maintenance Screen`_
- `Self-test Screen`_
- `Event record Screen`_
- `Version Screen`_
- `Language Screen`_

Screens decription
==================

Main Screen
------------

Main screen appears after a successful connection between MSHMI and the controller.
Main screen provides actual status for MS system. 

.. _Main Screen Components:
.. figure:: ../../_img/HMI/main-screen.PNG
	:figwidth: 500 px

	Main screen components

.. csv-table:: Main screen
   :file: ../../_tables/HMI/main.csv
   :delim: ;
   :header-rows: 1
   :widths: auto
   :class: tight-table
   :align: left


Menu Screen
------------

Menu screen contains all submenus for setup, status and information of MS system.

.. Important::
   Access to some screens is password protected!

.. figure:: ../../_img/HMI/menu-screen.PNG
	:figwidth: 500 px

	Menu screen components

.. csv-table:: Menu screen
   :file: ../../_tables/HMI/menu.csv
   :delim: ;
   :header-rows: 1
   :widths: auto
   :class: tight-table
   :align: left

MS Variables Screen
-------------------

Screen MS variables displays and allows to changing variables that are stored in MS
Controller memory. Variables are types **VL** (Long) in range 0 – 63 and type **VR** (Real) in
range 0 - 63.

.. figure:: ../../_img/HMI/variables.PNG
	:figwidth: 500 px

	MS variables screen components

.. csv-table:: MS variables screen
   :file: ../../_tables/HMI/variables.csv
   :delim: ;
   :header-rows: 1
   :widths: auto
   :class: tight-table
   :align: left

Navigation to MS variables screen and change value of variable

1. On Main screen tap Menu button.
2. On Menu screen tap on MS variables button.
3. To exit from MS variables screen, tap on Back button.
4. Select type of variable (VR or VL0) by tap on VR/VL button.
5. Select variable by tap on arrows 🔼 🔽
6. Entere desired value by tap on *Enter desired value* field 🟩
7. On screen numlock pad appears
8. Eneter desired value and tap on *Enter* button. To exit from numpad without changes tap on *Esc* button
9. To set current value becomes equal to desired, tap on green tick button ✅

.. _Navigation to MS variables Screen:
.. figure:: ../../_img/HMI/change-variable.PNG
   :figwidth: 500 px


.. Important::
   Variables list and changing values of variables is allowed only for authorized personnel!


Maintenance Screen
-------------------

Screen Maintenance displays maintenance information of MS system. This screen
provides information about maintenance parameters status of MS system – Total brakes, working time of MS, odometer, workmeter.
Based on current values of parameters is displayed what type of maintenance is needed. 
Maintenance type is displayed with letters A, B, C and D. Information regarding
different types can be taken by pressing *Maintenance Info* button.

.. figure:: ../../_img/HMI/maintenance.PNG
	:figwidth: 500 px

	Maintenance screen components

.. csv-table:: Maintenance screen
   :file: ../../_tables/HMI/maintenance.csv
   :delim: ;
   :header-rows: 1
   :widths: auto
   :class: tight-table
   :align: left

.. _Maintenance info:
.. figure:: ../../_img/HMI/change-maintenance.PNG
	:figwidth: 500 px

	Maintenance info pop up window



Self-test Screen
-----------------

Screen Self-Test displays values from last MS system self-test. 

.. figure:: ../../_img/HMI/self-test.PNG
	:figwidth: 500 px

	Self-test screen components

.. csv-table:: Self-test screen
   :file: ../../_tables/HMI/self-test.csv
   :delim: ;
   :header-rows: 1
   :widths: auto
   :class: tight-table
   :align: left


Event record Screen
-------------------

Screen Event Records gives option to choose between 3 logging groups. Opening
presents specific events of MS system. Every logging group stores last 10 events
after restart or power loss of MSHMI.

.. figure:: ../../_img/HMI/logging-groups.PNG
	:figwidth: 500 px

	Event record screen components

.. csv-table:: Event record screen
   :file: ../../_tables/HMI/event-record.csv
   :delim: ;
   :header-rows: 1
   :widths: auto
   :class: tight-table
   :align: left

.. _MS status log Screen:
.. figure:: ../../_img/HMI/status-log.PNG
	:figwidth: 500 px

	MS status log screen components

MS Status log group contains all events appears during MS system operation.

.. _MS warning log Screen:
.. figure:: ../../_img/HMI/warning-log.PNG
	:figwidth: 500 px

	MS warning log screen components

MS Warning log group contains all warning events appears during MS system operation.

.. _MS fault log Screen:
.. figure:: ../../_img/HMI/fault-log.PNG
	:figwidth: 500 px

	MS fault log screen components

MS Warning log group contains all fault events appears during MS system operation.

.. csv-table:: Log screens 
   :file: ../../_tables/HMI/log-components.csv
   :delim: ;
   :header-rows: 1
   :widths: auto
   :class: tight-table
   :align: left

Version Screen
-------------------

Screen Version presents information about MS sytem: name of project, HMI firmware version, Software
version and MS Controller firmware version.

.. figure:: ../../_img/HMI/system-information.PNG
	:figwidth: 500 px

	Version screen components

.. csv-table:: Version screen 
   :file: ../../_tables/HMI/system-information.csv
   :delim: ;
   :header-rows: 1
   :widths: auto
   :class: tight-table
   :align: left


Language Screen
-------------------

Screen Language allows change of screen language.

.. figure:: ../../_img/HMI/language.PNG
	:figwidth: 500 px

	Language screen components

.. csv-table:: Language screen 
   :file: ../../_tables/HMI/language.csv
   :delim: ;
   :header-rows: 1
   :align: left







