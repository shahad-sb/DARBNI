import cohere
import os

# getting API key
API_KEY= "bhopo2vlz6dGq4gZENrZCBbjUzDeggL3RZURsmjF"

# Setting up the cohere client
co = cohere.Client(API_KEY)

# set the max number of tokens to generate.
max_tokens = 1000

# Main function for suggesting gifts
def suggest(
    job_postion, 
    industry, 
    week_no,
    ):

    prompt=f"""Training Plan for {job_postion} in {industry} for {week_no} - Weekly Skill Set and Tasks with Detailed Lists. Don't add your explanation, just write the weeks and tasks. Do not exceed the plan from {week_no} weeks. Do not generate skill set. Encode the response such that it should be in following format: Week 1: do something,do something. Limit your response to {max_tokens} tokens."""

    response = co.generate(
    model='command-nightly',
    prompt=prompt,
    stop_sequences=["--"],
    max_tokens=max_tokens,
    temperature=0,
    )
    suggestions = response.generations[0].text # list of suggestions
    suggestions = parse_response(suggestions) # parsing suggestions
    return suggestions # removing extra space and return

def parse_response(suggestions):
    # converting suggestions to dictionary for easy access
    suggestions = suggestions.split("\n")
    suggestions = [suggestion.strip() for suggestion in suggestions]
    # creating a dictionary of week and tasks
    week_tasks = {}
    for suggestion in suggestions:
        if suggestion.startswith("Week"):
            week, tasks = suggestion.split(":")
            week_tasks[week] = []
            week_tasks[week] = [task.strip() for task in tasks.split(".") if task.strip() != ""]

    return week_tasks

if __name__ == "__main__":
    job_postion = "Software Engineer"
    industry = "Software"
    week_no = 2
    suggestions = suggest(job_postion, industry, week_no)
    print(suggestions)