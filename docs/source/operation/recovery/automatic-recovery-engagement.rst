==============================
Automatic Recovery Engagement 
==============================

.. include:: ../../_img/_image-substitutions.rst


Automatic recovery engagement is used when emergency load lowering is required in case 
when the hoist control chain is damaged and the main hoist brake is holding the load.

.. important::
   Automatic recovery engagement is applicable to MotoSuiveur® System equipped with Integrated Recovery Drive (MS-IRD).

.. important::
   Automatic recovery engagement is applicable when the MotoSuiveur® System and MS-IRD are healthy. 

.. note::
	Upon engagement, knocking sound is heard.


Automatic Recovery Engagement for MotoSuiveur® System with **MSCL** MS Controllers
====================================================================================

To perform Automatic recovery engagement follow the sequence:

.. why? in which situation? 


Steps
	.. 1. Electrical power of MotoSuiveur® System and MS-IRD is **ON**.

		.. This is not a user action

	1. Switch :guilabel:`🔑 RECOVERY MODE OFF/ON` to position **ON**.

		.. figure:: ../../_img/Recovery/recovery-switch-on.png
			:figwidth: 300 px
			:class: instructionimg

			Activating recovery mode

			- The :guilabel:`🟠 RECOVERY MODE` indicator light comes on.

		.. figure:: ../../_img/Recovery/recovery-indicator-on.png
			:figwidth: 300 px
			:class: instructionimg

			Recovery mode light indicator

		- MS Controller 7-segment display indicates recovery mode - |image041|.

	2. Wait for :guilabel:`🟢 RECOVERY ENGAGED` light indicator to come on.

		.. figure:: ../../_img/Recovery/recovery-engaged-on.png
			:figwidth: 300 px
			:class: instructionimg

			Recovery engaged

	.. 4. **Automatic recovery engagement is completed.**

	.. what confirm this? - Recovery engaged` light indicator to come on
	.. let the final step not be an action?

	3. If :guilabel:`🟢 RECOVERY ENGAGED` indicator does not illuminate after **30 seconds** a Reset of the MotoSuiveur® system is required.
	


Automatic Recovery Engagement for MotoSuiveur® System with **MSCD** MS Controllers
===================================================================================

To perform Automatic recovery engagement follow the sequence:

Steps
	.. 1. Electrical power of MotoSuiveur® System and MS-IRD is **on**.

	..

	1. Switch :guilabel:`🔑 BACKUP/RECOVERY MODE OFF/ON` to position **ON**.
	
	The :guilabel:`🟠 BACKUP/RECOVERY MODE` indicator light illuminate.
	MS Controller 7-segment display indicates **Backup mode** - |image058|.

	.. figure:: ../../_img/Recovery/backup-recovery-on.PNG
		:figwidth: 300 px
		:class: instructionimg

		Activating Backlup/Recovery mode

	
	.. figure:: ../../_img/Recovery/backup-recovery-indicator-on.PNG
		:figwidth: 300 px
		:class: instructionimg

		Backup/Recovery mode light indicator

	2. Restart the MotoSuiveur® System.

	.. figure:: ../../_img/Recovery/reset.png
		:figwidth: 300 px
		:class: instructionimg

		Reset of MotoSuiveur® System

	.. note::
		During reset :guilabel:`🔑 BACKUP/RECOVERY MODE OFF/ON` is on position **ON**

	3. MotoSuiveur® System starts engaging. 

	.. note::
		Engaging can be defined like knocking sound.

	4. Wait until :guilabel:`🟢 RECOVERY ENGAGED` light indicator is illuminated.


	.. figure:: ../../_img/Recovery/recovery-engaged-on.png
		:figwidth: 300 px
		:class: instructionimg

		Recovery engaged SMD

	.. 6. Automatic recovery engagement is complete.

	.. what is the signal that confirms it

	5. If :guilabel:`🟢 RECOVERY ENGAGED` indicator does not illuminate after **30 seconds** a Reset of the MotoSuiveur® system is required.
		After Reset, MotoSuiveur® system repeats steps **3 and 4 automatically**. 

	.. this "important" should be in the steps














