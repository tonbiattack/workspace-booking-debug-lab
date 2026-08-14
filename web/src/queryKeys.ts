export const bookingKeys = {
  availability: (roomId: string, from: string, to: string) => ['availability', roomId, from, to] as const,
  booking: (bookingId: string) => ['booking', bookingId] as const
}
