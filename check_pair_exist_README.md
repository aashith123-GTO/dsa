\# Check Pair Exists



\## Problem

Given an array and a target, return True/False — does any pair exist that sums to target?



Example: \[10,15,3,7], target=17 → True (10+7=17)



\## Approach — Complement Lookup (same pattern as Two Sum)

```python

def ischeck\_pair\_exist(num, target):

&#x20;   seen = {}

&#x20;   for i in range(len(num)):

&#x20;       needed = target - num\[i]

&#x20;       if needed in seen:

&#x20;           return True

&#x20;       seen\[num\[i]] = i

&#x20;   return False

```



Same core idea as Two Sum — check if the complement exists before storing. Used a dict here (storing index isn't strictly necessary since we only need True/False, but keeping it consistent with Two Sum's structure).



\*\*Why minus, not plus:\*\* I know `num\[i]`, I want `target`. Missing piece = target - num\[i] — solving `num\[i] + x = target` for x. Whenever I want to find something MISSING to complete a target, I subtract what I have from what I want.



\*\*Time:\*\* O(n) — single pass, O(1) dict lookup each step.

\*\*Space:\*\* O(n) — dict can grow up to n elements in the worst case (no pair found until the end).

