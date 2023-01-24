================
Control cabinet
================

.. note::
	Describes what standard MS electrical panel is like. I/O, components, connectors, options…

.. note::
	Source: :download:`User Manual-7.4.doc`

About the MotoSuiveur control system
=====================================

The Motosuiveur® control system comes with different architectures to meet the installation requirements.

The Motosuiveur has been designed to be integrated almost stand-alone on hoisting system and basically requires 
only the servo-motor controller to be connected to the main hoist panel. However, most of the time, 
the Motosuiveur is integrated in the control system with its own control system.

All configurations integrate the very same servo-motor controller software.


Description
=============

Servo-motor controller
------------------------

Each Motosuiveur is fitted with a servo-motor that adapts the rotation of the worm screw to the orders given to the hoist motor. 
The servo-motor is controlled by a controller that embeds a software especially developed by the Motosuiveur manufacturer.

The servo-motor controller is connected directly to the servo-motor through a dedicated cable 
that controls the servo-motor and sends position data back to the controller.


Nameplate
----------

Architecture of a *standalone* Motosuiveur Solution
======================================================

.. _Architecture of a standalone Motosuiveur Solution:
.. figure:: img/control-cabinet-01.jpg
	:figwidth: 600 px
	:align: center

	Architecture of a standalone Motosuiveur Solution

In the standalone architecture, the Motosuiveur servo-motor controller receives only inputs from the Main hoist control panel, 
basically [⬆️ Up] and [⬇️ Down] and potentially analog and digital inputs from the Motosuiveur sensors.

Worm screw positions coming from digital sensors are sent to the Main hoist control panel.


Integration of the Motosuiveur in the control system
=======================================================

.. _Integration of the Motosuiveur in the control system
.. figure:: img/control-cabinet-02.jpg
	:figwidth: 600 px
	:align: center

	Integration of the Motosuiveur in the control system