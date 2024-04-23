from enum import Enum

class PaymentStatus(Enum):
    COMPLETED = 0
    FAILED = 1
    PENDING = 2
    UNPAID = 3
    REFUNDED = 4