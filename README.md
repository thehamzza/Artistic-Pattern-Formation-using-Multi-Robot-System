This project describes the work on multi-robot pattern formation on any kind of 
arbitrary target patterns with the help of optimal robot deployment, using a method 
that is independent of the number of robots with having utilized the least possible 
resources necessary to achieve the desired goal of non-intersecting pattern or 
design formation. Generation of uniform sets of goal positions, allocation of the 
multi-robots on the respective goal assignments having optimal path and fast 
convergence into consideration and finally smooth deployment of robots to avoid 
collisions using distributed collision avoidance methods to consequently provide a 
representative set of desired patterns. In this method, the trajectories are visually 
appealing in the sense of being smooth, oscillation free, and showing fast 
convergence having used the reliable positioning and assignment algorithms to 
generate both visually and convincing final pattern formation by optimizing the 
robots’ goal positions as well as simple and smooth robot motions at the transitions 
of patterns.

Points to Remember:

1) delauny_voroni.py  and edgeDetection.py are python files that can be run in any IDE

2) hungarian_collision.py is python file that runs perfectly fine, but due to its 
scientific plots, many free software IDE don't support its visual outputs.

3) so we created one google colab file of hungarian and collision avoidance algorithm;
that is hungarian_collision.ipynb
it can be run on google colab, which supports scientific and advance plotting.

4) All test image files should be in the working directory

5) Do not change points text files, the program updates them automatically according to 
the assigned shape.

6) You can select the number of points that you want to keep out of canny
edge detection, in edge detetion file, other points will be eliminated.

7) You can select the number of robots also, by changing the variable number 
in hungarian file.

8) To use another image in hungarian_collision file, since we will be using another directory 
than delauny_voronoi, so update the points file manually. If all 3 files were running on 1 directory,
then it would not cause any problem.

Thank You
Regards,
M Hamza
