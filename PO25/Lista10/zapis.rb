module Zapis
    def zapisz_stan(file_name)
        File.open(file_name, 'wb') do |file|
            Marshal.dump(self, file)
        end
    end

    def self.wczytaj_stan(file_name)
        File.open(file_name, 'rb') do |file|
            Marshal.load(file)
        end
    end
end