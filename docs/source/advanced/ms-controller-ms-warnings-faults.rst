====================================================================
MS Controller Display of MotoSuiveur® System  Warnings and Faults
====================================================================

.. include:: /_img/_image-substitutions.rst

.. E02 (for example) is an internal error AND a MS System fault. How come?

.. most of the "Steps" are not actionable, insufficient and unclear

Introduction
=============

.. what is a warning and what is a fault?

Warnings and faults table
===========================

.. separate faults and warnings?

.. list-table::

    * - **Code** 
      - **Title**
    * - `E02`_
      - Screwing command during Self-Test
    * - `E03`_
      - Unscrewing command during Self-Test
    * - `E04`_
      - Both commands during Self-Test 
    * - `E05`_
      - ON signal missing during Self-Test 
    * - `E10`_
      - Blocked worm 
    * - `E11`_
      - Unscrewing ENABLE switch not centered 
    * - `E12`_
      - Screwing ENABLE switch not centered
    * - `E13`_
      - Unscrewing ENABLE switch not made
    * - `E14`_
      - Screwing ENABLE switch not made
    * - `E28`_
      - Incorrect MS firmware version 
    * - `F15`_
      - Worm backlash too big detected (Play too big) 
    * - `F17`_
      - Worm backlash too small detected (Play too small)
    * - `F20`_
      - Air detected 
    * - `F22`_
      - Damping too soft 
    * - `F23`_
      - Damping too hard
    * - `F33`_
      - Unscrewing Overspeed / Overspeed during lowering 
    * - `F34`_
      - Screwing Overspeed / Overspeed during lifting
    * - `E55`_
      - Oil



E02 
====

Title
    Screwing command during Self-Test

7-segment display 
    |7s-E| |7s-0| |7s-2| 

.. admonition:: Meaning 
    :class: warning 
    
    Active command for lifting from hoist control at the begining of Self-test detected.

Steps
    1. Check for pressed/held down button for hoist lifting command


E03
====

Title
    Unscrewing command during Self-Test

7-segment display 
    |7s-E| |7s-0| |7s-3| 

.. admonition:: Meaning 
    :class: warning 
    
    Active command for lowering from hoist control at the begining of Self-test detected.

Steps
    1. Check for pressed/held down button for hoist lowering command


E04
====

Title
    Both commands during Self-Test 

7-segment display 
    |7s-E| |7s-0| |7s-4| 

.. admonition:: Meaning 
    :class: warning 
    
    Active commands for lifting and lowering simultaneously from hoist control at the begining of Self-test detected.

Steps
    1. Check for pressed/held down button for hoist lifting and lowering command


E05
====

Title
    ON signal missing during Self-Test 

7-segment display 
    |7s-E| |7s-0| |7s-5| 

.. admonition:: Meaning 
    :class: warning 
    
    No ENABLE signal from hoist. Hoist PLC malfunction. Hoist PLC in fault. Lost connection between hoist PLC and MS Controller. Fault in hoist control system. Other causes are possible.

Steps
    1. Check electrical connection between hoist control cabinet and MS hoist cabinet. 
    2. Check hoist control system.


E10 
====

Title
    Blocked worm 

7-segment display 
    |7s-E| |7s-1| |7s-0| 

.. admonition:: Meaning 
    :class: warning 
    
    Worm is stuck.  Worm is locked to recovery mechanism (If MS-IRD is installed).

Steps
    1. Mechanical reset is needed. In case of Downward ENABLE off after recovery operation, moving I opposite side from hoist is needed.  

    .. clarify 

    2. Moving should continue until lamps indicators for Upward and Downward are on. 
    3. After manual reentering, MS reset is necessary.


E11
====

Title
    Unscrewing ENABLE switch not centered 

7-segment display 
    |7s-E| |7s-1| |7s-1| 

.. admonition:: Meaning 
    :class: warning 
    
    Switch USCRE is not in correct position.

Steps
    1. Visual check is and centering is needed.


E12
====

Title
    Screwing ENABLE switch not centered

7-segment display 
    |7s-E| |7s-1| |7s-2| 

.. admonition:: Meaning 
    :class: warning 
    
    Switch SCRE is not in correct position.

Steps
    1. Visual check is and centering is needed.


E13
====

Title
    Unscrewing ENABLE switch not made

7-segment display 
    |7s-E| |7s-1| |7s-3| 

.. admonition:: Meaning 
    :class: warning 
    
    USCRE switch is not reached from worm during Switch test.

Steps
    1. Visual check is needed.


E14
====

Title
    Screwing ENABLE switch not made 

7-segment display 
    |7s-E| |7s-1| |7s-4| 

.. admonition:: Meaning 
    :class: warning 
    
    SCRE switch is not reached from worm during Switch test.

Steps
    1. Visual check is needed.


E28
====

Title
    Incorrect MS firmware version 

7-segment display 
    |7s-E| |7s-2| |7s-8| 

.. admonition:: Meaning
    :class: warning 
    
    _

Steps 
    1. Please contact SIGUREN technologies.


F15
====

Title
    Worm backlash too big detected (Play too big) 

7-segment display 
    |7s-F| |7s-1| |7s-5| 

.. admonition:: Meaning 
    :class: warning 
    
    Worm play is greater than defined.

Steps
    1. Center the worm in position with Upward and Downward ENABLE indicators are on. 
    2. Wait 15 sec. 
    3. Reset MotoSuiveur® System.


F17
====

Title
    Worm backlash too small detected (Play too small)

7-segment display 
    |7s-F| |7s-1| 7 

.. admonition:: Meaning 
    :class: warning 
    
    Worm play is smaller than defined.

Steps
    1. Center the worm in position with Upward and Downward ENABLE indicators are on. 
    2. Wait 15 sec. 
    3. Reset MotoSuiveur® System.


F20
====

Title
    Air detected 

7-segment display 
    |7s-F| |7s-2| |7s-0| 

.. admonition:: Meaning 
    :class: warning 
    
    Presence of air into the oil inside the damping chamber

Steps
    1. Air bleeding is necessary. Please, contact MotoSuiveur® supplier support.


F22
====

Title
    Damping too soft 

7-segment display 
    |7s-F| |7s-2| |7s-2| 

.. admonition:: Meaning 
    :class: warning 
    
    Damping nozzles too open

Steps
    1. Center the worm in position with Upward and Downward ENABLE indicators are on. 
    2. Wait 15 sec. 
    3. Reset MotoSuiveur® System.


F23
====

Title
    Damping too hard

7-segment display 
    |7s-F| |7s-2| |7s-3| 

.. admonition:: Meaning 
    :class: warning 
    
    Damping nozzles too closed

Steps
    1. Center the worm in position with Upward and Downward ENABLE indicators are on. 
    2. Wait 15 sec. 
    3. Reset MotoSuiveur® System


F33
====

Title
    Unscrewing Overspeed / Overspeed during lowering 

7-segment display 
    |7s-F| |7s-3| |7s-3| 

.. admonition:: Meaning 
    :class: warning 
    
    Hoist speed exceeds maximum defined speed during lowering

Steps
    1. Reset MotoSuiveur® System.


F34
====

Title
    Screwing Overspeed / Overspeed during lifting

7-segment display 
    |7s-F| |7s-3| |7s-4| 

.. admonition:: Meaning 
    :class: warning 
    
    Hoist speed exceeds maximum defined speed during lifting

Steps
    1. Reset MotoSuiveur® System.


E55
====

Title
    Oil 

7-segment display 
    |7s-E| |7s-5| |7s-5| 

.. admonition:: Meaning 
    :class: warning 
    
    Low oil level in MS Unit

Steps
    1. Check MS Unit oil level. 
    2. Check health of MS oil level sensor. 
    3. Check health of connection between MotoSuiveur® oil level sensor and MotoSuiveur® control cabinet



