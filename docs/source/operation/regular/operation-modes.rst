================
Operation modes
================

.. _General view of the sequence of MS operation:
.. figure:: ../../_img/Regular-operations/MS-block-diagram-color_1.PNG
   :figwidth: 600 px
   :align: center

   General view of the sequence of MotoSuiveur operation

Operation sequence of MotoSuiveur system as follows:

1. Initial powering on
2. MS controller internal check
3. Checking for activated Recovery mode
4. MotoSuiveur system electrical and mechanical self-test
5. Check for successfully passed self-test
6. MotoSuiveur system enter in Following mode
7. During following mode MotoSuiveur system checks for hoist overspeed or faults
8. If Backup mode is activated, MotoSuiveur system enter in Backup mode
9. If Reset is performed by pressing Reset button, control voltage of MotoSuiveur system is off. After Reset button is released operation sequence start from point 1



:doc:`MS Controller internal check <../../../regular/controller-internal-check>`

:doc:`MS System self-test <../../../regular/self-test>`

:doc:`Following <../../../regular/following>`

:doc:`Backup <../../../recovery/backup-procedure>`

:doc:`Recovery <../../../recovery/recovery-operation>`

:doc:`MS System reset <../../../regular/system-reset>`