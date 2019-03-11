from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os

# PostgreSQLを指定してテーブルのcreateを指定
engine = create_engine("postgresql+psycopg2://test:333@153.126.146.72:5432/postgres", convert_unicode=True)
# bindにテーブルcreateを指定
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
# declarative_baseのインスタンス生成
Base = declarative_base()
# 実行用のセッション格納
Base.query = db_session.query_property()

def init_db():
    import db.models
    # Baseの内容でcreate実行
    Base.metadata.create_all(bind=engine)
