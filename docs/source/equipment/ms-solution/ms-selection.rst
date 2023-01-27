=================================
Selecting a MotoSuiveur Solution
=================================

.. include:: ../../_text-substitutions.rst

.. =========================================================================================================================

MotoSuiveur Unit selection
======================================

Arrest type selection
-----------------------

.. figure:: ../../_img/ms-selection-01.png
	:scale: 100 %
	:align: center

	MotoSuiveur type selection diagram

Arrest torque calculation
---------------------------

The main criterion is the arrest torque at full speed |Vmax|. 

The starting point to define this torque is the full load static torque at the drum (or at the MS wheel) |Cs|, without taking into account the efficiency.

.. figure:: ../../_img/ms-selection-02.png
	:scale: 100 %
	:align: center

	Hoist kinematic chain force analysis

The Passive Friction MotoSuiveur Unit is directly selected to ensure sufficient torque to stop the full load. 

.. math::

  C_{MS} ≥ 1.4C_S

The speed at the MotoSuiveur Unit wheel |Vmax| can be up to 100 RPM.


Examples
---------

Selecting a Passive Friction MotoSuiveur Unit (MSF)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. rubric:: Hoist input data

| SWL = **4900 kg**
| Dead weight = **100 Kg**
| Reeving = **2/1**
| Drum diameter = **250 mm**
| Gearbox ratio = **60**
| Motor speed = **3000 rpm**

| Is it possible to put a torque limiter? 
| **Yes**

| Is there important inertia after the torque limiter? 
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

|Cms|= 1.4 x Cs = 1.4x 3 065 = 4 291 Nm

According to :ref:`MotoSuiveur Unit arrest torque table`:

|Cms|= 4 291 Nm < 6 100 Nm 

**MS1** is the correct size of MotoSuiveur unit for this application.





MotoSuiveur control cabinet selection
======================================

MotoSuiveur load recovery add-on selection
=============================================

MotoSuiveur torque limiter add-on  selection
================================================