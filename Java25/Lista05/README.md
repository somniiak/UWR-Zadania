### Kompilacja
javac -d . wyjatki/*.java obliczenia/*.java rozgrywka/*.java Zgadywanka.java

### JavaDoc - obliczenia
javadoc -d doc obliczenia/*.java

### Jar - obliczenia
1. Kompilacja plików w folderze:
javac obliczenia/Wymierna.java

2. Stworzenie jar-a z folderu:
jar cf obliczenia.jar obliczenia

3. Kompilacja reszty z użyciem jar-a: (`-cp` - classpath)
javac -cp obliczenia.jar wyjatki/*.java rozgrywka/*.java Zgadywanka.java

4. Uruchamianie z jar-em: (`-ea` - enable assertions)
java -ea -cp .:obliczenia.jar Zgadywanka