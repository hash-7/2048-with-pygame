# 2048-with-pygame
An implementation of the game 2048 with pygame library

Check out my simpler version of 2048, also implemented with python, but not the pygame library. 

##Rules
<img src="http://imgur.com/0kDUWx4.png" height="350px">

There will be 16 empty slots on a 4x4 board.

The player will start with two numbers that are either two or four, on two random slots on the board.

The player uses <kbd>up</kbd>, <kbd>down</kbd>, <kbd>left</kbd>, <kbd>right</kbd> arrow key to move the numbers.

When moving the numbers to the right, all numbers will be pushed to the right of the board.

For instance:

<img src="http://imgur.com/sqe4hi0.png" height="350px">

The 4 and 2 in the first row will become (in the first row):

<img src="http://imgur.com/1DgEfla.png" height="350px">

And the program adds a 2 or 4 at a random slot. 


If two numbers are of the same value, they will be added together.

For instance 4 4 4:

<img src="http://i.imgur.com/tqmOS1k.png" height="350px">

will become 4 8 when pushed right :

<img src="http://i.imgur.com/WdTtfmI.png" height="350px">

and 8 4 when pushed left:

<img src="http://i.imgur.com/EicpYt4.png" height="350px">


If the player gets the number "2048" on the board, he/she wins.

The player looses if all the slots are filled in and he/she cannot make any move at all.
