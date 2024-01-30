=============================================
MS Controller Internal Errors
=============================================

.. include:: /_img/_image-substitutions.rst

.. E02 (for example) is an internal error AND a MS System fault. How come?

E01 - Overvoltage DC bus
=============================

7-segment display
    |7s-E| |7s-0| |7s-1|

.. admonition:: Meaning
    :class: warning
    
    An overvoltage has been detected on the internal DC bus.

.. admonition:: Possible causes
    :class: note
    
    - Overvoltage on the network
    - Overloaded ballast resistor

Steps
    1. _ 


E02 - Undervoltage DC bus 
===========================

7-segment display
    |7s-E| |7s-0| 

.. admonition:: Meaning
    :class: warning
    
    The internal DC bus has dropped below the configured minimum voltage

.. admonition:: Possible causes
    :class: note
    
    -

Steps
    1. This fault is managed while the drive is enabled.

.. what does "the fault is managed" mean?


E03 - I2t motor
===========================

Internal Error Title
    I2t motor

7-segment display
    |7s-E| |7s-0| 

.. admonition:: Meaning
    :class: warning
    
    Overload on the motor

.. admonition:: Possible causes
    :class: note
    
    - Mechanical hard point,
    - Bad power wiring, 
    - Motor feedback problem, 
    - Poorly controlled brake.

Steps
    1. _


E04 - Overcurrent
===========================

7-segment display
    |7s-E| |7s-0| 

.. admonition:: Meaning
    :class: warning

    A current greater than the maximum measurable current has been detected on at least one of the motor phases

.. admonition:: Possible causes
    :class: note
    
    -

Steps
    1. The drive must be powered 24VDC for 15 min before it can be unlocked.

.. what does it mean to "unlock" the drive? are we "acknowledging the fault"?

E05 - Short circuit
===========================

7-segment display
    |7s-E| |7s-0| 

.. admonition:: Meaning
    :class: warning
    
    A short-circuit between phases or the earthing of a motor phase has been detected

Steps
    1. The drive must be powered 24VDC for 15 min before it can be unlocked.

E06 - IGBT temperature
===========================

7-segment display
    |7s-E| |7s-0| 

.. admonition:: Meaning
    :class: warning
    
    Maximum temperature reached in the drive

.. admonition:: Possible causes
    :class: note
    
    -

Steps
    1. Wait for the temperature to drop back down to acknowledge the error.

E07 - Motor temperature 
===========================

7-segment display
    |7s-E| |7s-0| 

.. admonition:: Meaning
    :class: warning
    
    Maximum temperature reached in the motor

.. admonition:: Possible causes
    :class: note
    
    -

Steps
    1. Wait for the temperature to drop back down to acknowledge the error.

.. define "acknowledge the fault"

E08 - Resolver fault
===========================

7-segment display
    |7s-E| |7s-0| 

.. admonition:: Meaning
    :class: warning
    
    Defective resolver signals

.. admonition:: Possible causes
    :class: note
    
    -

Steps
    1. Check resolver connection between motor and control cabinet and resolver connector.


E09 - Coil temperature 
===========================

7-segment display
    |7s-E| |7s-0| 

.. admonition:: Meaning
    :class: warning
    
    Maximum temperature reached in the self

.. admonition:: Possible causes
    :class: note
    
    -

Steps
    1. Wait for the temperature to drop back down to acknowledge the error.


E16 - Resolver saturation
===========================

7-segment display
    |7s-E| |7s-1| |7s-F|

.. admonition:: Meaning
    :class: warning
    
    Sin - Cos resolver signals received too high

Steps
    1. Check resolver connection between motor and control cabinet and resolver connector.


E17 - 24V auxiliary supply error
=================================

7-segment display
    |7s-E| |7s-1| 7

.. missing the 7 

.. admonition:: Meaning
    :class: warning
    
    24V auxiliary supply error

.. admonition:: Possible causes
    :class: note
    
    - 24V auxiliary power supply is noisy 
    - or has a voltage dip (<15V). 

Steps
    1. Check the 24V supply.


