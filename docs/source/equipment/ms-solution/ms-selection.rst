=================================
Selecting a MotoSuiveur® Solution
=================================

.. include:: /_text-substitutions.rst

.. _example-ref:

MS Unit selection
======================================

Arrest type selection
-----------------------

.. figure:: /_img/archives/ms-selection-01.png
	:scale: 100 %
	:class: instructionimg

	MotoSuiveur® type selection diagram

Arrest torque calculation
---------------------------

The main criterion is the arrest torque at full speed |Vmax|. 

The starting point to define this torque is the full load static torque at the drum (or at the MS wheel) |Cs|, without taking into account the efficiency.

.. figure:: /_img/archives/ms-selection-02.png
	:scale: 100 %
	:class: instructionimg

	Hoist kinematic chain force analysis

The Passive Friction MS Unit is directly selected to ensure sufficient torque to stop the full load. 

.. math::

  C_{MS} ≥ 1.4C_S

The speed at the MS Unit wheel |Vmax| can be up to 100 RPM.




Example : Selecting a Passive Friction MS Unit (MSF)
----------------------------------------------------------------

.. rubric:: Hoist input data

| SWL = **4900 kg**
| Dead weight = **100 Kg**
| Reeving = **2/1**
| Drum diameter = **250 mm**
| Gearbox ratio = **60**
| Motor speed = **3000 rpm**

| Is it possible to put a MS Torque Limiter? 
| **Yes**

| Is there important inertia after the MS Torque Limiter? 
| **No**

| Is the rotation speed at drum exceeding 35 rpm?	
| **Yes**, see calculation below (50 rpm > 35 rpm)


+------------------------------+---------+-------------+--------+--------------------+
| Designation                  | Symbol  | Value       | Units  | Formula / comment  |
+==============================+=========+=============+========+====================+
| **Forces and torques**                                                             |
+------------------------------+---------+-------------+--------+--------------------+
| Load weight                  | WL      | **4,900**   | kg     |                    |
+------------------------------+---------+-------------+--------+--------------------+
| Dead weight                  | WT      | **100**     | kg     |                    |
+------------------------------+---------+-------------+--------+--------------------+
| Load + dead weight           | SWL     | 5,000       | kg     | =(WL+WT)           |
+------------------------------+---------+-------------+--------+--------------------+
| Gravity                      | g       | **9.81**    | m/s²   |                    |
+------------------------------+---------+-------------+--------+--------------------+
| Lifting force                | FL      | 49,050      | N      | =SWL*g             |
+------------------------------+---------+-------------+--------+--------------------+
| Reeving ratio                | im      | **2**       |        |                    |
+------------------------------+---------+-------------+--------+--------------------+
| Drum pitch diameter          | D       | **250**     | mm     |                    |
+------------------------------+---------+-------------+--------+--------------------+
| Gearbox ratio                | ir      | **60**      |        |                    |
+------------------------------+---------+-------------+--------+--------------------+
| Force at driven rope strand  | Fc      | 24,525      | N      | =SWL*g/im          |
+------------------------------+---------+-------------+--------+--------------------+
| Static torque at drum        | |Cs|    | 3,065       | Nm     | =Fc*D/2000         |
+------------------------------+---------+-------------+--------+--------------------+
| **Speeds**                                                                         |
+------------------------------+---------+-------------+--------+--------------------+
| Speed at High Speed Line     | SHSL    | **3,000**   | Rpm    |                    |
+------------------------------+---------+-------------+--------+--------------------+
| Speed at MS                  | SMS     | 50          | Rpm    | =SHSL/ir           |
+------------------------------+---------+-------------+--------+--------------------+

.. rubric:: Size of the MS

|Cms| = 1.4 x Cs = 1.4x 3 065 = 4 291 Nm

According to MS Unit arrest torque table:

|Cms| = 4 291 Nm < 6 100 Nm 

**MS1** is the correct size of MS Unit for this application.





MS control cabinet selection
======================================

MS load recovery add-on selection
=============================================

MS Torque Limiter add-on  selection
================================================