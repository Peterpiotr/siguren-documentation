==============
Following Mode
==============

..
    .. tags:: following, overspeed

.. include:: /_img/_image-substitutions.rst

Introduction
=============

Following Mode is the main operating mode of the MotoSuiveur® System.

Following Mode starts after a successful completion of MS Self-Test. 

.. note::
    See :doc:`/operation/regular/self-test`.

In Following Mode, the MotoSuiveur® System **simultaneously**:

    - follows hoist movements.
    - monitors for exceeding the :term:`rated speed` with defined positive tolerance. This threshold is called the :term:`overspeed`. 


States of Following Mode
=========================


Following Mode is separated into a **Rest State** and a **Follow State**. 
    :Rest State: 
        MotoSuiveur® System is waiting for a movement request. 
    :Follow State: 
        When a movement request is received, MotoSuiveur® System transitions into Follow State (= starts following hoist movements).


Rest State and Follow State are displayed on MS Controller 7-segment display and MS HMI "Main Screen" field :guilabel:`MotoSuiveur® System status` .

.. "status" instead of "state" on HMI.

.. note::
    See :doc:`/operation/regular/self-test`.

Following Mode logic
========================

After successful passed of self-test MotoSuiveur® System is in Rest State.

In Rest State, after a successful Self-Test and the presence of an enable signal from the crane, the following indicators are active **simultaneously**:

    - :guilabel:`🟢 Hoist enabled`, 
    - :guilabel:`🟢 Upward Enable` 
    - :guilabel:`🟢 Downward Enable`.


.. figure:: /_img/regular-operation/indicators-following-state.png
   :class: instructionimg
   :figwidth: 100 %

   Active indicators in following state

.. we just said we were in rest state and the caption of the image says following state

The following process is started after pressing the buttons to operate the hoist UP or DOWN.

If a limit switch prohibiting upward movement is activated during movement, the :guilabel:`🟢 Upward Enable` indicator becomes inactive - `Upward movement prohibited`.

In this state, no upward movement of the crane is allowed, and a short downward movement is required until the MS worm is cantered `Active indicators in following state`.
.. which "state"? one of the two states of the following mode?


.. figure:: /_img/regular-operation/indicators-following-state.png
   :class: instructionimg
   :figwidth: 100 %

   Upward movement prohibited

Accordingly, if the limit switch prohibiting downward movement is activated during movement, the :guilabel:`🟢 Downward Enable` indicator becomes inactive - `Downward movement prohibited`. 

In this state, no downward movement of the crane is allowed, and a short upward movement is required until the MS worm is cantered - `Active indicators in following state`.

.. figure:: /_img/regular-operation/downward-prohibited.png
   :class: instructionimg
   :figwidth: 100 %

   Downward movement prohibited

If the enable signal from the hoist to MotoSuiveur® System loss, the :guilabel:`🟢 Hoist enabled` indicator becomes inactive. 
In this case MotoSuiveur® System does not follow the hoist on a motion request. 
Accordingly, MotoSuiveur® System does not provide an Enable signal to hoist.

.. figure:: /_img/regular-operation/no-enable-signal.png
   :class: instructionimg
   :figwidth: 100 %

   No enable signal from hoist

The states described above do not put the MotoSuiveur® System in a fault state. 
Fault states can occur for a variety of reasons (overspeed detection, unwanted movement detection, loss of power supply etc.). 
When the hoist is requested to move, the MC starts to follow in the direction it is required. 
During following, the MC checks for exceeding the maximum permissible hoist speed. 
When the MotoSuiveur® System detects that the defined speed is exceeded, it trips, :guilabel:`🔴 Fault indicator` became active, 
Hoist enabled indicator became inactive and prevents the hoist from moving. 
Downward enable and Upward enable are ignored in fault state.
Fault message is displayed on MS Controller 7-segmend display and MS HMI.

.. figure:: /_img/regular-operation/ms-fault.png
   :class: instructionimg
   :figwidth: 100 %
   
   MotoSuiveur® System fault state
   
After MotoSuiveur® System enters a fault state, an operator (authorized personnel) response is required to identify the reason for the fault. 
Once the cause of the failure has been identified and resolved, a :doc:`Reset </operation/regular/system-Reset>` of the MotoSuiveur® System is required. 
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

.. _MS Controller 7-segment display:

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


MS HMI status messages
=======================

On MS HMI "Main Screen" status of MotoSuiveur® System is displayed.
In table below status messages are listed.

.. csv-table:: Status messages
   :file: /_tables/mshmi-status-messages.csv
   :header-rows: 1
   :delim: ;
   :widths: auto

