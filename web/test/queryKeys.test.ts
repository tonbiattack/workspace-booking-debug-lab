import assert from 'node:assert/strict'
import test from 'node:test'
import { bookingKeys } from '../src/queryKeys.js'
test('R12: availability cache keys distinguish room and time range', () => {
  assert.notDeepEqual(bookingKeys.availability('room-a', '2026-08-20T09:00:00Z', '2026-08-20T10:00:00Z'), bookingKeys.availability('room-b', '2026-08-20T09:00:00Z', '2026-08-20T10:00:00Z'))
  assert.notDeepEqual(bookingKeys.availability('room-a', '2026-08-20T09:00:00Z', '2026-08-20T10:00:00Z'), bookingKeys.availability('room-a', '2026-08-20T10:00:00Z', '2026-08-20T11:00:00Z'))
})
