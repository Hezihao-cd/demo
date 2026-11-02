cmake_minimum_required(VERSION 3.16)
project(hello LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

if(NOT CMAKE_BUILD_TYPE)
    set(CMAKE_BUILD_TYPE "Debug" CACHE STRING "Build type" FORCE)
endif()

file(GLOB_RECURSE APP_SRC "APP/*.c*")
add_executable(hello ${APP_SRC})
target_include_directories(hello PRIVATE ${CMAKE_CURRENT_SOURCE_DIR}/APP)
