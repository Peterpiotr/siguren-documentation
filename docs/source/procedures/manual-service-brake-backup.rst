========================================================
Back-up by manual action of the service brake procedure
========================================================

.. include:: ../procedures/img/substitutions.rst

.. ====================================================================================================================

.. note::
	Source: :download:`User Manual-7.4.doc`

This procedure has to be followed in case of main motor fault. The following procedure allows the operator to switch in back-up up mode with manual opening of the service brake. 

Comments:

- This procedure requires two operators (one for the manual service brake opening, the second one at the MS-1 cabinet).
- Ensure power to the motor is removed. =
- Each of the two operators can stop the operation: the first operator by closing the service brake, the other operator by stopping the rotation of MS.

|manual-service-brake-backup-01|
.. integrate this image to the procedure

.. list-table:: Back-up by manual action of the service brake procedure
   :widths: 5 95
   :header-rows: 1
   :class: instruction-table
  
   * - Step
     - Description
   * - **1**
     - On the main screen, press :guilabel:`Menu`.
   * - **2**
     - press :guilabel:`Back up mode` 
   * - **3**
     - Enter a level 2 (or 3) password
   * - **4**
     - On the activation screen of the back-up mode, press :guilabel:`activate back up mode` 
   * - **5**
     - | Operator n°1 : Allow the motion by pushing the button :guilabel:`UP` or :guilabel:`DOWN` on the touch screen
       | Operator n°2 : Simultaneously with operator n°1, release the service brake little by little in order to allow 
         the lowering of the load by gravity without reaching overspeed, otherwise the MotoSuiveur will block.

When the limit speed is reached, the MS goes into action intrinsically by blocking the worm.

Given the relatively slow speed, it is easy to stop the action on the brake before the end of the travel of the Motosuiveur®. The operation can then continue without any special intervention, since the screw goes back to its position automatically.
In case of hard blocking, it should be possible to release the Motosuiveur® by using the handle 

.. important::
    To switch back to “normal mode”, it is necessary to power-off then power-on the electrical cabinet.
