cmake_minimum_required(VERSION 3.12)
project(test_cmake_arg)

macro(test_cmake_arg arg1 arg2) # macro(name arg1 arg2)
    message(STATUS "arg1: ${arg1}")
    message(STATUS "arg2: ${arg2}")
    message(STATUS "arg1: ${ARGV0}") # 第一个参数
    message(STATUS "arg1: ${ARGV1}") # 第二个参数
    message(STATUS "arg rest: ${ARGN}") # 实际参数个数大于形参时，余下参数被ARGN捕获
    message(STATUS "number of args: ${ARGC}") # 参数个数
    message(STATUS "all args: ${ARGV}") # 所有参数
endmacro(test_cmake_arg) # endof macro

test_cmake_arg(1 2 3 4) # arg1 <- 1, arg2 <- 2, ARGN <- 3, 4

#output:
#-- arg1: 1
#-- arg2: 2
#-- arg1: 1
#-- arg1: 2
#-- arg rest: 3;4
#-- number of args: 4
#-- all args: 1;2;3;4

test_cmake_arg(arg1 arg2) # arg1 <- arg1, arg2 <- arg2, ARGN <- ()
#output:
#-- arg1: arg1
#-- arg2: arg2
#-- arg1: arg1
#-- arg1: arg2
#-- arg rest: 
#-- number of args: 2
#-- all args: arg1;arg2

test_cmake_arg(arg1) # 传参个数必须大于等于形参，否则编译不过
#output:
#CMake Error at CMakeLists.txt:36 (test_cmake_arg):
#  test_cmake_arg Macro invoked with incorrect arguments for macro named:
#  test_cmake_arg