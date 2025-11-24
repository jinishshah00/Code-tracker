# LeetCode Progress Index

Daily, an automated workflow captures newly accepted LeetCode solutions and records their metadata (difficulty, tags, timestamp, language) alongside the corresponding source file. The table below is the canonical, generated view of progress over time. It is rebuilt on each successful sync from the structured index in `metadata/problems_index.json`.

## Solved Problems

<!-- LEETCODE_TABLE_START -->
| # | Title | Difficulty | Tags | LeetCode Link | My Solution | Solved On |
|---|--------|------------|------|---------------|-------------|-----------|
| 1 | Maximum Ascending Subarray Sum | Easy | Array | [Link](https://leetcode.com/problems/maximum-ascending-subarray-sum/) | [Solution](solutions/python3/easy/maximum-ascending-subarray-sum.py) | 2024-02-06 09:29 UTC |
| 2 | Remove Duplicates from Sorted Array | Easy | Array, Two Pointers | [Link](https://leetcode.com/problems/remove-duplicates-from-sorted-array/) | [Solution](solutions/cpp/easy/remove-duplicates-from-sorted-array.cpp) | 2025-02-19 09:46 UTC |
| 3 | Remove Element | Easy | Array, Two Pointers | [Link](https://leetcode.com/problems/remove-element/) | [Solution](solutions/cpp/easy/remove-element.cpp) | 2025-02-19 10:10 UTC |
| 4 | Pascal's Triangle | Easy | Array, Dynamic Programming | [Link](https://leetcode.com/problems/pascals-triangle/) | [Solution](solutions/cpp/easy/pascals-triangle.cpp) | 2025-02-19 11:46 UTC |
| 5 | Pascal's Triangle II | Easy | Array, Dynamic Programming | [Link](https://leetcode.com/problems/pascals-triangle-ii/) | [Solution](solutions/cpp/easy/pascals-triangle-ii.cpp) | 2025-02-19 13:05 UTC |
| 6 | Plus One | Easy | Array, Math | [Link](https://leetcode.com/problems/plus-one/) | [Solution](solutions/cpp/easy/plus-one.cpp) | 2025-02-20 11:16 UTC |
| 7 | Find the Index of the First Occurrence in a String | Easy | Two Pointers, String, String Matching | [Link](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/) | [Solution](solutions/cpp/easy/find-the-index-of-the-first-occurrence-in-a-string.cpp) | 2025-02-21 10:38 UTC |
| 8 | Two Sum | Easy | Array, Hash Table | [Link](https://leetcode.com/problems/two-sum/) | [Solution](solutions/cpp/easy/two-sum.cpp) | 2025-03-01 22:56 UTC |
| 9 | Search Insert Position | Easy | Array, Binary Search | [Link](https://leetcode.com/problems/search-insert-position/) | [Solution](solutions/cpp/easy/search-insert-position.cpp) | 2025-03-01 23:12 UTC |
| 10 | Merge Sorted Array | Easy | Array, Two Pointers, Sorting | [Link](https://leetcode.com/problems/merge-sorted-array/) | [Solution](solutions/cpp/easy/merge-sorted-array.cpp) | 2025-03-01 23:37 UTC |
| 11 | Container With Most Water | Medium | Array, Two Pointers, Greedy | [Link](https://leetcode.com/problems/container-with-most-water/) | [Solution](solutions/python3/medium/container-with-most-water.py) | 2025-09-07 16:59 UTC |
| 12 | Valid Palindrome | Easy | Two Pointers, String | [Link](https://leetcode.com/problems/valid-palindrome/) | [Solution](solutions/python3/easy/valid-palindrome.py) | 2025-09-07 18:46 UTC |
| 13 | Two Sum II - Input Array Is Sorted | Medium | Array, Two Pointers, Binary Search | [Link](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) | [Solution](solutions/python3/medium/two-sum-ii-input-array-is-sorted.py) | 2025-11-23 22:59 UTC |
| 14 | 3Sum | Medium | Array, Two Pointers, Sorting | [Link](https://leetcode.com/problems/3sum/) | [Solution](solutions/python3/medium/3sum.py) | 2025-11-23 23:45 UTC |
| 15 | Trapping Rain Water | Hard | Array, Two Pointers, Dynamic Programming, Stack, Monotonic Stack | [Link](https://leetcode.com/problems/trapping-rain-water/) | [Solution](solutions/python3/hard/trapping-rain-water.py) | 2025-11-24 01:42 UTC |
| 16 | Binary Search | Easy | Array, Binary Search | [Link](https://leetcode.com/problems/binary-search/) | [Solution](solutions/python3/easy/binary-search.py) | 2025-11-24 02:52 UTC |
<!-- LEETCODE_TABLE_END -->

---

## Repository Layout

```
.
├── solutions/           # All solution files organized by language/difficulty
│   ├── python/
│   │   ├── easy/
│   │   ├── medium/
│   │   └── hard/
│   ├── cpp/
│   └── java/
├── metadata/            # Sync state and problem index
├── scripts/             # Sync automation scripts
└── .github/workflows/   # Daily sync automation
```

## Automation Summary

GitHub Actions (scheduled at 03:00 UTC) executes `scripts/sync.py`. The script:
1. Loads prior state from `metadata/state.json`.
2. Queries recent accepted submissions via LeetCode's GraphQL endpoints.
3. Filters only truly new problems (by slug and timestamp).
4. Writes/updates solution source files under `solutions/<language>/<difficulty>/`.
5. Appends entries to `metadata/problems_index.json`.
6. Regenerates the table between the markers below.
7. Advances `metadata/state.json` only after successful write operations.

Idempotence is preserved: failed runs do not advance state; re-runs reconcile safely. The README is a pure projection—no manual edits are needed inside the marked region.

---

*Last synchronized automatically.*
