# YouTube Music Player


## Wymagania wstępne

 - Python 3.8+
 - FFmpeg (wymagany do konwersji audio)
 - System operacyjny: Linux (zalecany) lub Windows

**Uwaga dla użytkowników Windowsa:** Należy zastąpić wszystkie wystąpienia `python3` na `py` w poniższych poleceniach.


## Instalacja

Przed użyciem aplikacji należy pobrać wymagane pakiety. Polecam także stworzyć środowisko wirtualne do uruchamiania projektu.

Stworzenie i uruchomienie środowiska:
```
python3 -m venv .venv
. .venv/bin/activate
```

Na Windowsie środowisko można otworzyć poleceniem:
```
.venv\Scripts\activate
```

Na koniec instalujemy pakiety:
```
python3 -m pip install -r requirements.txt
```


## Uruchamianie

Gdy uruchomimy środowisko wirtualne, możemy otworzyć aplikację poleceniem:
```
python3 app.py
```

Korzystanie z aplikacji:
 - Utwory można wyszukiwać za pomocą paska wyszukiwania na górze ekranu.
 - Wybrany utwór można odtworzyć, klikając na niego lub klawisz enter.
 - Wybranie innego utworu dodaje go na początek kolejki i zaczyna odtwarzanie.
 - Kolejkę utworów można kontrolować za pomocą przycisków w menu odtwarzania.

Skróty klawiszowe:
 - `Spacja` -  wstrzymanie odtwarzania
 - `Ctrl+A` - dodanie wszystkich utworów do kolejki
 - `A` - dodanie wybranego utworu do kolejki
 - `N` - przejście do następnego utworu
 - `P` - przejście do poprzedniego utworu


## Użyte klasy
- **SearchScreen**: Ekran główny z wyszukiwarką i listą utworów.
- **QueueInfo**: Informacje o kolejce i operacje na niej.
- **PlayerLoader**: Ekran ładowania podczas pobierania utworu.
- **PlayerMenu**: Menu odtwarzacza.
- **PlayerControls**: Przyciski sterujące odtwarzaniem.
- **PlayerProgress**: Pasek postępu i czas utworu.
- **AudioServer**: Obsługa odtwarzania audio przez `pygame`.
- **VideoDatabase**: Obsługa lokalnej bazy danych utworów.
- **QueueManager**: Zarządzanie kolejką utworów.

## Użyte wzorce projektowe

- **Singleton**: `VideoDatabase` sprawdza, czy dostępna jest baza danych z informacjami o utworach i korzysta z już utworzonej. W przeciwnym wypadku tworzona i używana jest nowa.
- **Obserwator**: `PlayerProgress`, `PlayerControls` i `PlayerLoader` reagują na zmiany stanu `AudioServer` lub `YoutubeVideo`.
- **Polecenie**: Skróty klawiszowe w `SearchScreen` kontrolują działanie `PlayerControls` i `QueueManager`.
- **Fasada**: Klasa `AudioServer` za pomocą prostych metod ułatwia kontrolę nad działaniem odtwarzania audio przez `pygame`. Podobnie, `VideoDatabase` ułatwia korzystanie z bazy danych z utworami.
- **Prototyp**: Klasy elementów menu dziedzicząpo wbudowanych klasach framworka Textual (`PlayerProgress` - `Static`, `PlayerMenu` - `Container`, etc.)
- **Kompozyt**: Cały interfejs graficzny podzielony jest na klasy które tworzą jednolitą całość, a każda spełnia swoją odrębną funkcję.
- **Stan**: Przyciski odtwarzacza zmieniają swoje zachowanie na podstawie stanu pobranego z `AudioServer` i `QueueManager`.

## Diagram klas

Diagram znajduje się w pliku **class_diagram.png**. Można go ponownie wygenerować poleceniem:
```
python3 -m plantuml class_diagram.plantuml
```
