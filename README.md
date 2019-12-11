## Environment Tests

The three environment tests are test_empty_env.py, test_small_package.py, and test_large_package.py, which test environment creation with different sizes of environments. These can be modified as necessary to run through environment creation an arbitrary number of times, and the test programs can be changed to import different libraries, import multiple libraries, etc.

## Serialization Tests

The test_functions.py script has several different Python functions that are serialized using different methods. The functions differ in their length, their "closure" (including global variables, outside function calls, etc.) and their imports. Note that Parsl functions have no external closure but rather are "pure" functions, so some of these functions would not work within a Parsl workflow. The test_serialization.py script runs the different serialization methods with these functions and prints the result times.
