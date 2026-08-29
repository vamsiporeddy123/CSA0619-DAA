def solve_diagonal_sudoku(board):
    n = 9
    digits = set(range(1, 10))

    rows = [set() for _ in range(n)]
    cols = [set() for _ in range(n)]
    boxes = [set() for _ in range(n)]
    diag1 = set()
    diag2 = set()

    for r in range(n):
        for c in range(n):
            value = board[r][c]
            if value == 0:
                continue

            b = (r // 3) * 3 + (c // 3)

            if value in rows[r] or value in cols[c] or value in boxes[b]:
                return False

            if r == c and value in diag1:
                return False

            if r + c == n - 1 and value in diag2:
                return False

            rows[r].add(value)
            cols[c].add(value)
            boxes[b].add(value)

            if r == c:
                diag1.add(value)

            if r + c == n - 1:
                diag2.add(value)

    def candidates(r, c):
        b = (r // 3) * 3 + (c // 3)
        used = rows[r] | cols[c] | boxes[b]

        if r == c:
            used |= diag1

        if r + c == n - 1:
            used |= diag2

        return digits - used

    def backtrack():
        best_cell = None
        best_candidates = None

        for r in range(n):
            for c in range(n):
                if board[r][c] != 0:
                    continue

                possible = candidates(r, c)

                if not possible:
                    return False

                if best_candidates is None or len(possible) < len(best_candidates):
                    best_cell = (r, c)
                    best_candidates = possible

                    if len(best_candidates) == 1:
                        break
            if best_candidates is not None and len(best_candidates) == 1:
                break

        if best_cell is None:
            return True

        r, c = best_cell
        b = (r // 3) * 3 + (c // 3)

        for value in sorted(best_candidates):
            board[r][c] = value
            rows[r].add(value)
            cols[c].add(value)
            boxes[b].add(value)

            if r == c:
                diag1.add(value)

            if r + c == n - 1:
                diag2.add(value)

            if backtrack():
                return True

            board[r][c] = 0
            rows[r].remove(value)
            cols[c].remove(value)
            boxes[b].remove(value)

            if r == c:
                diag1.remove(value)

            if r + c == n - 1:
                diag2.remove(value)

        return False

    return backtrack()


if __name__ == "__main__":
    puzzle = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    if solve_diagonal_sudoku(puzzle):
        for row in puzzle:
            print(*row)
    else:
        print("No solution exists.")
