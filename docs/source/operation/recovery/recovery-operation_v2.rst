==========================
Integrated Recovery System 
==========================

When it is necessary to use the MotoSuiveur® Integrated Recovery System, an assessment must be conducted to determine the location of the fault. 
The MotoSuiveur® Integrated Recovery System can only be deployed if the hoist's mechanical drive chain is not obstructed by any mechanical issues, 
such as a failure in the hoist gearbox or the main hoist (service) brake.

Should the failure allow for recovery, the procedure outlines the steps to be followed using the MotoSuiveur® Integrated Recovery System.

During the recovery process, it is essential that the main motor hoist service brake is operational and functioning correctly. 
This brake must be disengaged (either automatically or manually) throughout the recovery process, starting from the moment the 
Integrated Recovery System is activated.

The Integrated Recovery System is designed to independently ENABLE the raising or lowering of the load in case the main hoisting mechanism fails. 
This alternative hoisting method is activated via physical switches located in the MS Control Cabinet.

.. important::
	The causes of the fault should be clearly identified prior to any recovery operations.


Enabling Backup Lowering
-------------------------
  **1. Activate Recovery mode.** Activate Recovery mode by following the steps in :doc:`Automatic recovery engagement procedure </operation/recovery/automatic-recovery-engagement>`

  1. Allow recovery lowering and check for succesful engagement.

  .. how? where is engement defined? what signal do i get it has been achieved?

  2. Open hoist main brake.
  
  ..

  3. Turn the :guilabel:`Recovery Mode Down/Up` switch to position **Down**.
  
  .. figure:: /_img/recovery/recovery-down.png
  	:figwidth: 100 %

	Turning switch to position Down

Backup Lowering
-----------------

  5. Continue lowering until the load has reached a safe location and can be detached from the hoist.

Returning to Regular Operation
------------------------------

  6. Turn the :guilabel:`Recovery Mode Down/Up` switch to the neutral position. The hoist main (service) brake should **close**.

  .. figure:: /_img/recovery/recovery-neutral-position.png
  	:figwidth: 100 %

  	Turning switch to neutral position

  7. Recenter worm shaft.

  After detaching load, worm shaft recentering between limit switches is required. 
  Centering is performed:
  .. something missing?

  8. With hoist main brake closed Downward movement with Integrated Recovey System is required.

  .. figure:: /_img/recovery/recovery-down.png
  	:figwidth: 100 %

  	Turning switch to position Down for recentering.

  9. Movement continues until :guilabel:`🟢 Upward Enabled` and :guilabel:`🟢 Downward Enabled` indicator lights are both iluminated.

  .. figure:: /_img/recovery/Upward-downward-ENABLED-on.png
  	:figwidth: 100 %

  	Recentering of worm shaft


  10. Exit form Recovery mode.
  
  .. how?

  .. 11.Worm shaft is located between limit switches.

  11. Make a short **Upward** movement with Recovery System. This is required for disengaging the Recovery Mechanism from the worm shaft.

  ..
  
  12. Switch :guilabel:`Recovery Mode Down/Up` to position **UP** for 2 - 5 seconds. After that switch to **neutral position**.


  .. figure:: /_img/recovery/recovery-upward-short.PNG
  	:figwidth: 100 %

  	Short Upward movement


  12. Turn :guilabel:`🔑 Recovery Mode Off | On` switch to the position **OFF** 

  .. figure:: /_img/recovery/recovery-switch-off.png
  	:figwidth: 100 %

  	Switch off Recovery mode

  13.  Reset MotoSuiveur® System

    .. figure:: /_img/recovery/reset.png
    	:figwidth: 100 %

  14.  MotoSuiveur® System is ready to follow.
    
    .. What signal do I get for this?


  .. note::
  	Watch `Integrated Load Recovery video  <https://www.youtube.com/watch?v=3iZUa1VCCgs&t=228s&ab_channel=SIGUREN technologiestechnologies>`_
