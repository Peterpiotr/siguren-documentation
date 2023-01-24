Glossary
========

.. glossary::

   rated speed
      nominal speed

   overspeed
      Typically :guilabel:`Overspeed` is equal to:
      **Overspeed = Nominal speed + 10%**

   controller
      also called 'drive' or 'servo-drive'
      SMD servo drives are especially suitable for high dynamics and high precision.
      They integrate the power supply, the braking resistor, the mains filter and the safety function. 
      Thanks to their integrated inputs/outputs and PLC functions, they are suitable for a wide variety of applications.
      Industrial Ethernet communication busses provide networked configurations. The user-friendly Windows-based parameterization software 
      offers functions for easy setup and diagnostics.
      See `Digital DRIVE for Brushless motors SMD Series - Quick Start guide <https://www.serad.com/wp-content/uploads/Documentation/05%20-%20Variateurs%20pour%20moteur%20brushless/SMD/SMD%20-Quick%20Start%20Guide-2046-EN.pdf>`_ 
   
   Brake Release Tool
      (description)

   Wheel or wheel with skewed teeth 
      The wheel that is fitted to the hoisting shaft.

   Screw, Worm Screw or endless screw
      A shaft shaped with a screw at one side and spline of the other side. With the wheel, the screw is one of the main components of the MotoSuiveur.

   Screwing or screwing rotation
      Clockwise rotation of the screw viewed from spline part of the screw shaft (right handside on the drawing). 
      On an irreversible MotoSuiveur such as the hydraulic version, the screwing rotation corresponds 
      to the hoisting up rotation of the hoisting shaft and the wheel.

   Unscrewing or unscrewing rotation
      Anticlockwise rotation of the screw viewed from spline part of the screw shaft (right handside on the drawing). 
      On an irreversible MotoSuiveur such as the hydraulic version , the unscrewing rotation corresponds 
      to the hoisting down rotation of the hoisting shaft and the wheel.

   Screwing/Unscrewing and up/down
      Screwing and unscrewing are physically linked to the the worm screw of the Motosuiveur. 
      Since friction Motosuiveurs are reversible, in some installations screwing can be up while down on others. 
      On installations that have two Motosuiveurs, they can be mounted in opposite direction.

   Inward translation
      Translation of the screw as if the screw was rotating and translating in the screwing direction (clockwise).
      When the wheel is stopped, the translation can occur with the screwing rotation of the screw.
      During a hoisting down operation or a fall, when the wheel rotates faster than the screw, 
      the latter translates in the screwing direction towards the screwing hard stop

   Outward translation
      Translation of the screw as if the screw was rotating and translating in the unscrewing direction.
      When the wheel is stopped, the translation can occur with the unscrewing rotation of the screw.
      During a hoisting up operation when the wheel rotates faster than the screw, 
      the latter translates in the unscrewing direction towards the outward hard stop

   Inward hard stop
      The hard stop that limits the inward translation. The inward hard stop position is detected by a sensor.

   Outward hard stop
      The hard stop that limits the outward translation. The outward hard stop position is detected by a sensor.

   Reversibility
      The friction Motosuiveur® is mechanically reversible, which means that is can indifferently be mounted in one orientation 
      or the other and can absorb a fall according both mountings.
      When delivered with its control cabinet, the Motosuiveur® must either be mounted according 
      to the logics of the cabinet which cannot know how the Motosuiveur® is oriented.

   Friction absorber
      The friction absorber is a device fitted inside the wheel used to absorb and dissipate the energy of a sudden fall before the screw does its blocking job.
      The friction absorber is constituted of friction disks stacked alternatively with inner disks and outer disks. 
      Those disks are positioned inside the wheel. Stator disks are mechanically connected to the wheel while the inner disks are connected to the hoisting shaft.
      The disks are pressed together by a series of spring washers (Belleville washers). 
      The pressure is set by putting a number of washers that meets the installation requirements.

   Irreversibility
      The Hydraulic Motosuiveur® is irreversible, which means that it can absorb the energy of a fall only in one direction.

   Reaction arm
      The hydraulic absorbs the energy on a very short course. When the energy must be absorbed on a longer course of the load, 
      in order to have a smother deceleration, the Motosuiveur® can be mounted in a floating mode and be held by a reaction arm. 
      Fitted with an absorber, this arm absorbs the energy by letting the Motosuiveur® rotate from 0° to 330° according to the requirements.

   Recovery clutch or clutch
      The gear that is used to engage the recovery motor. The mechanism is quite similar to a Bendix motor starter.

   Clutch pinion wheel or pinion wheel in a clutch context
      The part of the recovery clutch that is driven by the recovery motor and that has only one degree of freedom : rotation.
      The pinion wheel is bored with a spline in its central axis to receive the flywheel.

   Clutch flywheel or flywheel
      The wheel that translates on the screw shaft guided by spline. 
      The external part of the flywheel is fitted with a hollow cylinder that has a position cam at is end.
      The flywheel is pushed by a spring that is protected by the flywheel cylinder an is fitted on a screw thread etched in the flywheel. 
      It can be tuned by turning it more or less in the thread.
      The spline of the flywheel posses a hook that is used to maintain the flywheel inside the pinion wheel during the recovery hoisting up operation.
      When the clutch pinion wheel and the flywheel are meshed, the recovery motor can drive the screw.

   Recovery engagement
      Procedure that consists of engaging the flywheel into the pinion wheel to mesh their splines in order to allow the recovery motor to drive the screw.
      It is composed of two phases:

      -	the pre-engagement that pushes the screw in its inward hard stop.
      -	The engagement that engages the flywheel into the pinion wheel.

      This operation is usually performed automatically by the control cabinet logics. It can be done when needed by other means.
      The engagement is detected by a sensor.

   Motosuiveur® control panel, control cabinet, control box or electrical cabinet
      The electrical cabinet that contains relays, logical unit, motor drivers, relays, circuit breakers and wiring.

   Proface, touch screen, programmable logic controller
      The Proface is the programmable logic controller that is the interface between the buttons and beacons 
      that are on the control panel, the driver of servo-motor(s) of the screw, the driver of the recovery motor 
      if any and the hoisting installation electrical cabinet.

   Drive, controller
      The motor controller that drives the Servo-motor. When control cabinet manages many Motosuiveurs, 
      each servo-motor is driven by its own drive.

   Recovery Motor Drive
      The recovery motor controller that drives the recovery motor. When control cabinet manages many Motosuiveurs, 
      each recovery motor is driven by its own drive.

   Normal mode
      The standard operating mode when no major fault occurs.

   Recovery mode
      Capability given to the Motosuiveur® when equiped with a recovery motor to perform hoisting up and down operations at low speed. 
      It is used when the main hoisting chain is faulty.

   Backup mode
      Feature that allows the load to be lowered down, by using minimal capabilities. The Motosuiveur® limits the free fall to programed level. 
      It is used as an extreme solution.
