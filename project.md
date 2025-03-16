# problem definition
## motivation
when i was in boarding school there was a food hall, and at the end of each meal you had to
load a conveyor belt connected to a dishwasher and two other students had an hour shift
of sorting the foodware after it passes through the dishwasher.

here is an illustration of a dishwasher
![similar dishwasher](./RCDH-23410934.jpg)

this inspired me to define the following task

## task description
students put their trays with the foodware on a table and robots will do the following for each
item to replace the students
1. remove large pieces of food from it
2. load it to the conveyor belt to the dishwasher
3. offload the item to the correct stack depending on the type of foodware*

*the types of foodware are tray, plate, bowl, cup, fork, spoon, and knife.

a tray
![tray](./tray.png)

## implementation strategy
to replace the students we need robots at two stations, one to replace the students at tasks 1, 2,
and another to replace the students at task 3.

here are the two robots
![robots](./robots.jpeg)
for both of them we'll use a Layered Control Architecture (LCA)
![LCA](./LCA.png)

## expected challenges
the challenge
- although the task is mostly automated, there still will be some manual intervention required
for things such as waste disposal, and picking up the clean items. that means that the robots
will have some interaction with unpredictable humans.
- there was high variance in the amount of work, thats to say the amount of students finishing
to eat is inconsistent, there can be 12 trays a minute which can be a lot of work.
- there would be food on the surface of the foodware, which can create a challenge for the robots
in the pick up stage.

how we will address these challenges
- for some parts such as picking up the clean items the human can wait for the robot to move,
and the robot can replan it's movement when it sees it surroundings change.
for other parts such as waste disposal, we'll add a pause button.
- we can have more than one robot at each station to handle the extra work.
- we can choose a gripper that can grip in many different ways to minimize the chance
of having to pick up in a dirty surface, have a place to clean the gripper.
we can also have a small hose to clean a place to grip.

# technical documentation
each stage of the technical documentation we'll do the for both robots.
we'll use RRT* for motion planning.

## task planning breakdown
first robot - let's break down stages 1, and 2.
planning
1. choose which of the foodware it can pick up.
2. pick it up.
3. decide there is a need to remove food from it's surface, if so, use the hose to remove the food.
4. put on conveyor belt
5. clean the gripper using the hose

second robot - now let's break down stage 3
planning
1. choose which of the foodware it can pick up.
2. pick it up.
3. put it in the right stack

## algorithm descriptions
choosing which foodware to pick up - using vision determine which foodware doesn't have other foodware on it, segment it
and determine it's position and type so the robot would know how to pick it up.

cleaning foodware - using vision determine if the foodware is dirty, if so, use the hose to clean it.

picking up foodware - using our knowledge of the foodware's type and position, the robot knows where to move to and grip it.

move the foodware
1. using vision and our knowledge of the foodware type determine where it is
2. depending on the task determine where it should be placed
3. plan the movement to the foodware for pick up, and move
4. grasp
5. plan the movement to the desired end location and orientation, and move
6. ungrasp it.

# implementation
## working code or pseudo code

## Error handling
the error handling would be the constant monitoring to determine what is our state, and replan
what the robot should do. for extreme cases we have a pause button.

## success criteria
the robot is successful if
- it can handle a tray in under 10 seconds
- it for 99% of the time it doesn't need an intervention from a human
- the foodware ends up clean, and sorted
- it doesn't harm the people around it
