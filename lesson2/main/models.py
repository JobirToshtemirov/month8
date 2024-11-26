import sqlalchemy
from sqlalchemy import DateTime, func, ForeignKey
from sqlalchemy.orm import relationship

from main.constants import UserStatus
from databases.database import metadata

users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("username", sqlalchemy.String, nullable=True),
    sqlalchemy.Column("full_name", sqlalchemy.String, nullable=True),
    sqlalchemy.Column("language", sqlalchemy.String, nullable=True),
    sqlalchemy.Column("chat_id", sqlalchemy.BigInteger, unique=True, nullable=False),
    sqlalchemy.Column("phone_number", sqlalchemy.String, nullable=True),
    sqlalchemy.Column("status", sqlalchemy.Enum(UserStatus), default=UserStatus.active, nullable=False),
    sqlalchemy.Column('created_at', DateTime(timezone=True), server_default=func.now(), nullable=False),
    sqlalchemy.Column('updated_at', DateTime(timezone=True), onupdate=func.now(), nullable=False)
)

meals = sqlalchemy.Table(
    "meals",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("meal_name", sqlalchemy.String, nullable=False),
    sqlalchemy.Column("description", sqlalchemy.String, nullable=True),
    sqlalchemy.Column("price", sqlalchemy.Float, nullable=False),
    sqlalchemy.Column("available", sqlalchemy.Boolean, default=True, nullable=False),
    sqlalchemy.Column("created_at", DateTime(timezone=True), server_default=func.now(), nullable=False),
    sqlalchemy.Column("updated_at", DateTime(timezone=True), onupdate=func.now(), nullable=False)
)

meal_categories = sqlalchemy.Table(
    "meal_categories",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("category_name", sqlalchemy.String, nullable=False),
)

meal_category_association = sqlalchemy.Table(
    "meal_category_association",
    metadata,
    sqlalchemy.Column("meal_id", sqlalchemy.Integer, ForeignKey("meals.id"), primary_key=True),
    sqlalchemy.Column("category_id", sqlalchemy.Integer, ForeignKey("meal_categories.id"), primary_key=True),
)

orders = sqlalchemy.Table(
    "orders",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("user_id", sqlalchemy.Integer, ForeignKey("users.id"), nullable=False),
    sqlalchemy.Column("meal_id", sqlalchemy.Integer, ForeignKey("meals.id"), nullable=False),  # Linking orders to meals
    sqlalchemy.Column("order_status", sqlalchemy.Enum(OrderStatus), default=OrderStatus.pending, nullable=False),
    sqlalchemy.Column("quantity", sqlalchemy.Integer, nullable=False),
    sqlalchemy.Column("total_price", sqlalchemy.Float, nullable=False),
    sqlalchemy.Column("order_date", DateTime(timezone=True), server_default=func.now(), nullable=False),
    sqlalchemy.Column("updated_at", DateTime(timezone=True), onupdate=func.now(), nullable=False)
)


class Order:
    __tablename__ = 'orders'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    user_id = sqlalchemy.Column(sqlalchemy.Integer, ForeignKey("users.id"), nullable=False)
    meal_id = sqlalchemy.Column(sqlalchemy.Integer, ForeignKey("meals.id"), nullable=False)
    meal = relationship("Meal", back_populates="orders")


user_basket = sqlalchemy.Table(
    'user_basket',
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("user_id", sqlalchemy.Integer, ForeignKey('users.id'), nullable=False),
    sqlalchemy.Column("meal_id", sqlalchemy.Integer, ForeignKey('meals.id'), nullable=False),
    sqlalchemy.Column("quantity", sqlalchemy.Integer, nullable=False),
    sqlalchemy.Column("price", sqlalchemy.Float, nullable=False)
)

user_basket.meal = relationship('Meal', backref='user_basket')
user_basket.user = relationship('User', backref='user_basket')