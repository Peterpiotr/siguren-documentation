==============
Following mode
==============

.. tags:: following, overspeed

.. include:: ../../_img/_image-substitutions.rst

Following operation mode starts after successful passed of self–test. 
The function of Following mode is intended for follow movements of the hoist/crane and to monitor 
for exceeding the :term:`rated speed` with defined positive tolerance. 

The speed, which is considered high is called :term:`overspeed`. 
         
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

Controller display
===================

:numref:`Symbols displayed on 7-segment display on MS controller` shows the 
symbols displayed on 7–segment display during following operation mode respectively when on rest.

.. _Symbols displayed on 7-segment display on MS controller:
.. csv-table:: Symbols displayed on 7-segment display on MS controller when on rest
   :file: ../../_tables/following-mode-digits-rest.csv
   :delim: ;
   :header-rows: 1
   :widths: 20, 80
   :class: tight-table
   :align: center

:numref:`Symbols displayed on 7-segment display on MS controller during movement` shows the 
symbols displayed on 7–segment display during following operation mode during movement.

.. _Symbols displayed on 7-segment display on MS controller during movement:
.. csv-table:: Symbols displayed on 7-segment display on MS controller during movement
   :file: ../../_tables/following-mode-digits-movement.csv
   :header-rows: 1
   :delim: ;
   :widths: 10, 20, 70
   :class: tight-table
   :align: center
