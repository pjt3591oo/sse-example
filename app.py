import uvicorn
from fastapi import FastAPI, Request
from sse_starlette.sse import EventSourceResponse

from fastapi.middleware.cors import CORSMiddleware
import time
import asyncio

app = FastAPI()

origins = ["http://localhost:8080"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

async def generator(req: Request):
  event_id = int(time.time() * 1000)

  while True:
    is_disconnected = await req.is_disconnected()
    if is_disconnected: break

    for i in range(3):

      yield {
        "event": "something_event",
        "id": event_id,
        "data": {"id": event_id, "msg": i},
      }

    await asyncio.sleep(3)

@app.get("/")
async def sse_test(req: Request):
  return EventSourceResponse(generator(req))

if __name__ == '__main__':
  uvicorn.run("app:app", host = '0.0.0.0', port=3000)