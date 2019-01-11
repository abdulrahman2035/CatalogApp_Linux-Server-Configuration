from database_setup import User, Base, Item, Category
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


engine = create_engine('sqlite:///itemcatalog.db',
                       connect_args={'check_same_thread': False})

# Connect the engine to a session
Session = sessionmaker(bind=engine)

# Setting up a Session object
session = Session()

user1 = User(
    name='Abdulrahman',
    email='contact.test@gmail.com',
    
)

session.add(user1)
session.commit()

category3 = Category(
    name='test category3',
    user=user1
)

session.add(category3)
session.commit()

item3 = Item(
    name='Item 3 test',
    description='It is an test item. to test the app',
    category=category3,
    user=user1
)

session.add(item3)
session.commit()

category4 = Category(
    name='test category4',
    user=user1
)

session.add(category4)
session.commit()

item4 = Item(
    name='Item 4 test',
    description='It is an test item. to test the app',
    category=category4,
    user=user1
)

session.add(item4)
session.commit()

print('Populate data to database is done')
