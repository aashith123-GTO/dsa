Problem 1:Finding Duplicates
Complexity



Time:

&#x20;First loop (building count dict): O(n) — every element visited once

&#x20;Second loop (checking duplicates): 

&#x20;  Best case: O(n) — if no duplicates, `not in duplicate` checks an empty/small list, cheap

&#x20;  Worst case: O(n²) — if array has many duplicates, `duplicate` list keeps growing, and `not in duplicate` re-scans it from the start every time, even after the first condition (`count > 1`) already passed



Space:O(n) for both best and worst case — dict and duplicate list are just storing up to n elements, no shortcuts possible since we need to hold that data.












Problem 2 :Two sum

Two Sum



Problem

Given an array of numbers and a target, return the indices of two numbers that add up to the target.



Example: \[1,2,4,5,6], target=9 → \[2,3] (arr\[2]+arr\[3] = 4+5 = 9)



How the Complement Pattern Works (in my own words)

Think of it like losing your friend in a crowd. You go around showing people his photo asking "have you seen him?" If they say no, you skip and ask the next person. If someone says yes, you found him.



That's how this pattern works — as you loop through the array, you check: "have I already seen the number that completes my target?" If yes, you found your pair. If no, you remember the current number and keep going, in case a LATER number needs it as its complement.



Brute Force Approach

def Two\_sum\_brute(arr, target):

&#x20;   for i in range(len(arr)):

&#x20;       for j in range(i+1, len(arr)):

&#x20;           if arr\[i]+arr\[j] == target:

&#x20;               return \[i, j]





Check every possible pair using two nested loops. `j` starts at `i+1` so we never pair a number with itself and never recheck the same pair twice.



Time:Best case O(1) — could match on the very first comparison. Worst case O(n²) — outer loop runs up to n times, inner loop runs up to n times for each, so total comparisons scale with n².





Space:O(1) — only using `i` and `j`, no extra memory that grows with input.











Optimal Approach (Hash Map / Complement Lookup)

def Two\_sum\_optimal(arr, target):

&#x20;   two\_sum = {}

&#x20;   for i in range(len(arr)):

&#x20;       missing\_piece = target - arr\[i]

&#x20;       if missing\_piece in two\_sum:

&#x20;           return \[two\_sum\[missing\_piece], i]

&#x20;       two\_sum\[arr\[i]] = i





One pass through the array. For each number, calculate its complement (`target - current number`), check if we've already seen it. If yes, return the pair. If no, store the current number so a future number can find it.



Why check before store: if you store the current number BEFORE checking, you risk a number matching with itself (e.g. \[3,3], target=6 would incorrectly return \[0,0] using the same index twice). Checking first guarantees the dict only contains numbers from earlier, different indices.



Time: O(n) — single pass, and dict lookup (`in two\_sum`) is O(1) each time. No separate best/worst split needed here since even the best case needs a minimum of 2 elements to form a pair.

Space: O(n) — dict can hold up to n elements in the worst case (no match until the last element).



Brute Force vs Optimal — the tradeoff

Brute force trades TIME for SPACE (O(n²) time, O(1) space).

Hash map trades SPACE for TIME (O(n) time, O(n) space).



&#x20;What I Learned

\- Order matters: checking before storing prevents false self-matches.

\- A loop's Big-O classification is based on its worst-case behavior, not the best-case scenario. Best case is a separate question about early exits.

\- Big tech evaluates worst case, not best case — so the hash map approach is the one to lead with in an interview.

