======================
Backup/Recovery mode
======================

.. include:: /_img/_image-substitutions.rst

.. ========================================================================================

.. note::
    Backup/Recovery mode is applicable only for MotoSuiveur® Systems equipped with **MSCD** MS Controller and equipped with **MS-IRD**!

.. note::
    Backup/Recovery operation mode functions are intended for *unusual* situations during MotoSuiveur® Systems operation. 

.. "function" vs "mode" vs "operation mode"

Controls and indicators of this function are located on the :doc:`control panel front door </ms-system/ms-controls/control-panel>`
- figure 3, items 4, 5, 10, 11.

Diagram below shows the principle of Backup/Recovery operation mode. 

.. _Principle of Backup/Recovery operation :
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

.. _Example for manual operation in Backup Mode:
.. figure:: /_img/archives/backup-mode-01.png
	:class: instructionimg

	Example for manual operation in Backup Mode 

.. note::
    See also and merge : :doc:`Backup procedure </operation/recovery/backup-procedure>`

.. important::
    In Backup Mode no ENABLE signal (On) **form** hoist to MotoSuiveur® is required to perform movement.
    If ENABLE signal **to** hoist is required, :guilabel:`🔑 Enable Override` should be used. 




Recovery operation mode
=========================

Recovery mode is second part of Backup/Recovery operation. 

This mode starts operating the way shown on `Principle of Backup/Recovery operation`.
.. do not use these references anymore?

After Reset of MotoSuiveur® System, MS Controller checks for active Backup/Recovery mode request (:guilabel:`🔑 Backup/Recovery OFF/ON` is **ON**). 
If request is active 7-segment display shows |7s-U| :guilabel:`🟠 Backup/Recovery Mode` and 
:doc:`automatic recovery engagement </operation/recovery/automatic-recovery-engagement>` start. 

Completion of **ENGAGEMENT** is indicated by :guilabel:`🟢 Recovery Engaged` indication lamp. 
If :guilabel:`🟢 Recovery Engaged` is not iluminated after first engagement, Reset ot MotoSuiveur® System is required.

After succesfull engagement of MS-IRD follow steps for :doc:`recovery operation </operation/recovery/recovery-operation>`

.. warning::
    Recovery function is mainly designed for safety lowering of the load. 
    Function allows very short lifting of the load only in cases where it is absolutely necessary!

.. warning::
    Before activating Backup/Recovery operation mode from local controls, 
    please make sure that this operation mode is not activated remotely. 
    
The verification consists of the following steps:
.. make into instructions

- :guilabel:`🟢 Backup/Recovery` and :guilabel:`🟢 Recovery engaged` lamp are **NOT ON**,
- :guilabel:`🔑 Backup/Recovery OFF/ON` is in position **OFF**,
- On MS Controller 7-segment display symbols |7s-058| or |7s-U| are **NOT** displayed.