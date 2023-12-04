==============
Following mode
==============

.. tags:: following, overspeed

.. include:: ../../_img/_image-substitutions.rst

Following operation mode starts after successful passed of self–test. 
The function of Following mode is intended for follow movements of the hoist/crane and to monitor 
for exceeding the :term:`rated speed` with defined positive tolerance. 
The speed, which is considered high is called :term:`overspeed`. 

Following is the main operating mode of the MotoSuiveur system. It is separated into Rest and Follow states. 
At Rest, MotoSuiveur system is waiting for a movement request.  
When a movement request is received, MotoSuiveur system starts following.
Rest and Following states are indicated on `MS Controller 7-segment display`_ and :doc:`MSHMI <../../equipment/control-interface/ms-hmi>` in :ms-hmi:`Main screen` field "MS system status:".
         
.. important::             
    By design MS **will not allow** overspeed. 

Following operation mode principle
====================================

Figure :numref:`Main principle of following operation mode and overspeed detection` 
present the main principle of Following operation mode (upper part) and Overspeed detection (lower part). 
MotoSuiveur system follows hoist/crane movement until overspeed is detected.
When overspeed is detected, MotoSuiveur system trips and mechanicaly lockes hoist/crane
to prevent load drop.

.. _Main principle of following operation mode and overspeed detection:
.. figure:: ../../_img/Peter/following-01.png
   :align: center

   Main principle of following operation mode and overspeed detection


.. _Following mode stages:
.. csv-table:: Following mode stages
   :file: ../../_tables/following-mode-stages.csv
   :delim: ;
   :header-rows: 0
   :widths: auto
   :class: tight-table
   :align: left

MS Controller display
=====================

.. _MS Controller 7-segment display:

:numref:`Symbols displayed on 7-segment display on MS controller` shows the 
symbols displayed on 7–segment display during following operation mode respectively when on rest.

.. _Symbols displayed on 7-segment display on MS controller:
.. csv-table:: Rest
   :file: ../../_tables/following-mode-digits-rest.csv
   :delim: ;
   :header-rows: 1
   :widths: auto
   :class: tight-table
   :align: center

:numref:`Symbols displayed on 7-segment display on MS controller during movement` shows the 
symbols displayed on 7–segment display during following operation mode during movement.

.. _Symbols displayed on 7-segment display on MS controller during movement:
.. csv-table:: Movement
   :file: ../../_tables/following-mode-digits-movement.csv
   :header-rows: 1
   :delim: ;
   :widths: auto
   :class: tight-table
   :align: center
