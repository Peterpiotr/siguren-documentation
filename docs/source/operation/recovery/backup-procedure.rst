=================
Backup Procedure
=================

.. note::
	Source is :doc:`49104-15-001 Operation  Maintenance Manual Issue D (1).pdf`

This :guilabel:`switch` allows the user to lower or raise the load with the MS unit ensuring no braking occurs. It does
this via the MotoSuiveur servo motor following the hoist movement whilst maintaining the normal position
for the worm.

[Raise signal]
This replicates the raise signal from the main hoist unit control panel without movement.
This is to prime the MotoSuiveur following motor in the raise direction. The raise movement is via the hoist
motor so in this case is not be isolated. Therefore any hoist movement will be required to be initiated by
some means but prior to the initiation the backup mode should enabled.

[Lower signal] 
This replicates the lower signal from the main hoist unit control panel without movement.
In the event of a fault on the hoist the hoist drive mechanism can be isolated, the MotoSuiveur backup
mode enabled, lower direction switch applied and through the release of the service brake by ‘fethering
the brake’ the MotoSuiveur will follow the rotation of the hoist without arresting. However if the hoist
achieves an over speed condition then the MotoSuiveur will arrest the load.

The following conditions apply to the control system when the backup procedure is initiated:

 - The MotoSuiveur motor speed is physically limited to 110% during normal operation
 - Hoist enable signals are ignored
 - MotoSuiveur switches are inhibited