# This entrypoint file to be used in development. Start by reading README.md
import mean_var_std
import reshape_list
from unittest import main

#print(reshape_list.reshape([0,1,2,3,4,5,6,7,8]))
mean_var_std.calculate([0,1,2,3,4,5,6,7,8])

# Run unit tests automatically
main(module='test_module', exit=False)