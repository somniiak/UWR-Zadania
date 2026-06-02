- **C, kompilator gcc 14.2.0**
```
gcc -std=gnu18 -Wall -Wextra -Wshadow -O2 -static -DJUDGE -o prog prog.c -lm
```

- **C++, kompilator gcc 14.2.0**
```
g++ -std=gnu++20 -Wall -Wextra -Wshadow -O2 -static -DJUDGE -o prog prog.cpp
```

- **Rust, kompilator rustc 1.85.0**
```
rustc --edition=2024 -C opt-level=2 -C target-feature=+crt-static -o prog prog.rs
```
