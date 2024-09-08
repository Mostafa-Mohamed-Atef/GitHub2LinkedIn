from github import Github, Auth
from transformers import pipeline
import os

def generate_post(readme_content):
    generator = pipeline('text-generation', model='gpt2')
    
    prompt = f"Generate a LinkedIn post about this project:\n\n{readme_content[:500]}..."
    generated_text = generator(prompt, max_length=200, num_return_sequences=1)[0]['generated_text']
    
    post = generated_text[len(prompt):].strip()
    
    return post

# GitHub setup
auth = Auth.Token("your github token")

try:
    with Github(auth=auth) as g:
        repo = g.get_repo("your repo")
        readme_content = repo.get_readme().decoded_content.decode()
        
        linkedin_post = generate_post(readme_content)
        print("Generated LinkedIn post:")
        print(linkedin_post)
except Exception as e:
    print(f"An error occurred: {e}")