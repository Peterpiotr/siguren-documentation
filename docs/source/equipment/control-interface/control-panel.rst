==============
Control Panel
==============

.. include:: /_img/_image-substitutions.rst

Layout of the control panel is defined according to pre-selected functionality relative to the MS Block Diagram. 
The control panel can be located on the control cabinet front door, can be external or a combination of both.
The operator has the facility to use the controls via switches or MSHMI.
The switches and HMI can be used to switch the operating modes of the MotoSuiveur® system.
Combination of active (ON) and inactive (OFF) signal lams gives current status of MotoSuiveur®. 


Front door panel layout
=======================

The control panel contains light indicators and control switches. They are divided into two groups: mandatory and optional.

Mandatory are:

- Hoist Enabled
- Fault
- Reset

The figure below shows an example overview of a control panel with and without MSHMI.

.. _Control panel figure:
.. figure:: /_img/Control-panel/control-panel-overview.png
	:align: center
	:figwidth: 600 px
	:alt: Control cabinet

	Control panel according documentation 

.. _General view of control panel:
.. figure:: /_img/Peter/control-panel-02.png
	:align: center
	:figwidth: 600 px
	:alt: Control cabinet

	Control panel as built


.. csv-table:: Control panel layout without MSHMI
   :file: ../../_tables/control-panel-legend.csv
   :delim: ;
   :header-rows: 1
   :widths: auto
   :class: tight-table
   :align: center


External control panel
======================

.. _General view of external control panel:
.. figure:: /_img/Peter/control-panel-external.png
	:align: center
	:figwidth: 600 px
	:alt: Control cabinet

	External control panel overview

.. csv-table:: External control panel
   :file: ../../_tables/control-panel-external.csv
   :delim: ;
   :header-rows: 1
   :widths: auto
   :class: tight-table
   :align: center


Mandatory signals and controls
==============================

Hoist enabled
^^^^^^^^^^^^^^

:guilabel:`🟢 Hoist enabled light` indicate that the MotoSuiveur® authorizes hoist movements. (figure 5).

Hoist enabled signal will be **ON** only in case if **ON** signal from hoist is **ON**.

Hoist enabled signal will be **ON** when :doc:`/operation/regular/self-test` procedure passes successfully and **ON** signal is available.
Then :guilabel:`🟢 Hoist enabled light` and :guilabel:`⚪ Healthy light` are **ON**. 
The signals are indicating ``system ready`` (``MotoSuiveur® ready``).



Fault 
^^^^^^

:guilabel:`🔴 Fault light` indicates three different types of faults:

	- MotoSuiveur® controller internal errors, described in section ????;
	- MotoSuiveur® faults (further called flt_num), described in section ????;
	- MotoSuiveur® warnings (further called wrn_num), described in section ???;

MotoSuiveur® :term:`controller` internal errors are related to MotoSuiveur® controller internal hardware, firmware, and MotoSuiveur® motor. 
This type of errors are with highest priority. 
If MotoSuiveur® controller internal fault appear further operation is prohibited.
	
.. note::	
 	:guilabel:`🔴 Fault light` is **ON** during MotoSuiveur® self-test.

.. warning:: 
	The system displays only last MotoSuiveur® warning (``wrn_num``) or MotoSuiveur® fault (``flt_num``) occurred.

Faults and warnings are displayed on MotoSuiveur® controller integrated 7-segment display. 
The display indicates all types of MotoSuiveur® warnings/faults and MotoSuiveur® controller internal errors. 
Indication is a combination of letters and numbers.
MotoSuiveur® controller internal faults are indicated with blinked combination of |image035|, number and finish with symbol |image039|.

MotoSuiveur® faults are displayed with combination of |image036| and number. 
MotoSuiveur® warnings are displayed with combination of |image035| and number. 


Reset 
^^^^^^

:guilabel:`🔘 Reset button` reset MotoSuiveur® system electrically and mechanically. After reset, MotoSuiveur® system is performing self-test. 


**References:**

:doc:`../../equipment/ms-solution/control-cabinet`