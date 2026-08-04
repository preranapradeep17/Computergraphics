cmake_minimum_required(VERSION 3.10)

project(ComputerGraphics)

set(CMAKE_CXX_STANDARD 17)

find_package(glfw3 REQUIRED)

include_directories(include)

add_executable(ComputerGraphics
    src/main.cpp
    src/glad.c
)

target_link_libraries(ComputerGraphics
    glfw
    "-framework OpenGL"
    "-framework Cocoa"
    "-framework IOKit"
    "-framework CoreVideo"
)