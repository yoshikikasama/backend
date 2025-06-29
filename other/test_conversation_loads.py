import json

with open('conversations.json', 'r') as f:
    data = json.load(f)

for item in data:
    title = item['title']
    create_time = item['create_time']
    update_time = item['update_time']
    current_node = item['current_node']
    
    print(f"Title: {title}")
    print(f"Create time: {create_time}")
    print(f"Update time: {update_time}")
    print(f"Current node: {current_node}")
    
    mapping = item['mapping']
    for key in mapping.keys():
        message = mapping[key]['message']
        if message:
            message_id = message['id']
            author_role = message['author']['role']
            content_parts = message['content']['parts']
            print(f"Message ID: {message_id}")
            print(f"Author role: {author_role}")
            print(f"Content parts: {content_parts}")
