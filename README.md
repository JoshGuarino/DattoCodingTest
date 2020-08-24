Simulating upgrade logic of meshed Access Points. Below is the task/challenge I was given.

Assignment: 
You are tasked with simulating problems with the upgrade logic of meshed Access Points. Given the following assumptions and rules, write a simulation in Python to answer the questions at the bottom of this page. Additionally, supply any extra code (outside of the simulation code) that was needed to answer these questions. 
Assume n gateways with m repeaters each on a simulated network. 
A gateway (GW) and a repeater (RP) are both access points (AP). Each AP should have a randomized check-in time offset from 0.00 to 5.00 minutes (two digit precision). 
In order to perform a complete firmware upgrade, each AP must check in a total of three times and run two processes. 
Upgrade cycle: 
Check-in #1: AP should set its download_firmware flag to TRUE 
Process #1: AP should “download” the firmware in a random amount of time from 0.00 to 5.00 minutes 
Check-in #2: AP should set its download_complete flag to TRUE 
Process #2: AP should “upgrade” its firmware in a random amount of time from 0.00 to 5.00 minutes 
Check-in #3: AP should set its upgrade_complete flag to TRUE 
AP rules: Each AP checks in at precise 5.00 minute intervals beginning from its check-in offset time. If an AP has not finished its download or upgrade within the 5 minute interval, it shall not proceed to the next check-in state and must wait for the next 5 minute check-in. 
GW rules: 
Each GW must wait to begin its upgrade process until each of its RPs have set its download_complete state to TRUE. 
RP rules: A RP can only check in if neither it nor its GW have begun Process #2 OR both the RP and its 
GW have completed Process #2. 
Example: 
There is a network with one GW with one RP. Each AP is initialized with a random check-in offset, a random download time, and a random upgrade time. The clock starts at 0.00 and each AP sets its download_firmware flag to TRUE when the clock reaches the check-in offset time for the given AP. 

GW check-in offset: 1.52 mins download time: 3.27 mins upgrade time: 4.11 mins C1: 1.52 P1: 4.79 C2: 6.52 P2: 12.59 C3: 16.52 
RP check-in offset: 3.48 mins download time: 2.28 mins upgrade time: 1.23 mins C1: 3.48 P1: 5.76 C2: 8.48 P2: 10.71 C3: 13.48 

Total network upgrade time in this example is 16.52 minutes. 
Questions: 
1. Given 10 gateways with 2 repeaters each, what is the average total upgrade time over 10 runs? 
2. Over these 10 runs, at the 8 minute mark, how many gateways and repeaters were at each point in the upgrade cycle? 
3. Which network upgrades faster on average, a network with 3 gateways with 4 repeaters each or a network with 4 gateways and 3 repeaters each? 
4. If the random times range from 0.00 to 6.00 minutes instead of 0.00 to 5.00, how does that affect the total average time on 10 runs? What new problems does this cause? 
Considerations: 
The clock need not be in real time. The code should be easily understood. Structure the code to maximize its utility for future use. Adding future functionality should be relatively straightforward. 
