# Prime Game

Maria and Ben are playing a game where they take turns choosing prime numbers from a set of consecutive integers starting from 1 up to and including n. The chosen number and its multiples are removed from the set. The player who cannot make a move loses the game.

They play x rounds of the game, with n potentially different for each round. Assuming Maria always goes first and both players play optimally, this program determines the winner of each game.

## Prototype

```python
def isWinner(x, nums):
    """
    Determine the winner of each game.
    
    Args:
        x (int): Number of rounds.
        nums (list): Array of n for each round.
    
    Returns:
        str or None: Name of the player that won the most rounds. If the winner cannot be determined, return None.
    """
```

## Constraints

- x: Number of rounds (1 <= x <= 10000)
- nums: Array of n for each round (1 <= n <= 10000)
- No importing of packages allowed

## Example

```python
x = 3
nums = [4, 5, 1]
# First round: 4
# Maria picks 2 and removes 2, 4, leaving 1, 3
# Ben picks 3 and removes 3, leaving 1
# Ben wins because there are no prime numbers left for Maria to choose
# Second round: 5
# Maria picks 2 and removes 2, 4, leaving 1, 3, 5
# Ben picks 3 and removes 3, leaving 1, 5
# Maria picks 5 and removes 5, leaving 1
# Maria wins because there are no prime numbers left for Ben to choose
# Third round: 1
# Ben wins because there are no prime numbers for Maria to choose
# Result: Ben has the most wins
print(isWinner(x, nums))  # Output: Ben
```
