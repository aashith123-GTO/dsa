Complexity



Time:

&#x20;First loop (building count dict): O(n) — every element visited once

&#x20;Second loop (checking duplicates): 

&#x20;  Best case: O(n) — if no duplicates, `not in duplicate` checks an empty/small list, cheap

&#x20;  Worst case: O(n²) — if array has many duplicates, `duplicate` list keeps growing, and `not in duplicate` re-scans it from the start every time, even after the first condition (`count > 1`) already passed



Space:O(n) for both best and worst case — dict and duplicate list are just storing up to n elements, no shortcuts possible since we need to hold that data.

