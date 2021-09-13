from app import app


@app.get("/")
@app.get("/health")
async def health_check():
    return {'health': 'OK'}
