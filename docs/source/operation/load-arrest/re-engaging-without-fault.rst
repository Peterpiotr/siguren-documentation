========================================================
Re-engaging from load arrest without presence of fault
========================================================

It is possible to have load arrest with and without the presence of fault.
In both case of load arrest Unscrewing enable switch is actuated. :guilabel:`🟢 Downward Enable` light indicator is **not** illuminated.

Steps
	1. Cause of the load arrest has been identified and eliminated.
	2. Hoist is healthy.
	3. Enable signal to MotoSuiveur® system from hoist is on.
	4. :guilabel:`🟢 Hoist Enabled` signal from MotoSuiveur® system to hoist is on*.
	5. Short upward movement is necessary (from hoist control) until :guilabel:`🟢 Downward Enable` light swiches to illuminated.
	6. Both light indicators :guilabel:`🟢 Downward Enable` and :guilabel:`🟢 Upward Enable` are illuminated.
	7. MotoSuiveur® system is ready to follow.

\*\ If :guilabel:`🟢 Hoist Enabled` signal is not illuminated, :guilabel:`🔑 Enable Override` should be used to force signal.
Forced signal should be used **only** for movement performing.

.. _Enable ovverride:
.. figure:: /_img/regular-operation/enable-override.PNG
	:figwidth: 300 px
	:align: center

	Enable override

.. note::             
     In case :guilabel:`🟢 Hoist Enabled` is not present after re-engagement a :doc:`Reset <../../operation/regular/system-reset>` of the MS system is required