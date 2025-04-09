cmake_minimum_required(VERSION 3.5)
project(lidar_obstacle_detector)

# Enable C++14
set(CMAKE_CXX_STANDARD 14)
set(CMAKE_POSITION_INDEPENDENT_CODE ON)

# Find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(std_msgs REQUIRED)
find_package(sensor_msgs REQUIRED)
find_package(tf2 REQUIRED)
find_package(tf2_ros REQUIRED)
find_package(tf2_geometry_msgs REQUIRED)
find_package(PCL REQUIRED)
find_package(Eigen3 REQUIRED)

# Optional: Replace or re-implement dynamic reconfigure if needed
# find_package(dynamic_reconfigure REQUIRED)

include_directories(
  include
  ${EIGEN3_INCLUDE_DIRS}
  ${PCL_INCLUDE_DIRS}
)

# Build the library
add_library(${PROJECT_NAME}
  src/obstacle_detector.cpp
)
ament_target_dependencies(${PROJECT_NAME}
  rclcpp
  std_msgs
  sensor_msgs
  tf2
  tf2_ros
  tf2_geometry_msgs
  PCL
)

# Build the executable
add_executable(obstacle_detector_node src/obstacle_detector_node.cpp)
target_link_libraries(obstacle_detector_node ${PROJECT_NAME})

ament_target_dependencies(obstacle_detector_node
  rclcpp
  std_msgs
  sensor_msgs
  tf2
  tf2_ros
  tf2_geometry_msgs
  PCL
)

# Install targets
install(TARGETS
  ${PROJECT_NAME}
  obstacle_detector_node
  DESTINATION lib/${PROJECT_NAME}
)

install(DIRECTORY include/
  DESTINATION include/
)

# Package export
ament_export_include_directories(include)
ament_export_dependencies(
  rclcpp
  std_msgs
  sensor_msgs
  tf2
  tf2_ros
  tf2_geometry_msgs
  PCL
)
ament_export_libraries(${PROJECT_NAME})

ament_package()

