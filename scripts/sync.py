"""
Sync Script - Main orchestrator for LeetCode sync process
"""

import os
import json
import sys
from pathlib import Path
from datetime import datetime
from typing import Dict, List
from dotenv import load_dotenv

# Load environment variables from .env file if it exists
load_dotenv()

# Add scripts directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from leetcode_client import get_new_solved_problems
from readme_updater import update_readme


class LeetCodeSync:
    """Main sync orchestrator"""
    
    def __init__(self, repo_root: str):
        """
        Initialize sync orchestrator
        
        Args:
            repo_root: Root directory of the repository
        """
        self.repo_root = Path(repo_root)
        self.metadata_dir = self.repo_root / "metadata"
        self.solutions_dir = self.repo_root / "solutions"
        self.state_file = self.metadata_dir / "state.json"
        self.index_file = self.metadata_dir / "problems_index.json"
        self.readme_file = self.repo_root / "README.md"
    
    def run(self):
        """Execute the full sync process"""
        print("=" * 60)
        print("LeetCode Sync Starting")
        print("=" * 60)
        
        # Step 1: Load state
        state = self._load_state()
        print(f"\nLast sync: {state.get('last_sync_at', 'Never')}")
        print(f"Last processed: {state.get('last_processed_submission_time', 'Never')}")
        
        # Step 2: Fetch new problems from LeetCode
        print("\n" + "-" * 60)
        print("Fetching new problems from LeetCode...")
        print("-" * 60)
        
        try:
            new_problems = get_new_solved_problems(state)
        except Exception as e:
            print(f"✗ Error fetching problems: {e}")
            sys.exit(1)
        
        if not new_problems:
            print("\n✓ No new problems found. Everything is up to date!")
            print("=" * 60)
            return
        
        print(f"\n✓ Found {len(new_problems)} new problem(s) to sync")
        
        # Step 3: Load problem index
        index = self._load_index()
        existing_slugs = {p["slug"] for p in index["problems"]}
        
        # Step 4: Process each new problem
        print("\n" + "-" * 60)
        print("Storing solution files...")
        print("-" * 60)
        
        latest_timestamp = state.get("last_processed_submission_time")
        
        for problem in new_problems:
            slug = problem["slug"]
            
            # Skip if already in index (shouldn't happen but just in case)
            if slug in existing_slugs:
                print(f"  ⊘ Skipping {slug} (already exists)")
                continue
            
            # Store solution file
            solution_path = self._store_solution(problem)
            
            # Add to index
            index_entry = {
                "slug": slug,
                "title": problem["title"],
                "difficulty": problem["difficulty"],
                "tags": problem["tags"],
                "leetcode_url": problem["leetcode_url"],
                "language": problem["language"],
                "solution_path": solution_path,
                "solved_at": problem["solved_at"]
            }
            index["problems"].append(index_entry)
            
            # Track latest timestamp
            if not latest_timestamp or problem["solved_at"] > latest_timestamp:
                latest_timestamp = problem["solved_at"]
            
            print(f"  ✓ {problem['title']} ({problem['language']}) -> {solution_path}")
        
        # Step 5: Save updated index
        self._save_index(index)
        print(f"\n✓ Updated problems index with {len(new_problems)} new problem(s)")
        
        # Step 6: Update README
        print("\n" + "-" * 60)
        print("Updating README.md...")
        print("-" * 60)
        
        try:
            update_readme(str(self.readme_file), str(self.index_file))
        except Exception as e:
            print(f"✗ Error updating README: {e}")
            sys.exit(1)
        
        # Step 7: Update state
        state["last_sync_at"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")
        state["last_processed_submission_time"] = latest_timestamp
        self._save_state(state)
        
        print(f"\n✓ Updated sync state (last processed: {latest_timestamp})")
        
        print("\n" + "=" * 60)
        print(f"✓ Sync Complete! Added {len(new_problems)} new problem(s)")
        print("=" * 60)
    
    def _load_state(self) -> Dict:
        """Load or initialize state.json"""
        if self.state_file.exists():
            with open(self.state_file, 'r') as f:
                return json.load(f)
        return {
            "last_sync_at": None,
            "last_processed_submission_time": None
        }
    
    def _save_state(self, state: Dict):
        """Save state.json"""
        with open(self.state_file, 'w') as f:
            json.dump(state, f, indent=2)
    
    def _load_index(self) -> Dict:
        """Load or initialize problems_index.json"""
        if self.index_file.exists():
            with open(self.index_file, 'r') as f:
                return json.load(f)
        return {"problems": []}
    
    def _save_index(self, index: Dict):
        """Save problems_index.json"""
        with open(self.index_file, 'w') as f:
            json.dump(index, f, indent=2)
    
    def _store_solution(self, problem: Dict) -> str:
        """
        Store solution code to appropriate file
        
        Args:
            problem: Problem dictionary with code, language, difficulty, slug
            
        Returns:
            Relative path to stored solution file
        """
        language = problem["language"]
        difficulty = problem["difficulty"].lower()
        slug = problem["slug"]
        extension = problem["extension"]
        code = problem["code"]
        
        # Build path: solutions/{language}/{difficulty}/{slug}.{ext}
        lang_dir = self.solutions_dir / language / difficulty
        lang_dir.mkdir(parents=True, exist_ok=True)
        
        solution_file = lang_dir / f"{slug}.{extension}"
        
        # Add header comment with problem info
        header = self._generate_file_header(problem)
        full_content = header + "\n\n" + code
        
        # Write solution file
        with open(solution_file, 'w', encoding='utf-8') as f:
            f.write(full_content)
        
        # Return relative path from repo root
        return str(solution_file.relative_to(self.repo_root))
    
    def _generate_file_header(self, problem: Dict) -> str:
        """Generate a header comment for solution files"""
        title = problem["title"]
        url = problem["leetcode_url"]
        difficulty = problem["difficulty"]
        tags = ", ".join(problem["tags"])
        solved_at = problem["solved_at"]
        
        # Choose comment style based on language
        lang = problem["language"]
        if lang in ["python", "python3"]:
            return f'''"""
{title}
{url}

Difficulty: {difficulty}
Tags: {tags}
Solved: {solved_at}
"""'''
        elif lang in ["cpp", "c", "java", "javascript", "typescript", "csharp", "go", "rust", "php", "scala"]:
            return f'''/**
 * {title}
 * {url}
 * 
 * Difficulty: {difficulty}
 * Tags: {tags}
 * Solved: {solved_at}
 */'''
        else:
            # Generic comment style
            return f'''# {title}
# {url}
# 
# Difficulty: {difficulty}
# Tags: {tags}
# Solved: {solved_at}'''


def main():
    """Main entry point"""
    # Get repo root (parent of scripts directory)
    script_dir = Path(__file__).parent
    repo_root = script_dir.parent
    
    # Run sync
    sync = LeetCodeSync(str(repo_root))
    sync.run()


if __name__ == "__main__":
    main()
