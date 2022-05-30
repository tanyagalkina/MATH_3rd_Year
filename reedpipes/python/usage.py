
def out(r):
    print('\tr{}\tradius (in cm) of pipe at the {}cm abscissa'.format(r, r))


def display_help():
    print("USAGE:\n\t./308reedpipes r0 r5 r10 r15 r20 n\n")
    print("DESCRIPTION")
    out(0)
    out(5)
    out(10)
    out(15)
    out(20)
    print("\tn\tnumber of points needed to display the radius")


