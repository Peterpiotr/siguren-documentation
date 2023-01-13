================
Control cabinet
================

Control panel
==============

Indication lamps and controls
------------------------------

Indication lamps and local controls are shown on figure 3. They are located on front door of control cabinet. 
Indication lamps indicates:
	- MS status - figure 3, items 2, 8;
	- allowed movement direction of hoist - figure 3, items 1, 3, 9;
	- recovery mode status - figure 3, items 10, 11.
  
Local controls are used for:
	- reset of MS - figure 3, item 7;
	- overrides MS enable signal (override ON signal) - figure 3, item 6;
	- enable and control MS Backup/ Recovery mode - figure 3 items 4, 5, 10, 11.

:numref:`Control signals between hoist and MS` shows schematically the control signals between hoist and MS. 
 
.. _Control signals between hoist and MS:
.. figure:: 05_images/controlSignals.png
	:scale: 100 %
	:align: center

	Control signals between hoist and MS

.. warning::
 	Local control commands can be duplicated with remotes!
	Please, check electrical circuit diagram!



Hoist enabled
^^^^^^^^^^^^^^^^^^^^^

Hoist enabled lamp indicate that the MS authorizes hoist movements. (figure 5). Hoist enabled signal will on only in case if ON signal from hoist is ON.

Hoist enabled signal will be ON when MS self-test pass successfully and ON signal is available then Hoist enabled and Healthy indicator lamps are on. The signals are indicating system ready (MS ready).



Fault 
^^^^^^^^^^^^^^^^^^^^^

Fault lamp (figure 3, item 2) indicates three different types of faults:
	- MS controller internal errors, described in section 7.1;
	- MS faults (further called flt_num), described in section 7.2;
	- MS warnings (further called wrn_num), described in section 7.2;

MS controller internal errors are related to MS controller internal hardware, firmware, and MS motor. This type of errors are with highest priority. If MS controller internal fault appear further operation is prohibited.
	
.. note::	
 	Fault lamp indicator is on during MS self-test.

.. warning:: 
	The system displays only last MS warning (wrn_num) or MS fault (flt_nim) occurred.

.. ------------- Substitution definitions for 7-segments digits -------------------
	to be able to include them INLINE in the next paragraph
.. |image001| image:: img/digits/image001.png 
.. |image003| image:: img/digits/image003.png 
.. |image007| image:: img/digits/image007.png 
.. |image009| image:: img/digits/image009.png 
.. |image011| image:: img/digits/image011.png 
.. |image013| image:: img/digits/image013.png 
.. |image015| image:: img/digits/image015.png 
.. |image017| image:: img/digits/image017.png 
.. |image019| image:: img/digits/image019.png 
.. |image021| image:: img/digits/image021.png 
.. |image023| image:: img/digits/image023.png 
.. |image025| image:: img/digits/image025.png 
.. |image027| image:: img/digits/image027.png 
.. |image029| image:: img/digits/image029.png
.. |image031| image:: img/digits/image031.png 
.. |image033| image:: img/digits/image033.png 
.. |image035| image:: img/digits/image035.png
.. |image036| image:: img/digits/image036.png
.. |image039| image:: img/digits/image039.png
.. |image041| image:: img/digits/image041.png 
.. --------------------------------

Faults and warnings are displayed on MS 7 - segment controller. The display indicates 
all types of MS warnings/faults and MS controller internal errors. 
Indication is a combination of letters and numbers. MS controller internal 
faults are indicated with blinked combination of |image035|, number and finish 
with symbol |image039|.

MS faults are displayed with combination of |image036| and number. 
MS warnings are displayed with combination of |image035| and number. 

.. rubric:: Displaying messages on MS controller 7 - segment display

On :numref:`MS controller internal error E01` is shown example for internal MS controller fault. 
On :numref:`MS warning number 10 (wrn_num = 10)` is shown example for MS warning.

.. _MS controller internal error E01:
.. figure:: 05_images/MScontrollerInternalErrorE01.png
	:scale: 100 %
	:align: center

	MS controller internal error E01 

.. _MS warning number 10 (wrn_num = 10):
.. figure:: 05_images/MSwarningNumber10.png
	:scale: 100 %
	:align: center

	MS warning number 10 (wrn_num = 10) 

.. note::		
 	After MS reset, all types of faults are cleared. Before MS reset, fault should be resolved.


Upward enable/Downward enable 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Upward enable/Downward enable are indicators for authorized direction of hoist movement. 
If one of the two directions is forbidden to move, it is necessary to move the hoist 
in the opposite direction in order to reset the system mechanically.

Movements upward and downward of hoist are correspond to screwing and unscrewing 
movement of MS worm. Movement directions of worm are corresponding to directions 
of clock. Direction screwing is clockwise, unscrewing direction is anticlockwise, 
viewed from cam part of the screw shaft as is shown 
on :numref:`MS Worm rotating directions`.
 
.. _MS Worm rotating directions:
.. figure:: 05_images/MSwormrotatingDirections.png
	:scale: 80 %
	:align: center

	MS Worm rotating directions 

.. line-block::
	1 - Screwing direction
	2 - Unscrewing direction

.. warning::
 	After MS reset or manual centering of the worm and MS restart, 
	no movement is performed or faults appears, please contact SIGUREN 
	technologies on address support@siguren.com


Backup/Recovery Off/On; Backup/Recovery Down/Up
^^^^^^^^^^^^^^^^^^^^^

Backup function allows the load to be lowered down, by using minimal functionalities 
when MS is in Following operation mode. Backup function ignore all settings related 
with nominal following operation mode and allows movement of the hoist with limited speed.

Recovery function is used when the main hoisting chain is faulty (for example damaged
brake of the hoist motor). Recovery system allows lowering load safety to the ground.

Enable Override
^^^^^^^^^^^^^^^^^^^^^

Enable override can be used if it is necessary to override Hoist enabled. This allows 
small movements for MS mechanically reset.

Lamp states
^^^^^^^^^^^^^^^^^^^^^

Combination of active (ON) and inactive (OFF) signal lams gives current status of MS. 
In Appendix Table 1 signal combinations are presented and described.


Drive
======

Drive=Controller

GUI
====