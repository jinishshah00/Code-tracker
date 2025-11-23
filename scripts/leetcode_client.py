"""
LeetCode Client - Fetches solved problems from LeetCode API
"""

import os
import requests
from datetime import datetime
from typing import List, Dict, Optional


class LeetCodeClient:
    """Client for interacting with LeetCode GraphQL API"""
    
    GRAPHQL_URL = "https://leetcode.com/graphql"
    
    # Language ID to extension mapping
    LANG_EXTENSIONS = {
        "python3": "py",
        "python": "py",
        "cpp": "cpp",
        "c": "c",
        "java": "java",
        "javascript": "js",
        "typescript": "ts",
        "csharp": "cs",
        "go": "go",
        "ruby": "rb",
        "swift": "swift",
        "kotlin": "kt",
        "rust": "rs",
        "php": "php",
        "scala": "scala",
        "mysql": "sql",
        "mssql": "sql",
        "oraclesql": "sql",
    }
    
    def __init__(self, username: str, session_cookie: str):
        """
        Initialize LeetCode client
        
        Args:
            username: LeetCode username
            session_cookie: LEETCODE_SESSION cookie value
        """
        self.username = username
        self.session = requests.Session()
        self.session.cookies.set("LEETCODE_SESSION", session_cookie, domain=".leetcode.com")
        self.session.cookies.set("csrftoken", "dummy", domain=".leetcode.com")
        self.session.headers.update({
            "Content-Type": "application/json",
            "Referer": "https://leetcode.com",
            "Origin": "https://leetcode.com",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest"
        })
    
    def get_new_solved_problems(self, last_processed_time: Optional[str] = None) -> List[Dict]:
        """
        Fetch solved problems from LeetCode
        
        Args:
            last_processed_time: ISO timestamp to fetch problems after (None = fetch all)
            
        Returns:
            List of problem dictionaries with keys:
            - slug: problem slug
            - title: problem title
            - difficulty: Easy/Medium/Hard
            - tags: list of topic tags
            - leetcode_url: full URL to problem
            - language: programming language
            - code: solution code
            - solved_at: ISO timestamp of when solved
        """
        print(f"Fetching submissions for user: {self.username}")
        
        # Get all submissions
        submissions = self._get_all_submissions()
        
        if not submissions:
            print("No submissions found")
            return []
        
        # Filter to accepted submissions only
        accepted_submissions = [s for s in submissions if s.get("statusDisplay") == "Accepted"]
        print(f"Found {len(accepted_submissions)} accepted submissions")
        
        # Filter by time if specified
        if last_processed_time:
            cutoff_timestamp = int(datetime.fromisoformat(last_processed_time.replace("Z", "+00:00")).timestamp())
            # Convert timestamp to int for comparison (it might be a string from API)
            accepted_submissions = [
                s for s in accepted_submissions 
                if int(s.get("timestamp", 0)) > cutoff_timestamp
            ]
            print(f"Found {len(accepted_submissions)} new submissions after {last_processed_time}")
        
        if not accepted_submissions:
            return []
        
        # Group by problem slug to get latest submission per problem
        problems_by_slug = {}
        for submission in accepted_submissions:
            slug = submission.get("titleSlug")
            timestamp = int(submission.get("timestamp", 0))
            
            if slug not in problems_by_slug or timestamp > int(problems_by_slug[slug].get("timestamp", 0)):
                problems_by_slug[slug] = submission
        
        print(f"Processing {len(problems_by_slug)} unique problems")
        
        # Get full details for each problem
        problems = []
        for slug, submission in problems_by_slug.items():
            try:
                problem_details = self._get_problem_details(slug, submission)
                if problem_details:
                    problems.append(problem_details)
                    print(f"  ✓ {problem_details['title']} ({problem_details['language']})")
            except Exception as e:
                print(f"  ✗ Failed to process {slug}: {e}")
                continue
        
        return problems
    
    def _get_all_submissions(self) -> List[Dict]:
        """Fetch all submissions for the user"""
        all_submissions = []
        offset = 0
        limit = 20
        
        while True:
            # Note: Argument order matters in GraphQL!
            query = """
            query recentAcSubmissions($username: String!, $limit: Int!) {
                recentAcSubmissionList(username: $username, limit: $limit) {
                    id
                    title
                    titleSlug
                    timestamp
                    statusDisplay
                    lang
                }
            }
            """
            
            variables = {
                "username": self.username,
                "limit": limit
            }
            
            payload = {
                "query": query,
                "variables": variables,
                "operationName": "recentAcSubmissions"
            }
            
            try:
                response = self.session.post(
                    self.GRAPHQL_URL,
                    json=payload,
                    timeout=30
                )
                
                # Print response for debugging
                if response.status_code != 200:
                    print(f"Response status: {response.status_code}")
                    print(f"Response body: {response.text[:500]}")
                
                response.raise_for_status()
                data = response.json()
                
                # Check for GraphQL errors
                if "errors" in data:
                    print(f"GraphQL errors: {data['errors']}")
                    break
                
                submissions = data.get("data", {}).get("recentAcSubmissionList", [])
                
                if not submissions:
                    break
                
                all_submissions.extend(submissions)
                
                # LeetCode's recentAcSubmissionList doesn't support pagination
                # It returns the most recent submissions (typically up to 20)
                break
                
            except requests.exceptions.RequestException as e:
                print(f"Error fetching submissions: {e}")
                if hasattr(e, 'response') and e.response is not None:
                    print(f"Response content: {e.response.text[:500]}")
                break
        
        return all_submissions
    
    def _get_problem_details(self, slug: str, submission: Dict) -> Optional[Dict]:
        """Get full details for a specific problem"""
        
        # Get problem metadata (difficulty, tags, etc.)
        query = """
        query getQuestionDetail($titleSlug: String!) {
            question(titleSlug: $titleSlug) {
                questionId
                title
                titleSlug
                difficulty
                topicTags {
                    name
                }
            }
        }
        """
        
        variables = {"titleSlug": slug}
        
        try:
            response = self.session.post(
                self.GRAPHQL_URL,
                json={"query": query, "variables": variables}
            )
            response.raise_for_status()
            data = response.json()
            
            question = data.get("data", {}).get("question", {})
            
            if not question:
                return None
            
            # Get the actual submission code
            code = self._get_submission_code(submission["id"])
            
            if not code:
                print(f"    Warning: No code found for {slug}")
                return None
            
            # Normalize language name
            language = submission.get("lang", "python3").lower()
            
            # Get file extension
            extension = self.LANG_EXTENSIONS.get(language, "txt")
            
            # Handle timestamp - could be int or string
            timestamp = submission.get("timestamp")
            if isinstance(timestamp, str):
                try:
                    timestamp = int(timestamp)
                except (ValueError, TypeError):
                    # If it's already an ISO string, use current time
                    timestamp = int(datetime.now().timestamp())
            
            return {
                "slug": slug,
                "title": question["title"],
                "difficulty": question["difficulty"],
                "tags": [tag["name"] for tag in question.get("topicTags", [])],
                "leetcode_url": f"https://leetcode.com/problems/{slug}/",
                "language": language,
                "extension": extension,
                "code": code,
                "solved_at": datetime.fromtimestamp(timestamp).isoformat() + "Z"
            }
            
        except Exception as e:
            print(f"    Error getting details for {slug}: {e}")
            return None
    
    def _get_submission_code(self, submission_id: str) -> Optional[str]:
        """Get the code for a specific submission"""
        query = """
        query submissionDetails($submissionId: Int!) {
            submissionDetails(submissionId: $submissionId) {
                code
                timestamp
            }
        }
        """
        
        variables = {"submissionId": int(submission_id)}
        
        payload = {
            "query": query,
            "variables": variables,
            "operationName": "submissionDetails"
        }
        
        try:
            response = self.session.post(
                self.GRAPHQL_URL,
                json=payload,
                timeout=30
            )
            
            if response.status_code != 200:
                print(f"    Submission code fetch failed: {response.status_code}")
                print(f"    Response: {response.text[:300]}")
                return None
            
            data = response.json()
            
            if "errors" in data:
                print(f"    GraphQL errors: {data['errors']}")
                return None
            
            submission_detail = data.get("data", {}).get("submissionDetails", {})
            code = submission_detail.get("code")
            
            if not code:
                print(f"    No code in response for submission {submission_id}")
            
            return code
            
        except Exception as e:
            print(f"    Error getting submission code: {e}")
            return None


def get_new_solved_problems(state: Dict) -> List[Dict]:
    """
    Main entry point for getting new solved problems
    
    Args:
        state: Dictionary with 'last_processed_submission_time' key
        
    Returns:
        List of new problem dictionaries
    """
    username = os.getenv("LEETCODE_USERNAME")
    session_cookie = os.getenv("LEETCODE_SESSION")
    
    if not username or not session_cookie:
        raise ValueError("LEETCODE_USERNAME and LEETCODE_SESSION environment variables required")
    
    client = LeetCodeClient(username, session_cookie)
    last_time = state.get("last_processed_submission_time")
    
    return client.get_new_solved_problems(last_time)
