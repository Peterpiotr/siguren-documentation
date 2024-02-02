===============
Control Panel 
===============

.. include:: /_img/_image-substitutions.rst

Layout of the control panel is defined according to pre-selected functionality relative to the MS Block Diagram. 
The control panel can be located on the MS Control Cabinet front door, can be external or a combination of both.
The operator has the facility to use the controls via switches or MS HMI.
The switches and HMI can be used to switch the operating modes of the MotoSuiveur® System.
Combination of active (ON) and inactive (OFF) signal lams gives current status of MotoSuiveur®. 

Mandatory signals and controls
==============================

Hoist ENABLED
---------------

:guilabel:`🟢 Hoist ENABLED light` indicate that the MotoSuiveur® authorizes hoist movements. (figure 5).

Hoist ENABLED signal will be **ON** only in case if **ON** signal from hoist is **ON**.

Hoist ENABLED signal will be **ON** when :doc:`/operation/regular/self-test` procedure passes successfully and **ON** signal is available.
Then :guilabel:`🟢 Hoist ENABLED light` and :guilabel:`⚪ Healthy light` are **ON**. 
The signals are indicating ``system ready`` (``MotoSuiveur® ready``).



Fault 
-------

:guilabel:`🔴 Fault light` indicates three different types of faults:

	- MS Controller internal errors, described in section ????;
	- MotoSuiveur® faults (further called flt_num), described in section ????;
	- MotoSuiveur® warnings (further called wrn_num), described in section ???;

MotoSuiveur® :term:`controller` internal errors are related to MS Controller internal hardware, firmware, and MotoSuiveur® motor. 
This type of errors are with highest priority. 
If MS Controller internal fault appear further operation is prohibited.
	
.. note::	
 	:guilabel:`🔴 Fault light` is **ON** during MotoSuiveur® Self-Test.

.. warning:: 
	The system displays only last MotoSuiveur® warning (``wrn_num``) or MotoSuiveur® fault (``flt_num``) occurred.

Faults and warnings are displayed on MS Controller integrated 7-segment display. 
The display indicates all types of MotoSuiveur® warnings/faults and MS Controller internal errors. 
Indication is a combination of letters and numbers.
MS Controller internal faults are indicated with blinked combination of |7s-E|, number and finish with symbol |7s-039|.

MotoSuiveur® faults are displayed with combination of |7s-F| and number. 
MotoSuiveur® warnings are displayed with combination of |7s-E| and number. 


Reset 
--------

:guilabel:`🔘 Reset` button resets the MotoSuiveur® System electrically and mechanically. After Reset, MotoSuiveur® System automatically runs a Self-Test. 



MS Control Cabinet front door panel layout
===========================================

The control panel contains light indicators and control switches. They are divided into two groups: mandatory and optional.

Mandatory are:

- Hoist Enabled
- Fault
- Reset

The figure below shows an example overview of a control panel with and without MS HMI.

.. figure:: /_img/control-panel/control-panel-overview.png
	:class: instructionimg
	:figwidth: 100 %
	:alt: MS Control Cabinet

	Control panel according to documentation 

.. figure:: /_img/archives/control-panel-02.png
	:class: instructionimg
	:figwidth: 100 %
	:alt: MS Control Cabinet

	Control panel as built


.. csv-table:: Control panel layout without MS HMI
   :file: /_tables/control-panel-legend.csv
   :delim: ;
   :header-rows: 1
   :widths: auto


Remote control panel
======================

.. figure:: /_img/archives/control-panel-external.png
	:class: instructionimg
	:figwidth: 100 %
	:alt: MS Control Cabinet

	External control panel overview

.. csv-table:: External control panel
   :file: /_tables/control-panel-external.csv
   :delim: ;
   :header-rows: 1
   :widths: auto




