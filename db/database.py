from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os

# PostgreSQLを指定してテーブルのcreateを指定
db_uri = os.environ.get('DATABASE_URL') or "postgresql://localhost/postgres"
engine = create_engine(db_uri, convert_unicode=True)
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
