##
## EPITECH PROJECT, 2021
## 306radiator
## File description:
## Makefile
##

SRC     =       radiator.py

RM		=		@rm -f

TESTDIR	=	tests/

TESTSRC =	$(TESTDIR)test_pacman.py

NAME = 			306radiator

all:    		$(NAME)

$(NAME):
		cp $(SRC) $@
		chmod +x $@
clean:
		rm -f *~
fclean: clean
		rm -f $(NAME)
		rm -rf __pycache__
	
tests_run:	 fclean
			@echo -e "\nTHIS IS TEST RUN\n"
			@python3 -m pytest -v $(TESTSRC) --cov=. --cov-report=html

re:     fclean  all

.PHONY:	all clean fclean tests_run re
