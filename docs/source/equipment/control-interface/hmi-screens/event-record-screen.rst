======================
Events Log Screens
======================

Events Log Screens gives option to choose between 3 logging groups. 
Opening presents specific events of MotoSuiveur® System. 
Every logging group stores last 10 events after restart or power loss of MS HMI.

.. correct the phrasing

.. "record" and "log" were used indiscriminately. Kept "log". "records" are the individual lines of the logs.

MS Logging Groups screen
=========================

.. figure:: /_img/hmi/logging-groups.PNG
    :figwidth: 100 %
    :align: center

    MS Logging Groups screen components

.. logging grOOps: needs to be corrected asap. In vijeo and in doc.

Screen elements
    ① :guilabel:`MS Status Log` button
        Go to MS Status Log screen
    ② :guilabel:`MS Warning Log` button
        Go to MS Warning Log screen
    ③ :guilabel:`MS Fault Log` button
        Go to MS Fault Log screen
    ④ :guilabel:`Back` button
        Redirect to Menu screen

..
    .. csv-table:: Event record screen
        :file: /_tables/hmi/event-record.csv
        :delim: ;
        :header-rows: 1
        :widths: auto
        :align: left


MS Status Log screen
=======================

MS Status log group contains all events appearing during MotoSuiveur® System operation.

.. figure:: /_img/hmi/status-log.PNG
    :figwidth: 100 %
    :align: center

    MS status log screen components

Screen elements
    ① MS Status logs table
        Chronologically arranged MS Status messages
    ② :guilabel:`Back` button
        Redirect to MS Logging Groups screen

.. comment on "Last Event"

MS Warning Log screen
=======================

MS Warning log group contains all warning events appearing during MotoSuiveur® System operation.

.. figure:: /_img/hmi/warning-log.PNG
    :figwidth: 100 %
    :align: center

    MS warning log screen components

.. screen does not show logged warnings

Screen elements
    ① MS Warning logs table
        Chronologically arranged MS Warnings messages
    ② :guilabel:`Back` button
        Redirect to MS Logging Groups screen


MS Fault Log screen
=======================

MS Fault log group contains all fault events appearing during MotoSuiveur® System operation.

.. figure:: /_img/hmi/fault-log.PNG
    :figwidth: 100 %
    :align: center

    MS fault log screen components

Screen elements
    ① MS Fault logs table
        Chronologically arranged MS Fault messages
    ② :guilabel:`Back` button
        Redirect to MS logging groups screen

.. it reads "DriFe fault" on the image.


..
    .. csv-table:: Log screens 
        :file: /_tables/hmi/log-components.csv
        :delim: ;
        :header-rows: 1
        :widths: auto
        :align: left

