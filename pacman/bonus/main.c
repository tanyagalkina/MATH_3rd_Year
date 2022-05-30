#include <ncurses.h>
#include <curses.h>
#include <string.h>
#include <unistd.h>
#include <stdio.h>
#include <time.h>
#include <stdlib.h>

int getX(char *str)
{
    int pos;
    int len = strlen(str);

    if (len == 7) {
        pos =  (int)(str[1] - '0');
    }
    if (len == 13) {
        pos =  (int)(str[7] - '0');
    }
    return pos;
}

int getY(char *str)
{
    int pos;
    int len = strlen(str);

    if (len == 7) {
        pos = (int)(str[4] - '0');
    }
    if (len == 13) {
        pos =  (int)(str[10] - '0');
    }
    return pos;
}

void createColor() 
{
    start_color();

    init_pair(1, COLOR_YELLOW, COLOR_YELLOW);
    init_pair(2, COLOR_RED, COLOR_RED);
    init_pair(3, COLOR_MAGENTA, COLOR_MAGENTA);
    init_pair(4,COLOR_BLUE, COLOR_BLUE);
}

bool printMap(char **map, char *newpos) {
    int len = strlen(newpos);
    int newi = getX(newpos);
    int newj = getY(newpos);
    int pos[2] = {0, 0};

    createColor();
    for (int i = 0; map[i] != NULL; i++) {
        for (int j = 0; map[i][j] != '\0'; j++) {
            if (map[i][j] == '1') {
                attron(A_BOLD | COLOR_PAIR(2));
                mvprintw(LINES/2 + i, ((COLS / 2) - (1 / 2)) + j, "+");
                attroff(A_BOLD | COLOR_PAIR(2));
            } if (map[i][j] == '0' || map[i][j] == 'F') {
                attron(A_BOLD | COLOR_PAIR(5));
                mvprintw(LINES/2 + i, ((COLS / 2) - (1 / 2)) + j, "_");
                attroff(A_BOLD | COLOR_PAIR(5));
            } if (map[i][j] == 'P') {
                attron(A_BOLD | COLOR_PAIR(1));
                mvprintw(LINES/2 + i, ((COLS / 2) - (1 / 2)) + j, "P");
                attroff(A_BOLD | COLOR_PAIR(1));
                pos[0] = i;
                pos[1] = j;
            } if (i == newi && j == newj) {
                attron(A_BOLD | COLOR_PAIR(3));
                mvprintw(LINES/2 + i, ((COLS / 2) - (1 / 2)) + j, "F");
                map[i][j] = 'F';
                attroff(A_BOLD | COLOR_PAIR(3));
            }
        }
    }
    return false;
}

char **getMap(char *str) {
    char *nmap = NULL;
    size_t lmap = 0;
    ssize_t read = 0;
    FILE *i = fopen(str, "r");
    char **map = NULL;
    int l = 0;
    int tmp = 0;
    char *lol = NULL;

    for (; (read = getline(&nmap, &lmap, i)) != -1; l++);
    map = malloc(sizeof(char *) * (l + 1));
    fseek(i, 0, SEEK_SET);
    int j = 0;
    while(l != 0) {
        getline(&nmap, &lmap, i);
        lol = strdup(nmap);
        map[j] = lol;
        j++;
        l--;
    }
    map[j] = NULL;
    return map;
}

int main(int argc, char **av)
{
    char *pos = NULL;
    size_t lpos = 0;
    FILE *j = fopen(av[2], "r");
    ssize_t read = 0;
    time_t *start = malloc(sizeof(time_t));
    time(start);
    time_t *now = malloc(sizeof(time_t));
    int len = 0;
    char **map = getMap(av[1]);

    initscr();
    curs_set(0);
    while (1) {
        clear();
        time(now);
        if (*now - *start >= 1) {
            read = getline(&pos, &lpos, j);
            if (read == -1) {
                break;
            }
            time(start);
            if (printMap(map, pos) == true)
                break;
            refresh();
        }
    }
    endwin();
    return 0;
}