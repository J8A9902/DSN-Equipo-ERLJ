from enum import Enum

class TaskStatus(Enum):
    IN_PROGRESS = 'IN_PROGRESS'
    UPLOADED = 'UPLOADED'
    PROCESSED ='PROCESSED'