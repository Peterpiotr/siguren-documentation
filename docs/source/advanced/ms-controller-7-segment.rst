=========================================
Reading MS Controller 7-Segment Messages
=========================================

.. mess of different expressions: warnings, faults, errors, of the MS, of the System, of the Controller, etc. 
.. Clarify

Display of faults/warnings
===========================

.. include:: /_img/_image-substitutions.rst

Any faults/warnings that occur during MS operation are displayed :

    - on the 7-segment display of the MS Controller,
    - on the HMI screen (if installed). 

Each fault is characterized by a number and a description. 

Faults are divided into two groups: 

    - **System faults** are related to the electrical performance of the MS Controller.
    - **MotoSuiveur® System faults** are related to operating of the MS Unit.

.. the names of the two fault groups are not different nor explicit enough


Faults and warnings displayed on MS 7-segment display of the controller indicate all types of MotoSuiveur® System warnings/faults and MS Controller internal errors. 
Indication is a combination of letters and numbers. 

**MS Controller internal faults** are indicated with a blinking combination of:

    |7s-E| + NUMBER + END symbol |7s-039|.

.. figure:: /_img/archives/MScontrollerInternalErrorE01.png
	:figwidth: 100 %
	:class: instructionimg

	MS Controller internal error displaying

**MotoSuiveur® System faults** are displayed with combination of |7s-F| and number. 

**MS warnings** are displayed with combination of |7s-E| and number. 

.. figure:: /_img/archives/MSwarningNumber10.png
	:figwidth: 100 %
	:class: instructionimg

	MotoSuiveur® System E10

.. warning::
 	In case of repetitive faults/warnings, please contact SIGUREN technologies technologies at support@siguren.com
