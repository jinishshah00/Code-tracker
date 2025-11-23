"""
README Updater - Manages the problems table in README.md
"""

import os
import json
from typing import List, Dict
from datetime import datetime


class ReadmeUpdater:
    """Updates the README.md file with solved problems table"""
    
    START_MARKER = "<!-- LEETCODE_TABLE_START -->"
    END_MARKER = "<!-- LEETCODE_TABLE_END -->"
    
    TABLE_HEADER = """| # | Title | Difficulty | Tags | LeetCode Link | My Solution | Solved On |
|---|--------|------------|------|---------------|-------------|-----------|"""
    
    def __init__(self, readme_path: str, index_path: str):
        """
        Initialize README updater
        
        Args:
            readme_path: Path to README.md file
            index_path: Path to problems_index.json file
        """
        self.readme_path = readme_path
        self.index_path = index_path
    
    def update(self):
        """Update the README.md file with current problems from index"""
        # Load all problems from index
        with open(self.index_path, 'r') as f:
            data = json.load(f)
            problems = data.get("problems", [])
        
        if not problems:
            print("No problems to add to README")
            return
        
        # Sort problems by solved_at timestamp (oldest first)
        problems.sort(key=lambda p: p.get("solved_at", ""))
        
        # Read current README content
        if os.path.exists(self.readme_path):
            with open(self.readme_path, 'r') as f:
                readme_content = f.read()
        else:
            # Create basic README structure if it doesn't exist
            readme_content = self._create_default_readme()
        
        # Build new table
        new_table = self._build_table(problems)
        
        # Replace table section
        updated_content = self._replace_table_section(readme_content, new_table)
        
        # Write back to file
        with open(self.readme_path, 'w') as f:
            f.write(updated_content)
        
        print(f"✓ Updated README.md with {len(problems)} problems")
    
    def _build_table(self, problems: List[Dict]) -> str:
        """Build the markdown table from problems list"""
        rows = [self.TABLE_HEADER]
        
        for idx, problem in enumerate(problems, start=1):
            # Format solved date
            solved_at = problem.get("solved_at", "")
            try:
                dt = datetime.fromisoformat(solved_at.replace("Z", "+00:00"))
                formatted_date = dt.strftime("%Y-%m-%d %H:%M UTC")
            except:
                formatted_date = solved_at
            
            # Format tags
            tags = ", ".join(problem.get("tags", []))
            
            # Build row
            row = (
                f"| {idx} "
                f"| {problem.get('title', '')} "
                f"| {problem.get('difficulty', '')} "
                f"| {tags} "
                f"| [Link]({problem.get('leetcode_url', '')}) "
                f"| [Solution]({problem.get('solution_path', '')}) "
                f"| {formatted_date} |"
            )
            rows.append(row)
        
        return "\n".join(rows)
    
    def _replace_table_section(self, content: str, new_table: str) -> str:
        """Replace the table section between markers"""
        # Check if markers exist
        if self.START_MARKER not in content or self.END_MARKER not in content:
            # Add markers and table at the end if they don't exist
            return content + "\n\n" + self.START_MARKER + "\n" + new_table + "\n" + self.END_MARKER + "\n"
        
        # Find positions of markers
        start_idx = content.find(self.START_MARKER)
        end_idx = content.find(self.END_MARKER)
        
        if start_idx == -1 or end_idx == -1 or start_idx >= end_idx:
            raise ValueError("Invalid marker positions in README.md")
        
        # Build new content
        before = content[:start_idx + len(self.START_MARKER)]
        after = content[end_idx:]
        
        return before + "\n" + new_table + "\n" + after
    
    def _create_default_readme(self) -> str:
        """Create a default README structure"""
        return f"""# LeetCode Daily Sync

This repository automatically syncs my solved LeetCode problems every day.

## Solved Problems

{self.START_MARKER}
{self.TABLE_HEADER}
{self.END_MARKER}

---

*Last updated by LeetCode sync bot*
"""


def update_readme(readme_path: str, index_path: str):
    """
    Main entry point for updating README
    
    Args:
        readme_path: Path to README.md
        index_path: Path to problems_index.json
    """
    updater = ReadmeUpdater(readme_path, index_path)
    updater.update()
