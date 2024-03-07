========================
Load Recovery Operations
========================

.. include:: /_img/_image-substitutions.rst

Using the MotoSuiveur® System recovery capabilities
====================================================

The MS Unit will never allow a load drop. It will arrest the hoist drum whenever the hoist brake is unable to do so. 
However, the MS Unit can be used as a gearbox to lower and even raise the load. 

.. note::
	The MS Unit is irreversible - meaning that load drop is impossible even when the MS Unit alone is used for recovering the load. 
	This allows the user to use the weight of the load without risking a load drop.

Three main methods can be used (and combined) to recover the load, depending on how the hoist brake 
and the MS Unit can be accessed and used in the emergency situation that requires the recovery:

- :ref:`Forced MS recovery`
- :ref:`MS followed gravity lowering`
- :ref:`MS assisted gravity lowering`


Forced MotoSuiveur® recovery
=============================

With the hoist brake open and the MS Unit holding the load, rotate the MS worm shaft with considerable torque. 
In this situation the MS Unit moves the load.
This way, a very high amount of torque must be applied on the MS shaft (approximately 1/8 of the barrel torque).

Using the following hardware:

- :doc:`Portable Recovery Tool </ms-system/ms-unit/rec-addons>` for sizes MS4 - MS7,
- :doc:`Handheld Recovery Tool </ms-system/ms-unit/rec-addons>` for sizes MS0 - MS3,
- For MS with Integrated Load Recovery the hardware is integrated and is remotely operated.

.. replace each link with link to specific page


Steps
  1. Open the hoist brake
  2. Rotate the worm shaft **only in anticlockwise direction** with the **following torque** to lower the SWL. 
  3. Maximum values shown in `Forced MS Recovery method max torques`.

  .. figure:: /_img/recovery/forced-ms-recovery.jpg
  	:figwidth: 100 %
  	:class: instructionimg

  	Forced recovery

  .. csv-table:: Forced MS Recovery method max torques
     :file: /_tables/forcedRecoveryTorque.csv
     :delim: ,
     :header-rows: 1
     :widths: auto


  .. important::
  	Indicative barrel speed: 0.1 - 0.3 rpm


Integrated Recovery System 
==========================

Preliminary steps
    1. When deciding a recovery with MotoSuiveur® Integrated Recovery System is required to be undertaken an assessment should be made to establish where the fault has occurred.

        .. important::
            Prior to any recovery operations commencing, the cause of the fault should be identified.

        .. preliminary step with see also to arrest cause analysis

    2. MotoSuiveur® Integrated Recovery System can only be used if the hoist is mechanical drive chain is not blocked by a mechanical means such as hoist gearbox failure or main hoist (service) brake failure.

        .. preliminary step

    3. If the failure does permit the recovery the procedure describes the process to be undertaken to complete the recovery using the integrated MotoSuiveur® recovery system.

        .. how does the user asses that "if"? we should provide guidance even though we cannot cover cases in detail. maybe a decision tree

    4. Whilst undertaking the recovery process and in all cases the main motor hoist service brake is required to be operable and correctly functioning. Тhis will then be required to be opened (automatically or manually) for the entire duration of the recovery starting from when the Integrated Recovery System is engaged.

    The purpose of the Integrated Recovery System is to provide an independent means of enabling the raising or lowering 
    the load in the event of a failure of the main hoisting mechanism.

    This means of hoisting is achieved and initiated from the MS Control Cabinet with physical switches. 


Steps
  1. Activating Recovery mode 
     
        Activate Recovery mode by following steps in :doc:`Automatic recovery engagement procedure </operation/recovery/automatic-recovery-engagement>`

  2. Recovery lowering

        After successful engagement, the recovery procedure can begin. To start lowering following actions are:

        2.1. Open hoist main brake.

        2.2. Turning the :guilabel:`Recovery Mode Down/Up`` switch to position **Down** .

        2.3. Lowering continues until the load has reached a safe location for detached from the hoist.

            .. figure:: /_img/recovery/recovery-down.png
                :figwidth: 100 %
                :class: instructionimg

                Turning switch to position Down

  3. Complete recovery lowering.

        When safe location is reached and load is detouched, the :guilabel:`Recovery Mode Down/Up` switch should be turned to the neutral position.
        Hoist main (service) brake has to **close**.

        .. detouched? is this a legitimate term in lifting?

        .. figure:: /_img/recovery/recovery-neutral-position.png
            :figwidth: 100 %
            :class: instructionimg

            Turning switch to neutral position

  4. Recentering worm shaft

    After detaching load, worm shaft recentering between limit switches is required. 
    Centering is performed:

    4.1 With hoist main brake closed Downward movement with Integrated Recovey System is required.

        .. figure:: /_img/recovery/recovery-down.png
            :figwidth: 100 %
            :class: instructionimg

            Turning switch to position Down for recentering

    4.2 Movement continues until :guilabel:`🟢 Upward Enabled` and :guilabel:`🟢 Downward Enabled` indicator lights are both iluminated.

        .. figure:: /_img/recovery/Upward-downward-ENABLED-on.png
            :figwidth: 100 %
            :class: instructionimg

            Recentering of worm shaft


  5. Exit form Recovery mode

    5.1 Worm shaft is located between limit switches.

    5.2 Short **Upward** movement with Recovery System is required for disengaging Recovery Mechanism from worm shaft.

        Switch :guilabel:`Recovery Mode Down/Up` to position **UP** for 2 - 5 seconds. After that switch to **neutral position**.

        .. figure:: /_img/recovery/recovery-upward-short.PNG
            :figwidth: 100 %
            :class: instructionimg

            Short Upward movement

    5.3 Turning :guilabel:`🔑 Recovery Mode Off | On` switch to the position **OFF** 

        .. figure:: /_img/recovery/recovery-switch-off.png
            :figwidth: 100 %
            :class: instructionimg

            Switch off Recovery mode

    5.4 Reset MotoSuiveur® System.

        .. figure:: /_img/recovery/reset.png
            :figwidth: 100 %
            :class: instructionimg

            Reset MotoSuiveur® System
        
        .. standalone step or should redirect to Reset procedure? or both? (harder to maintain) 
        .. consider that a user never resets for reset's sake, it's always as a step of a procedure with a concrete purpose 

.. note::
  	`Integrated Load Recovery video  <https://www.youtube.com/watch?v=3iZUa1VCCgs&t=228s&ab_channel=SIGUREN technologiestechnologies>`_
