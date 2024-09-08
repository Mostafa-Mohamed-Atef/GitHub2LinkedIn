from github import Github, Auth
from transformers import pipeline
import pyperclip

def generate_post(readme_content, project_name, repo_url):
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    summary = summarizer(readme_content, max_length=150, min_length=50, do_sample=False)[0]['summary_text']
    linkedin_post = f"""Excited to share my latest project: {project_name}! 🚀

{summary}

Check it out on GitHub for more details and how to get started:{repo_url}
"""
    
    return linkedin_post

#GitHub setup
auth = Auth.Token("your token")

try:
    with Github(auth=auth) as g:
        repo = g.get_repo("your repository")
        readme_content = repo.get_readme().decoded_content.decode()
        project_name = repo.name
        repo_url = repo.html_url
        linkedin_post = generate_post(readme_content, project_name, repo_url)
        print("Generated LinkedIn post:")
        print(linkedin_post)
        print("Want to copy the post to clipboard? (y/n)")
        if input() == "y":
            pyperclip.copy(linkedin_post)
except Exception as e:
    print(f"An error occurred: {e}")
