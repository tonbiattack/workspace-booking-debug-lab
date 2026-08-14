export interface AvailabilitySlot { roomId: string; from: string; to: string; available: boolean }
export interface BookingDetail { id: string; roomId: string; approverName: string; status: 'PENDING' | 'APPROVED' | 'CANCELLED' }
