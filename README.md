![alt text](https://img.shields.io/badge/status-stable-brightgreen)

# virat_fake

Package containing fake nodes for debugging and demonstration purposes

Nodes
-----

* fake_path

    * Sends fake path coordinates to follow, useful for controller debugging and demo

Dependancies
------------

* virat_msgs


Usage
-----

#### Send fake path coordintes to controller

Initialise controller (Important !)

```bash
roslaunch mpc_controller controller_init.launch
```

Send fake path coordinates

```bash
roslaunch virat_fake send_fake_path.launch
```

#### Visualize paths in rviz

Launch world

```bash
roslaunch virat_gazebo igvc_basic.launch
```

Launch rviz

```bash
roslaunch virat_gazebo virat_rviz.launch
```

Initialise Controller

```bash
roslaunch virat_controller controller_init.launch
```

Send fake path to controller (or use path from path planning module)

```bash
roslaunch virat_fake send_fake_path.launch
```
