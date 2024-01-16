=========================
What is MotoSuiveur® Unit
=========================

.. include:: ../../_img/_image-substitutions.rst

.. role:: mechpart
   :class: mechpart


The MotoSuiveur® Unit (referred to for short MS) is a proprietary system for the protection of the hoist load from mechanical or electrical failure and overspeed, 
and for the recovery of the load in the event of a failure. The unit is supplied with a proprietary control panel from the equipment manufacturers. 
The crane’s hardwired controls are interfaced to this panel to control the MotoSuiveur® in normal operation. 

The MotoSuiveur® Unit is a failsafe mechanical hoist arrester, designed and manufactured by Siguren Technologies LTD. 
The MotoSuiveur® Unit protects against failures in hoist drive trains that would otherwise lead to dropped loads or overloads.

MotoSuiveur® Unit provides mechanical failsafe protection in the event of any electrica or mechanical failure of the hoist drive train. 
In addition to the MotoSuiveur® Unit, a torque limiter is put in the drive-train to limit any overload into the hoist lifting mechanism. 


Description of components
=========================

Hydraulic Damping MotoSuiveur®
-------------------------------

.. figure:: ../../_img/MS_Unit/hydraulic-ms.PNG
   :figwidth: 600 px
   :align: center  
    

.. csv-table:: Hydraulic Damping MotoSuiveur® Unit components
   :file: ../../_tables/hydraulic_ms.csv
   :delim: ;
   :header-rows: 1
   :class: tight-table
   :align: left
   :widths: auto


Friction MotoSuiveur®
---------------------

.. figure:: ../../_img/MS_Unit/Friction.jpg
   :figwidth: 600 px
   :align: center  
    

.. csv-table:: Friction MotoSuiveur® Unit components
   :file: ../../_tables/friction_ms.csv
   :delim: ;
   :header-rows: 1
   :class: tight-table
   :align: left
   :widths: auto


Principle of MotoSuiveur® System
---------------------------------


The MS wheel is internally splined and is connected to a splined shaft attached to the crane drive train to transmit torque via plain bearings 
between the shaft and wheel to support the interface radially. 
The wheel interface consists of a plain bearing mounted between the wheel and casing for radial support where the wheel interacts directly 
with the casing for lateral and axial loads. 
The worm and wheel interact in a standard manner, with the mesh such that clearance is achieved and that the wheel cannot force rotation on to the worm. 
The worm bears onto the casing directly and is supported laterally and radially. 
Axial restraint is provided by spring which holds the worm in place where the normal servo motor torque is applied (i.e., under normal conditions). 
Extending from the worm in one direction is a shaft with a splined surface, this interfaces with a bevel gear with an internal spline and is axially free to translate 
along the worm shaft. Meshing with the bevel gear is its reciprocal gear, which is rigidly fixed to a servo motor, itself mounted to the casing. 
This motor provides rotation to the worm via the bevel gear arrangement at a pre-set torque. The worm conveys this torque onto the wheel through its mesh. 
The motor is actuated when the hoist operation is requested. When the servo motor actuates it allows the worm to convey the torque onto the wheel,
but this torque is insufficient to allow the crane drive to actuate, instead allowing the wheel to rotate with the drum shaft through the normal crane drive. 
Finally, to complete the moment couple between the drum shaft and the MS unit, a dowel pins mounts between the torque arm and the hoist body.


MotoSuiveur® Unit size
-----------------------

.. _MotoSuiveur® Unit arrest torque table:
.. csv-table:: MotoSuiveur® Unit arrest torque table
   :file: ../../_tables/ms-unit-torque.csv
   :delim: ;
   :header-rows: 1
   :widths: 10, 30, 30, 30
   :class: tight-table
   :align: center


Interfacing MotoSuiveur® System with hoist
==========================================

Mechanical interface with hoist
-------------------------------

The MotoSuiveur® wheel hub is interfaced mechanically to hoist drum via differend methods.

The MotoSuiveur® secured hoist system typically comprises of the following components shown below.

.. figure:: ../../_img/MS_Unit/MS_secured_hoist.png

.. csv-table:: MotoSuiveur® secured hoist
   :file: ../../_tables/MS-Secured-Hoist.csv
   :delim: ;
   :header-rows: 1
   :widths: auto
   :class: tight-table
   :align: left

1 - The MotoSuiveur® Unit can be fixed in different methods to the hoist. The following sections explain in more detail.

2 - Torque limiter is mandatory for hydraulic MS type

Electrical interface with hoist
-------------------------------

The MotoSuiveur® system is electrically controlled using typical components as shown in the figure below. 

MotoSuiveur® system is controlled by hoist commands. No external control is needed.

.. note::
   It is recommended hoist main power supply and MS main power supply are separated.

.. note::
   SIGUREN TECHNOLOGIES RECOMMENDS that the power supply to the MotoSuiveur® System should not be cut off by the E-stop button.


.. figure:: ../../_img/MS_Unit/MS-Electrical-description.jpg

.. csv-table:: MotoSuiveur® secured hoist
   :file: ../../_tables/electrical-interface.csv
   :delim: ;
   :header-rows: 1
   :widths: auto
   :class: tight-table
   :align: left
