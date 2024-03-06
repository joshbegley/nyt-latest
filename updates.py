import requests

README_URL = "https://raw.githubusercontent.com/joshbegley/nyt-latest/master/README.md"

def fetch_readme():
    response = requests.get(README_URL)
    response.raise_for_status()
    return response.text

def extract_data_blocks(content):
    blocks = content.strip().split('\n\n')
    return blocks

def find_new_blocks(new_blocks, existing_blocks):
    return [block for block in new_blocks if block not in existing_blocks]

def prepend_new_data(new_content, updates_file_path="updates.md", previous_content_path="previous.md"):
    try:
        with open(previous_content_path, 'r') as file:
            previous_content = file.read()
    except FileNotFoundError:
        previous_content = ""
    
    new_blocks = extract_data_blocks(new_content)
    previous_blocks = extract_data_blocks(previous_content)
    
    truly_new_blocks = find_new_blocks(new_blocks, previous_blocks)
    
    if truly_new_blocks:
        print("New updates found.")
        try:
            with open(updates_file_path, "r") as file:
                current_updates = file.read()
        except FileNotFoundError:
            current_updates = ""
        
        new_updates_str = '\n\n'.join(truly_new_blocks) + '\n\n' + current_updates
        
        with open(updates_file_path, "w") as file:
            file.write(new_updates_str)
            
    with open(previous_content_path, 'w') as file:
        file.write(new_content)

if __name__ == "__main__":
    content = fetch_readme()
    try:
        prepend_new_data(content)
    except FileNotFoundError:
        with open("updates.md", "w") as file:
            file.write(content)
        with open("previous.md", "w") as file:
            file.write(content)

