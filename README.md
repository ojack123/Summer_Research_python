# Time-Varying, Transition-Based, Rapidly-exploring Random Trees:

## File Descriptions:
``` t_rrt_time_varied.py``` 
- Main file. Run this to aquire path information for the user-specified map and actor vehicles.
- Map, actors, and starting conditions may be adjusted in ```main()```
- Current map setup is identical to that of Evan's three-lane highway scenario

``` plot_path.py ```
- Plots the specified path over time.
- Allows you to visualize the path as the threat field changes with time.

``` actor_motion.py``` 
- Aquires actor motion information from ```./car_info/``` and returns their encoded velocity and heading angles

``` json_converter.py```
- Aquires JSON-formatted data generated in ```t_rrt_time_varied.py```
- Writes necessary ego vehicle path information to ```./car_info/car_0.txt``` for use with the Carla driving simulator

```rrt.py```
- Unmodified RRT searching algorithm written by AtsushiSakai(@Atsushi_twi)

```t_rrt.py``` 
- Transition-based RRT searching algorithm with non-time varying threat field.


## Directories
``` ./out/```
- Location for path information and path image generated by ```t_rrt_time_varied.py```
  - **Note:** Remember to rename ```path_information.txt``` and ```path_output.png``` if you intend to save the most recent path information so it doesn't get overwritten.

``` ./saved_paths/```
- Various saved T-RRT-TV scenarios generated thoughout the development of the searching algorithm 
- May be visuallized by calling them in ```plot_path.py```

```./videos_and_images/```
- Various saved results generated throughout the development of the searching algorithm

```./videos_and_images/paper_media/```
- Contains results created for use in the recent paper

``` ./car_info/```
- Contains ego and actor vehicle information for use in the Carla driving simulator
- ```car_0.txt``` is the ego vehicle, with motion information updated automatically after running ```t_rrt_time_varied.py```
  - **Note:** Remember to rename ```car_0.txt``` if you intend to save the most recent path information so it doesn't get overwritten.
- ```car_[1-3].txt``` are actor vehicles with motion identical to those in Evan's 4D Dikjstra highway scenario

