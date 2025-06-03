#ifndef GAME_HPP
#define GAME_HPP

#include <map>
#include <ctime>
#include <string>
#include <iostream>

#include "exceptions.hpp"

class Game
{
    private:
        bool game_status = true;
        std::time_t game_start_time;
        int board[7][7] = {};
        int pieces = 32;

    public:
        Game();
        void draw_board();
        bool is_valid_move(int c, int r, char d);
        void make_move(int c, int r, char d);
        void get_input(std::string msg = " ");
        void scoreboard();
};

#endif