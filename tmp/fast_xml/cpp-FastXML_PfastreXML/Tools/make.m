mex -v CXXFLAGS='$CXXFLAGS -std=c++11 -O3' -largeArrayDims sparse_prod.cpp
mex -v CXXFLAGS='$CXXFLAGS -std=c++11 -O3' -largeArrayDims read_text_mat.cpp
mex -v CXXFLAGS='$CXXFLAGS -std=c++11 -O3' -largeArrayDims write_text_mat.cpp
mex -v CXXFLAGS='$CXXFLAGS -std=c++11 -O3' -largeArrayDims sort_sparse_mat.cpp

