from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Deity, Race, Guild, Skill, Character

engine = create_engine('sqlite:///characters.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

humtar = Deity(name='Humtar',
               title='Lord of Battle',
               description='One of the Five Pillars of Civilization and first to ascend.')

session.add(humtar)
session.commit()

weaving = Skill(name='Weaving',
                description='The ability to weave threads of energy into spells.',
                time='0')

session.add(weaving)
session.commit()

defend = Skill(name='Defend',
               description='Protect yourself from attacks.',
               time='0')

session.add(defend)
session.commit()

human = Race(name='Human',
             patron='Humtar',
             description='While most of the Five Pillars of Civilization changed their mortal followers to better suit \
                         their interests, Humtar did not. His humans are the same versatile creatures that they were \
                         at the dawn of the Second Age, and they are the only creatures with the original divine spark \
                         that allows them to weave spells.',
             skills='Weaving')

session.add(human)
session.commit()

city_guard = Guild(name='City Guards',
                   description='The guards of the city.',
                   skills='Defend')

session.add(city_guard)
session.commit()

joe = Character(name='Joe the Guard',
                race='Human',
                guild='City Guards',
                skills='Defend')

session.add(joe)
session.commit()
