from fastapi import FastAPI, Header, HTTPException
from .booking import AvailabilityCachePolicy
app = FastAPI(title='Workspace Booking API')
policy = AvailabilityCachePolicy()
@app.get('/internal/availability')
def availability(roomId: str, from_: str, to: str, x_request_id: str = Header(default='')):
    return {'items': [], 'requestId': x_request_id}
@app.get('/health')
def health(): return {'status': 'ok'}
@app.post('/internal/bookings/{booking_id}/approve')
def approve(booking_id: str): return {'id': booking_id, 'status': 'APPROVED', 'approverName': 'Operations Team'}
