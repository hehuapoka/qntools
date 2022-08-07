cmake_minimum_required(VERSION 3.5)

project(RemakeAssetui VERSION 0.1 LANGUAGES CXX)

set(CMAKE_INCLUDE_CURRENT_DIR ON)

set(CMAKE_AUTOUIC ON)
set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

set(QNTOOLS $ENV{QNTools})
set(USD_ROOT ${QNTOOLS}/libs/USD)
include_directories(${USD_ROOT}/include/boost-1_70)
include_directories(${QNTOOLS}/include)
#SET(CMAKE_INCLUDE_PATH ${CMAKE_INCLUDE_PATH} E:/Work/dev/qntools/libs/USD/include/boost-1_70)
#SET(CMAKE_LIBRARY_PATH ${CMAKE_LIBRARY_PATH} E:/Work/dev/qntools/libs/USD/lib)

# QtCreator supports the following variables for Android, which are identical to qmake Android variables.
# Check https://doc.qt.io/qt/deployment-android.html for more information.
# They need to be set before the find_package( ...) calls below.

#if(ANDROID)
#    set(ANDROID_PACKAGE_SOURCE_DIR "${CMAKE_CURRENT_SOURCE_DIR}/android")
#    if (ANDROID_ABI STREQUAL "armeabi-v7a")
#        set(ANDROID_EXTRA_LIBS
#            ${CMAKE_CURRENT_SOURCE_DIR}/path/to/libcrypto.so
#            ${CMAKE_CURRENT_SOURCE_DIR}/path/to/libssl.so)
#    endif()
#endif()




#boost
#FIND_PACKAGE(Boost)
#IF (Boost_FOUND)
#    INCLUDE_DIRECTORIES(${Boost_INCLUDE_DIR})
#    ADD_DEFINITIONS( "-DHAS_BOOST" )
#ENDIF()



find_package(QT NAMES Qt6 Qt5 COMPONENTS Widgets REQUIRED)
find_package(Qt${QT_VERSION_MAJOR} COMPONENTS Widgets REQUIRED)

set(PROJECT_SOURCES
        main.cpp
        widget.cpp
        widget.h
        EnvUtils.cpp
        EnvUtils.h
        widget.ui
        pricesstexture.cpp
        pricesstexture.h
)

if(${QT_VERSION_MAJOR} GREATER_EQUAL 6)
    qt_add_executable(RemakeAssetui
        MANUAL_FINALIZATION
        ${PROJECT_SOURCES}
    )
else()
    if(ANDROID)
        add_library(RemakeAssetui SHARED
            ${PROJECT_SOURCES}
        )
    else()
        add_executable(RemakeAssetui
            ${PROJECT_SOURCES}
        )
    endif()
endif()

target_link_libraries(RemakeAssetui PRIVATE Qt${QT_VERSION_MAJOR}::Widgets PUBLIC ${USD_ROOT}/lib/boost_filesystem-vc142-mt-x64-1_70.lib PUBLIC ${QNTOOLS}/lib/qndll.lib)

set_target_properties(RemakeAssetui PROPERTIES
    MACOSX_BUNDLE_GUI_IDENTIFIER my.example.com
    MACOSX_BUNDLE_BUNDLE_VERSION ${PROJECT_VERSION}
    MACOSX_BUNDLE_SHORT_VERSION_STRING ${PROJECT_VERSION_MAJOR}.${PROJECT_VERSION_MINOR}
)

if(QT_VERSION_MAJOR EQUAL 6)
    qt_finalize_executable(RemakeAssetui)
endif()
