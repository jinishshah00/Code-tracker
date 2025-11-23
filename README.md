# LeetCode Daily Sync

This repository automatically syncs my solved LeetCode problems every day.

## 📊 Progress Overview

Track your LeetCode journey with automated daily syncs. Every solution is automatically organized by language and difficulty.

## 🎯 Solved Problems

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
<!-- LEETCODE_TABLE_END -->

---

## 📁 Repository Structure

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

## 🤖 How It Works

This repository uses GitHub Actions to:
1. Check LeetCode daily for newly solved problems
2. Download solution code and metadata
3. Organize files by language and difficulty
4. Update this README with a summary table
5. Commit and push changes automatically

## 🚀 Setup Instructions

To set up this sync for your own account:

1. **Fork this repository**

2. **Get your LeetCode session cookie:**
   - Log into LeetCode
   - Open Developer Tools (F12) → Application → Cookies
   - Copy the value of `LEETCODE_SESSION` cookie

3. **Add GitHub Secrets:**
   - Go to your repo → Settings → Secrets and variables → Actions
   - Add these secrets:
     - `LEETCODE_USERNAME`: Your LeetCode username
     - `LEETCODE_SESSION`: The session cookie value

4. **Enable GitHub Actions:**
   - Go to Actions tab and enable workflows

That's it! The sync will run daily at 3 AM UTC automatically.

---

*Last updated by LeetCode sync bot 🤖*
