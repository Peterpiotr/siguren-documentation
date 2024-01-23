===========================================================
Backup mode by manual action of the service brake procedure
===========================================================


.. include:: /_img/_image-substitutions.rst

.. role:: mechpart
   :class: mechpart

MotoSuiveur® Followed Gravity Lowering
=======================================

Step Lowering
^^^^^^^^^^^^^^^^

.. note::
	This method can be used **only with Hydraulic Damping MotoSuiveur® Unit**.

This lowering method is based on pulse opening the hoist brake (manually or electrically) to lower the load a few centimeters per single open. 
The MotoSuiveur® Unit worm shaft will shift toward the damping chamber each time the brake is opened. 
The electrical or brake lever pulse must be short enough to not allow the worm to reach the MotoSuiveur® Unit elastomer at the bottom of the damping chamber. 
Then it is possible to return the worm shaft to its “centered” position by hand using Handheld recovery tool. 
Repeat this until the load reaches the floor.

This way, very low torque applied on the MotoSuiveur® Unit worm shaft will be needed (approximately 1/5000 of the barrel torque). 
Using handwheel / crank handle or standard ratchet handle.

The MotoSuiveur® Unit can automatically follow if switched to Backup Mode. 
This negates the need of manual operation at the worm shaft. 
In case of power outage, the MotoSuiveur® can be UPS/battery operated.
Furthermore, the MotoSuiveur® system can control the brake opening / closing, thus making the gravity load recovery automated.

Instructions
	1. Pulse the hoist brake to achieve less than 30 degrees barrel rotation by gravity.
	2. Rotate the worm shaft by hand **in anticlockwise direction** few rotations to centralize it between limit switches.
	3. Repeat steps 1 and 2 until load is safely lowered.

	.. figure:: /_img/archives/stepLowering.png
		:figwidth: 100 %
		
		Hydraulic Damping MS step lowering

.. important::
	Indicative mean barrel speed: 0.5 rpm


Backup Mode gravity lowering
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Backup mode gravity lowering is methos for semi-automated lowering. Manual opening of hoist motorbrake and automatically following of MotoSuiveur® system.
Backup mode allows following with limited speed and no fault detection.

Instructions
	1. Switch on the MotoSuiveur® System to :doc:`Backup Mode <backup-procedure>`.

	.. figure:: /_img/backup/switch-on-backup.png
		:figwidth: 100 %
		
		Switch on Backup Mode

	1. Order lowering by switch :guilabel:`Backup mode Down/Up` to position **Down**. 

	.. figure:: /_img/backup/backup-down-up-control.png
		:figwidth: 600 px
		
		Order lowering

	1. Progressively release the motor brake using the provided :mechpart:`Brake Release Tool`, until the load starts to rotate the barrel.

	.. figure:: /_img/backup/manual-open-hoist-brake.png
		:figwidth: 100 %
		
		Opening hoist main brake


	1. Use the Brake Release Tool to regulate and maintain the speed below the specified safe speed. A :guilabel:`🔊 buzzer` will sound when the safe speed is close.

	.. figure:: /_img/backup/speed-limit-buzzer.png
		:figwidth: 600 px
		
		Specified limit speed reached

	.. figure:: /_img/backup/backup-time-diagram.png
		:figwidth: 600 px
		
		Backup gravity lowering diagram


.. note::
	The MotoSuiveur® system will arrest the barrel if:

	-	lowering order is removed or,
	-	overspeed is reached.

.. note::
	After such arrest, the worm shaft can be returned to its “centered” position by using a tool (handheld).


.. important::
	In case of power outage, the MS can be UPS/battery operated.


.. important::
	Indicative barrel speed: 2 - 5 rpm


Assisted gravity lowering
----------------------------

In this type of lowering, only moderate torque is to be applied to the MS worm shaft (approximately 1/250 of the barrel torque).

Using the following hardware:

- Handheld Recovery Tool for MS sizes above MS4,
- Handwheel / crank handle or standard ratchet handle for sizes MS0 – MS3

Instructions
  1. Apply moderate torque to the MS worm shaft, using the appropriate method.

  ..

  2. Progressively release the motor brake, using the provided Brake Release Tool, until the load starts to rotate the barrel (as long as moderate torque is applied to the MS shaft).

  ..

  3. Rotate the MS worm shaft to lower the load.

  ..

  4. Use the Brake Release Tool to maintain the torque to be applied to on the worm shaft inside the specified limits.


.. figure:: /_img/archives/MSassistedGravityLowering.png
	:figwidth: 100%

	Assisted gravity lowering

.. csv-table:: Table of MS assisted gravity lowering max torques
   :file: ../../_tables/MSassistedGravityLowering.csv
   :header-rows: 1



Automated backup gravity lowering with controlling hoist brake by MotoSuiveur® System
--------------------------------------------------------------------------------------

This type of gravity lowering is fully automated and controlled by MotoSuiveur® system.
MotoSuiveur® system opens hoist main brake and follow load moving by gravitation.
Following continues until speed reaches predefined speed and MotoSuiveur® system closes hoist brake.
The starting and termination of the lowering is controlled by an operator.


Instructions
   1. Switch on the MotoSuiveur® System to :doc:`Backup Mode <backup-procedure>`.

   .. figure:: /_img/backup/switch-on-backup.png
   	:figwidth: 600 px
   	
   	Switch on Backup Mode

   2. Order lowering by switch and hold :guilabel:`Backup mode Down/Up` to position **Down**. 

   .. figure:: /_img/backup/backup-down-up-control.png
   	:figwidth: 600 px
   	
   	Order lowering

   3. MotoSuiveur® System starts automated gravity lowering by following algorithm

   .. figure:: /_img/backup/backup-mode-automatic-diagram.PNG
   	:figwidth: 300 px
   	
   	Automated gravity lowering algorithm

   4. Lowering continues until the load is safely positioned.

   .. figure:: /_img/backup/de-risk-icons.png
   	:figwidth: 200 px

   	Safely positioned load

   5. Stop lowering by switch and hold :guilabel:`Backup mode Down/Up` to **neutral** position.

   .. figure:: /_img/backup/backup-down-up-control-off.png
   	:figwidth: 300 px

   	End of lowering

   6. Load is ready to be unhooked
   
   ..

   7. Deactivate Backup mode via *Deactivating of Backup Mode* in :doc:`Backup Mode <backup-procedure>`


