==========================================
Operating in Following Mode (Normal Mode)
==========================================

..
    .. tags:: following, overspeed

.. include:: /_img/_image-substitutions.rst

Introduction
=============

Following Mode (also called Normal Mode) is the main operating mode of the MotoSuiveur® System.


In Following Mode, the MotoSuiveur® System **simultaneously**:

    - follows hoist movements.
    - monitors for exceeding the :term:`rated speed` with defined positive tolerance. This threshold is called the :term:`overspeed`. 

Following Mode is separated into a **Rest State** and a **Follow State**. 
    :Rest State: 
        MotoSuiveur® System is waiting for a movement request. 
    :Follow State: 
        When a movement request is received, MotoSuiveur® System transitions into Follow State (= starts following hoist movements).


Rest State and Follow State are displayed on MS Controller 7-segment display and MS HMI "Main Screen" field :guilabel:`MotoSuiveur® System status` .

.. show screenshot and image of what is displayed in each state

.. "status" instead of "state" on HMI.

Following Mode logic
=====================

After the successful completion of a Self-Test MotoSuiveur® System goes into Rest State.

.. seealso::
    :doc:`/operation/regular/self-test`.

In Rest State, in the presence of an ENABLE signal from the crane, the following indicators are ON **simultaneously**:

    - :guilabel:`🟢 Hoist ENABLED` 
    - :guilabel:`🟢 Upward ENABLE` 
    - :guilabel:`🟢 Downward ENABLE`

.. and what if we are in Rest State 
.. why is the ENABLE signal coming FROm the crane??

.. figure:: /_img/regular-operation/indicators-following-state.png
   :class: instructionimg
   :figwidth: 100 %

   MS Control Panel: ON indicators in following state

.. we just said we were in rest state and the caption of the image says following state

The following process is started after pressing the buttons to operate the hoist UP or DOWN.

.. "following process" is the Follow State?

If a limit switch prohibiting Upward movement is activated during movement, the :guilabel:`🟢 Upward ENABLE` indicator becomes inactive - `Upward movement prohibited`.

In this state, no Upward movement of the crane is allowed, and a short Downward movement is required until the MS worm is centered `Active indicators in following state`.
.. which "state"? one of the two states of the following mode?


.. figure:: /_img/regular-operation/indicators-following-state.png
   :class: instructionimg
   :figwidth: 100 %

   MS Control Panel: Upward movement prohibited

Accordingly, if the limit switch prohibiting Downward movement is activated during movement, the :guilabel:`🟢 Downward ENABLE` indicator becomes inactive - `Downward movement prohibited`. 

In this state, no Downward movement of the crane is allowed, and a short Upward movement is required until the MS worm is cantered - `Active indicators in following state`.

.. in this state meaning in "follow state"?

.. figure:: /_img/regular-operation/Downward-prohibited.png
   :class: instructionimg
   :figwidth: 100 %

   MS Control Panel: Downward movement prohibited

If the ENABLE signal from the hoist to MotoSuiveur® System is lost, the :guilabel:`🟢 Hoist ENABLED` indicator becomes inactive. 
In this case MotoSuiveur® System does not follow the hoist on a motion request. 

.. dont use "in this case"
.. 

Accordingly, MotoSuiveur® System does not provide an Enable signal to hoist.

.. figure:: /_img/regular-operation/no-ENABLE-signal.png
   :class: instructionimg
   :figwidth: 100 %

   MS Control Panel: No ENABLE signal from hoist

The states described above do not put the MotoSuiveur® System in a fault state. 
Fault states can occur for a variety of reasons (overspeed detection, unwanted movement detection, loss of power supply etc.). 
When the hoist is requested to move, the MC starts to follow in the direction it is required. 
During following, the MC checks for exceeding the maximum permissible hoist speed.

.. during following means in Following Mode?

When the MotoSuiveur® System detects that the defined speed is exceeded, it trips, :guilabel:`🔴 Fault indicator` became active, 
Hoist ENABLED indicator became inactive and prevents the hoist from moving. 
Downward ENABLE and Upward ENABLE are ignored in fault state.
Fault message is displayed on MS Controller 7-segmend display and MS HMI.

.. figure:: /_img/regular-operation/ms-fault.png
   :class: instructionimg
   :figwidth: 100 %
   
   MS Control Panel: MotoSuiveur® System fault state
   
After MotoSuiveur® System enters a fault state, an operator (authorized personnel) response is required to identify the reason for the fault. 
Once the cause of the failure has been identified and resolved, a :doc:`system-reset` of the MotoSuiveur® System is required. 
After a successful Self-Test following a Reset of MotoSuiveur® System, it enters in Following Mode.

Figure `Main principle of following operation mode and overspeed detection` 
present the main principle of Following Mode (upper part) and Overspeed detection (lower part). 
MotoSuiveur® System follows hoist/crane movement until overspeed is detected.
When overspeed is detected, MotoSuiveur® System **trips** and mechanicaly lockes hoist/crane
to prevent load drop.

.. figure:: /_img/archives/following-01.png
   :class: instructionimg
   :figwidth: 100 %

   Main principle of following operation mode and overspeed detection


.. csv-table:: Following Mode stages
   :file: /_tables/following-mode-stages.csv
   :delim: ;
   :header-rows: 0
   :widths: auto
   :align: left



MS Controller display
=====================

`Symbols displayed on 7-segment display on MS Controller` shows the 
symbols displayed on 7-segment display during Following Mode in Rest State.
During Rest State differend messages can be displayed on 7-segment display.
They are active only during Rest State.

.. csv-table:: Rest State
   :file: /_tables/following-mode-digits-rest.csv
   :delim: ;
   :header-rows: 1
   :widths: auto

`Symbols displayed on 7-segment display on MS Controller during movement` shows the 
symbols displayed on 7-segment display during following operation mode during movement.

.. csv-table:: Movement
   :file: /_tables/following-mode-digits-movement.csv
   :header-rows: 1
   :delim: ;
   :widths: auto


