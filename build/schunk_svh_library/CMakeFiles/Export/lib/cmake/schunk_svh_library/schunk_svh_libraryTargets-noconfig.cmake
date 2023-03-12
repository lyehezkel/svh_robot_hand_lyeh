#----------------------------------------------------------------
# Generated CMake target import file.
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "Schunk::svh-library" for configuration ""
set_property(TARGET Schunk::svh-library APPEND PROPERTY IMPORTED_CONFIGURATIONS NOCONFIG)
set_target_properties(Schunk::svh-library PROPERTIES
  IMPORTED_LOCATION_NOCONFIG "${_IMPORT_PREFIX}/lib/libsvh-library.so"
  IMPORTED_SONAME_NOCONFIG "libsvh-library.so"
  )

list(APPEND _IMPORT_CHECK_TARGETS Schunk::svh-library )
list(APPEND _IMPORT_CHECK_FILES_FOR_Schunk::svh-library "${_IMPORT_PREFIX}/lib/libsvh-library.so" )

# Import target "Schunk::svh-serial" for configuration ""
set_property(TARGET Schunk::svh-serial APPEND PROPERTY IMPORTED_CONFIGURATIONS NOCONFIG)
set_target_properties(Schunk::svh-serial PROPERTIES
  IMPORTED_LOCATION_NOCONFIG "${_IMPORT_PREFIX}/lib/libsvh-serial.so"
  IMPORTED_SONAME_NOCONFIG "libsvh-serial.so"
  )

list(APPEND _IMPORT_CHECK_TARGETS Schunk::svh-serial )
list(APPEND _IMPORT_CHECK_FILES_FOR_Schunk::svh-serial "${_IMPORT_PREFIX}/lib/libsvh-serial.so" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
