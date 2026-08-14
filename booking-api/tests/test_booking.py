import unittest
from datetime import datetime, timezone
from app.booking import AvailabilityCachePolicy, BookingSlot, atomic_approval, batch_participant_sql, normalize_calendar_time, required_approver_name
class BookingContractsTest(unittest.TestCase):
  def test_r02_does_not_cache_empty_availability(self): self.assertFalse(AvailabilityCachePolicy().should_cache([]))
  def test_r05_normalizes_to_utc(self): self.assertEqual(normalize_calendar_time(datetime(2026, 8, 20, 18, 0, tzinfo=timezone.utc)).tzinfo, timezone.utc)
  def test_r07_batches_participants(self): self.assertIn('in (?, ?, ?)', batch_participant_sql(3))
  def test_r08_requires_both_updates(self): self.assertFalse(atomic_approval(True, False))
  def test_r09_rejects_missing_approver(self):
    with self.assertRaises(ValueError): required_approver_name('')
  def test_r06_slot_has_version(self): self.assertEqual(BookingSlot('room-a', datetime.now(timezone.utc), datetime.now(timezone.utc)).version, 0)
if __name__ == '__main__': unittest.main()
