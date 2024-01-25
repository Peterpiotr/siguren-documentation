========================================================
Re-engaging from Load Arrest Without Presence of Fault
========================================================

.. It is possible to have load arrest with and without the presence of fault.
.. In both case of load arrest Unscrewing enable switch is actuated.

Preliminary steps
     1. Identify and resolve the cause for load arrest.
  
          .. note::
               See :doc:`/operation/load-arrest/determining-cause-for-load-arrest`
     
     2. Confirm that :guilabel:`🟢 Downward Enable` light indicator is OFF.
     
     2. Verify that hoist is healthy.

Steps
	3. Enable signal to MotoSuiveur® System from hoist is ON.
	4. :guilabel:`🟢 Hoist Enabled` signal from MotoSuiveur® System to hoist is on*.
	5. Short upward movement is necessary (from hoist control) until :guilabel:`🟢 Downward Enable` light swiches to illuminated.
	6. Both light indicators :guilabel:`🟢 Downward Enable` and :guilabel:`🟢 Upward Enable` are illuminated.
	7. MotoSuiveur® System is ready to follow.

\*\ If :guilabel:`🟢 Hoist Enabled` signal is not illuminated, :guilabel:`🔑 Enable Override` should be used to force signal.
Forced signal should be used **only** for movement performing.

.. _Enable ovverride:
.. figure:: /_img/regular-operation/enable-override.PNG
	:figwidth: 300 px
	:class: instructionimg

	Enable override

.. note::             
     In case :guilabel:`🟢 Hoist Enabled` is not present after re-engagement, follow :doc:`/operation/regular/system-reset`