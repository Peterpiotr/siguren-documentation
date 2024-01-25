================
Operation modes
================

.. _General view of the sequence of MS operation:
.. figure:: /_img/regular-operation/MS-block-diagram-color_1.PNG
   :figwidth: 100 %
   :class: instructionimg

   General view of the sequence of MotoSuiveur® operation

Operation sequence of MotoSuiveur® System as follows:

1. Initial powering on
2. MS Controller internal check
3. Checking for activated Recovery mode
4. MotoSuiveur® System electrical and mechanical self-test
5. Check for successfully passed self-test
6. MotoSuiveur® System enter in Following mode
7. During following mode MotoSuiveur® System checks for hoist overspeed or faults
8. If Backup mode is activated, MotoSuiveur® System enter in Backup mode
9. If Reset is performed by pressing Reset button, control voltage of MotoSuiveur® System is off. After Reset button is released operation sequence start from point 1

Releated pages:

:doc:`MS Controller internal check </operation/regular/controller-internal-check>`

:doc:`MotoSuiveur® System self-test </operation/regular/self-test>`

:doc:`Following </operation/regular/following>`

:doc:`Backup </operation/recovery/backup-procedure>`

:doc:`Recovery </operation/recovery/recovery-operation>`

:doc:`MotoSuiveur® System reset </operation/regular/system-reset>`