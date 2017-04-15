project(ros_package_pip_depends)
cmake_minimum_required(VERSION 3.0.0)

find_package(catkin REQUIRED COMPONENTS
  rospy
)

catkin_python_setup()

catkin_package(
    CATKIN_DEPENDS rospy
)

catkin_install_python(PROGRAMS
    nodes/example
    DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)