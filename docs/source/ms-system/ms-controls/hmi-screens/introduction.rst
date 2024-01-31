=============
Introduction
=============

Touchscreen
============

.. include:: /ms-system/_img/substitutions.rst

The MotoSuiveur® HMI (MS HMI) is a Schneider Magelis/Harmony HMI STU 655/855 color graphic touchscreen terminal 
programmed with the MotoSuiveur® HMI firmware by Siguren technologies.

.. confusing to use "firmware" for the controller and the hmi or ok?

MotoSuiveur® HMI communicates with the MotoSuiveur® Controller via the MODBUS RTU 485 protocol.

.. figure:: /_img/archives/ms-hmi-01.png
	:scale: 100 %
	:align: center

	MS Controller and MS HMI 

MS HMI significantly expands the capabilities of MotoSuiveur® System by allowing:

   - Monitoring of MotoSuiveur® System status,
   - Displaying values of:
     
     - oddometer.
     - brake counter.
   
   - Displayng warning and fault messages and guidance on how to solve them.
   - Displaying the events log. Last 10 events are stored in memory after MS HMI Reset or power OFF.
   - Change the MotoSuiveur® settings. Configuration has a secure access code at different levels.
   - Displaying maintenance information of MotoSuiveur®.


.. note::
   | MotoSuiveur® HMI is an optional part of the MotoSuiveur® System and can be ordered additionally.
   | MS HMI can be added/ordered at any stage of a project.


MS HMI functions
=================

.. Important::
   Presented MS HMI operations are for firmware version 1.3.5 for MSCD controller.

.. what is MSCD

.. what about other versions?

The functions of MS HMI are organized in screens. 

Each screen has a set of functions and/or indicators and a :guilabel:`Return` button for redirection to the previous screen (one level up).


.. figure:: /_img/hmi/HMI-tree.PNG
   :figwidth: 100 %
   :align: center

   Navigation in MS HMI (top screens)

