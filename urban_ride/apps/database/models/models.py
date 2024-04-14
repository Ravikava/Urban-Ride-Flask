from apps.helpers.base_model import BaseModel
from sqlalchemy.dialects import postgresql as pg
from datetime import datetime
from sqlalchemy.sql import func
from apps import db
# from .models import *

class User(BaseModel):
    __tablename__="user"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50),nullable=True)
    profile_image = db.Column(db.String(256))
    phone_number = db.Column(db.String(10), unique=True)
    email = db.Column(db.String(100), unique=True, nullable=True)
    is_email_verified = db.Column(db.Boolean, default=True)
    is_active = db.Column(db.Boolean, default=True)
    is_blocked = db.Column(db.Boolean, default=False)
    allow_multiple_login = db.Column(db.Boolean, default=False)
    meta_data = db.Column(pg.JSONB(),server_default='{}')
    
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now())
    
    user_device = db.relationship('UserDeviceInfo', foreign_keys='UserDeviceInfo.user_id', back_populates='user')

class UserDeviceInfo(BaseModel):
    __tablename__ = 'user_device_info'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'))
    device_id = db.Column(db.String(256))
    device_type = db.Column(db.String(20))
    device_name = db.Column(db.String(55))
    platform = db.Column(db.String(20))
    app_version = db.Column(db.String(35))
    os_version = db.Column(db.String(20))
    fcm_token = db.Column(db.String(256), nullable=True)
    
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now())
    
    # Define the relationship between FriendRequest and User (sender and receiver)
    user = db.relationship('User', foreign_keys=[user_id], back_populates='user_device')
    # receiver = db.relationship('User', foreign_keys=[receiver_id], back_populates='received_friend_requests')

    
class VehicleTypes(BaseModel):
    __tablename__ = 'vehicle_types'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    vehicle_class = db.Column(db.String(50))
    class_category = db.Column(db.String(50))
    seating_capacity = db.Column(db.Integer)
    icon = db.Column(db.String(256))
    is_enabled = db.Column(db.Boolean, default=True)
    
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now())
    
    # Define the relationship between Group and User
    # user = db.relationship('User', back_populates='groups')

    # # Define the relationship between Group and Expense
    # expenses = db.relationship('Expense', back_populates='group')
    
class TripTypes(BaseModel):
    __tablename__ = 'trip_types'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(56))
    title = db.Column(db.String(56))
    terms_condition = db.Column(pg.ARRAY(pg.JSONB()))
    is_enabled = db.Column(db.Boolean, default=True)
    
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now())
    

class UserLogin(BaseModel):
    __tablename__ = 'user_login'
    
    id = db.Column(db.Integer, primary_key=True)
    
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'))
    device_id = db.Column(db.String(100), nullable=False)
    device_name = db.Column(db.String(100), nullable=True)
    logged_in_status = db.Column(db.Boolean, default=False)
    login_at = db.Column(db.DateTime, server_default=func.now())
    logout_at = db.Column(db.DateTime, nullable=True)
    location = db.Column(pg.JSONB()) # lat-long
    
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now())

# class User(BaseModel):
#     __tablename__ = 'user'
    
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(50),nullable=False)
#     user_name = db.Column(db.String(50),nullable=True,unique=True)
#     profile_image = db.Column(db.String(256))
#     email = db.Column(db.String(255), unique=True, nullable=False)
#     phone_number = db.Column(db.String(10), unique=True)
#     dob = db.Column(db.String(12))
#     friends = db.Column(pg.ARRAY(db.Integer, as_tuple=False, dimensions=None, zero_indexes=False), nullable=True)
#     Group = db.Column(pg.ARRAY(db.Integer, as_tuple=False, dimensions=None, zero_indexes=False), nullable=True)
#     current_currency = db.Column(db.String(50),nullable=True)
#     all_currency_used = db.Column(pg.ARRAY(db.String(50), as_tuple=False, dimensions=None, zero_indexes=False), nullable=True)
#     device_ids = db.Column(pg.ARRAY(db.String(256), as_tuple=False, dimensions=None, zero_indexes=False), nullable=True)
#     created_at = db.Column(db.DateTime, server_default=func.now())
#     updated_at = db.Column(db.DateTime, server_default=func.now())
#     # Define the relationship between User and Group
#     # groups = db.relationship('Group', back_populates='user')

#     # Define the relationship between User and FriendRequest for sender and receiver
#     sent_friend_requests = db.relationship('FriendRequest', foreign_keys='FriendRequest.sender_id', back_populates='sender')
#     # received_friend_requests = db.relationship('FriendRequest', foreign_keys='FriendRequest.receiver_id', back_populates='receiver')
    

# class FriendRequest(BaseModel):
#     __tablename__ = 'friend_request'

#     id = db.Column(db.Integer, primary_key=True)
#     sender_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'))
#     receiver_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'))
#     friendship_status = db.Column(db.Boolean, default=False)
#     request_status = db.Column(db.String(20)) # ( pending,accepted,rejected )
#     created_at = db.Column(db.DateTime, server_default=func.now())
#     updated_at = db.Column(db.DateTime, server_default=func.now())
    
#     # Define the relationship between FriendRequest and User (sender and receiver)
#     sender = db.relationship('User', foreign_keys=[sender_id], back_populates='sent_friend_requests')
#     # receiver = db.relationship('User', foreign_keys=[receiver_id], back_populates='received_friend_requests')

    
# class Group(BaseModel):
#     __tablename__ = 'group'
    
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'))
#     group_name = db.Column(db.String(50),nullable=False)
#     group_image = db.Column(db.String(256))
#     group_description =db.Column(db.String(256))
#     group_members = db.Column(pg.ARRAY(db.Integer, as_tuple=False, dimensions=None, zero_indexes=False), nullable=True)
#     left_group_member = db.Column(pg.ARRAY(db.Integer, as_tuple=False, dimensions=None, zero_indexes=False), nullable=True)
#     group_balance = db.Column(db.Float)
#     group_status = db.Column(db.Boolean, default=True) # active or in-active Group
#     created_at = db.Column(db.DateTime, server_default=func.now())
#     updated_at = db.Column(db.DateTime, server_default=func.now())
    
#     # Define the relationship between Group and User
#     # user = db.relationship('User', back_populates='groups')

#     # # Define the relationship between Group and Expense
#     # expenses = db.relationship('Expense', back_populates='group')
# class Exepense(BaseModel):
#     __tablename__ = 'expense'
    
#     id = db.Column(db.Integer, primary_key=True)
#     expense_tag = db.Column(db.String(30),nullable=False)
#     total_amount = db.Column(db.Float)
#     expense_currency = db.Column(db.String(50))
#     expense_description = db.Column(db.String(256))
#     expense_image = db.Column(db.String(256))
#     expense_category = db.Column(db.String(50))
#     expense_comment = db.Column(db.String(256))
#     payer = db.Column(pg.ARRAY(pg.JSONB()))
#     payee = db.Column(pg.ARRAY(pg.JSONB()))
#     group_id = db.Column(db.Integer, db.ForeignKey('group.id', ondelete='CASCADE'))
#     is_deleted = db.Column(db.Boolean, default=False)
#     created_at = db.Column(db.DateTime, server_default=func.now())
#     updated_at = db.Column(db.DateTime, server_default=func.now())
    
#     # Define the relationship between Expense and User (currency)
#     # currency = db.relationship('User', foreign_keys=[expense_currency])

#     # # Define the relationship between Expense and Group
#     # group = db.relationship('Group', back_populates='expenses')
    
#     # snapshots = db.relationship('ExpenseSnapShot', back_populates='expense')
    
    
# class ExpenseSnapShot(BaseModel):
#     __tablename__ = 'expense_snapshot'
    
#     id = db.Column(db.Integer, primary_key=True)
#     expense_id = db.Column(db.Integer, db.ForeignKey('expense.id', ondelete='CASCADE'))
#     expense_snapshots = db.Column(pg.ARRAY(pg.JSONB()))
#     created_at = db.Column(db.DateTime, server_default=func.now())
#     updated_at = db.Column(db.DateTime, server_default=func.now())
    
#     # expense = db.relationship('Expense', back_populates='snapshots')
    

# class UserLogin(BaseModel):
#     __tablename__ = 'user_login'
    
#     id = db.Column(db.Integer, primary_key=True)
    
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'))
#     device_id = db.Column(db.String(100), nullable=False)
#     device_name = db.Column(db.String(100), nullable=True)
#     logged_in_status = db.Column(db.Boolean, default=False)
#     login_at = db.Column(db.DateTime, server_default=func.now())
#     logout_at = db.Column(db.DateTime, nullable=True)
#     location = db.Column(pg.JSONB()) # lat-long
    
#     created_at = db.Column(db.DateTime, server_default=func.now())
#     updated_at = db.Column(db.DateTime, server_default=func.now())
