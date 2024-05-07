from sqlalchemy import desc, func

from pojo.Message import Message
from config.databaseConnect import Session


class MessageService:
    def __init__(self):
        self.session = Session()

    def findByPage(self, page_size, page_num, timestamp):
        # 执行分页查询
        messages = self.session.query(Message).filter(Message.message_time <= str(timestamp)).order_by(
            desc(Message.message_time)).limit(page_size).offset((page_num - 1) * page_size).all()
        total_count = self.session.query(func.count(Message.message_id)).filter(
            Message.message_time <= str(timestamp)).scalar()
        self.session.commit()
        return myjson(messages, total_count)

    def findActive(self):
        messages = self.session.query(Message).filter(
            (Message.message_type == 'join') | (Message.message_type == 'leave')).all()
        return myjson2(messages)


def myjson(messages, total_count):
    result = []
    for message in messages:
        result.append({'value': message.message_text, 'type': message.message_type, 'time': message.message_time})
    return {'messages': result, 'total': total_count}


def myjson2(messages):
    result = []
    for message in messages:
        result.append({'value': message.message_text, 'type': message.message_type, 'time': message.message_time})
    return {'messages': result}
