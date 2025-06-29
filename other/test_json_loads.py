import json

with open('message_feedback.json', 'r') as f:
    data = json.load(f)
for item in data:
    message_id = item['message_id']
    conversation_id = item['conversation_id']
    user_id = item['user_id']
    rating = item['rating']
    content = json.loads(item['content'])['text']
    print(f"Message ID: {message_id}")
    print(f"Conversation ID: {conversation_id}")
    print(f"User ID: {user_id}")
    print(f"Rating: {rating}")
    print(f"Content: {content}")
