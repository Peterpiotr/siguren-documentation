============
Memory Card
============

.. include:: /_img/_image-substitutions.rst

.. from 49104-15-001-Operation-Maintenance-Manual-Issue-D.pdf

IMD Drive PC Loading / Saving procedure
========================================

An application developed with an IMD drive must be saved on a PC in order to be able to
load it later, for either modification or maintenance.

.. how is the application "developed WITH an IMD drive" ?

Saving an application on a PC 
-------------------------------

    - Connect the drive to the PC with the CIMDP cable.
    - Launch the iDPL software with the Start menu.

If you do not have the source project:

Steps
    1. In the welcome window, select :guilabel:`New Project`
    2. If asked whether to overwrite the default project, click on :guilabel:`Yes`
    3. For multi drives projects:
            
        - With the Project \ Setup window, declare the drives in the application (with their node number)
        - Select the drive you have to save
        
    4. In the Communication menu, click on :guilabel:`Receive drive`
    5. In the selection window, tick :guilabel:`All`
    6. Click on :guilabel:`Receive` to start the drive save in the PC
    7. In the Project menu, click on :guilabel:`Save as`
    8. In the window «Save project as», navigate to the save folder and enter the name of the project (e.g. : MyProject.IDW).

.. this should be illustrated

If you have the source project:

Steps
    1. In the welcome window, select :guilabel:`Open project`
    2. In the window «Open», navigate to the save folder
    3. Double click on the project (e.g. : MyProject.IDW).
    4. For multi drives projects: Select the drive you have to save.
    5. Navigate to: 
        
        | Communication
        |   └ **Receive drive**

    6. In the selection window, tick :guilabel:`Parameters`, :guilabel:`Variables`, :guilabel:`Saved data` and :guilabel:`Cams`.
    7. Click on :guilabel:`Receive` to start saving the drive in the PC project.

.. this should be illustrated

Loading an application in the drive
------------------------------------

Steps
    1. Connect the drive to the PC with the CIMDP cable.

        .. what is a CIMDP cable?

    2. Launch the iDPL software with the Start menu.
    3. In the welcome window, select :guilabel:`Open project`.
    4. In the window «Open project», navigate to the save folder.
    5. Double click on the iDPL project (e.g. : MyProject.IDW).
    6. For multi-drives projects: select the drive you have to load
    7. Navigate to:
            
        | Communication
        |   └ **Send drive**

    8. In the selection window, tick :guilabel:`All`
    9. Click on :guilabel:`Send` to start the project PC restoring data to the drive.

Loading a memory stick / Saving procedure
=========================================

.. memory stick = USB drive? = SD card? = something else?

This optional module ‘Memory Stick’ provides a quick and simple way of saving of the
whole drive data:

    - Parameters, 
    - Saved data, 
    - Cam profiles, 
    - Tasks,
    - Operating System.

When it is switched ON, the IMD Controller compares its data content with the Memory Stick data. If
they are different, the IMD is automatically reloaded with the Memory Stick data.
In case of empty Memory Stick at power ON, the data of the IMD is loaded on the Memory Stick.

.. should take the form of procedure steps

Steps
    1. .
    2. .

Status Display
===============

.. list-table:: Status Display during transfer
    :width: 100 %
    :widths: 25 75
    :header-rows: 1

    * - 7-segment display
      - Description
    * - |7s-d|
      - Data transfer from the Memory Stick to the Drive
    * - |7s-058|
      - Data transfer from the Drive to the Memory Stick
    * - |7s-E| |7s-1| |7s-8|
      - Error 18 : a write operation to the Memory Stick has failed : Removed or defective Memory stick.
    * - |7s-E| |7s-1| |7s-9|
      - | Error 19 : the Memory Stick transfer to the drive has not been done correctly because the data are incoherent. 
        | The Memory Stick has been erased and updated with the drive contents.