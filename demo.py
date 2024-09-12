import os
import sys

import the_Owl_witches_duel.programsRunner

os.chdir("the_Owl_witches_duel")
print(os.getcwd())
sys.path.insert(0, os.getcwd())

the_Owl_witches_duel.programsRunner.main()
