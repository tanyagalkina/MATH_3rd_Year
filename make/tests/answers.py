


FIRST_TEST = "\
[0 0 1 0 0 0]\n\
[0 0 1 0 0 1]\n\
[0 0 0 1 0 0]\n\
[0 0 0 0 0 0]\n\
[0 0 0 0 0 1]\n\
[0 0 0 1 0 0]\n\
\n\
fc.c -> fc.o -> tty\n\
fc.h -> fc.o -> tty\n\
fc.h -> tty.o -> tty\n\
fc.o -> tty\n\
tty.c -> tty.o -> tty\n\
tty.o -> tty\n"

FIRST_TEST_BREADTH = "\
cc -c fc.c\n\
cc -c tty.c\n\
cc -o tty tty.o fc.o\n"

TWO_COMMANDS = "\
compilation_command => 1\n\
compilation_command => 2\n"

TWO_TEST_BREADTH = "\
cc -c tty.c\n\
cc -o tty tty.o fc.o\n"

CRAZY_FILE_AA = "\
building aa into  ba\n\
building aa into  ca\n\
building ca into da\n\
building ba and da into ea\n"

CRAZY_FILE_BA = "building ba and da into ea\n"

CRAZY_FILE_CA = "\
building ca into da\n\
building ba and da into ea\n"

