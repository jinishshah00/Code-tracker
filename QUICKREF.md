# Quick Reference Guide

## 🚀 Repository Structure

```
Code-tracker/
├── .github/workflows/
│   └── leetcode-sync.yml        # GitHub Actions workflow
├── solutions/                    # All your solution code
│   ├── python/
│   │   ├── easy/
│   │   ├── medium/
│   │   └── hard/
│   ├── cpp/
│   └── java/
├── metadata/
│   ├── problems_index.json      # Master list of all problems
│   └── state.json               # Last sync timestamp
├── scripts/
│   ├── leetcode_client.py       # Fetches from LeetCode API
│   ├── readme_updater.py        # Updates README table
│   └── sync.py                  # Main orchestrator
├── .env.example                  # Template for credentials
├── .env                          # Your credentials (git-ignored!)
├── README.md                     # Your beautiful problem table
├── SETUP.md                      # Full setup instructions
├── requirements.txt              # Python dependencies
└── .gitignore                    # Git ignore rules
```

---

## 📝 Common Tasks

### First Time Setup
```bash
# 1. Get your LeetCode session cookie (see SETUP.md)

# 2. Create .env file
cp .env.example .env

# 3. Edit .env with your credentials
nano .env  # or code .env

# 4. Test locally
pip install -r requirements.txt
python scripts/sync.py

# 5. Push to GitHub
git add .
git commit -m "Initial LeetCode sync setup"
git push origin main

# 6. Add secrets on GitHub (for automation):
#    - LEETCODE_USERNAME
#    - LEETCODE_SESSION
# 7. Enable GitHub Actions in repo settings
```

### Manual Sync (Local)

**Option A: Using .env file (Recommended)**
```bash
# 1. Create/edit .env file
cp .env.example .env
nano .env  # Add your credentials

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run sync
python scripts/sync.py
```

**Option B: Using environment variables**
```bash
export LEETCODE_USERNAME="your-username"
export LEETCODE_SESSION="your-session-cookie"
python scripts/sync.py
```

### Trigger on GitHub
1. Go to **Actions** tab
2. Select **LeetCode Daily Sync**
3. Click **Run workflow**

### Update Session Cookie
When your cookie expires:

**For local .env file:**
1. Get new cookie from LeetCode (F12 → Application → Cookies)
2. Edit `.env` file and update `LEETCODE_SESSION` value

**For GitHub Secrets:**
1. Get new cookie from LeetCode
2. GitHub repo → Settings → Secrets → Update `LEETCODE_SESSION`

---

## 🔍 How to Check Status

### Check Last Sync
Look at `metadata/state.json`:
```json
{
  "last_sync_at": "2025-11-22T03:00:00Z",
  "last_processed_submission_time": "2025-11-21T18:30:00Z"
}
```

### Check Stored Problems
Look at `metadata/problems_index.json` - contains all stored problems

### Check GitHub Actions
1. Go to Actions tab
2. See recent workflow runs
3. Green ✓ = success, Red ✗ = failed

---

## 🐛 Debugging

### Enable Debug Mode
Edit `.github/workflows/leetcode-sync.yml` and add:
```yaml
- name: Run LeetCode sync
  env:
    LEETCODE_USERNAME: ${{ secrets.LEETCODE_USERNAME }}
    LEETCODE_SESSION: ${{ secrets.LEETCODE_SESSION }}
    DEBUG: "true"  # Add this
  run: python scripts/sync.py
```

### Test Authentication Locally
**With .env file:**
```bash
# Make sure .env is set up, then:
python -c "
import os
from dotenv import load_dotenv
load_dotenv()
from scripts.leetcode_client import LeetCodeClient
username = os.getenv('LEETCODE_USERNAME')
session = os.getenv('LEETCODE_SESSION')
client = LeetCodeClient(username, session)
print('✓ Authentication successful!')
"
```

**With environment variables:**
```bash
export LEETCODE_USERNAME="your-username"
export LEETCODE_SESSION="your-cookie"
python -c "
from scripts.leetcode_client import LeetCodeClient
import os
client = LeetCodeClient(os.getenv('LEETCODE_USERNAME'), os.getenv('LEETCODE_SESSION'))
print('✓ Authentication successful!')
"
```

### Check for New Submissions
```bash
# Run sync and check output
python scripts/sync.py
```

---

## ⚙️ Configuration Options

### Change Sync Schedule
Edit `.github/workflows/leetcode-sync.yml`:
```yaml
schedule:
  - cron: "0 3 * * *"  # Daily at 3 AM UTC
```

Cron examples:
- `0 */6 * * *` - Every 6 hours
- `0 0 * * *` - Daily at midnight
- `0 12 * * MON` - Every Monday at noon

### Customize README Table
Edit `scripts/readme_updater.py`:
- Modify `TABLE_HEADER` for different columns
- Change `_build_table()` for different formatting

### Add More Languages
No config needed! The system auto-detects and creates directories as you solve problems in new languages.

---

## 📊 File Formats

### problems_index.json
```json
{
  "problems": [
    {
      "slug": "two-sum",
      "title": "Two Sum",
      "difficulty": "Easy",
      "tags": ["Array", "Hash Table"],
      "leetcode_url": "https://leetcode.com/problems/two-sum/",
      "language": "python3",
      "solution_path": "solutions/python/easy/two-sum.py",
      "solved_at": "2025-11-22T10:30:00Z"
    }
  ]
}
```

### state.json
```json
{
  "last_sync_at": "2025-11-22T03:00:00Z",
  "last_processed_submission_time": "2025-11-22T10:30:00Z"
}
```

---

## 🎯 Workflow Behavior

### When New Problems Found
1. Fetch from LeetCode
2. Store solution files
3. Update problems_index.json
4. Regenerate README table
5. Update state.json
6. Commit and push

### When No New Problems
1. Fetch from LeetCode
2. Find nothing new
3. Exit (no commit)

---

## 🔐 Security Notes

### Never Commit:
- ❌ Your `LEETCODE_SESSION` cookie in code
- ❌ Your credentials in files
- ❌ `.env` files with secrets

### Always Use:
- ✅ GitHub Secrets for credentials
- ✅ Environment variables
- ✅ `.gitignore` to exclude sensitive files

---

## 💡 Pro Tips

1. **Run manually after solving** - Don't wait for the daily schedule
2. **Check Actions tab** - Monitor for failures
3. **Rotate cookies** - Update when you change LeetCode password
4. **Backup metadata/** - Keep your problem index safe
5. **Star the repo** - Track your progress publicly

---

## 🆘 Quick Troubleshooting

| Problem | Solution |
|---------|----------|
| No new problems found | Wait a bit, LeetCode may have delay |
| Authentication failed | Update `LEETCODE_SESSION` secret |
| Workflow doesn't run | Check Actions are enabled in Settings |
| Files not pushed | Check workflow permissions in Settings → Actions |
| Cookie expired | Get new cookie from browser |

---

## 📚 Additional Resources

- **Full Setup Guide**: See `SETUP.md`
- **Main README**: See `README.md`
- **LeetCode API**: Used internally by `leetcode_client.py`
- **GitHub Actions Docs**: https://docs.github.com/actions

---

**Made with ❤️ for LeetCode grinders**
