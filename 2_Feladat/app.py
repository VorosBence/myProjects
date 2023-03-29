from readFile import *
from compute import *



if __name__ == '__main__':
    db = readFile()
    StepCompute = Compute(db)
    StepCompute.searchLoop()

