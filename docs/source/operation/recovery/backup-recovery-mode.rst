======================
Backup/Recovery mode
======================

.. include:: ../../_img/_image-substitutions.rst

.. ========================================================================================

.. note::
    Backup/Recovery mode is applicable only for MotoSuiveur Systems equipped with **MSCD** MS Controller and equipped with **MS-IRD**!

.. note::
    Backup/Recovery operation mode functions are intended for *unusual* situations during MotoSuiveur Systems operation. 

.. "function" vs "mode" vs "operation mode"

Controls and indicators of this function are located on the :doc:`control panel front door <../../equipment/control-interface/control-panel>`
– figure 3, items 4, 5, 10, 11.

Diagram below shows the principle of Backup/Recovery operation mode. 

.. _Principle of Backup/Recovery operation :
.. figure:: ../../_img/Peter/backup-mode-02.png
    :align: center
    :figwidth: 600 px

	Principle of Backup/Recovery operation 

Backup/Recovery decision figures located in on principle diagram with dotted outline, 
represent the places where request for these operation modes are checked. 

Switching to Backup/Recovery mode is performed through :guilabel:`🔑 Backup/Recovery OFF/ON` key switch. 
After switching :guilabel:`🔑 Backup/Recovery OFF/ON key` to position **ON**, Backup mode start operating. 

|image058| :guilabel:`indication for backup mode` is displayed on 7–segment display and :guilabel:`🟠 Backup/Recovery Mode` indicator lamp is iluminated.
 
.. important::
    Backup function ignore all settings and fault detection related with following operation and allows movement of hoist with hoist limited speed.


Backup operation mode
=========================

In Backup operating mode, control is performed through commands for lifting and lowering of the hoist. 
In cases where the hoist control chain is damaged, control can be performed manually with :guilabel:`🔑 Backup/Recovery Down/Up` switch
located :doc:`control panel front door <../../equipment/control-interface/control-panel>` or directly on control terminals via a wire bridge. 

.. _Example for manual operation in backup mode:
.. figure:: ../../_img/Peter/backup-mode-01.png
	:align: center

	Example for manual operation in backup mode 

.. note::
    See also and merge : :doc:`Backup procedure <../../operation/recovery/backup-procedure>`

.. important::
    In Backup mode no enable signal (On) **form** hoist to MotoSuiveur is required to perform movement.
    If enable signal **to** hoist is required, :guilabel:`🔑 Enable Override` should be used. 




Recovery operation mode
=========================

Recovery mode is second part of Backup/Recovery operation. 

This mode starts operating the way shown on :numref:`Principle of Backup/Recovery operation`.

After reset of MotoSuiveur System, MS Controller checks for active Backup/Recovery mode request (:guilabel:`🔑 Backup/Recovery Off/On` is **ON**). 
If request is active 7–segment display shows |image041| :guilabel:`🟠 Backup/Recovery Mode` is iluminated and 
:doc:`automatic recovery engagement <../../operation/recovery/automatic-recovery-engagement>` start. 

Completion of **ENGAGEMENT** is indicated by :guilabel:`🟢 Recovery Engaged` indication lamp. 
If :guilabel:`🟢 Recovery Engaged` is not iluminated after first engagement, reset ot MotoSuiveur system is required.

After succesfull engagement of MS-IRD follow steps for :doc:`recovery operation <../../operation/recovery/recovery-operation>`

.. warning::
    Recovery function is mainly designed for safety lowering of the load. 
    Function allows very short lifting of the load only in cases where it is absolutely necessary!

.. warning::
    Before activating Backup/Recovery operation mode from local controls, 
    please make sure that this operation mode is not activated remotely. 
    
The verification consists of the following steps:

- :guilabel:`🟢 Backup/Recovery` and :guilabel:`🟢 Recovery engaged` lamp are **NOT ON**,
- :guilabel:`🔑 Backup/Recovery Off/On` is in position **OFF**,
- On MS Controller 7–segment display symbols |image058| or |image041| are **NOT** displayed.