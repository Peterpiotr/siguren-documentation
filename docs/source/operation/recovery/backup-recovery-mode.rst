==================================
Activating Backup/Recovery Mode
==================================

.. include:: /_img/_image-substitutions.rst

.. note::
    Backup/Recovery mode is applicable only for MotoSuiveur® Systems equipped with **MSCD** MS Controller and equipped with **MS-IRD**.

.. note::
    Backup/Recovery operation mode functions are intended for *unusual* situations during MotoSuiveur® Systems operation. 

.. "function" vs "mode" vs "operation mode"

.. replace the following with an image and circled numbers
    Controls and indicators of this function are located on the :doc:`control panel front door </ms-system/ms-controls/control-panel>`
    - figure 3, items 4, 5, 10, 11.

Diagram below shows the principle of Backup/Recovery operation mode. 

.. figure:: /_img/archives/backup-mode-02.png
    :class: instructionimg
    :figwidth: 100 %

    Principle of Backup/Recovery operation 

Backup/Recovery decision figures located in on principle diagram with dotted outline, 
represent the places where request for these operation modes are checked. 

Switching to Backup/Recovery mode is performed through :guilabel:`🔑 Backup/Recovery OFF/ON` key switch. 
After switching :guilabel:`🔑 Backup/Recovery OFF/ON key` to position **ON**, Backup Mode start operating. 

|7s-058| :guilabel:`indication for Backup Mode` is displayed on 7-segment display and :guilabel:`🟠 Backup/Recovery Mode` indicator lamp is iluminated.
 
.. important::
    Backup function ignore all settings and fault detection related with following operation and allows movement of hoist with hoist limited speed.


Backup operation mode
=========================

In Backup operating mode, control is performed through commands for lifting and lowering of the hoist.

In cases where the hoist control chain is damaged, control can be performed manually with :guilabel:`🔑 Backup/Recovery Down/Up` switch
located :doc:`control panel front door </ms-system/ms-controls/control-panel>` or directly on control terminals via a wire bridge. 

.. figure:: /_img/archives/backup-mode-01.png
	:class: instructionimg

	Example for manual operation in Backup Mode 


.. important::
    In Backup Mode no ENABLE signal (On) **form** hoist to MotoSuiveur® is required to perform movement.
    If ENABLE signal **to** hoist is required, :guilabel:`🔑 Enable Override` should be used. 


Recovery operation mode
=========================

Recovery mode is the second part of Backup/Recovery operation. 

.. warning::
    Before activating Backup/Recovery operation mode from local controls, 
    please make sure that this operation mode is not activated remotely. 

.. this warning should be a prelimnary step, not mentioned after the fact

This mode starts operating the way shown on `Principle of Backup/Recovery operation`.

.. do not use these references anymore?

After Reset of MotoSuiveur® System, MS Controller checks for active Backup/Recovery mode request (:guilabel:`🔑 Backup/Recovery OFF/ON` is **ON**). 

If request is active 7-segment display shows |7s-U| :guilabel:`🟠 Backup/Recovery Mode` and 
:doc:`/operation/recovery/automatic-recovery-engagement` starts. 

Completion of **ENGAGEMENT** is indicated by :guilabel:`🟢 Recovery Engaged` indication lamp. 
If :guilabel:`🟢 Recovery Engaged` is not iluminated after first engagement, Reset ot MotoSuiveur® System is required.

After succesfull engagement of MS-IRD follow steps for :doc:`/operation/recovery/recovery-operation`

.. these should not be separated. why would a user do a "successful engagement" if he is not looking to do a recovery?

.. warning::
    Recovery function is mainly designed for safety lowering of the load. 
    Function allows very short lifting of the load only in cases where it is absolutely necessary!



The verification consists of the following steps:
.. make into instructions

Steps
    - :guilabel:`🟢 Backup/Recovery` and :guilabel:`🟢 Recovery engaged` lamp are **NOT ON**.
    - :guilabel:`🔑 Backup/Recovery OFF/ON` is in position **OFF**.
    - On MS Controller 7-segment display symbols |7s-058| or |7s-U| are **NOT** displayed.

.. so what IS displayed?

.. how do we go back to Following Mode from here?