========================================================
Re-engaging from Load Arrest Without Presence of Fault
========================================================

.. It is possible to have load arrest with and without the presence of fault.
.. In both case of load arrest Unscrewing ENABLE switch is actuated.

Preliminary steps
     1. Identify and resolve the cause for load arrest.
  
        .. seealso::
            :doc:`/operation/load-arrest/determining-cause-for-load-arrest`
     
     2. Confirm that :guilabel:`🟢 Downward ENABLE` light indicator is OFF.
     
     3. Verify that hoist is healthy.

        .. how? or is that outside of our scope?

Steps
	1. Enable signal to MotoSuiveur® System from hoist is ON.
	2. :guilabel:`🟢 Hoist Enabled` signal from MotoSuiveur® System to hoist is on*.
	3. Short Upward movement is necessary (from hoist control) until :guilabel:`🟢 Downward ENABLE` light swiches to illuminated.
	4. Both light indicators :guilabel:`🟢 Downward ENABLE` and :guilabel:`🟢 Upward ENABLE` are illuminated.
	5. MotoSuiveur® System is ready to follow.

\*\ If :guilabel:`🟢 Hoist Enabled` signal is not illuminated, :guilabel:`🔑 Enable Override` should be used to force signal.
Forced signal should be used **only** for movement performing.

.. _Enable ovverride:
.. figure:: /_img/regular-operation/ENABLE-override.PNG
	:figwidth: 100 %
	:class: instructionimg

	Enable override

.. note::             
     In case :guilabel:`🟢 Hoist Enabled` is not present after re-engagement, follow :doc:`/operation/regular/system-Reset`