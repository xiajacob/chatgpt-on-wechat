from sqlalchemy import Column, Integer, String, DateTime, Text, Enum, ForeignKey, TIMESTAMP, BigInteger
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    open_id = Column(String(255), nullable=False, unique=True)
    union_id = Column(String(255), default=None)
    follow_time = Column(DateTime, default=None)
    membership_start_time = Column(DateTime, default=None)
    membership_end_time = Column(DateTime, default=None)
    is_blacklisted = Column(Integer, nullable=False, default=0)
    remarks = Column(Text)
    is_delete = Column(Integer, nullable=False, default=0)
    created_at = Column(TIMESTAMP, default=None)
    updated_at = Column(TIMESTAMP, default=None, onupdate=None)


class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True, autoincrement=True)
    product_name = Column(String(255), nullable=False)
    service_duration = Column(Integer, default=None)
    price = Column(Integer, default=None)
    description = Column(Text)
    is_delete = Column(Integer, nullable=False, default=0)
    created_at = Column(TIMESTAMP, default=None)
    updated_at = Column(TIMESTAMP, default=None, onupdate=None)


class WechatPaymentOrder(Base):
    __tablename__ = 'wechat_payment_orders'
    id = Column(Integer, primary_key=True, autoincrement=True)
    order_no = Column(String(64), nullable=False, unique=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    open_id = Column(String(255), nullable=False)
    product_id = Column(Integer, ForeignKey('products.id'), default=None)
    total_amount = Column(Integer, nullable=False)
    pay_amount = Column(Integer, nullable=False)
    currency = Column(String(3), default='CNY')
    trade_type = Column(String(20), nullable=False)
    transaction_id = Column(String(64), default=None)
    payment_status = Column(Enum('UNPAID', 'PAID', 'REFUND', 'CLOSED'), nullable=False, default='UNPAID')
    payment_time = Column(DateTime, default=None)
    notify_url = Column(String(255), default=None)
    client_ip = Column(String(45), default=None)
    device_info = Column(String(32), default=None)
    out_trade_no = Column(String(64), default=None)
    is_delete = Column(Integer, nullable=False, default=0)
    create_time = Column(TIMESTAMP, default=None)
    update_time = Column(TIMESTAMP, default=None, onupdate=None)
    attach = Column(Text)


class MidjourneyUsageLog(Base):
    __tablename__ = 'midjourney_usage_log'
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    open_id = Column(String(255), default=None)
    user_prompt = Column(Text, nullable=False)
    api_mode = Column(Enum('fast', 'relax'), nullable=False)
    request_time = Column(TIMESTAMP, default=None)
    completion_time = Column(DateTime, default=None)
    is_successful = Column(Integer, nullable=False, default=0)
    is_delete = Column(Integer, nullable=False, default=0)
    created_at = Column(TIMESTAMP, default=None)
    updated_at = Column(TIMESTAMP, default=None, onupdate=None)
