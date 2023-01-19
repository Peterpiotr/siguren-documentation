======================
MotoSuiveur self-test
======================

.. include:: ../substitutions.rst

After :doc:`internal-test` finishes, Self-test operation mode (further called self - test) starts. On figure 15 a) symbols indicated self-test steps on MS controller 7 - segment display are shown. On figure 15 b) is shown sequence of self-test steps.

.. _Self-test steps symbols:
.. csv-table:: Self-test steps symbols
   :file: tables/SelfTestStepsSymbols.csv
   :header-rows: 1
   :class: tight-table
   :width: 100
..   :widths: 1, 5

"*" steps are applicable only for hydraulic MS.

.. raw::
	<div class="mxgraph" style="max-width:100%;border:1px solid transparent;" data-mxgraph="{&quot;highlight&quot;:&quot;#0000ff&quot;,&quot;nav&quot;:true,&quot;resize&quot;:true,&quot;toolbar&quot;:&quot;zoom layers tags lightbox&quot;,&quot;edit&quot;:&quot;_blank&quot;,&quot;xml&quot;:&quot;&lt;mxfile host=\&quot;app.diagrams.net\&quot; modified=\&quot;2023-01-19T17:49:30.321Z\&quot; agent=\&quot;5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36\&quot; etag=\&quot;WYVu8E3OQ6yDaXgzcEEA\&quot; version=\&quot;20.6.0\&quot; type=\&quot;onedrive\&quot;&gt;&lt;diagram id=\&quot;C5RBs43oDa-KdzZeNtuy\&quot; name=\&quot;Page-1\&quot;&gt;7VhZc9MwEP41Hp5gfKRO+ojTpgVCB2ihw6NiK7aI7DWynINfzyqWYzsOOYD0yDSTB+16s5L2+/aIDacfz68ESaOPEFBu2GYwN5wLw7atjm0b6msGi0LTPesUilCwQBtVilv2i2qlqbU5C2jWMJQAXLK0qfQhSagvGzoiBMyaZmPgzV1TEtKW4tYnvK29Z4GMCm3P7lb6a8rCqNzZcs+LJzEpjfVNsogEMKupnEvD6QsAWazieZ9yFbwyLvfvFvd8OHGv3n/OfpKv3oe7m2+vC2eDQ36yuoKgify/rjW4U8JzHS99V7koAyggTwKqnJiG40Uy5ri0cPmDSrnQgJNcAqpAyAhCSAgfAqTabgyJ1GaWkmkSvFXAojzi4E8K1YBxrvdASdv3UMqkgMkKO+VgBYQy5mREuUf8Sbg8aB84CHyUQEKVqwDJoO9SHe6y0np7xlZjkEEufLrFztEUJyKk2/y5hZ06X42nGrkrCjGVYoEGgnIi2bRJZqJzIlzZVbjjQkN/AA2cFg2GJE5V1gPNklcSVzMQky3cULjMIibpbUqWAZphOWnypc4DvKoXcpJlGsUdIB8G0pQKSedbw1o+dXVu6+LW0+KsqhRWmf5RrUp0zCMB0WkB8R2L50tK/ktKunumZNmxduakJktJjL1TVHv6BCyRNRMYjzM82Dp1Vhv+PZvOWmy6gRaZduPxrOn2SGTqHsYl68lzyf1Di3A5hsEbCVyFapXyPAyRLOguMZxBu3ZFEI/ybHe7aGCsGDQgMeMqXteUT6lkPtnQVAhnIe574SPcVGwmD27JkhAlt5LulmTF+nvEZtNtNpuVXO825oZu0ztWt+m2MP2E6BXQ2SZf4ntiHd+x10A4f+yW39unSD/rEvzgHb+sprtbvrVnmdbsMd84+GkQ6OlPAed7zZQvY8BxGGaf2iBQnrDGJy/no/YkMMpFshwEIJcvk8C2ScDe1IQedBIoC2EN1C80JQzBNIenOAes//PvOI89B5SVogkBVzG1zSLDTgyD9VnMsY6HAYrVm9qiFFbvu53L3w==&lt;/diagram&gt;&lt;/mxfile&gt;&quot;}"></div>
	<script type="text/javascript" src="https://viewer.diagrams.net/js/viewer-static.min.js"></script>


.. _Sequence of self-test steps:
.. figure:: img/SequenceSelfTestSteps.png
	:scale: 100 %
	:align: center

	Sequence of self-test steps 

Fields with *, ** and *** are related with Table 2 in section 7.2


Electrical test
=================

Test checks for active signals on inputs of the MS controller before self-test begin.

:numref:`Steps of Electrical test` shows the steps of the electrical test. 

.. _Steps of Electrical test:
.. figure:: img/stepsElectricalTest.png
	:scale: 100 %
	:align: center

	Steps of Electrical test 


.. warning::
 	In case of repetitive faults, please contact SIGUREN technologies at support@siguren.com!


Switch test
============

Switch test check connection between MS controller and ``SCRE`` / ``USCRE`` switches (figure 2, items 4, 5), centered position and functionality of switches. 

:numref:`Steps of Switch test` shows the steps of the switch test. 

.. _Steps of Switch test:
.. figure:: img/stepsSwitchTest.png
	:scale: 100 %
	:align: center

	Steps of Switch test 


In Table 2 located in appendix are shown steps for visual check of Switch test. 
Visual check of Switch test is necessary only if faults appear during the test repeatedly.

.. important::
 	In case of repeatedly `wrn_num` occurs, please check:
	
    	- connection between MS control cabinet and ``SCRE/USCRE`` switches;
    	- functionality of ``SCRE`` and ``USCRE`` switches;
    	- signals on inputs of MS controller and operational relays ``RSESw`` and ``RUESw`` located in MS control cabinet


Play test
===========

Play test measures play between worm and worm wheel. 

:numref:`Play test steps` shows the steps of Play test.

.. _Play test steps:
.. figure:: img/playTestSteps.png
	:scale: 100 %
	:align: center

	Play test steps

.. warning::
 	In case of repetitive faults, please contact SIGUREN Technologies on address support@siguren.com!