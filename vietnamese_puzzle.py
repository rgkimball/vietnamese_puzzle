# rgkimball - rgk.io
# 2016/12/10

from __future__ import division
from timeit import default_timer as timer
import itertools

def run():

  start = timer()

  global folder
  folder = ".\\solutions\\"

  set = getset()

  for i in solutionrange():
    testformula(set, i)

  end = timer()
  runtime = (end - start)
  print "Script finished; ran in %.4f second(s)." % float(runtime)


def getset():
  return range(1,10)


def solutionrange():
  return range(-1,250)


def testformula(set,answer):

  if len(set) != 9:
    print "Invalid set length: %d" % len(set)
    return False

  solution_set = list()

  for this_set in itertools.permutations(set):
    result = this_set[0] + (13 * this_set[1] / this_set[2]) + this_set[3] + (12 * this_set[4]) - this_set[5] - 11 + (this_set[6] * this_set[7] / this_set[8]) - 10

    if round(result,4) == answer:
      # print str(this_set) + " = " + str(result)
      solution_set.append(this_set)

  found_str = "%d: %d solutions found" % (answer, len(solution_set))
  print found_str

  f = open(folder + str(answer) + ".txt", 'w')
  f.write(found_str)
  for set in solution_set:
    f.write("\n" + str(set))
  f.close()

run()
