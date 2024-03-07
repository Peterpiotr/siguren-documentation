==========================
Operating in Backup Mode
==========================

..
    =================
    Backup Procedure
    =================

.. Backup Procedure means the procedure to follow to enter into backup mode?
    or the way to use backup mode?
    everything that can be done with backup mode?

.. the "Backup Mode" 's purpose is to execute the "Backup". ie backup mode is a one of the modes, associated to a logic sequence
    and Backup is the name of what? the operation itself?

.. include:: /_img/_image-substitutions.rst

Introduction
==============

.. From User Manual-7.4.doc

In case of incident or accident, the MS stops the load. It should then set up a procedure to restore the handling. 
It is the purpose of the Backup Mode which are described in procedures 2.1 to 2.4

These situations can be very diverse, but can be distinguished depending on the availability of electrical means, 
and the following solutions are summarized in the table below:


.. list-table::

    * - 
      - **Running of the motor/ brake**
      - **Running of the MotoSuiveur® System**
      - **Number of operators**
      - **Procedure to perform**
    * - **Main motor and/ or brake failure**
      - Backup by manual action of the service brake
      - Automatic tracking of the MS
      - 2
      - Backup by manual action of the service brake
    * - **MS Motor failure**
      - Electrical lowering / lifting
      - Manual tracking of the MS (Manual command handle)
      - 3
      - Backup by manual action of the service brake and manual rotation of the MotoSuiveur®
    * - **MS Motor and main motor failure** 
      - Backup by manual action of the service brake 
      - Manual tracking of the MS (Manual command handle)
      - 3
      - Backup by manual action of the service brake and manual rotation of the MotoSuiveur®
    * - **Maladjustment or control-command problem**
      - Electrical lowering / lifting
      - Automatic tracking of the MS
      - 1
      - Electrical/ automatic Backup
    * - **Main kinematic chain unavailable (breakage)**
      - N/A
      - Lowering/ lifting forced on MS
      - 1
      - Backup by forced lowering


This function is used when an incident occurs and the MotoSuiveur® stops the load.

The Backup could be done whatever the case, safely, by acting simultaneously on the two kinematic chains, by available means.

The procedures n° 2.1 to 2.4 help the operator on the actions to be done.

.. note::
    If the MS is operational, it allows the movement of the main motor only at low speed.

.. end of extract from User Manual-7.4.doc


Backup Mode is intended to allow hoist movements in some special situations. 

The :guilabel:`🔑 Backup Mode OFF/ON` key switch allows the user to lower or raise the load with the MS Unit 
ensuring no braking occurs. It does this via the MS Unit servo motor following the hoist movement whilst 
maintaining the normal position for the worm.

The hoist and MotoSuiveur® System are controlled in the same way as in Following Mode - from the hoist control panel. 

.. note::
    The MotoSuiveur® System can also be equipped with a switch that duplicates the signals from the hoist - :guilabel:`Backup Mode Down/Up`.

When Backup Mode is activated:

- All MotoSuiveur® System logic faults (overspeed, etc) are inhibited.
- "Hoist ENABLED" signal is forced.
- MS Unit limit switches are inhibited.
- MS Unit motor speed is physically limited to 110% during regular operation.
- Hoist ENABLE signals are ignored.

.. "during regular operation"? but we are in backup mode.


Activating and operating Backup Mode
=======================================

.. not preliminary steps? nothing to check before going into backup mode?

Steps
  1. Activate Backup Mode by turning the :guilabel:`Backup Mode OFF | ON` \*\ or :guilabel:`Backup/Recovery Mode OFF | ON` \**\ switch to the **ON** position.

    .. figure:: /_img/backup/switch-on-backup.png
        :figwidth: 100 %
        :class: instructionimg

        Switching ON Backup Mode

    .. note::
        \*\ For MotoSuiveur® Systems equipped with **MSCL** MS Controller

        \**\ For MotoSuiveur® Systems equipped with **MSCD** MS Controller

        .. clarify

  2. The Backup Mode ENABLE indicator goes ON.

        .. figure:: /_img/backup/backup-light-on.png
            :figwidth: 100 %
            :class: instructionimg

            Backup Mode light indicator goes ON
  	
     - A symbol |7s-058| for activated Backup Mode is displayed on the 7-segment indicator of the MS Controller.

  3. MotoSuiveur® System is in Backup Mode.
  4. Starting movements by hoist control.


.. there should be a "Operating in Backup Mode" section

Deactivating Backup Mode
===========================

.. not preliminary steps? nothing to check before leaving backup mode?

Steps
   1. Deactivate Backup Mode by turning the :guilabel:`🔑 Backup Mode OFF/ON` key switch to the **OFF** position.

        .. figure:: /_img/backup/switch-off-backup.png
            :figwidth: 100 %
            :class: instructionimg

            Switching off Backup Mode

      - The Backup Mode indicator light goes OFF.
       
       .. this light is called "Backup Mode ENABLE indicator" above

        .. figure:: /_img/backup/backup-light-off.png
            :figwidth: 100 %
            :class: instructionimg

            Backup Mode indicator light goes off

      - On the 7-segment display of MS Controller, the symbol |7s-058| remain active meaning that **Backup Mode operation is still activated**.

        .. that can be confusing for the user. 

   2. Apply a Reset to the MotoSuiveur® System.  
      
      .. seealso::
         :doc:`/operation/regular/system-reset`
     
      - **After Reset, Backup Mode is deactivated.**

        .. what symbol on the 7-s display now? user needs to check that the step is successfull!

    
