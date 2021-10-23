import sqlalchemy
import sqlalchemy.ext.declarative
import sqlalchemy.orm


engine = sqlalchemy.create_engine('mysql+pymysql://root:username@127.0.0.1/db_name')

Base = sqlalchemy.ext.declarative.declarative_base()


class Person(Base):
    __tablename__ = 'persons'
    id = sqlalchemy.Column(
        sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String(14))


# dataをengineへ挿入
Base.metadata.create_all(engine)

# 作成したengineにアクセスするsessionを作る
Session = sqlalchemy.orm.sessionmaker(bind=engine)
session = Session()

# データのcreate
p1 = Person(name='Mike')
session.add(p1)
p2 = Person(name='Nancy')
session.add(p2)
p3 = Person(name='Jun')
session.add(p3)

p4 = session.query(Person).filter_by(name='Mike').first()
p4.name = 'Michel'
session.add(p4)
p5 = session.query(Person).filter_by(name='Nancy').first()
session.delete(p5)

session.commit()

# データのread
persons = session.query(Person).all()
for person in persons:
    print(person.id, person.name)


