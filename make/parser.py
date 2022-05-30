class Block:
    def __init__(self, target, src, builds):
        self.target = target ##target name
        self.src = src     ## list if src
        self.builds = builds  ## list of builds


def parse_lines(lines):

    blocks = []

    target = ""
    src = []
    builds = []

    for ln in lines:
        if ":" in ln:
            ##could check if the line is valid
            blk = Block(target, src, builds)
            blocks.append(blk)
            builds = []
            parts = ln.split(':')
            target = parts[0]
            src = parts[1].split()
        else:
            builds.append(ln)

    blk = Block(target, src, builds)
    blocks.append(blk)

    return blocks