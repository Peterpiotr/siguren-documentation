==========
Self-test
==========

After :doc:`internal-test` finishes, Self-test operation mode (further called self - test) starts. On figure 15 a) symbols indicated self-test steps on MS controller 7 - segment display are shown. On figure 15 b) is shown sequence of self-test steps.

.. _Self-test steps symbols:
.. csv-table:: Self-test steps symbols
   :file: 06_tables/SelfTestStepsSymbols.csv
   :header-rows: 1
   :width: 100
..   :widths: 1, 5

"*" steps are applicable only for hydraulic MS.

.. _Sequence of self-test steps:
.. figure:: img/SequenceSelfTestSteps.png
	:scale: 100 %
	:align: center

	Sequence of self-test steps 

Fields with *, ** and *** are related with Table 2 in section 7.2



Electrical test
+++++++++++++++++++++++++++++

On :numref:`Steps of Electrical test`  test are shown. Test checks for active signals on 
inputs of the MS controller before self-test begin.

.. _Steps of Electrical test:
.. figure:: img/stepsElectricalTest.png
	:scale: 100 %
	:align: center

	Steps of Electrical test 


.. warning::
 	In case of repetitive faults, please contact SIGUREN technologies on address support@siguren.com!


Switch test
+++++++++++++++++++

Switch test check connection between MS controller and SCRE/USCRE switches 
(figure 2, items 4, 5), centered position and functionality of switches. 
On figure 8 are shown steps of Switch test. 

In Table 2 located in appendix are shown steps for visual check of Switch test. 
Visual check of Switch test is necessary only in case if repetitive faults during 
the test appears.
 
.. _Steps of Switch test:
.. figure:: img/stepsSwitchTest.png
	:scale: 100 %
	:align: center

	Steps of Switch test 

testing this :term:`wrn_num` here

.. note::
 	In case of repeatedly `wrn_num` occurs, please check:
	
    	- connection between MS control cabinet and SCRE/USCRE switches;
    	- functionality of SCRE and USCRE switches;
    	- signals on inputs of MS controller and operational relays RSESw and RUESw located in MS control cabinet;

Play test
+++++++++++++++++++

Play test measures play between worm and worm wheel. On :numref:`Play test steps` steps of Play 
test are shown.

.. _Play test steps:
.. figure:: img/playTestSteps.png
	:scale: 100 %
	:align: center

	Play test steps

.. warning::
 	In case of repetitive faults, please contact SIGUREN Technologies on address support@siguren.com!