import csv
import os
import operator
import sys
from utils import *
import colorama
from colorama import Fore, Style, init


def find_by_name(nickname, graph):
    for s in graph:
        if s.nickname == nickname:
            return s

class Task:
    def __init__(self, line, graph):
        self.begin_start = -1
        self.begin_end = -1
        self.nickname = line[0]
        line.pop(0)
        self.name = line[0]
        line.pop(0)
        self.duration = int(line[0])
        line.pop(0)
        self.masters = line
        self.indegree = len(self.masters)
        self.time_range = 0

        self.slaves = []
        if find_by_name(self.nickname, graph):
            display_error('CANNOT GET TWO IDENTICAL OBJECTS')
        graph.append(self)


    def set_time_range(self):
        if self.begin_end is not -1:
            self.time_range = self.begin_end - self.begin_start

    def display_one(self):
        if self.begin_end is  -1:
            print("{} must begin at t={}".format(self.nickname, self.begin_start))
        else:
            print("{} must begin between t={} and t={}".format(self.nickname, self.begin_start, self.begin_end))

    def display_two(self):
        print(self.nickname, end='\t')
        print("(", self.time_range, ")", sep="", end='\t')

        print(" " * self.begin_start, end='')
        print("=" * self.duration)



def get_graph(filename):

    graph = []
    count = 0
    try:
        with open(filename, newline='') as tasks:
            lines = csv.reader(tasks, delimiter=';')

            for line in lines:
                if len(line) is not 0:
                    count += 1
                    Task(line, graph)
            if count is 0:
                display_error('THE FILE YOU PROVIDED IS EMPTY')

    except FileNotFoundError:
        display_error("FILE NOT FOUND")
    except OSError:
        display_error("OS ERROR")
        #print(f"OS error occurred trying to open {filename}", file=sys.stderr)
        #sys.exit(84)
    except Exception as err:
        print(f"Unexpected error opening {filename} is", repr(err))
        sys.exit(84)
    for task in graph:
        if task.masters:
           for ms in task.masters:
                master = find_by_name(ms, graph)
                if master:
                    master.slaves.append(task.nickname)
    for task in graph:
        if task.masters:
            for ms in task.masters:
                if ms in task.slaves:
                    display_error("CIRCLE DEPENDENCIES ARE NOT ALLOWED")

    return graph