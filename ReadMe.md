# Sudoku Solver

Got a Sudoku puzzle that you just can't figure out?  Simply enter it into an Excel document (I use Google Drive)(use ' ' for empty cells, or else it won't copy them), copy the 9x9 grid, and paste it into `board.txt`.  Run `python script.py` and I'll take care of the rest.

If you'd rather enter it into the graphical text document of `board_old.txt` (looks sorta snazzy, if I do say so myself), run `python old_script.py` instead.

The parsing can be a bit picky, and I'm slowly working to make it more adaptable.  However, that is one of the least fun parts of this project.  PLEASE let me know if you encounter any parsing errors when you input your sheet.

# My Strategy

I'm certain there are better algorithms out there, but being a Sudoku fan myself I wanted to algorithmize the strategy I use when solving the paper version.  It's such an odd feeling teaching a computer how to do something that I've never put into words before.

## 1. Set Possibles

Each space has a number of possibles.  My strategy was to record these in each space and slowly whittle them down.

Once a space has only one possible, set the value of the space as that one possible.

## 2. The Count Elimination

If a space shares a row, column, or 'block' (3x3 square) with a solved space, we can eliminate the value of that solved space from our space's possibles.

This is adapted from my "Count 1-9, if only one is possible, then the space is solved" strategy.

For example, if a space has possibles 2, 3, and 5, and a 2 and 3 are in its row, then we can eliminate 2 and 3 from its possibles.  Hence, there is only one possible, so we set the value of the space to that possible.

## 3. The Space Elimination

If a space is the only space in its row, column, or block to have a possible, then set the value as that possible.

This is adapted from my "Eliminate all-but-one space from a row, column, or block that can be a certain number".

For example, if there are 5 empty spaces in a block, but four of them can't be 5, then the remaining space must be 5.

## 4. Rinse and Repeat

My solution algorithm does each of these over and over again until the puzzle is solved.  I haven't found a Sudoku that can't be solved by this yet.  Let me know if you do!

# To Dos

1. Kill an endless loop if nothing can happen.
1. Do something cute when it's solved.
2. Add a "Solve" button in case the user doesn't want to click many times.
3. Show an "I can't solve that board" if my algorithm cannot solve.
4. Add a "guess" functionality to the backend so that more boards can be solved.
