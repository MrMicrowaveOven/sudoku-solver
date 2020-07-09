# Sudoku Solver

Update: I made an HTML interface!  Click [here](https://sudoku-hint.herokuapp.com/) to check it out!

Got a Sudoku puzzle that you just can't figure out?  Simply enter it into the interface and I'll take care of the rest.

# My Strategy

I'm certain there are better algorithms out there, but being a Sudoku fan myself I wanted to algorithmize the strategy I use when solving the paper version.  It's such an odd feeling teaching a computer how to do something that I've never put into words before.  Here are the four steps that I use:

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
2. Do something cute when it's solved.
3. Add a "guess" functionality to the backend so that boards can be solved regardless of strategy.
