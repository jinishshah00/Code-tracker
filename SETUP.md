# LeetCode Auto-Sync Setup Guide

## 🎯 Quick Start

Follow these steps to get your LeetCode problems syncing automatically to GitHub.

---

## 📋 Prerequisites

- A GitHub account
- A LeetCode account with solved problems
- Basic familiarity with GitHub (creating repos, adding secrets)

---

## 🔧 Step 1: Get Your LeetCode Session Cookie

The sync needs to authenticate with LeetCode to fetch your submissions. Here's how to get your session cookie:

### Method 1: Using Chrome/Edge
1. Go to [leetcode.com](https://leetcode.com) and **log in**
2. Press `F12` to open Developer Tools
3. Go to the **Application** tab (Chrome) or **Storage** tab (Edge)
4. In the left sidebar, expand **Cookies** → `https://leetcode.com`
5. Find the cookie named `LEETCODE_SESSION`
6. **Copy the entire value** (it's a long string)

### Method 2: Using Firefox
1. Go to [leetcode.com](https://leetcode.com) and **log in**
2. Press `F12` to open Developer Tools
3. Go to the **Storage** tab
4. In the left sidebar, expand **Cookies** → `https://leetcode.com`
5. Find the cookie named `LEETCODE_SESSION`
6. **Copy the entire value**

### Method 3: Using Safari
1. Go to [leetcode.com](https://leetcode.com) and **log in**
2. Enable Developer Menu: Safari → Preferences → Advanced → Check "Show Develop menu"
3. Press `Cmd+Option+I` to open Web Inspector
4. Go to the **Storage** tab
5. Click on **Cookies** → `https://leetcode.com`
6. Find `LEETCODE_SESSION` and **copy the value**

⚠️ **Important Notes:**
- This cookie acts like your password - keep it secret!
- If you log out of LeetCode, this cookie will expire and you'll need a new one
- The cookie value is typically a very long alphanumeric string

---

## 🔐 Step 2: Configure Your Credentials

You have two options for providing your LeetCode credentials:

### Option A: Using .env File (Recommended for Local Testing)

This is the easiest way for local development and testing:

1. **Copy the example file:**
   ```bash
   cp .env.example .env
   ```

2. **Edit the .env file:**
   ```bash
   # Open in your editor
   nano .env
   # or
   code .env
   ```

3. **Fill in your credentials:**
   ```env
   LEETCODE_USERNAME=your-leetcode-username
   LEETCODE_SESSION=paste-your-session-cookie-here
   ```

4. **Save the file**

✅ That's it! The `.env` file is automatically loaded by the sync script.

⚠️ **Security Note:** The `.env` file is in `.gitignore` so it won't be committed to git. Never commit your credentials!

### Option B: Using Environment Variables (Alternative)

You can also set environment variables directly:

```bash
export LEETCODE_USERNAME="your-username"
export LEETCODE_SESSION="your-session-cookie"
```

---

## 🚀 Step 3: Test Locally (Optional but Recommended)

Before pushing to GitHub, test the sync on your machine:

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the sync:**
   ```bash
   python scripts/sync.py
   ```

3. **Check the output:**
   - ✅ Should fetch your LeetCode problems
   - ✅ Should create solution files in `solutions/`
   - ✅ Should update `README.md` with the table
   - ✅ Should update metadata files

If you see errors, check that:
- Your `.env` file has the correct credentials
- Your `LEETCODE_SESSION` cookie is valid
- You have solved at least one problem on LeetCode

---

## 📤 Step 4: Push to GitHub

1. **Push this repo to GitHub** (if you haven't already):
   ```bash
   git add .
   git commit -m "Initial setup of LeetCode sync"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/Code-tracker.git
   git push -u origin main
   ```

## 🔐 Step 5: Add GitHub Secrets (For Automation)

For GitHub Actions to run automatically, you need to add your credentials as secrets:

1. **Go to your repository on GitHub**

2. **Navigate to Settings:**
   - Click the **Settings** tab (top right of your repo page)

3. **Add Secrets:**
   - In the left sidebar, click **Secrets and variables** → **Actions**
   - Click the green **New repository secret** button

4. **Add LEETCODE_USERNAME:**
   - Name: `LEETCODE_USERNAME`
   - Secret: `your-leetcode-username` (just the username, not email)
   - Click **Add secret**

5. **Add LEETCODE_SESSION:**
   - Click **New repository secret** again
   - Name: `LEETCODE_SESSION`
   - Secret: Paste the entire cookie value you copied in Step 1
   - Click **Add secret**

✅ You should now have 2 secrets:
- `LEETCODE_USERNAME`
- `LEETCODE_SESSION`

---

## ✅ Step 6: Enable GitHub Actions

1. Go to the **Actions** tab in your repository
2. If prompted, click **I understand my workflows, go ahead and enable them**
3. You should see the workflow "LeetCode Daily Sync"

---

## 🚀 Step 7: Test the GitHub Actions Workflow

Let's make sure everything works before waiting for the daily schedule:

1. Go to the **Actions** tab
2. Click on **LeetCode Daily Sync** workflow in the left sidebar
3. Click the **Run workflow** button (dropdown on the right)
4. Click the green **Run workflow** button
5. Wait a minute, then refresh the page
6. Click on the running/completed workflow to see the logs

**What to look for:**
- ✅ Green checkmarks = Success!
- ❌ Red X = Something went wrong (check the logs)

Common issues:
- **Authentication failed**: Double-check your `LEETCODE_SESSION` cookie
- **No username**: Verify `LEETCODE_USERNAME` is set correctly
- **No problems found**: This is fine if you haven't solved anything new since the last sync

---

## 📅 Step 8: Understand the Schedule

The workflow runs automatically:
- **Daily at 3 AM UTC** (adjust the cron schedule in `.github/workflows/leetcode-sync.yml` if you want a different time)
- **Manual runs** anytime via the Actions tab

### Change the schedule:
Edit `.github/workflows/leetcode-sync.yml`:
```yaml
schedule:
  - cron: "0 3 * * *"  # Change this line
```

Examples:
- `"0 0 * * *"` = Midnight UTC
- `"0 12 * * *"` = Noon UTC  
- `"0 */6 * * *"` = Every 6 hours

---

## 🎉 You're Done!

Your repository will now:
1. ✅ Check LeetCode daily for new solved problems
2. ✅ Download your solution code
3. ✅ Organize files by language and difficulty
4. ✅ Update README.md with a beautiful table
5. ✅ Commit and push changes automatically

---

## 🔍 How to Verify It's Working

After solving a problem on LeetCode:

1. Wait for the next scheduled run (or trigger manually)
2. Check your repository for:
   - New files in `solutions/{language}/{difficulty}/`
   - Updated `README.md` with the new problem in the table
   - New commit from `leetcode-bot`

---

## 🛠️ Troubleshooting

### "Error: Invalid credentials" or "Authentication failed"
- Your `LEETCODE_SESSION` cookie has expired
- Log into LeetCode again and get a fresh cookie (Step 1)
- Update the `LEETCODE_SESSION` secret in GitHub

### "No problems found" but I just solved one
- Wait a few minutes - LeetCode may have a slight delay
- Try running the workflow manually
- Check that your solution was **accepted** (not just submitted)

### Workflow doesn't run automatically
- Check that GitHub Actions is enabled
- Verify the `.github/workflows/leetcode-sync.yml` file exists
- Make sure you've committed and pushed all files

### "Permission denied" when pushing
- The workflow uses `GITHUB_TOKEN` which is automatically provided
- Ensure your repository settings allow GitHub Actions to write
- Go to Settings → Actions → General → Workflow permissions → Select "Read and write permissions"

---

## 🔄 Updating Your Cookie

Your `LEETCODE_SESSION` cookie will eventually expire (when you log out or after some time). When it does:

1. Get a new cookie following Step 1
2. Update the GitHub secret:
   - Go to Settings → Secrets and variables → Actions
   - Click on `LEETCODE_SESSION`
   - Click **Update secret**
   - Paste the new value
   - Click **Update secret**

---

## 🎨 Customization

### Add more languages
The system automatically supports Python, C++, Java, JavaScript, TypeScript, C#, Go, Ruby, Swift, Kotlin, Rust, PHP, and Scala.

Directories are created on-demand as you solve problems in new languages.

### Change the README format
Edit `scripts/readme_updater.py` to customize the table format, add statistics, or change the styling.

### Add more metadata
Edit `scripts/leetcode_client.py` to fetch additional problem data like hints, companies, or frequency.

---

## 📞 Need Help?

If you run into issues:
1. Check the workflow logs in the Actions tab for detailed error messages
2. Verify all secrets are set correctly
3. Ensure your LeetCode session cookie is valid
4. Make sure you've solved at least one problem on LeetCode

---

**Happy coding! 🎯**
