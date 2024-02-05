=========================================================
MS Control Cabinet Electrical Interface
=========================================================


.. figure:: /_img/archives/generalViewConnectionsMS-MSCC.png
	:figwidth: 100 %
	:class: instructionimg

	Electrical connection of the MS Control Cabinet


.. list-table:: MotoSuiveur® System electrical components

    * - **Component**
      - **Description**
    * - T1
      - MotoSuiveur® System power supply
    * - T2
      - Digital inputs
    * - T3
      - MS sensors/switches
    * - T4
      - Digital outputs
    * - T5
      - Analogue input
    * - T6
      - MS servo motor power supply
    * - T7
      - MS servo motor resolver
    * - T8
      - Recovery motor power supply
    * - T9
      - Heater
    

Terminals **T1, T2, T4, T4, T6, T7** are mandatory.


In the table below is presented a complete and detailed description of the terminals.

The set of inputs and outputs is defined in advance for each project based on pre-configuration diagram (MS block diagram).


.. list-table:: Detailed description of terminals

    * - **Terminal**
      - **Signal type**
      - **Signal name**
      - **Description**
    * - T1
      - PS
      - MS Power supply
      - Specifies the supply voltage type of main power supply
    * - 
      - PS
      - Recovery power supply
      - Specifies the supply voltage type of Recovery*
    * - 
      - PS
      - Vontrol power supply
      - Specifies the supply voltage type of Control power supply*
    * - T2
      - CV
      - +24VDC
      - MS Control voltage**
    * - 
      - DI
      - On
      - Enable MS to operate. Signal for hoist healthy
    * - 
      - DI
      - Up
      - Command for moving hoist direction UP
    * - 
      - DI
      - Down
      - Command for moving hoist direction DOWN
    * - 
      - DI
      - Reset
      - Reset MotoSuiveur® System***
    * - 
      - CV
      - +24VDC
      - MS Control voltage**
    * - 
      - DI
      - Backup Mode
      - Start MS Backup Mode****
    * - 
      - CV
      - +24VDC
      - MS Control voltage**
    * - 
      - DI
      - Recovery mode
      - Start MS Recovery mode****
    * - 
      - DI
      - Recovery Up
      - Command for lifting with Recovery
    * - 
      - DI
      - Recovery Down
      - Command for lowering with Recovery
    * - T3
      - DI
      - MS Switches/Proximity Sensors
      - Status of MS position switches/Oil Level Sensor
    * - T4
      - CV
      - Input (MAX 250VAC/VDC)
      - Control voltage from hoist
    * - 
      - DO
      - Hoist Enabled
      - Enable signal for Hoist to operate. MS Healthy
    * - 
      - DO
      - Fault
      - MotoSuiveur® System in fault
    * - 
      - DO
      - Upward Enabled
      - Upward (lifting) hoist movement is allowed
    * - 
      - DO
      - Downward Enabled
      - Downward (lowering) hoist movement is allowed
    * - 
      - DO
      - Fault Buzzer/Warning Beaco
      - Output for buzzer   or beacon
    * - 
      - DO
      - Backup Mode
      - Backup Mode is activated
    * - 
      - DO
      - Oil Warning
      - MS low oil level warning
    * - 
      - DO
      - Low Temperature Warning
      - Warning for low ambient temperature
    * - T5
      - AI
      - Temp
      - Temperature sensor
    * - 
      - AI
      - Temp
      - Temperature sensor
    * - T6
      - PS
      - MS servo motor power supply
      - MS servo motor power supply
    * - T7
      - RES
      - MS servo motor resolver
      - MS servo motor resolver converter
    * - T8
      - PS
      - Recovery motor power supply
      - Recovery motor power supply
    * - T9
      - PS
      - MS Unit heater
      - Heater for MS Unit


| \*\  If power supply is separated
| \**\  Control voltage from MS MS Control Cabinet
| \***\  After Reset command MS performs Self-Test
| \****\  Backup and Recovery mode in some models can be combined in common switch Backup/Recovery
 	 
| PS - Power Supply
| DI - Digital Input
| DO - Digital Output/Relay Contact Output
| AI - Analog Input
| AO - Analog Output
| RES - Resolver 
| CV - Control Voltage

