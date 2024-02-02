===================
Operation Sequence
===================

.. remake with numbers in circles on the diagram 

.. should we call this a loop?

.. figure:: /_img/regular-operation/MS-block-diagram-color_1.PNG
   :figwidth: 100 %
   :class: instructionimg

   Diagram of MotoSuiveur® System Operation sequence

Operation sequence of the MotoSuiveur® System
    1. Initial power ON.
    2. MS Controller internal check.
        
        .. seealso::
            :doc:`controller-internal-check`

    4. Check for activated Recovery mode.
    5. MotoSuiveur® System electrical and mechanical Self-Test.

        .. seealso::
            :doc:`Self-Test`

    7. Check for successfully passed Self-Test.
    8. MotoSuiveur® System enter in Following Mode.
    9. During Following Mode MotoSuiveur® System checks for hoist overspeed or faults.
    10. If Backup mode is activated, MotoSuiveur® System enter in Backup mode.
    11. If Reset is performed by pressing Reset button, control voltage of MotoSuiveur® System is OFF. 
        
        After Reset button is released operation sequence start from 1.

        .. seealso::
            :doc:`system-reset`

.. "control voltage of MS is OFF" clarify/why is it important here