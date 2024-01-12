===========================
Load Recovery Operations v2
===========================

.. include:: ../../_img/_image-substitutions.rst

.. ====================================================================================================================

.. role:: mechpart
   :class: mechpart

Using the MotoSuiveur® system recovery capabilities
===================================================

The MotoSuiveur® Unit will never allow a load drop. It will arrest the hoist drum whenever the hoist brake is unable to do so. 
However, the MotoSuiveur® Unit can be used as a gearbox to lower and even raise the load. 

.. note::
	The MotoSuiveur® Unit is irreversible – meaning that load drop is impossible even when the MotoSuiveur® Unit alone is used for recovering the load. 
	This allows the user to use the weight of the load without risking a load drop.

Three main methods can be used (and combined) to recover the load, depending on how the hoist brake 
and the MotoSuiveur® Unit can be accessed and used in the emergency situation that requires the recovery:

- :ref:`Forced MS recovery`
- :ref:`MS followed gravity lowering`
- :ref:`MS assisted gravity lowering`


Forced MotoSuiveur® Recovery
----------------------------

With the hoist brake open and the MotoSuiveur® Unit holding the load, rotate the MS :mechpart:`worm shaft` with considerable torque. 
In this situation the MotoSuiveur® Unit moves the load.
This way, a very high amount of torque must be applied on the MS shaft (approximately 1/8 of the barrel torque).

Using the following hardware:

- :doc:`Portable Recovery Tool <../../ms-solution/rec-addons.rst>` for sizes MS4 - MS7, or
- :doc:`Handheld Recovery Tool <../../ms-solution/rec-addons.rst>` for sizes MS0 - MS3

For MS with :doc:`Integrated Remote Recovery` the hardware is integrated and is remotely operated.

Instructions
  1. Open the hoist brake
  2. Rotate the :mechpart:`worm shaft` **only in anticlockwise direction** with the **following torque** to lower the SWL. 
  3. Maximum values shown in :numref:`Forced MS Recovery method max torques`.

.. _Forced MS recovery:
.. figure:: ../../_img/Recovery/forced-ms-recovery.jpg
	:figwidth: 600 px

	Forced recovery

.. _Forced MS Recovery method max torques:
.. csv-table:: Forced MS Recovery method max torques
   :file: ../../_tables/forcedRecoveryTorque.csv
   :delim: ,
   :header-rows: 1
   :widths: auto
   :class: tight-table


.. important::
	Indicative barrel speed: 0.1 - 0.3 rpm


Integrated Recovery System 
==========================

When deciding a recovery with MotoSuiveur® Integrated Recovery System is required to be undertaken an assessment should be made to establish where the fault has occurred. 
MotoSuiveur® Integrated Recovery System can only be used if the hoist is mechanical drive chain is not blocked by a mechanical means such as 
hoist gearbox failure or main hoist (service) brake failure.
.. very hard to understand. rephrase.
In the event the failure does permit the recovery the procedure describes the process to be undertaken to complete the 
recovery utilising the integrated MotoSuiveur® recovery system.

Whilst undertaking the recovery process and in all cases the main motor hoist service brake is required to be operable and correctly functioning. 
Тhis will then be required to be opened (automatically or manually) for the entire duration of the recovery starting from when the Integrated Recovery System is engaged.

The purpose of the Integrated Recovery System is to provide an independent means of enabling the raising or lowering the load in the event of a failure of the main hoisting mechanism.
This means of hoisting is achieved and initiated from the MotoSuiveur® System control cabinet with physical switches. 

.. important::
	Prior to any recovery operations commencing, the cause of the fault should be identified.

Instructions
  **1. Activate Recovery mode.** Activate Recovery mode by following the steps in :doc:`Automatic recovery engagement procedure <../../operation/recovery/automatic-recovery-engagement>`

  2. Allow recovery lowering.

  After successful engagement, the recovery procedure can begin. To start lowering following actions are:

  3. Open hoist main brake.

  4. Turn the :guilabel:`Recovery Mode Down/Up` switch to position **Down**. The hoist should start lowering.

  .. figure:: ../../_img/Recovery/recovery-down.png
  	:figwidth: 250 px

	Turning switch to position Down

  5. Continue lowering until the load has reached a safe location and can be detached from the hoist.

  6. Turn the :guilabel:`Recovery Mode Down/Up` switch to the neutral position. The hoist main (service) brake should **close**.

  .. figure:: ../../_img/Recovery/recovery-neutral-position.png
  	:figwidth: 250 px

  	Turning switch to neutral position

  7. Recenter worm shaft.

  After detaching load, worm shaft recentering between limit switches is required. 
  Centering is performed:
  .. something missing?

  8. With hoist main brake closed downward movement with Integrated Recovey System is required.

  .. figure:: ../../_img/Recovery/recovery-down.png
  	:figwidth: 250 px

  	Turning switch to position Down for recentering.

  9. Movement continues until :guilabel:`🟢 Upward Enabled` and :guilabel:`🟢 Downward Enabled` indicator lights are both iluminated.

  .. figure:: ../../_img/Recovery/upward-downward-enabled-on.png
  	:figwidth: 250 px

  	Recentering of worm shaft


  10. Exit form Recovery mode.


  11. Worm shaft is located between limit switches.

  12. Make a short **upward** movement with Recovery System (required for disengaging the Recovery Mechanism from the worm shaft).

  Switch :guilabel:`Recovery Mode Down/Up` to position **UP** for 2 - 5 seconds. After that switch to **neutral position**.


  .. figure:: ../../_img/Recovery/recovery-upward-short.PNG
  	:figwidth: 250 px

  	Short upward movement


  13.  Turn :guilabel:`🔑 Recovery Mode Off | On` switch to the position **OFF** 

  .. figure:: ../../_img/Recovery/recovery-switch-off.png
  	:figwidth: 250 px

  	Switch off Recovery mode

  14. Reset MotoSuiveur® System

  .. figure:: ../../_img/Recovery/reset.png
  	:figwidth: 250 px

  15. MotoSuiveur® System is ready to follow.


  .. note::
  	Watch `Integrated Load Recovery video  <https://www.youtube.com/watch?v=3iZUa1VCCgs&t=228s&ab_channel=SIGURENtechnologies>`_
