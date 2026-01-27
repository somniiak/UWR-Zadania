def print_indent(n, width):
    print(f"{n:>{width}}", end=' ')

def tabliczka(x1, x2, y1, y2, d):
    if (x1 > x2 or y1 > y2):
        raise "Niepoprawne wartości."

    cols = [x1 + i * d for i in range(int((x2 - x1) / d) + 1)]
    rows = [y1 + i * d for i in range(int((y2 - y1) / d) + 1)]
    if cols[-1] != x2: cols.append(x2)
    if rows[-1] != y2: rows.append(y2)

    products = [[i * j for i in cols] for j in rows]

    all_values = cols + rows + [p for row in products for p in row]
    width = max(len(str(v)) for v in all_values) + 1

    print(" " * width, end=' ')
    for c in cols:
        print_indent(c, width)
    print()

    for i, r in enumerate(rows):
        print_indent(r, width)
        for val in products[i]:
            print_indent(val, width)
        print()


tabliczka(3.0, 5.0, 2.0, 4.0, 1.0)
tabliczka(-1.1, 3.1, 3.33, 4.9, 1.25)
