Task Definition
  - [] Clear description of the chosen task
  - [] Identification of constraints and challenges
Task Decomposition
  - [] Break down the complex task into basic operations
  - [] Identify the critical path and potential bottlenecks
Motion Planning Strategy
  - [] Design movement sequences
  - [] Consider obstacle avoidance
Implementation Plan
  - [] Develop modular code structure (pseudo code is sufficient)
  - [] Include error handling and recovery
  - [] Define success criteria


# problem definition
## motivation
when i was in boarding school there was a food hall, and at the end of each meal you had to
load a conveyor belt connected to a dishwasher and two other students had an hour shift
of sorting the foodware after it passes through the dishwasher.

here is an illustration
![similar dishwasher](./RCDH-23410934.jpg)

this inspired me to define the following task

## task description
students put their trays with the foodware on a table and robots will do the following for each
item to replace the students
1. remove large pieces of food from it
2. load it to the conveyor belt to the dishwasher
3. offload the item to the correct stack depending on the type of foodware*

*the types of foodware are tray, plate, bowl, cup, fork, spoon, and knife.

## implementation strategy
to replace the students we need robots at two stations one to replace the students at tasks 1,2, and
another to replace the students at task 3.

we'll define a Layered Control Architecture (LCA)
![LCA](./LCA.png)


## expected challenges
- although the task is mostly automated, there still will be some manual intervention required
for things such as waste disposal, and picking up the clean items. that means that the robots
will have some interaction with unpredictable humans.
- there was high variance in the amount of work, thats to say the amount of students finishing
to eat is inconsistent, there can be 12 trays a minute which can be a lot of work.
- there would be food on the surface of the foodware, which can create a challenge for the robots to pick up.


# technical documentation
## task planning breakdown


## algorithm descriptions


## code documentation


## test results


# implementation
## working code or pseudo code


## performance analysis
