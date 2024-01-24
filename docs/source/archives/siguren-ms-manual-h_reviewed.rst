==================================
SIGUREN technologies MS MANUAL h_reviewed.docx
==================================

.. note::
   | From docx:
   | `SIGUREN technologies MS MANUAL h_reviewed.docx <https://siguren.sharepoint.com/:w:/s/Processdesign/EeVnJNbzx9ZAk8VM70NnPoYBNSV8YuV39I3vRaFSFK8XnQ?e=obFj18>`_

|image1|

+-----------------+----------------------------------------------------+
| Document type   | Manual                                             |
+=================+====================================================+
| Title           | MotoSuiveur® manual                                |
+-----------------+----------------------------------------------------+
| Reference       | Draft hydraulic                                    |
+-----------------+----------------------------------------------------+
| Author          | Dimitar Georgiev                                   |
+-----------------+----------------------------------------------------+
| Approved by     | Yavor Pachov                                       |
+-----------------+----------------------------------------------------+
| Last revision   | 11/11/2020                                         |
| date            |                                                    |
+-----------------+----------------------------------------------------+

**Contents**
============

`1 Introduction <#introduction>`__ `3 <#introduction>`__

`2 Glossary (to be replaced for
Hydraulic) <#glossary-to-be-replaced-for-hydraulic>`__
`4 <#glossary-to-be-replaced-for-hydraulic>`__

`3 Connect MS to control cabinet <#connect-ms-to-control-cabinet>`__
`8 <#connect-ms-to-control-cabinet>`__

`4 Indication lamps and controls <#indication-lamps-and-controls>`__
`15 <#indication-lamps-and-controls>`__

`4.1 Hoist enabled. <#hoist-enabled.>`__ `16 <#hoist-enabled.>`__

`4.2 Fault <#fault>`__ `16 <#fault>`__

`4.3 Upward enable/Downward enable <#upward-enabledownward-enable>`__
`18 <#upward-enabledownward-enable>`__

`4.4 Backup/Recovery Off/On; Backup/Recovery
Down/Up <#backuprecovery-offon-backuprecovery-downup>`__
`19 <#backuprecovery-offon-backuprecovery-downup>`__

`4.5 Enable Override <#enable-override>`__ `19 <#enable-override>`__

`4.6 Lamp states <#lamp-states>`__ `19 <#lamp-states>`__

`5 MS operating modes <#ms-operating-modes>`__
`20 <#ms-operating-modes>`__

`5.1 MS controller internal check <#ms-controller-internal-check>`__
`20 <#ms-controller-internal-check>`__

`5.2 Self-test operation mode <#self-test-operation-mode>`__
`20 <#self-test-operation-mode>`__

`5.2.1 Electrical test <#electrical-test>`__ `22 <#electrical-test>`__

`5.2.2 Switch test <#switch-test>`__ `23 <#switch-test>`__

`5.2.3 Play test <#play-test>`__ `24 <#play-test>`__

`5.3 Following operation mode <#following-operation-mode>`__
`25 <#following-operation-mode>`__

`5.4 Backup/Recovery operation mode <#backuprecovery-operation-mode>`__
`28 <#backuprecovery-operation-mode>`__

`6 Troubleshoot and maintenance <#troubleshoot-and-maintenance>`__
`31 <#troubleshoot-and-maintenance>`__

`6.1 Troubleshooting via MS controller 7 – segment
display <#troubleshooting-via-ms-controller-7-segment-display>`__
`31 <#troubleshooting-via-ms-controller-7-segment-display>`__

`6.1.1 MS controller internal errors <#ms-controller-internal-errors>`__
`31 <#ms-controller-internal-errors>`__

`6.1.2 MS faults and warnings <#ms-faults-and-warnings>`__
`33 <#ms-faults-and-warnings>`__

`6.2 MSHMI <#mshmi>`__ `35 <#mshmi>`__

`6.3 Maintenance <#maintenance>`__ `36 <#maintenance>`__

`7 Appendix 1: Signal Lamps <#appendix-1-signal-lamps>`__
`39 <#appendix-1-signal-lamps>`__

**Revision history**

+---------+-----------------------------------------+----------+------+
| R       | Description                             | Revision | Au   |
| evision |                                         | date     | thor |
+=========+=========================================+==========+======+
| A       | Initial version                         | 16       | DG   |
|         |                                         | .04.2020 |      |
+---------+-----------------------------------------+----------+------+
| B       | Add information in all sections,        | 06       | DG   |
|         | “Operations state” is replaced with     | .08.2020 |      |
|         | “Operation mode”. „Electrical and       |          |      |
|         | automation” is replaced with “Manual”,  |          |      |
|         | add figures.                            |          |      |
+---------+-----------------------------------------+----------+------+
| C       | Information added about spare parts and | 10       | DG   |
|         | lubricants                              | .09.2020 |      |
+---------+-----------------------------------------+----------+------+
|         |                                         |          |      |
+---------+-----------------------------------------+----------+------+
|         |                                         |          |      |
+---------+-----------------------------------------+----------+------+

**
**

**Introduction**
================

Object of this manual is to present operation modes of MotoSuiveur®
(further called MS). Manual describes electrical part of MS, MS
operation modes, troubleshooting and maintenance. On figure 1 is
presented MS main block diagram.

|image2|

Hoist motor & brake

**Figure 1** MotoSuiveur® main block diagram

Glossary (to be replaced for Hydraulic)
=======================================

|image3|

+---+-------------------------------+----------------------------------+
| * | **Name**                      | **Description**                  |
| * |                               |                                  |
| № |                               |                                  |
| * |                               |                                  |
| * |                               |                                  |
+===+===============================+==================================+
| 1 | Recovery motor                | Recovery power transmission      |
|   |                               | train. To be used to safely      |
|   |                               | lower (or shortly raise) the     |
|   |                               | load in case of emergency.       |
+---+-------------------------------+----------------------------------+
| 2 | Recovery transmission         |                                  |
+---+-------------------------------+----------------------------------+
| 3 | Recovery engaged switch (RS)  | Recovery transmission train      |
|   |                               | engaged                          |
+---+-------------------------------+----------------------------------+
| 4 | Unscrewing enable switch      | Stops and prevent further hoist  |
|   | (USCRE)                       | movement in this direction       |
+---+-------------------------------+----------------------------------+
| 5 | Screwing enable switch (SCRE) |                                  |
+---+-------------------------------+----------------------------------+
| 6 | Worm switch cam               | Acts on SCRE and USCRE           |
+---+-------------------------------+----------------------------------+
| 7 | Recovery engagement nut with  | Engages the recovery             |
|   | switch cam                    | transmission to the worm and     |
|   |                               | acts on RS                       |
+---+-------------------------------+----------------------------------+
| 8 | MS motor                      | Allows normal operation          |
|   |                               | following                        |
+---+-------------------------------+----------------------------------+
| 9 | Friction worm wheel           | Acts as brake if the external    |
|   |                               | toothed ring is stopped by the   |
|   |                               | worm                             |
+---+-------------------------------+----------------------------------+
| 1 | Worm                          |                                  |
| 0 |                               |                                  |
+---+-------------------------------+----------------------------------+

**Figure 2** MS Unit components

|image4|

+----+----------------------------------+------------------------------+
| №  | Name                             | Description                  |
+====+==================================+==============================+
| 1  | Hoist enabled lamp               | MS authorizes hoist          |
|    |                                  | movements                    |
+----+----------------------------------+------------------------------+
| 2  | Fault lamp                       | MS is in fault               |
+----+----------------------------------+------------------------------+
| 3  | Upward enabled lamp              | MS authorizes hoist for      |
|    |                                  | upward movement              |
+----+----------------------------------+------------------------------+
| 4  | Backup/Recovery off/on selector  | Off - normal movement        |
|    | key                              | ON – Backup mode             |
|    |                                  | ON + Reset – Recovery mode   |
+----+----------------------------------+------------------------------+
| 5  | Backup/Recovery down/up key      | Up/Down command for Recovery |
|    |                                  | mode                         |
+----+----------------------------------+------------------------------+
| 6  | Enable override selector key     | Allow hoist movement when    |
|    |                                  | (1) is off                   |
+----+----------------------------------+------------------------------+
| 7  | Reset button                     | MS reset                     |
+----+----------------------------------+------------------------------+
| 8  | Healthy lamp                     | MS controller and MS motor   |
|    |                                  | healthy                      |
+----+----------------------------------+------------------------------+
| 9  | Downward enable lamp             | MS authorizes hoist for      |
|    |                                  | downward movement            |
+----+----------------------------------+------------------------------+
| 10 | Recovery mode lamp               | Active Backup/Recovery mode  |
+----+----------------------------------+------------------------------+
| 11 | Recovery engaged lamp            | Recovery is engaged          |
+----+----------------------------------+------------------------------+

**Figure 3** General view of MS control cabinet front door

|image5|

**Figure 4** General view of the sequence of MS operation modes

Mechanical characteristics of MS are presented on the nameplate of the
MS. The nameplate of the MS indicates the maximum rotating speed, the
corresponding braking torque and other characteristics (mass, oil
quantity, etc.). Example is shown on figure 5.

|image6|

**Figure 5** MS nameplate

Connect MS to control cabinet
=============================

After mechanical assembly of MS to hoist is done, electrical connection
must be made between MS and control cabinet. Figure 7 shows general view
of typical MS Unit electrical components that should be connected
according specific for the project electrical circuit diagram.

|image7|

+---+-------------------------------+---+-------------------------------+
| № | Description                   | № | Description                   |
+===+===============================+===+===============================+
| 1 | C8 – Recovery motor connector | 3 | C6 – Power connector          |
+---+-------------------------------+---+-------------------------------+
| 2 | TSW – Position switches       | 4 | C7 – Resolver connector       |
|   | terminal                      |   |                               |
+---+-------------------------------+---+-------------------------------+

**Figure 6** Electrical connections of MS Unit

Connectors C6 and C7 (figure 6 points 3 and 4) should be made according
following specification:

-  For C7 connector screened cable with 4 twisted pairs, 0.25 mm² should
   be used. Ground the shield of the feedback should be connected to GND
   – figure 7 a);

-  For C6 connector should be used screened cable, 4 core, 1.5 mm².
   Ground the shield of the feedback should be connected to GND – Figure
   7 b).

Figure 7 c) shows signal arrangement of connector on motor side for
motor type Kollmorgen.

Figure 7 d) shows general MS motor view.

|image8|

a) C7 connector

|image9|

b) C6 connector

+-------------+---+---+----------+------+--------------------------------+---+
| Connector   | № |   | Name     | Des  |                                |   |
|             |   |   |          | crip |                                |   |
|             |   |   |          | tion |                                |   |
+=============+===+===+==========+======+================================+===+
| |image10|   | 1 |   | NC       | Not  |                                |   |
|             |   |   |          | c    |                                |   |
|             |   |   |          | onne |                                |   |
|             |   |   |          | cted |                                |   |
+-------------+---+---+----------+------+--------------------------------+---+
|             | 2 |   | TEMP-    | M    |                                |   |
|             |   |   |          | otor |                                |   |
|             |   |   |          | tem  |                                |   |
|             |   |   |          | pera |                                |   |
|             |   |   |          | ture |                                |   |
|             |   |   |          | se   |                                |   |
|             |   |   |          | nsor |                                |   |
|             |   |   |          | Lo   |                                |   |
+-------------+---+---+----------+------+--------------------------------+---+
|             | 3 |   | COS-     | Co   |                                |   |
|             |   |   |          | sine |                                |   |
|             |   |   |          | Lo   |                                |   |
+-------------+---+---+----------+------+--------------------------------+---+
|             | 4 |   | SIN-     | Sine |                                |   |
|             |   |   |          | Lo   |                                |   |
+-------------+---+---+----------+------+--------------------------------+---+
|             | 5 |   | REF-     | R    |                                |   |
|             |   |   |          | efer |                                |   |
|             |   |   |          | ence |                                |   |
|             |   |   |          | Lo   |                                |   |
+-------------+---+---+----------+------+--------------------------------+---+
|             | 6 |   | TEMP+    | M    |                                |   |
|             |   |   |          | otor |                                |   |
|             |   |   |          | tem  |                                |   |
|             |   |   |          | pera |                                |   |
|             |   |   |          | ture |                                |   |
|             |   |   |          | se   |                                |   |
|             |   |   |          | nsor |                                |   |
|             |   |   |          | Hi   |                                |   |
+-------------+---+---+----------+------+--------------------------------+---+
|             | 7 |   | COS+     | Co   |                                |   |
|             |   |   |          | sine |                                |   |
|             |   |   |          | Hi   |                                |   |
+-------------+---+---+----------+------+--------------------------------+---+
|             | 8 |   | SIN+     | Sine |                                |   |
|             |   |   |          | Hi   |                                |   |
+-------------+---+---+----------+------+--------------------------------+---+
|             | 9 |   | REF+     | R    |                                |   |
|             |   |   |          | efer |                                |   |
|             |   |   |          | ence |                                |   |
|             |   |   |          | Hi   |                                |   |
+-------------+---+---+----------+------+--------------------------------+---+
|             | 1 |   | NC       | Not  |                                |   |
|             | 0 |   |          | c    |                                |   |
|             |   |   |          | onne |                                |   |
|             |   |   |          | cted |                                |   |
+-------------+---+---+----------+------+--------------------------------+---+
|             | 1 |   | NC       | Not  |                                |   |
|             | 1 |   |          | c    |                                |   |
|             |   |   |          | onne |                                |   |
|             |   |   |          | cted |                                |   |
+-------------+---+---+----------+------+--------------------------------+---+
| Connector   |   | № |          | Name | Description                    |   |
+-------------+---+---+----------+------+--------------------------------+---+
| |image11|   |   | 1 |          | V    | Motor phase V                  |   |
+-------------+---+---+----------+------+--------------------------------+---+
|             |   | 2 |          | PE   | Motor earth                    |   |
+-------------+---+---+----------+------+--------------------------------+---+
|             |   | 3 |          | W    | Motor phase W                  |   |
+-------------+---+---+----------+------+--------------------------------+---+
|             |   | 4 |          | U    | Motor phase U                  |   |
+-------------+---+---+----------+------+--------------------------------+---+
|             |   | A |          | NC   | Not connected                  |   |
|             |   | , |          |      |                                |   |
|             |   | B |          |      |                                |   |
|             |   | , |          |      |                                |   |
|             |   | C |          |      |                                |   |
|             |   | , |          |      |                                |   |
|             |   | D |          |      |                                |   |
+-------------+---+---+----------+------+--------------------------------+---+

c) Kollmorgen motor

|A picture containing table, sitting, kitchen, man Description
automatically generated|

d) General view of MS motor

**Figure 7** Connectors C6 and C7

+--------+-------------------------------------------------------------+
|        | **ATTENTION**                                               |
+========+=============================================================+
| |A     | **C6 and C7 must be connected according specification!      |
| close  | Wrong connection can cause motor damage!**                  |
| up of  |                                                             |
| a logo |                                                             |
| Descr  |                                                             |
| iption |                                                             |
| a      |                                                             |
| utomat |                                                             |
| ically |                                                             |
| gene   |                                                             |
| rated| |                                                             |
+--------+-------------------------------------------------------------+

[STRIKEOUT:Connector C8 (figure 6, point 1) is MS recovery motor
electrical connector. Recovery motor is DC motor controlled by Siguren
motor controller MSRM4514. Working voltage of motor is 48VDC therefore
is very important motor to be connected correct. Correct connection is
shown on figure 8].

|A picture containing indoor, sitting, kitchen, person Description
automatically generated|

**Figure 8** MS recovery motor C8 terminal connection

Position switches are used for allowing or prohibits hoist movement.
Position switches are using in active output signal via NC contact.
Signal from switches should be active in case when switches are not in
contact with worm and worm is in correct position. Figure 9 a)
combination of signals form position switches is shown. Position
switches are shown on figure 9 b).

+------------+---------------+--------------------+------------------+
| SCRE       | USCRE         | Upward enable      | Downward enable  |
+============+===============+====================+==================+
| |          | |Checkmark|   | |Checkmark|        | |Checkmark|      |
| Checkmark| |               |                    |                  |
+------------+---------------+--------------------+------------------+
| |          | |Close|       | |Checkmark|        | |Close|          |
| Checkmark| |               |                    |                  |
+------------+---------------+--------------------+------------------+
| |Close|    | |Checkmark|   | |Close|            | |Checkmark|      |
+------------+---------------+--------------------+------------------+
| |Close|    | |Close|       | N/A; MS controller |                  |
|            |               | fault; Switch      |                  |
|            |               | fault              |                  |
+------------+---------------+--------------------+------------------+
| |          | - Active      |                    |                  |
| Checkmark| | signal        |                    |                  |
+------------+---------------+--------------------+------------------+
| |Close|    | - Inactive    |                    |                  |
|            | signal        |                    |                  |
+------------+---------------+--------------------+------------------+

a) combination of signals from position switches

|image12|

**b)** position switches

**Figure 9** Position mechanical switches

Terminal block TSW (Terminal SWitches) is used for connection of worm
position proxy sensors/switches and control cabinet. Figure 10 shows
general view of TSW and description of terminals.

|image13|

+--------+-------------------------------------------------------------+
| №      | Description                                                 |
+========+=============================================================+
| 1      | +24VDC. Supply USCRE position switch                        |
+--------+-------------------------------------------------------------+
| 2      | Signal from USCRE position switch                           |
+--------+-------------------------------------------------------------+
| 3      | +24VDC. Supply SCRE position switch                         |
+--------+-------------------------------------------------------------+
| 4      | Signal from SCRE position switch                            |
+--------+-------------------------------------------------------------+
| 5      | +24VDC. Supply Recovery position switch                     |
+--------+-------------------------------------------------------------+
| 6      | Signal from position switch                                 |
+--------+-------------------------------------------------------------+

**Figure 10** Termina block TSW

Terminal blocks in control cabinet are for connection between MS and
control cabinet. Terminal blocks are described in Table 1.

**Table 1** Control cabinet terminals

+--------+-------------------------------------------------------------+
| Te     | Description                                                 |
| rminal |                                                             |
| block  |                                                             |
+========+=============================================================+
| T1     | Power supply                                                |
+--------+-------------------------------------------------------------+
| T2     | Digital inputs                                              |
+--------+-------------------------------------------------------------+
| T3     | MS sensors/switches                                         |
+--------+-------------------------------------------------------------+
| T4     | Digital outputs                                             |
+--------+-------------------------------------------------------------+
| T5     | Analogue I/O                                                |
+--------+-------------------------------------------------------------+
| T6     | MS motor power supply                                       |
+--------+-------------------------------------------------------------+
| T7     | MS motor resolver                                           |
+--------+-------------------------------------------------------------+
| T8     | Recovery motor power supply                                 |
+--------+-------------------------------------------------------------+
| T9     | Heater                                                      |
+--------+-------------------------------------------------------------+

Figure 11 shows general view of connection between MS and control
cabinet (MSCC). For more detail about connection, please review
electrical circuit diagram for the corresponding project.

|image14|\ **Figure 11** General view of connection between MS and MSCC

Indication lamps and controls
=============================

*Indication lamps* and *local* *controls* are shown on figure 3. They
are located on front door of control cabinet.

*Indication lamps* indicates:

- MS status – figure 3, items 2, 8;

- allowed movement direction of hoist – figure 3, items 1, 3, 9;

- recovery mode status – figure 3, items 10, 11.

*Local controls* are used for:

- reset of MS – figure 3, item 7;

- overrides MS enable signal (override ON signal) – figure 3, item 6;

- enable and control MS Backup/ Recovery mode – figure 3 items 4, 5, 10,
11.

Figure 12 shows schematically the control signals between hoist and MS.

|image15|

**Figure 12** Control signals between hoist and MS

+--------+-------------------------------------------------------------+
|        | **ATTENTION**                                               |
+========+=============================================================+
| |A     | **Local control commands can be duplicated with remotes!    |
| close  | Please, check electrical circuit diagram!**                 |
| up of  |                                                             |
| a logo |                                                             |
| Descr  |                                                             |
| iption |                                                             |
| a      |                                                             |
| utomat |                                                             |
| ically |                                                             |
| gene   |                                                             |
| rated| |                                                             |
+--------+-------------------------------------------------------------+

Hoist enabled.
--------------

*Hoist enabled* lamp indicate that the MS authorizes hoist movements.
(figure 5). *Hoist enabled* signal will on only in case if ON signal
from hoist is ON.

*Hoist enabled* signal will be ON when MS self-test pass successfully
and ON signal is available then **Hoist enabled** and **Healthy**
indicator lamps are on. The signals are indicating system ready (MS
ready).

Fault 
------

*Fault lamp* (figure 3, item 2) indicates three different types of
faults:

- MS controller internal errors, described in section 7.1;

- MS faults (further called flt_num), described in section 7.2;

- MS warnings (further called wrn_num), described in section 7.2;

MS controller internal errors are related to MS controller internal
hardware, firmware, and MS motor. This type of errors are with highest
priority. If MS controller internal fault appear further operation is
prohibited.

+--------+-------------------------------------------------------------+
|        | **INFORMATION**                                             |
+========+=============================================================+
| |A     | **Fault lamp indicator is on during MS self-test.**         |
| p      |                                                             |
| icture |                                                             |
| cont   |                                                             |
| aining |                                                             |
| d      |                                                             |
| rawing |                                                             |
| Descr  |                                                             |
| iption |                                                             |
| a      |                                                             |
| utomat |                                                             |
| ically |                                                             |
| gene   |                                                             |
| rated| |                                                             |
+--------+-------------------------------------------------------------+

+--------+-------------------------------------------------------------+
|        | **ATTENTION**                                               |
+========+=============================================================+
| |A     | **The system displays only last MS warning (wrn_num) or MS  |
| close  | fault (flt_nim) occurred.**                                 |
| up of  |                                                             |
| a logo |                                                             |
| Descr  |                                                             |
| iption |                                                             |
| a      |                                                             |
| utomat |                                                             |
| ically |                                                             |
| gene   |                                                             |
| rated| |                                                             |
+--------+-------------------------------------------------------------+

Faults and warnings are displayed on MS 7 – segment controller. The
display indicates all types of MS warnings/faults and MS controller
internal errors. Indication is a combination of letters and numbers. MS
controller internal faults are indicated with blinked combination of
|image16|, number and finish with symbol |image17|.

MS faults are displayed with combination of\ |image18| and number. MS
warnings are displayed with combination of |image19| and number.

On figure 13 a) is shown example for internal MS controller fault. On
figure 13 b) is shown example for MS warning.

|image20|

a) MS controller internal error E01

|image21|

b) MS warning number 10 (wrn_num = 10)

**Figure 13** Displaying messages on MS controller 7 – segment display

+--------+-------------------------------------------------------------+
|        | **INFORMATION**                                             |
+========+=============================================================+
| |A     | **After MS reset, all types of faults are cleared. Before   |
| p      | MS reset, fault should be resolved.**                       |
| icture |                                                             |
| cont   |                                                             |
| aining |                                                             |
| d      |                                                             |
| rawing |                                                             |
| Descr  |                                                             |
| iption |                                                             |
| a      |                                                             |
| utomat |                                                             |
| ically |                                                             |
| gene   |                                                             |
| rated| |                                                             |
+--------+-------------------------------------------------------------+

Upward enable/Downward enable 
------------------------------

*Upward enable/Downward enable* are indicators for authorized direction
of hoist movement. If one of the two directions is forbidden to move, it
is necessary to move the hoist in the opposite direction in order to
reset the system mechanically.

Movements *upward* and *downward* of hoist are correspond to *screwing*
and *unscrewing* movement of MS worm. Movement directions of worm are
corresponding to directions of clock. Direction screwing is clockwise,
unscrewing direction is anticlockwise, viewed from cam part of the screw
shaft as is shown on figure 14.

|image22|

1 – Screwing direction

2 – Unscrewing direction

**Figure 14** MS Worm rotating directions

+--------+-------------------------------------------------------------+
|        | **ATTENTION**                                               |
+========+=============================================================+
| |A     | **After MS reset or manual centering of the worm and MS     |
| close  | restart, no movement is performed or faults appears, please |
| up of  | contact SIGUREN technologies technologies on address                     |
| a logo | support@siguren.com**                                       |
| Descr  |                                                             |
| iption |                                                             |
| a      |                                                             |
| utomat |                                                             |
| ically |                                                             |
| gene   |                                                             |
| rated| |                                                             |
+--------+-------------------------------------------------------------+

Backup/Recovery Off/On; Backup/Recovery Down/Up
-----------------------------------------------

*Backup* function allows the load to be lowered down, by using minimal
functionalities when MS is in Following operation mode. *Backup*
function ignore all settings related with nominal following operation
mode and allows movement of the hoist with limited speed.

*Recovery* function is used when the main hoisting chain is faulty (for
example damaged brake of the hoist motor). Recovery system allows
lowering load safety to the ground.

Enable Override
---------------

*Enable override* can be used if it is necessary to override Hoist
enabled. This allows small movements for MS mechanically reset.

Lamp states
-----------

Combination of active (ON) and inactive (OFF) signal lams gives current
status of MS. In Appendix Table 1 signal combinations are presented and
described.

MS operating modes
==================

MS controller internal check
----------------------------

At power on (or restart) MS starts operating according figure 3.
According sequence of MS operation modes first operation is MS
controller internal check. Internal check is intended to hardware,
firmware of MS controller, MS motor and MS motor resolver.

In case of fault, fault is visualized on 7 – segment display as
described in 5.1.2. Further operations are prohibited. List with MS
controller internal faults are listed in section 7.1.

Self-test operation mode
------------------------

After MS controller internal check finishes, Self-test operation mode
(further called self – test) starts. On figure 15 a) symbols indicated
self-test steps on MS controller 7 – segment display are shown. On
figure 15 b) is shown sequence of self-test steps.

+------------+------------------+------------+-----------------------+
| **Symbol** | **Description**  | **Symbol** | **Description**       |
+============+==================+============+=======================+
| |image23|  | Homing           | |image24|  | Un-screwing enable    |
|            |                  |            | switch not made       |
+------------+------------------+------------+-----------------------+
| |image25|  | Waiting piston   | |image26|  | Screwing enable       |
|            | return           |            | switch not made       |
+------------+------------------+------------+-----------------------+
| |image27|  | Blocked          | |image28|  | Screwing enable       |
|            |                  |            | switch not centered   |
+------------+------------------+------------+-----------------------+
| |image29|  | Checking MS      | |image30|  | Un-screwing enable    |
|            | firmware (Soft)  |            | switch not centered   |
+------------+------------------+------------+-----------------------+
| |image31|  | Electrical test  | |image32|  | Damping plus\*        |
+------------+------------------+------------+-----------------------+
| |image33|  | Switch test      | |image34|  | Damping minus\*       |
+------------+------------------+------------+-----------------------+
| |image35|  | Damping\*        | |image36|  | Play minus            |
+------------+------------------+------------+-----------------------+
| |image37|  | Air\*            | |image38|  | Play plus             |
+------------+------------------+------------+-----------------------+
| |image39|  | Play             | |image40|  | Error / Fault         |
|            |                  | /|image41| |                       |
+------------+------------------+------------+-----------------------+
| \* -       |                  |            |                       |
| *steps are |                  |            |                       |
| applicable |                  |            |                       |
| only for   |                  |            |                       |
| hydraulic  |                  |            |                       |
| MS*        |                  |            |                       |
|            |                  |            |                       |
| a)         |                  |            |                       |
| Self-test  |                  |            |                       |
| steps      |                  |            |                       |
| symbols    |                  |            |                       |
+------------+------------------+------------+-----------------------+

|image42|

*Fields with \*, \*\* and \**\* are related with Table 2 in section 7.2*

b) sequence of self-test steps

**Figure 15** *Self – test* operation mode

Electrical test
~~~~~~~~~~~~~~~

On figure 16 steps of *Electrical test* are shown. Test checks for
active signals on inputs of the MS controller before self-test begin.

|image43|

**Figure 16** Steps of *Electrical test*

+--------+-------------------------------------------------------------+
|        | **ATTENTION**                                               |
+========+=============================================================+
| |A     | **In case of repetitive faults, please contact SIGUREN technologies      |
| close  | technologies on address support@siguren.com!**              |
| up of  |                                                             |
| a logo |                                                             |
| Descr  |                                                             |
| iption |                                                             |
| a      |                                                             |
| utomat |                                                             |
| ically |                                                             |
| gene   |                                                             |
| rated| |                                                             |
+--------+-------------------------------------------------------------+

Switch test
~~~~~~~~~~~

*Switch test* check connection between MS controller and SCRE/USCRE
switches (figure 2, items 4, 5), centered position and functionality of
switches. On figure 8 are shown steps of *Switch test*. In Table 2
located in appendix are shown steps for visual check of *Switch test*.
Visual check of *Switch test* is necessary only in case if repetitive
faults during the test appears.

|image44|

**Figure 17** Steps of *Switch test*

+-------+--------------------------------------------------------------+
|       | **INFORMATION**                                              |
+=======+==============================================================+
| |A    | **In case of repeatedly wrn_num occurs, please check:**      |
| pi    |                                                              |
| cture | -  **connection between MS control cabinet and SCRE/USCRE    |
| conta |    switches;**                                               |
| ining |                                                              |
| dr    | -  **functionality of SCRE and USCRE switches;**             |
| awing |                                                              |
| D     | -  **- signals on inputs of MS controller and operational    |
| escri |    relays RSESw and RUESw located in MS control cabinet;**   |
| ption |                                                              |
| aut   |                                                              |
| omati |                                                              |
| cally |                                                              |
| gener |                                                              |
| ated| |                                                              |
+-------+--------------------------------------------------------------+

Play test
~~~~~~~~~

*Play test* measures play between worm and worm wheel. On figure 18
steps of *Play test* are shown.

|image45|

**Figure 18** *Play test* steps

+--------+-------------------------------------------------------------+
|        | **ATTENTION**                                               |
+========+=============================================================+
| |A     | **In case of repetitive faults, please contact SIGUREN technologies      |
| close  | Technologies on address support@siguren.com!**              |
| up of  |                                                             |
| a logo |                                                             |
| Descr  |                                                             |
| iption |                                                             |
| a      |                                                             |
| utomat |                                                             |
| ically |                                                             |
| gene   |                                                             |
| rated| |                                                             |
+--------+-------------------------------------------------------------+

Following operation mode
------------------------

*Following operation mode* starts after successful passed of self –
test. The function of this operation mode is intended for follow
movements of the hoist and to monitor for exceeding the rated speed
(nominal speed) with defined positive tolerance. The speed, which is
considered high is called *Overspeed*. By design MS will not allow
*Overspeed*. Typically O\ *verspeed* is equal to:

Overspeed = Nominal speed + 10% (1)

Figure 19 is presents main principle of *Following operation mode* and
overspeed detection. On figure 20 steps of following operation mode is
presented. On figure 21 are shown symbols displayed on 7 – segment
display during following operation mode.

|image46|

+------------------------+---------------------------------------------+
| 1 – Acceleration       | 4 – Exceeding nominal speed                 |
+========================+=============================================+
| 2 – Following          | 5 – Overspeed detection                     |
+------------------------+---------------------------------------------+
| 3 – Deceleration       | 6 – Overspeed detected. MS is breaking      |
+------------------------+---------------------------------------------+

**Figure 19** Main principle of following operation mode and overspeed
detection

|image47|

**Figure 20** Principle of Following operation mode

+-----------------------+----------------------------------------------+
| **At rest**           |                                              |
+=======================+==============================================+
| Symbol                | Description                                  |
+-----------------------+----------------------------------------------+
| |image48|             | Unscrewing enable switch sctivated           |
+-----------------------+----------------------------------------------+
| |image49|             | Screwing enable switch activated             |
+-----------------------+----------------------------------------------+
| |image50|             | Both commands                                |
|                       |                                              |
|                       | activated                                    |
+-----------------------+----------------------------------------------+
| |image51|             | Maintenance “A”                              |
+-----------------------+----------------------------------------------+
| |image52|             | Maintenance “B”                              |
+-----------------------+----------------------------------------------+
| |image53|             | Maintenance “C”                              |
+-----------------------+----------------------------------------------+
| |image54|             | Maintenance “D”                              |
+-----------------------+----------------------------------------------+
| |image55|             | Rest (normal)                                |
+-----------------------+----------------------------------------------+

+-----------+-----------------------+----------------------------------+
| **During  |                       |                                  |
| m         |                       |                                  |
| ovement** |                       |                                  |
+===========+=======================+==================================+
| Symbol    | Description           | Explanation                      |
+-----------+-----------------------+----------------------------------+
| |image56| | Centering             | The worm is positioned to the    |
|           |                       | center of its backlash, to       |
|           |                       | prepare for the next             |
|           |                       |                                  |
|           |                       | movement                         |
+-----------+-----------------------+----------------------------------+
| |image57| | Screwing Tackling     | Upward movement start            |
+-----------+-----------------------+----------------------------------+
| |image58| | Unscrewing            | Downward movement start          |
|           |                       |                                  |
|           | Tackling              |                                  |
+-----------+-----------------------+----------------------------------+
| |image59| | Screwing              | Upward movement following        |
|           |                       |                                  |
|           | Following             |                                  |
+-----------+-----------------------+----------------------------------+
| |image60| | Unscrewing            | Downward movement following      |
|           |                       |                                  |
|           | Following             |                                  |
+-----------+-----------------------+----------------------------------+
| |image61| | Near Overspeed        | Starts blinking the more and     |
|           |                       | more rapidly as the speed        |
|           |                       | approaches the                   |
|           |                       |                                  |
|           |                       | 'overspeed' threshold setting    |
+-----------+-----------------------+----------------------------------+
| |image62| | Near Underspeed       | Starts blinking the more and     |
|           |                       | more rapidly as the speed        |
|           |                       | approaches the                   |
|           |                       |                                  |
|           |                       | 'underspeed' threshold setting   |
+-----------+-----------------------+----------------------------------+
| |image63| | Fault                 | Fault detected                   |
+-----------+-----------------------+----------------------------------+

**Figure 21** Symbols displayed on 7 – segment display on MS controller

Backup/Recovery operation mode
------------------------------

*Backup/Recovery* operation mode functions are intended to unusual
situations during MS operating. Controls and indicators of this
functions are located on control panel front door – figure 3, items 4,
5, 10, 11.

On figure 23 is shown principle of Backup/Recovery operation mode.
Backup/Recovery decision figures located in figures 15 and 20 with
dotted outline, represent the places where request for these operation
modes are checked.

Switching on Recovery/backup mode is performed through Backup/Recovery
OFF/ON key – figure 2, item 4. After switching Backup/Recovery mode on,
*Backup mode* start operating. On 7 – segment display indication for
backup mode is displayed |image64| and *Recovery mode* lamp is on.
Backup function ignore all settings related with following operation and
allows movement of hoist with hoist limited speed.

In Backup operating mode, control is performed trough commands for
lifting and lowering of the hoist. In case of hoist control chain is
damaged, control can be performed manually directly on control terminals
located in MS control cabinet via wire bridge. Example is shown on
figure 22. In *Backup mode* no ON signal is required to perform movement
of MS.

|image65|

**Figure 22** Example for manual operation in backup mode

|image66|

**Figure 23** Principle of Backup/Recovery operation

Recovery mode is second part of *Backup/Recovery operation*. This mode
start operates the way is shown on figure 23. After reset, MS checks for
active *Backup/Recovery mode* request (*Backup/Recovery operational key*
is ON). If request is active 7 – segment display shows symbol for
Recovery mode |image67| and engagement start. Engagement function is
used to engage recovery mechanism to the worm via recovery nut – figure
1, item 7.

Completion of engagement is indicated by Recovery engaged indication
lamp (figure 3, point 10). If lamp is off after first engagement, reset
is needed. Reset will activate engagement again.

Controlling of Recovery is with 3 – position key *Backup/Recovery
Down/Up* located on front door of control cabinet – figure 3 item 5.
Also Recovery can be controller remotely if that is provided by
electrical circuit diagram.

After engagement is complete and Recovery engagement lamp is on, brake
of main hoist motor should be released. Otherwise motor brake will
prohibit movements. Brake should remain open until recovery operation
done.

For disengagement, load should be on safe place, main hoist motor brake
should be closed. Command for lowering should be given to MS until both
lamps for Upward enable and Downward enable becomes on.

+--------+-------------------------------------------------------------+
|        | **ATTENTION**                                               |
+========+=============================================================+
| |A     | **Recovery function is mainly designed for safety lowering  |
| close  | of the load. Function allows very short lifting of the load |
| up of  | only in case if it is absolutely necessary!**               |
| a logo |                                                             |
| Descr  |                                                             |
| iption |                                                             |
| a      |                                                             |
| utomat |                                                             |
| ically |                                                             |
| gene   |                                                             |
| rated| |                                                             |
+--------+-------------------------------------------------------------+

+--------+-------------------------------------------------------------+
|        | **ATTENTION**                                               |
+========+=============================================================+
| |A     | **Before activating Backup/Recovery operation mode from     |
| close  | local controls (figure 3, item 4), please make sure that    |
| up of  | operation mode is not activated remotely. The verification  |
| a logo | consists of the following steps:**                          |
| Descr  |                                                             |
| iption | -  **Recovery mode lamp and Recovery engaged lamp are       |
| a      |    off;**                                                   |
| utomat |                                                             |
| ically | -  **Backup/Recovery control key is in position “0”         |
| gene   |    (OFF);**                                                 |
| rated| |                                                             |
|        | -  **On 7 – segment display symbols** |image68| **or**      |
|        |    |image69| **are not displayed.**                         |
+--------+-------------------------------------------------------------+

Troubleshoot and maintenance
============================

Troubleshooting of MS can be done by few ways:

- via signal lamps located on front door – Appendix 1;

- via MS controller 7 – segment display – section 6.1;

- via touchscreen HMI (MSHMI) – section 6.2.

Troubleshooting via MS controller 7 – segment display
-----------------------------------------------------

MS controller internal errors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------+-----------------------------+-----------------------------+
| **M      | **Description**             | **Possible cases**          |
| essage** |                             |                             |
+==========+=============================+=============================+
| E01      | DC bus overvoltage: An      | This fault may be due to    |
|          | overvoltage has been        | overvoltage on the network  |
|          | detected on the internal DC | or due to overloaded        |
|          | bus.                        | ballast resistor.           |
+----------+-----------------------------+-----------------------------+
| E02      | Undervoltage DC Bus: The    | This fault is managed while |
|          | internal DC bus has dropped | the drive is enabled.       |
|          | below the configured        |                             |
|          | minimum voltage.            |                             |
+----------+-----------------------------+-----------------------------+
| E03      | I²t motor: Overload on the  | Mechanical hard point, bad  |
|          | motor.                      | power wiring, motor         |
|          |                             | feedback problem, poorly    |
|          |                             | controlled brake.           |
+----------+-----------------------------+-----------------------------+
| E04      | Overcurrent: A current      | The drive must be powered   |
|          | greater than the maximum    | 24VDC for 15 min before it  |
|          | measurable current has been | can be unlocked.            |
|          | detected on at least one of |                             |
|          | the motor phases.           |                             |
+----------+-----------------------------+-----------------------------+
| E05      | Short circuit: A            | The drive must be powered   |
|          | short-circuit between       | 24VDC for 15 min before it  |
|          | phases or the earthing of a | can be unlocked.            |
|          | motor phase has been        |                             |
|          | detected.                   |                             |
+----------+-----------------------------+-----------------------------+
| E06      | IGBT temperature: maximum   | It is impossible to         |
|          | temperature reached in the  | acknowledge the fault until |
|          | drive.                      | the temperature has gone    |
|          |                             | back down.                  |
+----------+-----------------------------+-----------------------------+
| E07      | Motor temperature: maximum  | It is impossible to         |
|          | temperature reached in the  | acknowledge the fault until |
|          | motor.                      | the temperature has gone    |
|          |                             | back down.                  |
+----------+-----------------------------+-----------------------------+
| E08      | Resolver fault: Defective   | Check resolver connection   |
|          | resolver signals.           | between motor and control   |
|          |                             | cabinet and resolver        |
|          |                             | connector.                  |
+----------+-----------------------------+-----------------------------+
| E09      | Coil temperature: maximum   | It is impossible to         |
|          | temperature reached in the  | acknowledge the fault until |
|          | self.                       | the temperature has gone    |
|          |                             | back down.                  |
+----------+-----------------------------+-----------------------------+
| E16      | Resolver saturation: Sin /  | Check resolver connection   |
|          | Cos resolver signals        | between motor and control   |
|          | received too high.          | cabinet and resolver        |
|          |                             | connector.                  |
+----------+-----------------------------+-----------------------------+
| E17      | 24V auxiliary supply error. | This fault is triggered if  |
|          |                             | the 24V auxiliary power     |
|          |                             | supply is noisy or has a    |
|          |                             | voltage dip (<15V). Check   |
|          |                             | the 24V supply.             |
+----------+-----------------------------+-----------------------------+

MS faults and warnings
~~~~~~~~~~~~~~~~~~~~~~

+----------+-----------------------------+----------------------------+
| **M      | **Description**             | **Possible cases**         |
| essage** |                             |                            |
+==========+=============================+============================+
| E02      | Screwing command during     | Check for pressed/held     |
|          | self-test \*                | down button for hoist      |
|          |                             | lifting command.           |
+----------+-----------------------------+----------------------------+
| E03      | Unscrewing command during   | Check for pressed/held     |
|          | self-test \*                | down button for hoist      |
|          |                             | lowering command           |
+----------+-----------------------------+----------------------------+
| E04      | Both commands during        | Check for pressed/held     |
|          | self-test \*                | down button for hoist      |
|          |                             | lifting and lowering       |
|          |                             | command                    |
+----------+-----------------------------+----------------------------+
| E05      | ON signal missing during    | ON signal from hoist       |
|          | self-test \*                | missing (figure 12). Check |
|          |                             | electrical connection      |
|          |                             | between hoist control      |
|          |                             | cabinet and MS hoist       |
|          |                             | cabinet. ON signal from    |
|          |                             | hoist to MS is available   |
|          |                             | Check hoist control        |
+----------+-----------------------------+----------------------------+
| E10      | Blocked worm                | Worm is locked to recovery |
|          |                             | mechanism. Worm is stuck.  |
|          |                             | Mechanical reset is        |
|          |                             | needed. In case of         |
|          |                             | Downward enable off after  |
|          |                             | recovery operation, moving |
|          |                             | I opposite side from hoist |
|          |                             | is needed. Moving should   |
|          |                             | continue until lamps       |
|          |                             | indicators for upward and  |
|          |                             | downward are on. After     |
|          |                             | manual reentering, MS      |
|          |                             | reset is necessary.        |
+----------+-----------------------------+----------------------------+
| E11      | Unscrewing enable switch    | Switch USCRE is not in     |
|          | not centered \*\*           | correct position. Visual   |
|          |                             | check is and centering is  |
|          |                             | needed                     |
+----------+-----------------------------+----------------------------+
| E12      | Screwing enable switch not  | Switch SCRE is not in      |
|          | centered \*\*               | correct position. Visual   |
|          |                             | check is and centering is  |
|          |                             | needed                     |
+----------+-----------------------------+----------------------------+
| E13      | Unscrewing enable switch    | USCRE switch is not        |
|          | not made \*\*               | reached from worm during   |
|          |                             | Switch test. Visual check  |
|          |                             | is needed.                 |
+----------+-----------------------------+----------------------------+
| E14      | Screwing enable switch not  | SCRE switch is not reached |
|          | made \*\*                   | from worm during Switch    |
|          |                             | test. Visual check is      |
|          |                             | needed.                    |
+----------+-----------------------------+----------------------------+
| E28      | Incorrect MS firmware       | Please, contact Siguren    |
|          | version                     | technologies               |
+----------+-----------------------------+----------------------------+
| F15      | Worm backlash too big       | Worm play is greater than  |
|          | detected (Play too big)     | defined.                   |
|          | \**\*                       |                            |
+----------+-----------------------------+----------------------------+
| F17      | Worm backlash too small     | Worm play is smaller than  |
|          | detected (Play too small)   | defined.                   |
|          | \**\*                       |                            |
+----------+-----------------------------+----------------------------+
| F20      | Air detected                | Presence of air into the   |
|          |                             | oil inside the damping     |
|          |                             | chamber                    |
+----------+-----------------------------+----------------------------+
| F22      | Damping too soft            | Damping nozzles too open   |
+----------+-----------------------------+----------------------------+
| F23      | Damping too hard            | Damping nozzles too closed |
+----------+-----------------------------+----------------------------+
| F33      | Unscrewing Overspeed.       | Hoist speed exceeds        |
|          | Overspeed during lowering   | maximum defined speed      |
|          |                             | during lowering            |
+----------+-----------------------------+----------------------------+
| F34      | Screwing Overspeed.         | Hoist speed exceeds        |
|          | Overspeed during lifting    | maximum defined speed      |
|          |                             | during lifting             |
+----------+-----------------------------+----------------------------+

+--------+-------------------------------------------------------------+
|        | **ATTENTION**                                               |
+========+=============================================================+
| |A     | **In case of repetitive faults, please contact SIGUREN technologies      |
| close  | Technologies on address support@siguren.com!**              |
| up of  |                                                             |
| a logo |                                                             |
| Descr  |                                                             |
| iption |                                                             |
| a      |                                                             |
| utomat |                                                             |
| ically |                                                             |
| gene   |                                                             |
| rated| |                                                             |
+--------+-------------------------------------------------------------+

MSHMI
-----

The MSHMI is a Schneider Magelis HMI STU 655/855 color graphic
touchscreen terminal programmed with the MSHMI firmware by Siguren
technologies. MSHMI communicates with MS controller via MODBUS RTU
protocol – figure 24.

|image70|

**Figure 24** MSHMI

Advantages if using MSHMI to operating with MS® are:

- Display MotoSuiveur® status information in the form of messages, event
listings, graphics and numerical values;

- Change the MotoSuiveur® configuration. Configuration is a secure
access code at different levels;

- Change operating mode of MotoSuiveur®;

- Display maintenance information of MotoSuiveur®.

+--------+-------------------------------------------------------------+
|        | **INFORMATION**                                             |
+========+=============================================================+
| |A     | **MSHMI is not part from standard MS equipment and can be   |
| p      | ordered additionally.**                                     |
| icture |                                                             |
| cont   |                                                             |
| aining |                                                             |
| d      |                                                             |
| rawing |                                                             |
| Descr  |                                                             |
| iption |                                                             |
| a      |                                                             |
| utomat |                                                             |
| ically |                                                             |
| gene   |                                                             |
| rated| |                                                             |
+--------+-------------------------------------------------------------+

Maintenance
-----------

Due to inherent dangers in the maintenance and testing of electrical
equipment, special attention should be paid to safety, not only to the
personnel working the immediate area but also to equipment under test,
maintenance and repair.

All personnel operating in the relevant area should observe these
procedures and pay due regard to safety Local Safety Rules and
Regulations.

It is advisable that at least two fully trained engineers be present at
all times when the equipment is being tested, maintained or serviced.

All equipment under electrical test should have WARNING NOTICES
displayed saying that equipment tests are in progress. Any ancillary
equipment, for example, test equipment and instruments, should be safe
and prominent notices around the equipment should advertise any danger,
which may exist. Any notices displayed in pursuing these procedures
should be removed as soon as they are no longer applicable, to emphasize
the special significance of their presence.

If it becomes necessary to carry out maintenance, testing or setting up
to work on the equipment requiring access by opening doors, removing
covers etc., then safety hazards may arise. Then risk assessments should
be carried out and safe-working practices followed.

A duty holder should be responsible for ensuring that the equipment is
made accessible only to authorized personnel to carry out specific tasks
after receiving permission.

The user should ensure that maintenance setting up and authorized and
competent persons only carry out testing of the equipment. The following
basic rules should be adhered to:

1. Before commencing maintenance works, the supply to the equipment must
be isolated, locked off and the appropriate safety documents issued.

2. Comply with safe working conditions.

3. Do not work on the equipment when it is energized.

4. Ensure that all persons working on the equipment are familiar with
instructions and information provided in this manual.

5. Providing that the equipment is functioning correctly and all
personnel responsible for operating it are complying with the conditions
specified, the electrical equipment may be deemed to be “properly used”
and should be safe and free from health hazards.

The reliability of the Motosuiveur® will depend if the maintenance
procedure is strictly adhered to. Maintenance operations are to be done
based either on the Maintenance type displayed on MS controller 7 –
segment display or on a time basis wherever the smallest value applies.

Maintenance Intervals: - A= Weekly, B= Monthly, C= 3 Monthly, D= 6
Monthly E= Annually, F= 2 Years, G=5 Years, H=10 Years

**Table 2** MS maintenance intervals

+---------------------------+---+---+---+---+---+---+---+---+---------+--------+
| **MS Unit**     | A | B | C | D | E | F | G | H | Worm    | Cont   |
|                           |   |   |   |   |   |   |   |   | R       | roller |
|                           |   |   |   |   |   |   |   |   | otation | 7-S    |
|                           |   |   |   |   |   |   |   |   | Count   | egment |
|                           |   |   |   |   |   |   |   |   | (HMI)   | D      |
|                           |   |   |   |   |   |   |   |   |         | isplay |
+===========================+===+===+===+===+===+===+===+===+=========+========+
| MS fixation to barrel and |   |   |   |   | ● |   |   |   | 75E\ :  | |ima   |
| to hoist structure        |   |   |   |   |   |   |   |   | sup:`6` | ge71|; |
|                           |   |   |   |   |   |   |   |   |         | |ima   |
|                           |   |   |   |   |   |   |   |   |         | ge72|; |
|                           |   |   |   |   |   |   |   |   |         | |ima   |
|                           |   |   |   |   |   |   |   |   |         | ge73|; |
|                           |   |   |   |   |   |   |   |   |         | |im    |
|                           |   |   |   |   |   |   |   |   |         | age74| |
+---------------------------+---+---+---+---+---+---+---+---+---------+--------+
|                           | V |   |   |   |   |   |   |   |         |        |
|                           | i |   |   |   |   |   |   |   |         |        |
|                           | s |   |   |   |   |   |   |   |         |        |
|                           | u |   |   |   |   |   |   |   |         |        |
|                           | a |   |   |   |   |   |   |   |         |        |
|                           | l |   |   |   |   |   |   |   |         |        |
|                           | i |   |   |   |   |   |   |   |         |        |
|                           | n |   |   |   |   |   |   |   |         |        |
|                           | s |   |   |   |   |   |   |   |         |        |
|                           | p |   |   |   |   |   |   |   |         |        |
|                           | e |   |   |   |   |   |   |   |         |        |
|                           | c |   |   |   |   |   |   |   |         |        |
|                           | t |   |   |   |   |   |   |   |         |        |
|                           | i |   |   |   |   |   |   |   |         |        |
|                           | o |   |   |   |   |   |   |   |         |        |
|                           | n |   |   |   |   |   |   |   |         |        |
|                           | . |   |   |   |   |   |   |   |         |        |
|                           | C |   |   |   |   |   |   |   |         |        |
|                           | h |   |   |   |   |   |   |   |         |        |
|                           | e |   |   |   |   |   |   |   |         |        |
|                           | c |   |   |   |   |   |   |   |         |        |
|                           | k |   |   |   |   |   |   |   |         |        |
|                           | F |   |   |   |   |   |   |   |         |        |
|                           | a |   |   |   |   |   |   |   |         |        |
|                           | s |   |   |   |   |   |   |   |         |        |
|                           | t |   |   |   |   |   |   |   |         |        |
|                           | e |   |   |   |   |   |   |   |         |        |
|                           | n |   |   |   |   |   |   |   |         |        |
|                           | e |   |   |   |   |   |   |   |         |        |
|                           | r |   |   |   |   |   |   |   |         |        |
|                           | s |   |   |   |   |   |   |   |         |        |
|                           | , |   |   |   |   |   |   |   |         |        |
|                           | e |   |   |   |   |   |   |   |         |        |
|                           | t |   |   |   |   |   |   |   |         |        |
|                           | c |   |   |   |   |   |   |   |         |        |
|                           | . |   |   |   |   |   |   |   |         |        |
+---------------------------+---+---+---+---+---+---+---+---+---------+--------+
| MS Motor Transmission     |   |   |   |   | ● |   |   |   | 75E\ :  | |ima   |
| Grease:                   |   |   |   |   |   |   |   |   | sup:`6` | ge75|; |
|                           |   |   |   |   |   |   |   |   |         | |ima   |
| REPSOL NLGI 00            |   |   |   |   |   |   |   |   |         | ge76|; |
|                           |   |   |   |   |   |   |   |   |         | |ima   |
|                           |   |   |   |   |   |   |   |   |         | ge77|; |
|                           |   |   |   |   |   |   |   |   |         | |im    |
|                           |   |   |   |   |   |   |   |   |         | age78| |
+---------------------------+---+---+---+---+---+---+---+---+---------+--------+
|                           | A |   |   |   |   |   |   |   |         |        |
|                           | d |   |   |   |   |   |   |   |         |        |
|                           | d |   |   |   |   |   |   |   |         |        |
|                           | o |   |   |   |   |   |   |   |         |        |
|                           | r |   |   |   |   |   |   |   |         |        |
|                           | R |   |   |   |   |   |   |   |         |        |
|                           | e |   |   |   |   |   |   |   |         |        |
|                           | p |   |   |   |   |   |   |   |         |        |
|                           | l |   |   |   |   |   |   |   |         |        |
|                           | a |   |   |   |   |   |   |   |         |        |
|                           | c |   |   |   |   |   |   |   |         |        |
|                           | e |   |   |   |   |   |   |   |         |        |
|                           | i |   |   |   |   |   |   |   |         |        |
|                           | f |   |   |   |   |   |   |   |         |        |
|                           | n |   |   |   |   |   |   |   |         |        |
|                           | e |   |   |   |   |   |   |   |         |        |
|                           | c |   |   |   |   |   |   |   |         |        |
|                           | e |   |   |   |   |   |   |   |         |        |
|                           | s |   |   |   |   |   |   |   |         |        |
|                           | s |   |   |   |   |   |   |   |         |        |
|                           | a |   |   |   |   |   |   |   |         |        |
|                           | r |   |   |   |   |   |   |   |         |        |
|                           | y |   |   |   |   |   |   |   |         |        |
+---------------------------+---+---+---+---+---+---+---+---+---------+--------+
| Oil Level                 |   |   |   |   | ● |   |   |   | 75E\ :  | |ima   |
|                           |   |   |   |   |   |   |   |   | sup:`6` | ge79|; |
| SIGUREN technologies MS Oil SQ32       |   |   |   |   |   |   |   |   |         | |ima   |
|                           |   |   |   |   |   |   |   |   |         | ge80|; |
|                           |   |   |   |   |   |   |   |   |         | |ima   |
|                           |   |   |   |   |   |   |   |   |         | ge81|; |
|                           |   |   |   |   |   |   |   |   |         | |im    |
|                           |   |   |   |   |   |   |   |   |         | age82| |
+---------------------------+---+---+---+---+---+---+---+---+---------+--------+
|                           | V |   |   |   |   |   |   |   |         |        |
|                           | i |   |   |   |   |   |   |   |         |        |
|                           | s |   |   |   |   |   |   |   |         |        |
|                           | u |   |   |   |   |   |   |   |         |        |
|                           | a |   |   |   |   |   |   |   |         |        |
|                           | l |   |   |   |   |   |   |   |         |        |
|                           | i |   |   |   |   |   |   |   |         |        |
|                           | n |   |   |   |   |   |   |   |         |        |
|                           | s |   |   |   |   |   |   |   |         |        |
|                           | p |   |   |   |   |   |   |   |         |        |
|                           | e |   |   |   |   |   |   |   |         |        |
|                           | c |   |   |   |   |   |   |   |         |        |
|                           | t |   |   |   |   |   |   |   |         |        |
|                           | i |   |   |   |   |   |   |   |         |        |
|                           | o |   |   |   |   |   |   |   |         |        |
|                           | n |   |   |   |   |   |   |   |         |        |
|                           | . |   |   |   |   |   |   |   |         |        |
|                           | A |   |   |   |   |   |   |   |         |        |
|                           | d |   |   |   |   |   |   |   |         |        |
|                           | d |   |   |   |   |   |   |   |         |        |
|                           | i |   |   |   |   |   |   |   |         |        |
|                           | f |   |   |   |   |   |   |   |         |        |
|                           | n |   |   |   |   |   |   |   |         |        |
|                           | e |   |   |   |   |   |   |   |         |        |
|                           | c |   |   |   |   |   |   |   |         |        |
|                           | e |   |   |   |   |   |   |   |         |        |
|                           | s |   |   |   |   |   |   |   |         |        |
|                           | s |   |   |   |   |   |   |   |         |        |
|                           | a |   |   |   |   |   |   |   |         |        |
|                           | r |   |   |   |   |   |   |   |         |        |
|                           | y |   |   |   |   |   |   |   |         |        |
|                           | . |   |   |   |   |   |   |   |         |        |
+---------------------------+---+---+---+---+---+---+---+---+---------+--------+
| Worm Outer Piston Assy    |   |   |   |   |   |   | ● |   | 150E\ : | |ima   |
|                           |   |   |   |   |   |   |   |   | sup:`6` | ge83|; |
| Part No: MSL-01-P04       |   |   |   |   |   |   |   |   |         | |ima   |
|                           |   |   |   |   |   |   |   |   |         | ge84|; |
|                           |   |   |   |   |   |   |   |   |         | |im    |
|                           |   |   |   |   |   |   |   |   |         | age85| |
+---------------------------+---+---+---+---+---+---+---+---+---------+--------+
|                           | R |   |   |   |   |   |   |   |         |        |
|                           | e |   |   |   |   |   |   |   |         |        |
|                           | p |   |   |   |   |   |   |   |         |        |
|                           | l |   |   |   |   |   |   |   |         |        |
|                           | a |   |   |   |   |   |   |   |         |        |
|                           | c |   |   |   |   |   |   |   |         |        |
|                           | e |   |   |   |   |   |   |   |         |        |
|                           | \ |   |   |   |   |   |   |   |         |        |
|                           | * |   |   |   |   |   |   |   |         |        |
+---------------------------+---+---+---+---+---+---+---+---+---------+--------+
| MS Oil                    |   |   |   |   |   |   |   | ● | 450E\ : | |ima   |
|                           |   |   |   |   |   |   |   |   | sup:`6` | ge86|; |
| SIGUREN technologies MS Oil SQ32       |   |   |   |   |   |   |   |   |         | |im    |
|                           |   |   |   |   |   |   |   |   |         | age87| |
+---------------------------+---+---+---+---+---+---+---+---+---------+--------+
|                           | R |   |   |   |   |   |   |   |         |        |
|                           | e |   |   |   |   |   |   |   |         |        |
|                           | p |   |   |   |   |   |   |   |         |        |
|                           | l |   |   |   |   |   |   |   |         |        |
|                           | a |   |   |   |   |   |   |   |         |        |
|                           | c |   |   |   |   |   |   |   |         |        |
|                           | e |   |   |   |   |   |   |   |         |        |
|                           | . |   |   |   |   |   |   |   |         |        |
|                           | C |   |   |   |   |   |   |   |         |        |
|                           | l |   |   |   |   |   |   |   |         |        |
|                           | e |   |   |   |   |   |   |   |         |        |
|                           | a |   |   |   |   |   |   |   |         |        |
|                           | n |   |   |   |   |   |   |   |         |        |
|                           | m |   |   |   |   |   |   |   |         |        |
|                           | a |   |   |   |   |   |   |   |         |        |
|                           | g |   |   |   |   |   |   |   |         |        |
|                           | n |   |   |   |   |   |   |   |         |        |
|                           | e |   |   |   |   |   |   |   |         |        |
|                           | t |   |   |   |   |   |   |   |         |        |
|                           | p |   |   |   |   |   |   |   |         |        |
|                           | l |   |   |   |   |   |   |   |         |        |
|                           | u |   |   |   |   |   |   |   |         |        |
|                           | g |   |   |   |   |   |   |   |         |        |
|                           | s |   |   |   |   |   |   |   |         |        |
|                           | . |   |   |   |   |   |   |   |         |        |
+---------------------------+---+---+---+---+---+---+---+---+---------+--------+
| Wheel Lip Seal NBR 70 Sh  |   |   |   |   |   |   |   | ● | 900E\ : | |im    |
| A                         |   |   |   |   |   |   |   |   | sup:`6` | age88| |
|                           |   |   |   |   |   |   |   |   |         |        |
| Reference: 100x120x7.5    |   |   |   |   |   |   |   |   |         |        |
+---------------------------+---+---+---+---+---+---+---+---+---------+--------+
|                           | R |   |   |   |   |   |   |   |         |        |
|                           | e |   |   |   |   |   |   |   |         |        |
|                           | p |   |   |   |   |   |   |   |         |        |
|                           | l |   |   |   |   |   |   |   |         |        |
|                           | a |   |   |   |   |   |   |   |         |        |
|                           | c |   |   |   |   |   |   |   |         |        |
|                           | e |   |   |   |   |   |   |   |         |        |
|                           | \ |   |   |   |   |   |   |   |         |        |
|                           | * |   |   |   |   |   |   |   |         |        |
+---------------------------+---+---+---+---+---+---+---+---+---------+--------+
| O-Rings NBR 70 Sh A       |   |   |   |   |   |   |   | ● | 900E\ : | D      |
|                           |   |   |   |   |   |   |   |   | sup:`6` |        |
| References: 200x2; 53x4   |   |   |   |   |   |   |   |   |         |        |
+---------------------------+---+---+---+---+---+---+---+---+---------+--------+
|                           | R |   |   |   |   |   |   |   |         |        |
|                           | e |   |   |   |   |   |   |   |         |        |
|                           | p |   |   |   |   |   |   |   |         |        |
|                           | l |   |   |   |   |   |   |   |         |        |
|                           | a |   |   |   |   |   |   |   |         |        |
|                           | c |   |   |   |   |   |   |   |         |        |
|                           | e |   |   |   |   |   |   |   |         |        |
|                           | \ |   |   |   |   |   |   |   |         |        |
|                           | * |   |   |   |   |   |   |   |         |        |
+---------------------------+---+---+---+---+---+---+---+---+---------+--------+

*
\* Replace earlier if leaks are present and maintenance history is
unknown*

**Table 3** Integrated recovery mechanism maintenance intervals

+---------------------------+---+---+---+---+---+---+---+---+---------+--------+
| **Integrated Recovery     | A | B | C | D | E | F | G | H | Worm    | Cont   |
| system of MotoSuiveur®    |   |   |   |   |   |   |   |   | R       | roller |
| Unit**                    |   |   |   |   |   |   |   |   | otation | 7-S    |
|                           |   |   |   |   |   |   |   |   | Count   | egment |
|                           |   |   |   |   |   |   |   |   | (HMI)   | D      |
|                           |   |   |   |   |   |   |   |   |         | isplay |
+===========================+===+===+===+===+===+===+===+===+=========+========+
| Fixation to MS Unit       |   |   |   |   | ● |   |   |   | 75E\ :  | |ima   |
|                           |   |   |   |   |   |   |   |   | sup:`6` | ge89|; |
|                           |   |   |   |   |   |   |   |   |         | |ima   |
|                           |   |   |   |   |   |   |   |   |         | ge90|; |
|                           |   |   |   |   |   |   |   |   |         | |ima   |
|                           |   |   |   |   |   |   |   |   |         | ge91|; |
|                           |   |   |   |   |   |   |   |   |         | |im    |
|                           |   |   |   |   |   |   |   |   |         | age92| |
+---------------------------+---+---+---+---+---+---+---+---+---------+--------+
|                           | V |   |   |   |   |   |   |   |         |        |
|                           | i |   |   |   |   |   |   |   |         |        |
|                           | s |   |   |   |   |   |   |   |         |        |
|                           | u |   |   |   |   |   |   |   |         |        |
|                           | a |   |   |   |   |   |   |   |         |        |
|                           | l |   |   |   |   |   |   |   |         |        |
|                           | i |   |   |   |   |   |   |   |         |        |
|                           | n |   |   |   |   |   |   |   |         |        |
|                           | s |   |   |   |   |   |   |   |         |        |
|                           | p |   |   |   |   |   |   |   |         |        |
|                           | e |   |   |   |   |   |   |   |         |        |
|                           | c |   |   |   |   |   |   |   |         |        |
|                           | t |   |   |   |   |   |   |   |         |        |
|                           | i |   |   |   |   |   |   |   |         |        |
|                           | o |   |   |   |   |   |   |   |         |        |
|                           | n |   |   |   |   |   |   |   |         |        |
|                           | . |   |   |   |   |   |   |   |         |        |
|                           | C |   |   |   |   |   |   |   |         |        |
|                           | h |   |   |   |   |   |   |   |         |        |
|                           | e |   |   |   |   |   |   |   |         |        |
|                           | c |   |   |   |   |   |   |   |         |        |
|                           | k |   |   |   |   |   |   |   |         |        |
|                           | F |   |   |   |   |   |   |   |         |        |
|                           | a |   |   |   |   |   |   |   |         |        |
|                           | s |   |   |   |   |   |   |   |         |        |
|                           | t |   |   |   |   |   |   |   |         |        |
|                           | e |   |   |   |   |   |   |   |         |        |
|                           | n |   |   |   |   |   |   |   |         |        |
|                           | e |   |   |   |   |   |   |   |         |        |
|                           | r |   |   |   |   |   |   |   |         |        |
|                           | s |   |   |   |   |   |   |   |         |        |
+---------------------------+---+---+---+---+---+---+---+---+---------+--------+
| Recovery Transmission     |   |   |   |   |   |   | ● |   | -       | -      |
| Grease:                   |   |   |   |   |   |   |   |   |         |        |
|                           |   |   |   |   |   |   |   |   |         |        |
| REPSOL NLGI 00            |   |   |   |   |   |   |   |   |         |        |
+---------------------------+---+---+---+---+---+---+---+---+---------+--------+
|                           | A |   |   |   |   |   |   |   |         |        |
|                           | d |   |   |   |   |   |   |   |         |        |
|                           | d |   |   |   |   |   |   |   |         |        |
|                           | o |   |   |   |   |   |   |   |         |        |
|                           | r |   |   |   |   |   |   |   |         |        |
|                           | R |   |   |   |   |   |   |   |         |        |
|                           | e |   |   |   |   |   |   |   |         |        |
|                           | p |   |   |   |   |   |   |   |         |        |
|                           | l |   |   |   |   |   |   |   |         |        |
|                           | a |   |   |   |   |   |   |   |         |        |
|                           | c |   |   |   |   |   |   |   |         |        |
|                           | e |   |   |   |   |   |   |   |         |        |
|                           | i |   |   |   |   |   |   |   |         |        |
|                           | f |   |   |   |   |   |   |   |         |        |
|                           | n |   |   |   |   |   |   |   |         |        |
|                           | e |   |   |   |   |   |   |   |         |        |
|                           | c |   |   |   |   |   |   |   |         |        |
|                           | e |   |   |   |   |   |   |   |         |        |
|                           | s |   |   |   |   |   |   |   |         |        |
|                           | s |   |   |   |   |   |   |   |         |        |
|                           | a |   |   |   |   |   |   |   |         |        |
|                           | r |   |   |   |   |   |   |   |         |        |
|                           | y |   |   |   |   |   |   |   |         |        |
+---------------------------+---+---+---+---+---+---+---+---+---------+--------+
| IR system engagement      |   |   |   |   | ● |   |   |   | 75E\ :  | |ima   |
|                           |   |   |   |   |   |   |   |   | sup:`6` | ge93|; |
|                           |   |   |   |   |   |   |   |   |         | |ima   |
|                           |   |   |   |   |   |   |   |   |         | ge94|; |
|                           |   |   |   |   |   |   |   |   |         | |ima   |
|                           |   |   |   |   |   |   |   |   |         | ge95|; |
|                           |   |   |   |   |   |   |   |   |         | |im    |
|                           |   |   |   |   |   |   |   |   |         | age96| |
+---------------------------+---+---+---+---+---+---+---+---+---------+--------+
|                           | T |   |   |   |   |   |   |   |         |        |
|                           | e |   |   |   |   |   |   |   |         |        |
|                           | s |   |   |   |   |   |   |   |         |        |
|                           | t |   |   |   |   |   |   |   |         |        |
|                           | E |   |   |   |   |   |   |   |         |        |
|                           | n |   |   |   |   |   |   |   |         |        |
|                           | g |   |   |   |   |   |   |   |         |        |
|                           | a |   |   |   |   |   |   |   |         |        |
|                           | g |   |   |   |   |   |   |   |         |        |
|                           | e |   |   |   |   |   |   |   |         |        |
|                           | m |   |   |   |   |   |   |   |         |        |
|                           | e |   |   |   |   |   |   |   |         |        |
|                           | n |   |   |   |   |   |   |   |         |        |
|                           | t |   |   |   |   |   |   |   |         |        |
|                           | / |   |   |   |   |   |   |   |         |        |
|                           | D |   |   |   |   |   |   |   |         |        |
|                           | i |   |   |   |   |   |   |   |         |        |
|                           | s |   |   |   |   |   |   |   |         |        |
|                           | e |   |   |   |   |   |   |   |         |        |
|                           | n |   |   |   |   |   |   |   |         |        |
|                           | g |   |   |   |   |   |   |   |         |        |
|                           | a |   |   |   |   |   |   |   |         |        |
|                           | g |   |   |   |   |   |   |   |         |        |
|                           | e |   |   |   |   |   |   |   |         |        |
|                           | m |   |   |   |   |   |   |   |         |        |
|                           | e |   |   |   |   |   |   |   |         |        |
|                           | n |   |   |   |   |   |   |   |         |        |
|                           | t |   |   |   |   |   |   |   |         |        |
|                           | F |   |   |   |   |   |   |   |         |        |
|                           | u |   |   |   |   |   |   |   |         |        |
|                           | n |   |   |   |   |   |   |   |         |        |
|                           | c |   |   |   |   |   |   |   |         |        |
|                           | t |   |   |   |   |   |   |   |         |        |
|                           | i |   |   |   |   |   |   |   |         |        |
|                           | o |   |   |   |   |   |   |   |         |        |
|                           | n |   |   |   |   |   |   |   |         |        |
+---------------------------+---+---+---+---+---+---+---+---+---------+--------+

*\* Replace earlier if leaks are present and maintenance history is
unknown*

Appendix 1: Signal Lamps
========================

**Table 1** Combination of active and inactive signal lams

+---+---+---+-----+-----+-----------------------+--------------------+
| * |   |   |     |     | **Status**            | **Correction**     |
| * |   |   |     |     |                       |                    |
| S |   |   |     |     |                       |                    |
| i |   |   |     |     |                       |                    |
| g |   |   |     |     |                       |                    |
| n |   |   |     |     |                       |                    |
| a |   |   |     |     |                       |                    |
| l |   |   |     |     |                       |                    |
| l |   |   |     |     |                       |                    |
| a |   |   |     |     |                       |                    |
| m |   |   |     |     |                       |                    |
| p |   |   |     |     |                       |                    |
| * |   |   |     |     |                       |                    |
| * |   |   |     |     |                       |                    |
+===+===+===+=====+=====+=======================+====================+
| * | * | * | *   | *   |                       |                    |
| * | * | * | *Re | *Re |                       |                    |
| F | E | H | cov | cov |                       |                    |
| a | n | e | ery | ery |                       |                    |
| u | a | a | mod | eng |                       |                    |
| l | b | l | e** | age |                       |                    |
| t | l | t |     | d** |                       |                    |
| * | e | h |     |     |                       |                    |
| * | d | y |     |     |                       |                    |
|   | * | * |     |     |                       |                    |
|   | * | * |     |     |                       |                    |
+---+---+---+-----+-----+-----------------------+--------------------+
| 0 | 0 | 0 | 1   | 0   | MS Power off.         | Check MS           |
|   |   |   |     |     | Recovery pre-engaged  | electrical         |
|   |   |   |     |     |                       | equipment and MS   |
|   |   |   |     |     |                       | power supply.      |
|   |   |   |     |     |                       | Check for fault or |
|   |   |   |     |     |                       | warning number.    |
+---+---+---+-----+-----+-----------------------+--------------------+
| 0 | 0 | 0 | 1   | 1   | MS Power off.         | Check MS           |
|   |   |   |     |     | Recovery engaged      | electrical         |
|   |   |   |     |     | (Recovery mode)       | equipment and MS   |
|   |   |   |     |     |                       | power supply.      |
|   |   |   |     |     |                       | Check for fault or |
|   |   |   |     |     |                       | warning number.    |
+---+---+---+-----+-----+-----------------------+--------------------+
| 0 | 1 | 0 | 0   | 0   | Not allowed           | Check electrical   |
|   |   |   |     |     | (Indication for       | equipment. Check   |
|   |   |   |     |     | hardware problem)     | for fault or       |
|   |   |   |     |     |                       | warning number.    |
+---+---+---+-----+-----+-----------------------+--------------------+
| 1 | 0 | 0 | 0   | 0   | MS Hardware fault.    | Check MS fault     |
|   |   |   |     |     | (wiring, power        | number.            |
|   |   |   |     |     | supply, etc.)         |                    |
+---+---+---+-----+-----+-----------------------+--------------------+
| 1 | 1 | 0 | 0   | 0   | Not allowed           | Check MS           |
|   |   |   |     |     | (Indication for       | electrical         |
|   |   |   |     |     | hardware problem)     | equipment. Check   |
|   |   |   |     |     |                       | for MS fault or    |
|   |   |   |     |     |                       | warning number.    |
+---+---+---+-----+-----+-----------------------+--------------------+
| 0 | 0 | 1 | 1   | 0   | Self-test or recovery | -                  |
|   |   |   |     |     | pre-engagement        |                    |
+---+---+---+-----+-----+-----------------------+--------------------+
| 0 | 0 | 1 | 1   | 1   | Self-test or recovery | -                  |
|   |   |   |     |     | mode                  |                    |
+---+---+---+-----+-----+-----------------------+--------------------+
| 0 | 1 | 1 | 0   | 0   | Normal (ready or      | -                  |
|   |   |   |     |     | following)            |                    |
+---+---+---+-----+-----+-----------------------+--------------------+
| 1 | 0 | 1 | 0   | 0   | MS Fault (overspeed,  | Check fault or     |
|   |   |   |     |     | self-test, etc.)      | warning number.    |
+---+---+---+-----+-----+-----------------------+--------------------+
| 1 | 1 | 1 | 0   | 0   | Not allowed           | Check electrical   |
|   |   |   |     |     | (Indication for       | equipment. Check   |
|   |   |   |     |     | hardware problem)     | for fault or       |
|   |   |   |     |     |                       | warning number.    |
+---+---+---+-----+-----+-----------------------+--------------------+

+-------------------+--------------------------------------------------+
| **Legend:**       |                                                  |
+===================+==================================================+
|                   | Mandatory signals/indicators                     |
+-------------------+--------------------------------------------------+
|                   | Optional signals/indicators                      |
+-------------------+--------------------------------------------------+

**
**

**Table 2** Visual check of switch test

+-------------+--------------------------+-----------------------------+
| **Step**    | **Picture**              | **Description**             |
+=============+==========================+=============================+
| Start       | |image97|                | Initial centered position   |
|             |                          | of the worm.                |
+-------------+--------------------------+-----------------------------+
| Moving next | |image98|                | Worm is moved next to USCRE |
| to USCRE    |                          | switch.                     |
| switch      |                          |                             |
+-------------+--------------------------+-----------------------------+
| USCRE       | |image99|                | Check for the presence of   |
| signal ?    |                          | USCRE signal on input 2 of  |
|             |                          | MS Controller. Upward       |
|             |                          | enable lamp should be on.   |
+-------------+--------------------------+-----------------------------+
| Moving worm | |image100|               | After worm pressed switch,  |
| to press    |                          | USCRE signal should be      |
| USCRE       |                          | inactive.                   |
| switch      |                          |                             |
+-------------+--------------------------+-----------------------------+
| USCRE       | |image101|               | After worm pressed switch,  |
| signal ?    |                          | Upward enable lamp should   |
|             |                          | be off                      |
+-------------+--------------------------+-----------------------------+
| Moving next | |image102|               | Worm is moved next to SCRE  |
| to SCRE     |                          | switch.                     |
| switch      |                          |                             |
+-------------+--------------------------+-----------------------------+
| SCRE signal | |image103|               | Check for the presence of   |
| ?           |                          | USCRE signal on input 3 of  |
|             |                          | MS Controller. Downward     |
|             |                          | enable lamp should be on.   |
+-------------+--------------------------+-----------------------------+
| Moving worm | |image104|               | After worm pressed switch,  |
| to press    |                          | SCRE signal should be       |
| SCRE switch |                          | inactive.                   |
+-------------+--------------------------+-----------------------------+
| SCRE signal | |image105|               | After worm pressed switch,  |
| ?           |                          | Downward enable lamp should |
|             |                          | be off.                     |
+-------------+--------------------------+-----------------------------+
| End         | |image106|               | Center worm between         |
|             |                          | switches. Downward enable   |
|             |                          | and Upward enable lamps     |
|             |                          | should be on.               |
+-------------+--------------------------+-----------------------------+

.. |image1| image:: /_img/archives/siguren-ms-manual-h_reviewed/media/image1.png
   :width: 2.34328in
   :height: 0.50744in
.. |image2| image:: /_img/archives/siguren-ms-manual-h_reviewed/media/image2.png
   :width: 6.26806in
   :height: 5.59236in
.. |image3| image:: /_img/archives/siguren-ms-manual-h_reviewed/media/image3.png
   :width: 6.26646in
   :height: 5.63954in
.. |image4| image:: /_img/archives/siguren-ms-manual-h_reviewed/media/image4.png
   :width: 6.26806in
   :height: 4.81597in
.. |image5| image:: /_img/archives/siguren-ms-manual-h_reviewed/media/image5.png
   :width: 4.08012in
   :height: 9.31169in
.. |image6| image:: /_img/archives/siguren-ms-manual-h_reviewed/media/image6.png
   :width: 2.80233in
   :height: 4.43034in
.. |image7| image:: /_img/archives/siguren-ms-manual-h_reviewed/media/image7.png
   :width: 6.26806in
   :height: 4.81597in
.. |image8| image:: /_img/archives/siguren-ms-manual-h_reviewed/media/image8.png
   :width: 5.75452in
   :height: 1.96365in
.. |image9| image:: /_img/archives/siguren-ms-manual-h_reviewed/media/image9.png
   :width: 5.15652in
   :height: 1.57222in
.. |image10| image:: /_img/archives/siguren-ms-manual-h_reviewed/media/image10.png
   :width: 1.23913in
   :height: 1.20667in
.. |image11| image:: /_img/archives/siguren-ms-manual-h_reviewed/media/image11.png
   :width: 1.19277in
   :height: 1.17219in
.. |A picture containing table, sitting, kitchen, man Description automatically generated| image:: /_img/archives/siguren-ms-manual-h_reviewed/media/image12.jpeg
   :width: 4.75652in
   :height: 2.49256in
.. |A close up of a logo Description automatically generated| image:: /_img/archives/siguren-ms-manual-h_reviewed/media/image13.png
   :width: 0.57431in
   :height: 0.51042in
.. |A picture containing indoor, sitting, kitchen, person Description automatically generated| image:: /_img/archives/siguren-ms-manual-h_reviewed/media/image14.jpeg
   :width: 5.12778in
   :height: 3.02326in
.. |Checkmark| image:: /_img/archives/siguren-ms-manual-h_reviewed/media/image16.svg
   :width: 0.37313in
   :height: 0.37313in
.. |Close| image:: /_img/archives/siguren-ms-manual-h_reviewed/media/image18.svg
   :width: 0.38806in
   :height: 0.38806in
.. |image12| image:: /_img/archives/siguren-ms-manual-h_reviewed/media/image19.png
   :width: 5.46269in
   :height: 3.21342in
.. |image13| image:: /_img/archives/siguren-ms-manual-h_reviewed/media/image20.png
   :width: 3.74444in
   :height: 1.8375in
.. |image14| image:: /_img/archives/siguren-ms-manual-h_reviewed/media/image21.png
   :width: 6.26806in
   :height: 4.86389in
.. |image15| image:: /_img/archives/siguren-ms-manual-h_reviewed/media/image22.png
   :width: 3.54545in
   :height: 3.78903in
.. |A picture containing drawing Description automatically generated| image:: /_img/archives/siguren-ms-manual-h_reviewed/media/image23.png
   :width: 0.41791in
   :height: 0.41415in
.. |image16| image:: /_img/archives/siguren-ms-manual-h_reviewed/media/image24.png
   :width: 0.19652in
   :height: 0.29038in
.. |image17| image:: /_img/archives/siguren-ms-manual-h_reviewed/media/image25.png
   :width: 0.1617in
   :height: 0.24713in
.. |image18| image:: /_img/archives/siguren-ms-manual-h_reviewed/media/image26.png
   :width: 0.18154in
   :height: 0.27375in
.. |image19| image:: /_img/archives/siguren-ms-manual-h_reviewed/media/image24.png
   :width: 0.19652in
   :height: 0.29038in
.. |image20| image:: /_img/archives/siguren-ms-manual-h_reviewed/media/image25.png
   :width: 4.98958in
   :height: 0.62903in
.. |image21| image:: /_img/archives/siguren-ms-manual-h_reviewed/media/image27.png
   :width: 2.89928in
   :height: 0.64583in
.. |image22| image:: /_img/archives/siguren-ms-manual-h_reviewed/media/image28.png
   :width: 4.63596in
   :height: 3.69583in
.. |image23| image:: /_img/archives/siguren-ms-manual-h_reviewed/media/image29.gif
   :width: 0.21354in
   :height: 0.375in
.. |image24| image:: /_img/archives/siguren-ms-manual-h_reviewed/media/image30.gif
   :width: 0.20548in
   :height: 0.37153in
.. |image25| image:: /_img/archives/siguren-ms-manual-h_reviewed/media/image31.gif
   :width: 0.21354in
   :height: 0.375in
.. |image26| image:: /_img/archives/siguren-ms-manual-h_reviewed/media/image32.gif
   :width: 0.20313in
   :height: 0.36632in
.. |image27| image:: /_img/archives/siguren-ms-manual-h_reviewed/media/image33.gif
   :width: 0.19965in
   :height: 0.3869in
.. |image28| image:: /_img/archives/siguren-ms-manual-h_reviewed/media/image34.gif
   :width: 0.21181in
   :height: 0.36285in
.. |image29| image:: /_img/archives/siguren-ms-manual-h_reviewed/media/image35.gif
   :width: 0.21354in
   :height: 0.375in
.. |image30| image:: /_img/archives/siguren-ms-manual-h_reviewed/media/image36.gif
   :width: 0.21937in
   :height: 0.36632in
.. |image31| image:: /_img/archives/siguren-ms-manual-h_reviewed/media/image37.gif
   :width: 0.21354in
   :height: 0.375in
.. |image32| image:: /_img/archives/siguren-ms-manual-h_reviewed/media/image38.gif
   :width: 0.20976in
   :height: 0.37326in
.. |image33| image:: /_img/archives/siguren-ms-manual-h_reviewed/media/image39.gif
   :width: 0.21354in
   :height: 0.375in
.. |image34| image:: /_img/archives/siguren-ms-manual-h_reviewed/media/image40.gif
   :width: 0.21528in
   :height: 0.36111in
.. |image35| image:: /_img/archives/siguren-ms-manual-h_reviewed/media/image41.gif
   :width: 0.21354in
   :height: 0.375in
.. |image36| image:: /_img/archives/siguren-ms-manual-h_reviewed/media/image40.gif
   :width: 0.20895in
   :height: 0.375in
.. |image37| image:: /_img/archives/siguren-ms-manual-h_reviewed/media/image42.gif
   :width: 0.21354in
   :height: 0.375in
.. |image38| image:: /_img/archives/siguren-ms-manual-h_reviewed/media/image43.gif
   :width: 0.20895in
   :height: 0.36285in
.. |image39| image:: /_img/archives/siguren-ms-manual-h_reviewed/media/image44.gif
   :width: 0.21354in
   :height: 0.375in
.. |image40| image:: /_img/archives/siguren-ms-manual-h_reviewed/media/image45.gif
   :width: 0.21354in
   :height: 0.375in
.. |image41| image:: /_img/archives/siguren-ms-manual-h_reviewed/media/image26.png
   :width: 0.33579in
   :height: 0.50635in
.. |image42| image:: /_img/archives/siguren-ms-manual-h_reviewed/media/image46.png
   :width: 4.98148in
   :height: 8.57143in
.. |image43| image:: /_img/archives/siguren-ms-manual-h_reviewed/media/image470.png
   :width: 2.625in
   :height: 6.35813in
.. |image44| image:: /_img/archives/siguren-ms-manual-h_reviewed/media/image48.png
   :width: 5.60241in
   :height: 5.77993in
.. |image45| image:: /_img/archives/siguren-ms-manual-h_reviewed/media/image49.png
   :width: 5.84766in
   :height: 6.37758in
.. |image46| image:: /_img/archives/siguren-ms-manual-h_reviewed/media/image50.png
   :width: 4.85867in
   :height: 5.32468in
.. |image47| image:: /_img/archives/siguren-ms-manual-h_reviewed/media/image51.png
   :width: 4.24374in
   :height: 9.27273in
.. |image48| image:: /_img/archives/siguren-ms-manual-h_reviewed/media/image52.png
   :width: 0.23126in
   :height: 0.40365in
.. |image49| image:: /_img/archives/siguren-ms-manual-h_reviewed/media/image53.png
   :width: 0.23077in
   :height: 0.40171in
.. |image50| image:: /_img/archives/siguren-ms-manual-h_reviewed/media/image54.png
   :width: 0.22598in
   :height: 0.39713in
.. |image51| image:: /_img/archives/siguren-ms-manual-h_reviewed/media/image55.png
   :width: 0.22135in
   :height: 0.39259in
.. |image52| image:: /_img/archives/siguren-ms-manual-h_reviewed/media/image56.png
   :width: 0.21484in
   :height: 0.39598in
.. |image53| image:: /_img/archives/siguren-ms-manual-h_reviewed/media/image57.png
   :width: 0.23615in
   :height: 0.40692in
.. |image54| image:: /_img/archives/siguren-ms-manual-h_reviewed/media/image58.png
   :width: 0.22786in
   :height: 0.39984in
.. |image55| image:: /_img/archives/siguren-ms-manual-h_reviewed/media/image59.png
   :width: 0.23201in
   :height: 0.40273in
.. |image56| image:: /_img/archives/siguren-ms-manual-h_reviewed/media/image60.png
   :width: 0.24038in
   :height: 0.40889in
.. |image57| image:: /_img/archives/siguren-ms-manual-h_reviewed/media/image61.png
   :width: 0.22436in
   :height: 0.40913in
.. |image58| image:: /_img/archives/siguren-ms-manual-h_reviewed/media/image62.png
   :width: 0.2277in
   :height: 0.39556in
.. |image59| image:: /_img/archives/siguren-ms-manual-h_reviewed/media/image63.png
   :width: 0.20833in
   :height: 0.37173in
.. |image60| image:: /_img/archives/siguren-ms-manual-h_reviewed/media/image64.png
   :width: 0.23237in
   :height: 0.39589in
.. |image61| image:: /_img/archives/siguren-ms-manual-h_reviewed/media/image65.png
   :width: 0.21073in
   :height: 0.38354in
.. |image62| image:: /_img/archives/siguren-ms-manual-h_reviewed/media/image66.png
   :width: 0.22581in
   :height: 0.41619in
.. |image63| image:: /_img/archives/siguren-ms-manual-h_reviewed/media/image67.png
   :width: 0.22436in
   :height: 0.40126in
.. |image64| image:: /_img/archives/siguren-ms-manual-h_reviewed/media/image68.png
   :width: 0.2248in
   :height: 0.39408in
.. |image65| image:: /_img/archives/siguren-ms-manual-h_reviewed/media/image69.emf
   :width: 2.88264in
   :height: 3.45694in
.. |image66| image:: /_img/archives/siguren-ms-manual-h_reviewed/media/image70.png
   :width: 4.9717in
   :height: 7.43878in
.. |image67| image:: /_img/archives/siguren-ms-manual-h_reviewed/media/image71.png
   :width: 0.2185in
   :height: 0.37718in
.. |image68| image:: /_img/archives/siguren-ms-manual-h_reviewed/media/image68.png
   :width: 0.15225in
   :height: 0.2669in
.. |image69| image:: /_img/archives/siguren-ms-manual-h_reviewed/media/image71.png
   :width: 0.15423in
   :height: 0.26623in
.. |image70| image:: /_img/archives/siguren-ms-manual-h_reviewed/media/image72.png
   :width: 4.03345in
   :height: 4.0625in
.. |image71| image:: /_img/archives/siguren-ms-manual-h_reviewed/media/image73.png
   :width: 0.11024in
   :height: 0.20079in
.. |image72| image:: /_img/archives/siguren-ms-manual-h_reviewed/media/image74.png
   :width: 0.11417in
   :height: 0.19685in
.. |image73| image:: /_img/archives/siguren-ms-manual-h_reviewed/media/image75.png
   :width: 0.11024in
   :height: 0.19685in
.. |image74| image:: /_img/archives/siguren-ms-manual-h_reviewed/media/image76.png
   :width: 0.11417in
   :height: 0.19685in
.. |image75| image:: /_img/archives/siguren-ms-manual-h_reviewed/media/image73.png
   :width: 0.11024in
   :height: 0.20079in
.. |image76| image:: /_img/archives/siguren-ms-manual-h_reviewed/media/image74.png
   :width: 0.11417in
   :height: 0.19685in
.. |image77| image:: /_img/archives/siguren-ms-manual-h_reviewed/media/image75.png
   :width: 0.11024in
   :height: 0.19685in
.. |image78| image:: /_img/archives/siguren-ms-manual-h_reviewed/media/image76.png
   :width: 0.11417in
   :height: 0.19685in
.. |image79| image:: /_img/archives/siguren-ms-manual-h_reviewed/media/image73.png
   :width: 0.11024in
   :height: 0.20079in
.. |image80| image:: /_img/archives/siguren-ms-manual-h_reviewed/media/image74.png
   :width: 0.11417in
   :height: 0.19685in
.. |image81| image:: /_img/archives/siguren-ms-manual-h_reviewed/media/image75.png
   :width: 0.11024in
   :height: 0.19685in
.. |image82| image:: /_img/archives/siguren-ms-manual-h_reviewed/media/image76.png
   :width: 0.11417in
   :height: 0.19685in
.. |image83| image:: /_img/archives/siguren-ms-manual-h_reviewed/media/image74.png
   :width: 0.11417in
   :height: 0.19685in
.. |image84| image:: /_img/archives/siguren-ms-manual-h_reviewed/media/image75.png
   :width: 0.11024in
   :height: 0.19685in
.. |image85| image:: /_img/archives/siguren-ms-manual-h_reviewed/media/image76.png
   :width: 0.11417in
   :height: 0.19685in
.. |image86| image:: /_img/archives/siguren-ms-manual-h_reviewed/media/image75.png
   :width: 0.11024in
   :height: 0.19685in
.. |image87| image:: /_img/archives/siguren-ms-manual-h_reviewed/media/image76.png
   :width: 0.11417in
   :height: 0.19685in
.. |image88| image:: /_img/archives/siguren-ms-manual-h_reviewed/media/image76.png
   :width: 0.11417in
   :height: 0.19685in
.. |image89| image:: /_img/archives/siguren-ms-manual-h_reviewed/media/image73.png
   :width: 0.11024in
   :height: 0.20079in
.. |image90| image:: /_img/archives/siguren-ms-manual-h_reviewed/media/image74.png
   :width: 0.11417in
   :height: 0.19685in
.. |image91| image:: /_img/archives/siguren-ms-manual-h_reviewed/media/image75.png
   :width: 0.11024in
   :height: 0.19685in
.. |image92| image:: /_img/archives/siguren-ms-manual-h_reviewed/media/image76.png
   :width: 0.11417in
   :height: 0.19685in
.. |image93| image:: /_img/archives/siguren-ms-manual-h_reviewed/media/image73.png
   :width: 0.11024in
   :height: 0.20079in
.. |image94| image:: /_img/archives/siguren-ms-manual-h_reviewed/media/image74.png
   :width: 0.11417in
   :height: 0.19685in
.. |image95| image:: /_img/archives/siguren-ms-manual-h_reviewed/media/image75.png
   :width: 0.11024in
   :height: 0.19685in
.. |image96| image:: /_img/archives/siguren-ms-manual-h_reviewed/media/image76.png
   :width: 0.11417in
   :height: 0.19685in
.. |image97| image:: /_img/archives/siguren-ms-manual-h_reviewed/media/image77.jpeg
   :width: 2.15625in
   :height: 1.82292in
.. |image98| image:: /_img/archives/siguren-ms-manual-h_reviewed/media/image78.jpeg
   :width: 2.23958in
   :height: 1.80208in
.. |image99| image:: /_img/archives/siguren-ms-manual-h_reviewed/media/image79.jpeg
   :width: 1.20833in
   :height: 1.86458in
.. |image100| image:: /_img/archives/siguren-ms-manual-h_reviewed/media/image80.jpeg
   :width: 2.21875in
   :height: 1.85417in
.. |image101| image:: /_img/archives/siguren-ms-manual-h_reviewed/media/image81.jpeg
   :width: 1.0625in
   :height: 1.79167in
.. |image102| image:: /_img/archives/siguren-ms-manual-h_reviewed/media/image82.jpeg
   :width: 2.22917in
   :height: 1.875in
.. |image103| image:: /_img/archives/siguren-ms-manual-h_reviewed/media/image83.jpeg
   :width: 1.15625in
   :height: 1.83333in
.. |image104| image:: /_img/archives/siguren-ms-manual-h_reviewed/media/image84.jpeg
   :width: 2.14583in
   :height: 2.04167in
.. |image105| image:: /_img/archives/siguren-ms-manual-h_reviewed/media/image85.jpeg
   :width: 1.0625in
   :height: 1.75in
.. |image106| image:: /_img/archives/siguren-ms-manual-h_reviewed/media/image77.jpeg
   :width: 2.15625in
   :height: 1.82292in
