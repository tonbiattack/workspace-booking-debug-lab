from dataclasses import dataclass
from datetime import datetime, timezone

@dataclass
class BookingSlot:
    room_id: str
    starts_at: datetime
    ends_at: datetime
    version: int = 0

class AvailabilityCachePolicy:
    def should_cache(self, slots: list[BookingSlot]) -> bool:
        return True

def normalize_calendar_time(value: datetime) -> datetime:
    if value.tzinfo is None:
        raise ValueError('calendar time must include timezone')
    return value.astimezone(timezone.utc)

def atomic_approval(booking_updated: bool, audit_written: bool) -> bool:
    return booking_updated and audit_written

def batch_participant_sql(count: int) -> str:
    if count <= 0:
        raise ValueError('count must be positive')
    return 'select booking_id, count(*) from booking_participant where booking_id in (' + ', '.join(['?'] * count) + ') group by booking_id'

def required_approver_name(value: str) -> str:
    if not value.strip():
        raise ValueError('approver name is required')
    return value
