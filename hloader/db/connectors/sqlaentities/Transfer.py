"""Transfer module"""
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from hloader.db.connectors.sqlaentities.Base import Base
from hloader.entities.Transfer import Transfer


class Transfer(Base, Transfer):
    __tablename__ = "HL_TRANSFERS"

    transfer_id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)  # SERIAL NOT NULL
    scheduler_transfer_id = Column(String)  # TEXT
    job_id = Column(Integer, ForeignKey('HL_JOBS.job_id'), nullable=False)  # INTEGER NOT NULL
    transfer_status = Column(String, default=Transfer.Status.WAITING)  # TEXT
    transfer_start = Column(DateTime(timezone=True),
                            default=datetime.now())  # TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
    transfer_last_update = Column(DateTime(timezone=True),
                                  onupdate=datetime.now())  # TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
    last_modified_value = Column(String, nullable=False)  # TEXT NOT NULL

    # TODO create a new Transfer status table

    job = relationship("hloader.db.connectors.sqlaentities.Job.Job")
