"""
Cybersecurity Job Search Bot
Scrapes jobs from multiple platforms and filters based on your profile
"""

import requests
from bs4 import BeautifulSoup
import json
import time
from datetime import datetime
import sqlite3
from typing import List, Dict
import re

class JobScraper:
    def __init__(self, db_path="jobs.db"):
        self.db_path = db_path
        self.init_database()
        
        # Your profile - customize these!
        self.profile = {
            'experience_level': 'entry',
            'skills': ['python', 'sast', 'dast', 'soc', 'security', 'burp suite', 
                      'owasp', 'nmap', 'wireshark', 'splunk', 'security+'],
            'keywords': ['appsec', 'application security', 'soc analyst', 
                        'security analyst', 'junior security', 'entry level security'],
            'location': 'remote',  # Change this to your preferred location
            'excluded_keywords': ['senior', 'lead', '5+ years', '7+ years', 'architect']
        }
    
    def init_database(self):
        """Initialize SQLite database to track jobs"""
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS jobs
                     (id TEXT PRIMARY KEY,
                      title TEXT,
                      company TEXT,
                      location TEXT,
                      url TEXT,
                      description TEXT,
                      posted_date TEXT,
                      match_score INTEGER,
                      source TEXT,
                      applied INTEGER DEFAULT 0,
                      date_found TEXT)''')
        conn.commit()
        conn.close()
    
    def calculate_match_score(self, job_title: str, job_description: str) -> int:
        """Calculate how well a job matches your profile (0-100)"""
        score = 0
        text = (job_title + " " + job_description).lower()
        
        # Keyword matching
        keyword_matches = sum(1 for keyword in self.profile['keywords'] if keyword in text)
        score += keyword_matches * 15
        
        # Skill matching
        skill_matches = sum(1 for skill in self.profile['skills'] if skill in text)
        score += skill_matches * 10
        
        # Exclude senior positions
        for excluded in self.profile['excluded_keywords']:
            if excluded in text:
                score -= 30
        
        # Bonus for entry-level indicators
        entry_indicators = ['entry level', 'junior', '0-2 years', 'graduate', 'early career']
        if any(indicator in text for indicator in entry_indicators):
            score += 20
        
        return max(0, min(100, score))
    
    def scrape_indeed(self, search_terms: List[str]) -> List[Dict]:
        """Scrape Indeed for jobs"""
        jobs = []
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        
        for term in search_terms:
            try:
                url = f"https://www.indeed.com/jobs?q={term.replace(' ', '+')}&l={self.profile['location']}"
                print(f"Searching Indeed for: {term}")
                
                # Note: Indeed has anti-scraping measures, this is a basic example
                # For production, consider using Indeed API or LinkedIn API
                response = requests.get(url, headers=headers, timeout=10)
                
                if response.status_code == 200:
                    soup = BeautifulSoup(response.content, 'html.parser')
                    # Parse job cards (structure may change)
                    job_cards = soup.find_all('div', class_='job_seen_beacon')
                    
                    for card in job_cards[:5]:  # Limit to avoid overwhelming
                        try:
                            title = card.find('h2', class_='jobTitle')
                            company = card.find('span', class_='companyName')
                            location = card.find('div', class_='companyLocation')
                            
                            if title and company:
                                job = {
                                    'title': title.get_text(strip=True),
                                    'company': company.get_text(strip=True),
                                    'location': location.get_text(strip=True) if location else 'N/A',
                                    'url': f"https://www.indeed.com{title.find('a')['href']}" if title.find('a') else '',
                                    'description': '',
                                    'source': 'Indeed'
                                }
                                jobs.append(job)
                        except Exception as e:
                            continue
                
                time.sleep(2)  # Be respectful with rate limiting
                
            except Exception as e:
                print(f"Error scraping Indeed for {term}: {e}")
        
        return jobs
    
    def scrape_cybersecurity_jobs_sites(self) -> List[Dict]:
        """Scrape specialized cybersecurity job boards"""
        jobs = []
        
        # Example sites (you'd need to implement actual scraping for each)
        sites = {
            'CyberSecJobs': 'https://www.cybersecurityjobs.com/',
            'InfoSec Jobs': 'https://www.infosec-jobs.com/',
        }
        
        # Placeholder - implement actual scraping
        print("Checking specialized cybersecurity job boards...")
        
        return jobs
    
    def search_github_jobs(self) -> List[Dict]:
        """Search for security-related positions on GitHub"""
        jobs = []
        # GitHub Jobs API was deprecated, but you could scrape company career pages
        # or use other APIs
        return jobs
    
    def save_jobs(self, jobs: List[Dict]):
        """Save jobs to database with match scores"""
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        
        new_jobs = 0
        for job in jobs:
            job_id = f"{job['company']}_{job['title']}".replace(' ', '_')
            match_score = self.calculate_match_score(job['title'], job.get('description', ''))
            
            try:
                c.execute('''INSERT OR IGNORE INTO jobs 
                           (id, title, company, location, url, description, 
                            posted_date, match_score, source, date_found)
                           VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                         (job_id, job['title'], job['company'], job['location'],
                          job['url'], job.get('description', ''), 
                          job.get('posted_date', ''), match_score,
                          job['source'], datetime.now().strftime('%Y-%m-%d')))
                
                if c.rowcount > 0:
                    new_jobs += 1
            except Exception as e:
                print(f"Error saving job: {e}")
        
        conn.commit()
        conn.close()
        return new_jobs
    
    def get_top_matches(self, limit=10) -> List[Dict]:
        """Get top matching jobs from database"""
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        
        c.execute('''SELECT title, company, location, url, match_score, source, date_found
                    FROM jobs 
                    WHERE applied = 0 AND match_score > 30
                    ORDER BY match_score DESC, date_found DESC
                    LIMIT ?''', (limit,))
        
        jobs = []
        for row in c.fetchall():
            jobs.append({
                'title': row[0],
                'company': row[1],
                'location': row[2],
                'url': row[3],
                'match_score': row[4],
                'source': row[5],
                'date_found': row[6]
            })
        
        conn.close()
        return jobs
    
    def mark_as_applied(self, job_id: str):
        """Mark a job as applied"""
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        c.execute('UPDATE jobs SET applied = 1 WHERE id = ?', (job_id,))
        conn.commit()
        conn.close()
    
    def run_search(self):
        """Main search function"""
        print("🔍 Starting job search...")
        print(f"Profile: {self.profile['experience_level']} level")
        print(f"Target roles: {', '.join(self.profile['keywords'][:3])}")
        print("-" * 50)
        
        all_jobs = []
        
        # Search Indeed
        all_jobs.extend(self.scrape_indeed(self.profile['keywords'][:3]))
        
        # Add other sources
        all_jobs.extend(self.scrape_cybersecurity_jobs_sites())
        
        # Save to database
        new_jobs = self.save_jobs(all_jobs)
        
        print(f"\n✅ Found {len(all_jobs)} total jobs")
        print(f"📝 {new_jobs} new jobs added to database")
        
        # Show top matches
        print("\n🎯 Top Matches:")
        print("-" * 50)
        top_matches = self.get_top_matches(10)
        
        for i, job in enumerate(top_matches, 1):
            print(f"\n{i}. {job['title']} at {job['company']}")
            print(f"   Location: {job['location']}")
            print(f"   Match Score: {job['match_score']}/100")
            print(f"   Source: {job['source']}")
            print(f"   URL: {job['url']}")
        
        return top_matches


def main():
    """Example usage"""
    scraper = JobScraper()
    
    # Run the search
    jobs = scraper.run_search()
    
    # Export to JSON for review
    with open('top_jobs.json', 'w') as f:
        json.dump(jobs, f, indent=2)
    
    print("\n💾 Results saved to top_jobs.json")
    print("\n💡 Tip: Set this script to run daily with a cron job or Task Scheduler!")


if __name__ == "__main__":
    main()
