===============
Memory card
===============

.. include:: ../substitutions.rst

.. ============================================================================================

.. note::
	Source is :doc:`49104-15-001 Operation  Maintenance Manual Issue D (1).pdf`

IMD Drive PC Loading / Saving procedure
=========================================

An application developed with an IMD drive must be saved on a PC in order to be able to
load it later, for either modification or maintenance.

Saving an application on a PC 
-------------------------------

 - Connect the drive to the PC with the CIMDP cable.
 - Launch the iDPL software with the Start menu.

.. topic:: If you don’t have the source project

  - In the welcome window, select New Project
  - If the software asks you to overwrite the default project, click on Yes
  - For multi-drives projects :
    - With the Project \ Setup window, declare the drives in the application (with their node number)
    - Select the drive you have to save
  - In the Communication menu, click on Receive drive
  - In the selection window, tick All
  - Click on Receive to start the drive save in the PC
  - In the Project menu, click on Save as
  - In the window «Save project as», go to the save folder and enter the name of the project (e.g. : MyProject.IDW).

.. topic:: If you have the source project

  - In the welcome window, select Open project
  - In the window «Open», go to the save folder
  - Double click on the project (e.g. : MyProject.IDW).
  - For multi drives projects : select the drive you have to save
  - Go into Communication \ Receive drive
  - In the selection window, tick Parameters, Variables, Saved data and Cams.
  - Click on Receive to start saving the drive in the PC project.

Application loading in the drive
----------------------------------

 - Connect the drive to the PC with the CIMDP cable.
 - Launch the iDPL software with the Start menu.
 - In the welcome window, select Open project
 - In the window «Open project», go to the save folder
 - Double click on the iDPL project (e.g. : MyProject.IDW).
 - For multi-drives projects: select the drive you have to load
 - Go to Communication \ Send drive
 - In the selection window, tick All
 - Click on Send to start the project PC restoring data to the drive.

MEMORY STICK Loading / Saving procedure
=========================================

This optional module ‘Memory Stick’ provides a quick and simple way of saving of the
whole drive data: Parameters, Saved data, Cam profiles, Tasks and Operating System.
When it is switched on, the IMD compares its data content with the Memory Stick data. If
they are different, the IMD is automatically reloaded with the Memory Stick data.
In case of empty Memory Stick at power on, the data’s of the IMD are loaded inside the
Memory Stick.

The Memory Stick is automatically updated during a PC loading to an IMD :

 - The Parameters
 - The saved data or trajectories
 - The cams or saved data
 - The tasks
 - The Operating System
  
Status Display
===============

.. list-table:: Status Display during transfer
  :width: 600 px
  :widths: 25 75
  :header-rows: 1

  * - 7-segment display
    - Description
  * - |image048|
    - Data transfer from the Memory Stick to the Drive
  * - |image058|
    - Data transfer from the Drive to the Memory Stick
  * - |image035| |image013| |image055|
    - Error 18 : a write operation to the Memory Stick has failed : Removed or defective Memory stick.
  * - |image035| |image013| |image060|
    - | Error 19 : the Memory Stick transfer to the drive has not been done correctly because the data are incoherent. 
      | The Memory Stick has been erased and updated with the drive contents.