
import operator
from errors import check_args, check_src
from parser import parse_lines, Block



class Source:
    def __init__(self, name):
        self.name = name
        self.slaves = []
        self.masters = []
        self.builds = []
        self.build_strings = []
        self.level = -1
        self.stage = -1
        self.built = False


def is_in_sources(name, src):
    for s in src:
        if s.name == name:
            return True
    return False


def create_src(src, blk, s):
    if not is_in_sources(s, src):
        new_source = Source(s)
        src.append(new_source)
    for sr in src:
            if sr.name == s:
                if blk.target not in sr.slaves:
                    sr.slaves.append(blk.target)
                    sr.slaves.sort()
                for bb in blk.builds:
                    if bb not in sr.build_strings:    
                        sr.build_strings.append(bb)



def fill_in_sources(src, blocks):
    for blk in blocks:
        if blk.target and not is_in_sources(blk.target, src):
            new_source = Source(blk.target)
            src.append(new_source)
        for s in src:
            if s.name == blk.target:
                s.builds = blk.builds
                for sr in blk.src:
                    s.masters.append(sr)
            for sr in blk.src:
                create_src(src, blk, sr)


def get_sources(av):

    lines = check_args(av)
    blocks = parse_lines(lines)
    src = []

    fill_in_sources(src, blocks)
    sorted_src = sorted(src, key=operator.attrgetter('name'))

    check_src(sorted_src)
    return sorted_src