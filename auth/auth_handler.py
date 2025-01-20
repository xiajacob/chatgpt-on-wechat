# coding=utf-8
"""
Created on 2025/1/12

@author: xiajinyang
"""
from auth.db import Database
from auth.models import User
from wechatpy import WeChatClient
from datetime import datetime

from channel.wechatmp.wechatmp_channel import WechatMPChannel


class AuthHandler:
    def __init__(self):
        self.db = Database()
        self.client = WechatMPChannel().client

    def add_user(self, open_id):
        # Use wechatpy to get unionid and follow_time
        user_info = self.client.user.get(open_id)
        union_id = user_info.get('unionid')
        follow_time = datetime.fromtimestamp(user_info.get('subscribe_time'))

        with self.db.get_session() as session:
            new_user = User(
                open_id=open_id,
                union_id=union_id,
                follow_time=follow_time,
                is_blacklisted=False,
            )
            session.add(new_user)

    def has_conversation_permission(self, open_id):
        with self.db.get_session() as session:
            user = session.query(User).filter(User.open_id == open_id).first()
            if user and user.membership_end_time and user.membership_end_time > datetime.now():
                return True
            return False

    #检查用户是否有对话权限，返回True或False。当用户的会员结束时间晚于当前时间，则认为有对话权限

# Usage example:
# auth_handler = AuthHandler(appid='your_appid', secret='your_secret')
# auth_handler.add_user(open_id="user_open_id")
# has_permission = auth_handler.has_conversation_permission(open_id="user_open_id")
