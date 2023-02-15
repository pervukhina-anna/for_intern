from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import declarative_base, sessionmaker


Base = declarative_base()

CONNECTION = 'postgresql://postgres:postgres@localhost:5432/spacex'

engine = create_engine(CONNECTION, echo=True)

session = sessionmaker(engine)

class Rocket(Base):
    __tablename__ = 'rockets'
    id = Column(String, primary_key=True)
    name = Column(String)
    description = Column(String)
    wikipedia = Column(String)


class Launch(Base):
    __tablename__ = 'launches'
    id = Column(String, primary_key=True)
    details = Column(String)
    mission_name = Column(String)
    # article_link = Column(String)
    # flickr_images = Column(JSONB)
    # mission_patch = Column(String)
    # mission_patch_small = Column(String)
    # presskit = Column(String)
    # reddit_campaign = Column(String)
    # reddit_launch = Column(String)
    # reddit_media = Column(String)
    # reddit_recovery = Column(String)
    # video_link = Column(String)
    # wikipedia = Column(String)


Base.metadata.create_all(engine)
