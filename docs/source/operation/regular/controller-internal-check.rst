========================================
Running an MS Controller Internal Check
========================================

.. include:: /_img/_image-substitutions.rst

Introduction
=============

After initial power ON or after Reset is performed, MS Controller runs an internal check.

All steps and actions from initialization are displayed on the integrated 7-segment display.

The internal initialization sequence is:
    Initial initialization check **>** MS Controller Firmware version check **>** Fieldbus address check


Initialization check
======================
.. changed from "Initial initialization check"

Steps
    1. Observe this sequence on the MS Controller 7-segment display.

        .. list-table:: Initialization sequence

            * - |start|

                1. Start of internal check.

              - |driver|

                2. Communication initialization.

              - |communication|

                3. Communication initialization OK.

            * - |init-app-done|

                3. Initialization of loaded software OK.

              - |init-done| 

                5. Initialization done.

              - .. empty

       - **Initialization check passed successfully.**
       
.. so what?

        .. make the pictures bigger

MS Firmware version check
============================

Currently MS Controllers are operating with MS Firmware version 1.4.2.
On picture below is shown sequence for OS version 1.4.2 displaying.

.. should we use "OS" or "Firmware" ?

Steps
    1. Observe this sequence on the MS Controller 7-segment display.

        .. list-table:: MS Firmware version sequence

            * - |1|

                1.

              - |none|

                2.

              - |4|

                3.

            * - |none|

                4.

              - |2|

                5.

              - 

       - **MS Controller version is confirmed.**


Fieldbus address check
========================


.. note::

    Fieldbus address is configurated by nodeID DIP switches located on MS Controller front side.


Steps
    1. Observe this sequence on the MS Controller 7-segment display.

        .. list-table:: Example for nodeID address 01 sequence

            * - |image049|

                1.

              - |image059|

                2.

              - |none|

                3.

              - |1|

                4.

       - **Fieldbus address is confirmed.**

      .. note:: 
        Video with presented example is shown below:

        .. image:: /_img/7-segment/MS-Controller-internal-check/internal-check.gif
            :width: 100 %
            :class: instructionimg

.. replace with image for use in pdf






.. Initialization==========================================================
.. |start|          image:: /_img/7-segment/MS-Controller-internal-check/start.PNG
.. |init-done|      image:: /_img/7-segment/MS-Controller-internal-check/init-done.PNG
.. |init-app-done|  image:: /_img/7-segment/MS-Controller-internal-check/Init-application-done.PNG
.. |feetback|       image:: /_img/7-segment/MS-Controller-internal-check/feedback-ok.PNG
.. |driver|         image:: /_img/7-segment/MS-Controller-internal-check/Driver-initialized.PNG
.. |communication|  image:: /_img/7-segment/MS-Controller-internal-check/Communication-Ok.PNG


.. OS Version==============================================================
.. |1|          image:: /_img/7-segment/OS-version/1.PNG
.. |2|          image:: /_img/7-segment/OS-version/2.PNG   
.. |4|          image:: /_img/7-segment/OS-version/4.PNG
.. |none|       image:: /_img/7-segment/OS-version/none.PNG