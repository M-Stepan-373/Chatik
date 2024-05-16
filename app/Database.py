import json

class Message:
    content: str
    time: str
    author: str
    is_gif: bool

    def __init__(self, *, content: str, time: str, author: str, is_gif: bool):
        self.content = content
        self.time = time
        self.author = author
        self.is_gif = is_gif

class Database:
    def __init__(self, filename='./database.json'):
        self.filename = filename
        with open(self.filename, 'r') as f:
            self.content = json.loads(f.read())

    def save_db(self):
        with open(self.filename, 'w') as f:
            f.write(json.dumps(self.content))

    def write_message(self, *, msg: Message):
        self.content[str(self.get_db_size())] = {
            'content': msg.content, 
            'time': msg.time,
            'author': msg.author,
            'is_gif': msg.is_gif,
            'id': self.get_db_size()
        }

    def read_message(self, *, id: int):
        value = self.content[str(id)]
        return Message(
            content=value['content'],
            time=value['time'],
            author=value['author'],
            is_gif=value['is_gif'],
        )
    
    def get_db_size(self):
        return len(self.content.keys())
