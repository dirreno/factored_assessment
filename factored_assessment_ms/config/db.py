from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://admin:admin@localhost:3306/factored_assessment_db")

meta = MetaData()

conn = engine.connect()