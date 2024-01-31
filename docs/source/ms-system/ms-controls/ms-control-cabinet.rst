=============================
MotoSuiveur® Control Cabinet
=============================

MotoSuiveur® Control Cabinet (MSCC) is built according to the configuration of the MS control diagram. 

Description
=============

.. figure:: /_img/control-cabinet/Control-cabinet-overview.png
   :figwidth: 100 %
   :align: center

   MS Control Cabinet (example)  
    
Elements
    ① MS HMI Touchscreen (Human-Machine Interface)
            Shows actual MotoSuiveur® System status and information.
    ② Controls and indicator lights
            Change MotoSuiveur® operating mode. Actual status of MotoSuiveur® System.
    ③ Nameplate
            The nameplate of the MS Control Cabinet indicates model, serial number, date of production, voltage / power requirements.
    ④ Cable glands
            Control panel cables I/O.


..
    .. csv-table:: MS Control Cabinet overview
        :file: /_tables/control-cabinet-overview.csv
        :delim: ;
        :header-rows: 1
        :align: left
        :widths: auto


Nameplate
----------

MS Control Cabinet have nameplate located on front side of the door indicating input power (voltage, frequency, current), serial number, date.

The nameplate of the MS Control Cabinet indicates model, serial number, date of production, voltage / power requirements.
Exemplary general appearance of MS Control Cabinet nameplate shown on figure below.

.. figure:: /_img/control-cabinet/control-cabinet-nameplate.png
	:figwidth: 100 %
	:class: instructionimg

	MS Control Cabinet Nameplate

.. make it larger


Architecture of a MotoSuiveur® System
======================================================

.. figure:: /_img/archives/controlSignals.png
	:figwidth: 100 %
	:class: instructionimg

	Hoist-MS Control Signals

In the standalone architecture, the MS Controller receives only inputs from the main hoist control panel, 
basically [🔼 Up] and [🔽 Down] on terminal block T2. 

Terminal block T4 is a set of digital outputs (relays) providing MotoSuiveur® status information, as well as an enable signal for operation, 
enabling upward and downward movement signals.

Terminal blocks T3, T5\*\, T6, T7 and T8 are analog and digital inputs for MotoSuiveur® standalone system.

On figure below is presented the architecture of the MotoSuiveur® Solution.


\*\ *T5 is not shown on figure below*

.. why?

.. figure:: /_img/archives/generalViewConnectionsMS-MSCC.png
	:figwidth: 100 %
	:class: instructionimg

	MS Control Cabinet Connections

.. lines are crossing and confusing the drawing. MS is not red. update illustration

Integration of the MotoSuiveur® System in the hoist control system
=====================================================================

The integration of the MotoSuiveur® System into the control system of a new or existing hoist is done by pre-configuring the MS I/O interface. 

All electrical parameters and iterfaces are specified by the pre-configuration diagram.

.. why "pre-configuration" and not "configuration". say that its because it is done in the feasibility study?

.. figure:: /_img/control-cabinet/control-cabinet-configuration.png
	:figwidth: 100 %
	:class: instructionimg

	Integration of the MotoSuiveur® System in hoist control system

.. is the the "pre-configuration diagram" or something else? explicit
.. needs circled numbers 