#include "game.hpp"
#include "exceptions.hpp"

Game::Game() {
    for (int i = 0; i < 7; i ++) {
        for (int j = 0; j < 7; j++) {
            // Pole środkowe
            if (i == 3 && j == 3)
                continue;
            // Pola poza planszą
            if (i <= 1 || i >= 5) {
                if (j <= 1 || j >= 6)
                    continue;
            }
            // Rozstawienie pionków
            board[i][j] = 1;
        }
    }

    // Mierzenie czasu
    game_start_time = std::time(0);

    // Rozpoczęcie gry
    get_input();
}

void Game::draw_board() {
    // https://stackoverflow.com/questions/23369503/get-size-of-terminal-window-rows-columns

    // Wymiary okna
    int const WIDTH = WEXITSTATUS(std::system("exit `tput cols`"));
    int const HEIGHT = WEXITSTATUS(std::system("exit `tput lines`"));

    // Czyszczenie okna
    std::system("clear");

    // Znaki pionków
    std::string pieces[7][7];
    for (int i = 0; i < 7; i++) {
        for (int j = 0; j < 7; j++) {
            pieces[i][j] = board[i][j] == 1 ? "♟️" : " ";
        }
    }

    std::cout << std::string((HEIGHT - 21) / 2, '\n');
    std::cout << std::string((WIDTH - 29) / 2, ' ') << "    A | B | C | D | E | F | G    \n\n";
    std::cout << std::string((WIDTH - 34) / 2, ' ') << "            ┌───┬───┬───┐        \n";
    std::cout << std::string((WIDTH - 34) / 2, ' ') << "1           | " << pieces[2][0] << " | " << pieces[3][0] << " | " << pieces[4][0] << " |        \n";
    std::cout << std::string((WIDTH - 34) / 2, ' ') << "-           ├───┼───┼───┤        \n";
    std::cout << std::string((WIDTH - 34) / 2, ' ') << "2           | " << pieces[2][1] << " | " << pieces[3][1] << " | " << pieces[4][1] << " |        \n";
    std::cout << std::string((WIDTH - 34) / 2, ' ') << "-   ┌───┬───┼───┼───┼───┼───┬───┐\n";
    std::cout << std::string((WIDTH - 34) / 2, ' ') << "3   | " << pieces[0][2] << " | " << pieces[1][2] << " | " << pieces[2][2] << " | " << pieces[3][2] << " | " << pieces[4][2] << " | " << pieces[5][2] << " | " << pieces[6][2] << " |\n";
    std::cout << std::string((WIDTH - 34) / 2, ' ') << "-   ├───┼───┼───┼───┼───┼───┼───┤\n";
    std::cout << std::string((WIDTH - 34) / 2, ' ') << "4   | " << pieces[0][3] << " | " << pieces[1][3] << " | " << pieces[2][3] << " | " << pieces[3][3] << " | " << pieces[4][3] << " | " << pieces[5][3] << " | " << pieces[6][3] << " |\n";
    std::cout << std::string((WIDTH - 34) / 2, ' ') << "-   ├───┼───┼───┼───┼───┼───┼───┤\n";
    std::cout << std::string((WIDTH - 34) / 2, ' ') << "5   | " << pieces[0][4] << " | " << pieces[1][4] << " | " << pieces[2][4] << " | " << pieces[3][4] << " | " << pieces[4][4] << " | " << pieces[5][4] << " | " << pieces[6][4] << " |\n";
    std::cout << std::string((WIDTH - 34) / 2, ' ') << "-   └───┴───┼───┼───┼───┼───┴───┘\n";
    std::cout << std::string((WIDTH - 34) / 2, ' ') << "6           | " << pieces[2][5] << " | " << pieces[3][5] << " | " << pieces[4][5] << " |        \n";
    std::cout << std::string((WIDTH - 34) / 2, ' ') << "-           ├───┼───┼───┤        \n";
    std::cout << std::string((WIDTH - 34) / 2, ' ') << "7           | " << pieces[2][6] << " | " << pieces[3][6] << " | " << pieces[4][6] << " |        \n";
    std::cout << std::string((WIDTH - 34) / 2, ' ') << "            └───┴───┴───┘        \n";
    std::cout << std::string(HEIGHT / 2 - 8, '\n');
}

bool Game::is_valid_move(int c, int r, char d) {
    // Pole docelowe pionka
    int target_col;
    int target_row;

    // Pole atakowanego pionka
    int attacked_col;
    int attacked_row;

    switch (d) {
        case 'U':
            target_col = c;
            target_row = r - 2;
            attacked_col = c;
            attacked_row = r - 1;
            break;
        case 'D':
            target_col = c;
            target_row = r + 2;
            attacked_col = c;
            attacked_row = r + 1;
            break;
        case 'L':
            target_col = c - 2;
            target_row = r;
            attacked_col = c - 1;
            attacked_row = r;
            break;
        case 'R':
            target_col = c + 2;
            target_row = r;
            attacked_col = c + 1;
            attacked_row = r;
            break;
        default:
            return false;
    }

    // Pola poza planszą
    if (c <= 1 || c >= 5) {
        if (r <= 1 || r >= 5) {
            return false;
        }
    }
    if (c < 0 || c > 6 || r < 0 || r > 6)
            return false;
    if (target_col <= 1 || target_col >= 5) {
        if (target_row <= 1 || target_row >= 5) {
            return false;
        }
    }
    if (target_col < 0 || target_col > 6 || target_row < 0 || target_row > 6)
            return false;

    // Bicie z pustego pola
    if (board[c][r] == 0)
        return false;

    // Przeskakiwane pole puste
    if (board[attacked_col][attacked_row] == 0)
        return false;

    // Pole zajęte
    if (board[target_col][target_row] == 1)
        return false;

    return true;
}

void Game::make_move(int c, int r, char d) {
    std::string msg;

    // Pole docelowe pionka
    int target_col;
    int target_row;

    // Pole atakowanego pionka
    int attacked_col;
    int attacked_row;

    try {
        switch (d) {
            case 'U':
                target_col = c;
                target_row = r - 2;
                attacked_col = c;
                attacked_row = r - 1;
                break;
            case 'D':
                target_col = c;
                target_row = r + 2;
                attacked_col = c;
                attacked_row = r + 1;
                break;
            case 'L':
                target_col = c - 2;
                target_row = r;
                attacked_col = c - 1;
                attacked_row = r;
                break;
            case 'R':
                target_col = c + 2;
                target_row = r;
                attacked_col = c + 1;
                attacked_row = r;
                break;
            default:
                throw niepoprawny_kierunek();
        }

        // Niepoprawnych ruch
        if (!is_valid_move(c, r, d))
           throw niedozwolony_ruch();

        board[c][r] = 0;
        board[attacked_col][attacked_row] = 0;
        board[target_col][target_row] = 1;
        pieces--;

        msg =
            std::string(1, 'A' + c) + std::to_string(r + 1) + "->" +
            std::string(1, 'A' + target_col) + std::to_string(target_row + 1) +
            "\t(Bicie " + std::string(1, 'A' + attacked_col) + std::to_string(attacked_row + 1) + ")";
    }

    catch (const wyjatek_samotnika& e) {
        msg = e.what();
    }

    get_input(msg);
}

void Game::get_input(std::string msg) {
    std::string move;
    std::string error_msg = msg;

    int col;
    int row;
    char dir;

    // Sprawdzanie dostępności ruchów
    int available_moves = 0;
    for (int i = 0; i < 7; i ++) {
        for (int j = 0; j < 7; j++) {
            // Pola poza planszą
            if (i <= 1 || i >= 5) {
                if (j <= 1 || j >= 5)
                    continue;
            }
            for (char d : {'U', 'D', 'L', 'R'}) {
                if (is_valid_move(i, j, d))
                    available_moves++;
            }
        }
    }
    if (available_moves == 0)
        game_status = false;

    while (game_status) {
        draw_board();

        std::cout << error_msg;
        std::cout << "\nInput> ";
        std::cin >> move;

        // Wyjście
        if (move == "exit")
            game_status = false;

        // Sprawdzanie wejście
        try {
            // Błędne wejście
            if (move.size() != 3)
                throw niepoprawny_format();

            // Blędna kolumna
            if (toupper(move[0]) < 'A' || toupper(move[0]) > 'G')
                throw niepoprawna_kolumna();

            // Błędny wiersz
            if (move[1] - '0' < 1 || move[1] - '0' > 7)
                throw niepoprawny_wiersz();

            col = toupper(move[0]) - 'A';
            row = move[1] - '0' - 1;
            dir = toupper(move[2]);

            break;
        }

        catch (const wyjatek_samotnika& e) {
            error_msg = e.what();
        }
    }
    
    if (game_status)
        make_move(col, row, dir);
    else
        scoreboard();
}

void Game::scoreboard() {
    draw_board();

    // Czas gry
    std::time_t game_end_time = std::time(0);
    double game_total_time = game_end_time - game_start_time;
    int time_mins = game_total_time / 60;
    int time_secs = game_total_time - time_mins * 60;
    std::string time_str =
        std::to_string(time_mins) + "m" +
        std::to_string(time_secs) + "s";

    // Statystki gry
    if (pieces == 1)
        std::cout << "WYGRANA\n";
    else
        std::cout << "PRZEGRANA\n"; 
    std::cout << "CZAS:" << time_str << "\n";
    std::cout << "PIONKI:" << pieces << "\n";
}