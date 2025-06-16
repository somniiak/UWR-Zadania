# Artur Dzido
# Lista 9
# Ruby 3.3.8

require_relative 'gra'
require_relative 'gracz_bot'
require_relative 'gracz_czlowiek'

SAVE_FILE = 'state.dat'

if File.exist?(SAVE_FILE)
    puts "Znaleziono zapisany stan gry. Czy chcesz wznowić? (T/N)"
    print "(Input)> "
    inp = gets.chomp.downcase
    if inp == 't'
        gra = Zapis.wczytaj_stan(SAVE_FILE)
    else
        File.delete(SAVE_FILE)
    end
end

if gra.nil?
    player = GraczCzlowiek.new("Gregg")
    bot = GraczBot.new("Tux")
    gra = Gra.new([player, bot])
end

# Pułapka na sygnał INT (interrupt), czyli CTRL+C
trap("INT") do
    puts "\nZapisuję stan gry..."
    gra.zapisz_stan(SAVE_FILE)
    puts "Stan gry zapisany."
    exit
end  

gra.play_game
