from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.v1.routers import menu
from api.v1.routers import orders
from api.v1.routers import orders

app = FastAPI(title="Dyne-in API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(menu.router, prefix="/api")
app.include_router(orders.router, prefix="/api")

@app.get("/")
async def root():
    return {"message": "Welcome to Dyne-in API"}
  
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
