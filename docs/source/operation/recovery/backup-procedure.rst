=================
Backup Procedure
=================

.. include:: ../../_img/_image-substitutions.rst

Backup mode is available is intended to allow hoist movements in some special situations. 
This :guilabel:`🔑 Backup Mode Off/On` allows the user to lower or raise the load with the MotoSuiveur Unit ensuring no braking occurs. It does
this via the MotoSuiveur Unit servo motor following the hoist movement whilst maintaining the normal position for the worm.

The hoist crane and MotoSuiveur system are controlled in the same way as in Follow mode - from the hoist control panel. 
The MotoSuiveur system can also be equipped with a switch that duplicates the signals from the hoist - :guilabel:`Backup mode Down/Up`.

When Backup mode is activated:
- The MotoSuiveur Unit motor speed is physically limited 
- All MotoSuiveur System logic faults (over speed etc) are inhibited.
- "Hoist Enabled" signal is forced.
- MotoSuiveur Unit limit switches are inhibited.
- The MotoSuiveur Unit motor speed is physically limited to 110% during normal operation.
- Hoist enable signals are ignored.


Backup procedure
----------------

Activating and operating of Backup Mode
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Activate Backup mode by turning the :guilabel:`Backup Mode Off | On` \*\ or :guilabel:`Backup/Recovery Mode Off | On` \**\ switch to the **On** position.

.. _Switch on Backup mode:
.. figure:: ../../_img/Backup/switch-on-backup.png
	:figwidth: 600 px
	:align: center

	Switching on Backup Mode

.. note::
	\*\ For MotoSuiveur systems equipped with **MSCL** MS Controller

	\**\ For MotoSuiveur systems equipped with **MSCD** MS Controller

2. The Backup mode enable indicator illuminates. A symbol |image058| for activated Backup mode is displayed on the 7-segment indicator of the MS controller.

.. _Switch on Backup mode light:
.. figure:: ../../_img/Backup/backup-light-on.png
	:figwidth: 600 px
	:align: center

	Backup Mode light illunminates
	
3. MotoSuiveur system is in Backup mode.
4. Starting movements by hoist control.
   

Deactivating of Backup Mode
^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Deactivate Backup mode by turning the Backup Off | On switch to the **Off** position.

.. _Switch off Backup mode:
.. figure:: ../../_img/Backup/switch-off-backup.png
	:figwidth: 600 px
	:align: center

	Switching off Backup Mode

2. The backup mode indicator  is not illuminated . On the 7-segment indicator of MS controller the symbol |image058| remain active ana **Backup mode operation is still activated**.

.. _Switch off Backup mode light:
.. figure:: ../../_img/Backup/backup-light-off.png
	:figwidth: 600 px
	:align: center

	Backup Mode light off

3. :doc:`Reset <../../operation/regular/system-reset>` of the MotoSuiveur system is required. After Reset Backup mode is deactivated.

