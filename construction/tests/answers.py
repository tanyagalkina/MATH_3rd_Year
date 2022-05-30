#put your defines here =>


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

FIRST_TEST = "\
"

WRONG_NUMBER_ARGS = "\
Wrong number of args, please try with -h ...\n"

HOUSE_ANSWER = "\
Total duration of construction: 28 weeks\n\n\
Lan must begin at t=0\n\
Fou must begin at t=3\n\
Car must begin at t=11\n\
Mas must begin between t=11 and t=13\n\
Cov must begin at t=15\n\
Ele must begin at t=17\n\
Plu must begin at t=18\n\
Hea must begin between t=18 and t=25\n\
Fin must begin at t=19\n\n\
Lan\t(0)\t===\n\
Fou\t(0)\t   ========\n\
Car\t(0)\t           ====\n\
Mas\t(2)\t           ====\n\
Cov\t(0)\t               ==\n\
Ele\t(0)\t                 =\n\
Plu\t(0)\t                  =\n\
Hea\t(7)\t                  ===\n\
Fin\t(0)\t                   =========\n"