=========================
Following operation mode
=========================

.. include:: ../substitutions.rst

Following operation mode starts after successful passed of self–test. 
The function of this operation mode is intended for follow movements of the hoist and to monitor 
for exceeding the :term:`rated speed` with defined positive tolerance. 

The speed, which is considered high is called :term:`overspeed`. 

.. important::
    By design MS **will not allow** overspeed. 

Following operation mode principle
====================================

test :numref:`Main principle of following operation mode and overspeed detection` and :numref:`Following mode stages` 
present the main principle of Following operation mode and overspeed *detection*. 

.. _Main principle of following operation mode and overspeed detection:
.. figure:: img/following-01.png
    :align: center
    :scale: 80 %

	Main principle of following operation mode and overspeed detection 

.. _Following mode stages:
.. csv-table:: Following mode stages
   :file: tables/following-mode-stages.csv
   :delim: ;
   :header-rows: 0
   :widths: 20, 80
   :class: tight-table
   :align: center

The steps of following operation mode are presented on :numref:`Steps of Following operation mode`.

.. _Steps of Following operation mode:
.. figure:: img/following-02.png
	:align: center

	Steps of Following operation mode 


Controller display
===================

:numref:`Symbols displayed on 7-segment display on MS controller` shows the 
symbols displayed on 7–segment display during following operation mode respectively when on rest.

.. _Symbols displayed on 7-segment display on MS controller:
.. csv-table:: Symbols displayed on 7-segment display on MS controller when on rest
   :file: tables/following-mode-digits-rest.csv
   :delim: ;
   :header-rows: 1
   :widths: 20, 80
   :class: tight-table
   :align: center

:numref:`Symbols displayed on 7-segment display on MS controller during movement` shows the 
symbols displayed on 7–segment display during following operation mode during movement.

.. _Symbols displayed on 7-segment display on MS controller during movement:
.. csv-table:: Symbols displayed on 7-segment display on MS controller during movement
   :file: tables/following-mode-digits-movement.csv
   :header-rows: 1
   :delim: ;
   :widths: 20, 20, 60
   :class: tight-table
   :align: center
