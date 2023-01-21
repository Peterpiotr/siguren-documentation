============================
Load recovery operation
============================

.. role:: mechpart
   :class: mechpart

.. note::
    Based on :download:`Using the MS Recovery Capabilities <../archives/using-the-ms-recovery-capabilities-02.docx>`

.. container:: twocol

    .. container:: leftside

        text on left column

    .. container:: rightside

        text on right column

+---------------------------------------------------------------+-------------------------------------------------------------+
| ::                                                            |                                                             |
|                                                               |                                                             |
|   Footnote references, like [5]_.                             |   Footnote references, like [5]_.                           |
|   Note that footnotes may get                                 |   Note that footnotes may get                               |
|   rearranged, e.g., to the bottom of                          |   rearranged, e.g., to the bottom of                        |
|   the "page".                                                 |   the "page".                                               |
|                                                               |                                                             |
|   .. [5] A numerical footnote. Note                           |   .. [5] A numerical footnote. Note                         |
|      there's no colon after the ``]``.                        |      there's no colon after the ``]``.                      |
+---------------------------------------------------------------+-------------------------------------------------------------+
| ::                                                            |                                                             |
|                                                               |                                                             |
|   Autonumbered footnotes are                                  |   Autonumbered footnotes are                                |
|   possible, like using [#]_ and [#]_.                         |   possible, like using [#]_ and [#]_.                       |
|                                                               |                                                             |
|   .. [#] This is the first one.                               |   .. [#] This is the first one.                             |
|   .. [#] This is the second one.                              |   .. [#] This is the second one.                            |
|                                                               |                                                             |
|   They may be assigned 'autonumber                            |   They may be assigned 'autonumber                          |
|   labels' - for instance,                                     |   labels' - for instance,                                   |
|   [#fourth]_ and [#third]_.                                   |   [#fourth]_ and [#third]_.                                 |
|                                                               |                                                             |
|   .. [#third] a.k.a. third_                                   |   .. [#third] a.k.a. third_                                 |
|                                                               |                                                             |
|   .. [#fourth] a.k.a. fourth_                                 |   .. [#fourth] a.k.a. fourth_                               |
+---------------------------------------------------------------+-------------------------------------------------------------+
| ::                                                            |                                                             |
|                                                               |                                                             |
|   Auto-symbol footnotes are also                              |   Auto-symbol footnotes are also                            |
|   possible, like this: [*]_ and [*]_.                         |   possible, like this: [*]_ and [*]_.                       |
|                                                               |                                                             |
|   .. [*] This is the first one.                               |   .. [*] This is the first one.                             |
|   .. [*] This is the second one.                              |   .. [*] This is the second one.                            |
+---------------------------------------------------------------+-------------------------------------------------------------+
| ::                                                            |                                                             |
|                                                               |                                                             |
|   Citation references, like [CIT2002]_.                       |   Citation references, like [CIT2002]_.                     |
|   Note that citations may get                                 |   Note that citations may get                               |
|   rearranged, e.g., to the bottom of                          |   rearranged, e.g., to the bottom of                        |
|   the "page".                                                 |   the "page".                                               |
|                                                               |                                                             |
|   .. [CIT2002] A citation                                     |   .. [CIT2002] A citation                                   |
|      (as often used in journals).                             |      (as often used in journals).                           |
|                                                               |                                                             |
|   Citation labels contain alphanumerics,                      |   Citation labels contain alphanumerics,                    |
|   underlines, hyphens and fullstops.                          |   underlines, hyphens and fullstops.                        |
|   Case is not significant.                                    |   Case is not significant.                                  |
|                                                               |                                                             |
|   Given a citation like [this]_, one                          |   Given a citation like [this]_, one                        |
|   can also refer to it like this_.                            |   can also refer to it like this_.                          |
|                                                               |                                                             |
|   .. [this] here.                                             |   .. [this] here.                                           |
+---------------------------------------------------------------+-------------------------------------------------------------+
| ::                                                            |                                                             |
|                                                               |                                                             |
|   External hyperlinks, like Python_.                          |   External hyperlinks, like Python_.                        |
|                                                               |                                                             |
|   .. _Python: http://www.python.org/                          |   .. _Python: http://www.python.org/                        |
+---------------------------------------------------------------+-------------------------------------------------------------+
| ::                                                            |                                                             |
|                                                               |                                                             |
|   External hyperlinks, like `Python                           |   External hyperlinks, like `Python                         |
|   <http://www.python.org/>`_.                                 |   <http://www.python.org/>`_.                               |
+---------------------------------------------------------------+-------------------------------------------------------------+
| ::                                                            |                                                             |
|                                                               |                                                             |
|   Internal crossreferences, like example_.                    |   Internal crossreferences, like example_.                  |
|                                                               |                                                             |
|   .. _example:                                                |   .. _example:                                              |
|                                                               |                                                             |
|   This is an example crossreference target.                   |   This is an example crossreference target.                 |
+---------------------------------------------------------------+-------------------------------------------------------------+
| ::                                                            |                                                             |
|                                                               |                                                             |
|   Python_ is `my favourite                                    |   Python_ is `my favourite                                  |
|   programming language`__.                                    |   programming language`__.                                  |
|                                                               |                                                             |
|   .. _Python: http://www.python.org/                          |   .. _Python: http://www.python.org/                        |
|                                                               |                                                             |
|   __ Python_                                                  |   __ Python_                                                |
+---------------------------------------------------------------+-------------------------------------------------------------+
| ::                                                            |   .. _titles are targets, too:                              |
|                                                               |                                                             |
|   Titles are targets, too                                     |                                                             |
|   =======================                                     |   Titles are targets, too                                   |
|                                                               |                                                             |
|   Implict references, like `Titles are targets, too`_.        |   Implict references, like                                  |
|                                                               |   `Titles are targets, too`_.                               |
+---------------------------------------------------------------+-------------------------------------------------------------+
|                                                                                                                             |
|Directives are a general-purpose extension mechanism, a way of adding support for new constructs without adding              |
|new syntax. For a description of all standard directives, see reStructuredText Directives (http://is.gd/2Ecqh).              |
|                                                                                                                             |
+---------------------------------------------------------------+-------------------------------------------------------------+
| ::                                                            |                                                             |
|                                                               |                                                             |
|   For instance:                                               |   For instance:                                             |
|                                                               |                                                             |
|   .. image:: magnetic-balls.jpg                               |   .. image:: magnetic-balls.jpg                             |
|      :width: 40pt                                             |      :width: 40pt                                           |
|                                                               |                                                             |
+---------------------------------------------------------------+-------------------------------------------------------------+
|                                                                                                                             |
|                                                                                                                             |
| Substitutions are like inline directives, allowing graphics and arbitrary constructs within text.                           |
|                                                                                                                             |
+---------------------------------------------------------------+-------------------------------------------------------------+
| ::                                                            |                                                             |
|                                                               |                                                             |
|   The |biohazard| symbol must be used on containers used to   |   The |biohazard| symbol must be used on containers used to |
|   dispose of medical waste.                                   |   dispose of medical waste.                                 |
|                                                               |                                                             |
|   .. |biohazard| image:: biohazard.png                        |   .. |biohazard| image:: biohazard.png                      |
|      :align: middle                                           |      :align: middle                                         |
|      :width: 12                                               |      :width: 12                                             |
+---------------------------------------------------------------+-------------------------------------------------------------+
|                                                                                                                             |
| Any text which begins with an explicit markup start but doesn't use the syntax of any of the constructs above, is a comment.|
|                                                                                                                             |
+---------------------------------------------------------------+-------------------------------------------------------------+
| ::                                                            |                                                             |
|                                                               |                                                             |
|   .. This text will not be shown                              |   .. This text will not be shown                            |
|      (but, for instance, in HTML might be                     |      (but, for instance, in HTML might be                   |
|      rendered as an HTML comment)                             |      rendered as an HTML comment)                           |
+---------------------------------------------------------------+-------------------------------------------------------------+
| ::                                                            |                                                             |
|                                                               |                                                             |
|   An "empty comment" does not                                 |   An "empty comment" does not                               |
|   consume following blocks.                                   |   consume following blocks.                                 |
|   (An empty comment is ".." with                              |   (An empty comment is ".." with                            |
|   blank lines before and after.)                              |   blank lines before and after.)                            |
|                                                               |                                                             |
|   ..                                                          |   ..                                                        |
|                                                               |                                                             |
|           So this block is not "lost",                        |           So this block is not "lost",                      |
|           despite its indentation.                            |           despite its indentation.                          |
+---------------------------------------------------------------+-------------------------------------------------------------+

The MS will never allow a load drop. It will arrest the hoist drum whenever the hoist brake is unable to do so. 
However, the MS can be used as a gearbox to lower and even raise the load. 

.. note::
	The MS is irreversible – meaning that load drop is impossible even when the MS alone is used for recovering the load. 
	This allows the user to use the weight of the load without risking a load drop.

Three main methods can be used (and combined) to recover the load, depending on how the hoist brake 
and the MotoSuiveur Unit can be accessed and used in the emergency situation that requires the recovery:

- :ref:`Forced MS recovery`
- :ref:`MS followed gravity lowering`
- :ref:`MS assisted gravity lowering`


Forced MS recovery
===================

With the hoist brake open and the MotoSuiveur Unit holding the load, rotate the MS :mechpart:`worm shaft` with considerable torque. 
In this situation the MotoSuiveur Unit moves the load.
This way, a very high amount of torque must be applied on the MS shaft (approximately 1/8 of the barrel torque).

Using the following hardware:

- :doc:`Portable Recovery Tool` for sizes MS4 - MS7, or
- :doc:`Handheld Recovery Tool` for sizes MS0 - MS3

For MS with :doc:`Integrated Remote Recovery` the hardware is integrated and is remotely operated.

Instructions
-------------

-	Open the hoist brake
-	Rotate the :mechpart:`worm shaft` with the following torque to lower the SWL (maximum values)

.. csv-table:: Forced MS Recovery method max torques
   :file: tables/forcedRecoveryTorque.csv
   :header-rows: 1
   :class: tight-table

.. important::
	Indicative barrel speed: 0.1 - 0.3 rpm


MS followed gravity lowering
=============================

Step lowering
--------------

.. note::
	This method can be used only with Hydraulic Damping MS.

.. "method" vs "procedure" vs ...

- Pulse the hoist brake (manually or electrically) to lower the load a few centimeters. The MS :mechpart:`worm shaft` will shift toward the damping chamber. The electrical or brake lever pulse must be short enough to not allow the worm to reach the :mechpart:`elastomer` at the bottom of the damping chamber. 
- Then it is possible to return the :mechpart:`worm shaft` to its “centered” position by hand. 
- Repeat this until the load reaches the floor.

This way, very low torque applied on the MS shaft will be needed (approximately 1/5000 of the barrel torque). 
Using handwheel / crank handle or standard ratchet handle.

The MS can automatically follow if switched to Backup Mode. 
This negates the need of manual operation at the :mechpart:`worm shaft`. 
In case of power outage, the MS can be UPS/battery operated.
Furthermore, the MS can control the brake opening / closing, thus making the gravity load recovery automated.

Instructions
+++++++++++++++

.. _Hydraulic Damping MS step lowering picture:
.. figure:: img/stepLowering.png
	:scale: 75 %
	:align: center
	
	Hydraulic Damping MS step lowering

-	Pulse the hoist brake to achieve less than 30 degrees barrel rotation by gravity
-	Rotate the :mechpart:`worm shaft` by hand few rotations to centralize it
-	Repeat

.. important::
	Indicative mean barrel speed: 0.5 rpm


Backup Mode gravity lowering
------------------------------

- Switch the MS to :doc:`backup-recovery-mode`,
- Order lowering. 
- Progressively release the motor brake using the provided :mechpart:`Brake Release Tool`, until the load starts to rotate the barrel. 
- Use the Brake Release Tool to regulate and maintain the speed below the specified safe speed. A :guilabel:`🔊 buzzer` will sound when the safe speed is close.

The MS will arrest the barrel if:

-	lowering order is removed or
-	overspeed is reached

After such arrest, the worm shaft can be returned to its “centered” position by using a standard wrench.

In case of power outage, the MS can be UPS/battery operated.

Instructions
++++++++++++++

.. _Backup Mode gravity lowering picture :
.. figure:: img/backupGravityLowering.png
	:scale: 75 %
	:align: center
	
	Backup Mode gravity lowering

- Switch the MS to Backup Mode and 
- order lowering
- Progressively untighten the motor brake, using the :mechpart:`Brake Release Tool`, until the load starts to rotate the barrel. 
- Use the Brake Release Tool to regulate and maintain the speed below the specified safe speed. A :guilabel:`🔊 buzzer` will sound when the safe speed is close.

.. important::
	Indicative barrel speed: 2 - 5 rpm


MS assisted gravity lowering
=============================

- Apply moderate torque to the MS :mechpart:`worm shaft`. 
- Progressively release the motor brake, using the provided Brake Release Tool, until the load starts to rotate the barrel. 
- The barrel stops when no torque is applied to the MS :mechpart:`worm shaft`.

In this scenario, only moderate torque is to be applied to the MS :mechpart:`worm shaft` (approximately 1/250 of the barrel torque).

Using the following hardware:
- Handheld Recovery Tool for MS sizes above MS4,
- Handwheel / crank handle or standard ratchet handle for sizes MS0 – MS3

Instructions
+++++++++++++

.. _MS assisted gravity lowering picture: 
.. figure:: img/MSassistedGravityLowering.png
	:scale: 75 %
	:align: center
	
	MS assisted gravity lowering

- Apply moderate torque to the MS :mechpart:`worm shaft`, using the appropriate method,
- Progressively release the motor brake, using the provided Brake Release Tool, until the load starts to rotate the barrel (as long as moderate torque is applied to the MS shaft),
- Rotate the MS :mechpart:`worm shaft` to lower the load,
- Use the Brake Release Tool to maintain the torque to be applied to on the worm shaft inside the specified limits.

.. csv-table:: MS assisted gravity lowering max torques
   :file: tables/MSassistedGravityLowering.csv
   :header-rows: 1
   :class: tight-table

