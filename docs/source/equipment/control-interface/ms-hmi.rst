========
MotoSuiveur HMI
========

.. include:: ../equipment/_img/substitutions.rst


The MotoSuiveur HMI (MSHMI) is a Schneider Magelis/Harmony HMI STU 655/855 color graphic touchscreen terminal 
programmed with the MotoSuiveurHMI firmware by Siguren technologies. 
MotoSuiveur HMI communicates with the MotoSuiveur controller via MODBUS RTU 485 protocol.

MSHMI significantly expands the capabilities of MotoSuiveur system by allowing:

- Monitoring of actual MotoSuiveur system status
- Displayng value of oddometer 
- Displayng value of  brake counter
- Displayng warning and fault messages and guidance on how to solve them
- Displaying log of events. Last 10 events are stored in memory after MSHMI reset or power off
- Change the MotoSuiveur configuration. Configuration has a secure access code at different levels
- Display maintenance information of MotoSuiveur


.. _MotoSuiveur HMI view:
.. figure:: ../../_img/ms-hmi-01.png
	:scale: 100 %
	:align: center

	MotoSuiveur HMI 

.. note::
    MotoSuiveurHMI is not part of standard MotoSuiveur equipment and can be ordered additionally.

MSHMI Touch Screen Operations
=============================

The functions of MSHMI presented above are organized in screens. 
Each screen has a set of functions and/ or indicators and a button to return to the previous screen (one level up).


Main Screen
------------
.. _Main Screen Components:
.. figure:: ../../_img/HMI/main-screen.PNG
	:figwidth: 500 px

	Main Screen Components

.. csv-table:: Main screen
   :file: ../../_tables/HMI/main.csv
   :delim: ;
   :header-rows: 1
   :widths: auto
   :class: tight-table
   :align: center

Menu Screen
------------

+-------------------------------------+
| Navigation                          |
+=====================================+
| Main screen ➔ Menu screen          |
+-------------------------------------+


.. _Menu Screen Components:
.. figure:: ../../_img/HMI/menu-screen.PNG
	:figwidth: 500 px

	Menu Screen Components

.. csv-table:: Menu screen
   :file: ../../_tables/HMI/menu.csv
   :delim: ;
   :header-rows: 1
   :widths: auto
   :class: tight-table
   :align: center

MS variables Screen
------------

.. _MS variables Screen:
.. figure:: ../../_img/HMI/variables.PNG
	:figwidth: 500 px

	Menu Screen Components

.. csv-table:: MS variables screen
   :file: ../../_tables/HMI/variables.csv
   :delim: ;
   :header-rows: 1
   :widths: auto
   :class: tight-table
   :align: center


.. _Navigation to MS variables Screen:
.. figure:: ../../_img/HMI/change-variable.PNG
	:figwidth: 500 px

   Navigation to MS variables screen

To open MS Variables screen from the Main screen the following is required:

1. On Main screen tap Menu button.
2. On Menu screen tap on MS variables button.
3. To exit from MS variables screen, tap on Back button.



Comments:

-	See “User rights” to check the rights and authorized access depending on the entered password
-	To quit the password menu, click on “ESC”
-	To erase the last digit, press “BS”
-	To erase all digits, press “CLR”
-	To switch from lower case to capital letters (or back), press “CAPS”
-	For security reasons, when a password is entered, the authorization is given during 5 minutes for the access of each level. After 5 minutes, the operator should enter the password again
-	The required password level is the minimum level asked to the operator (for instance, when level 2 is required, the operator can enter level 2 or level 3)
-	If the password is wrong, this screen is displayed.