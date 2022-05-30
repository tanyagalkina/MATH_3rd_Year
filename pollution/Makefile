##
## EPITECH PROJECT, 2021
## 308reedpipes
## File description:
## Makefile
##

SRC     =		./python/pollution.py			\
				./python/errors.py				\
				./python/usage.py				\
				./python/calc.py

RM		=		@rm -f

TESTDIR	=	./python/tests/

TESTSRC =	$(TESTDIR)test_reedpipes.py

NAME = 			309pollution

all:    		$(NAME)

$(NAME):
		cp $(SRC) .
		cp pollution.py $@
		
		chmod +x $@
clean:
		rm -f *~
fclean: clean
		rm -f $(NAME)
		rm -f *.py
		rm -rf __pycache__
	
tests_run:	 fclean
			@echo -e "\nTHIS IS TEST RUN\n"
			@python3 -m pytest -v $(TESTSRC) --cov=. --cov-report=html

re:     fclean  all

.PHONY:	all clean fclean tests_run re
