from fastapi import FastAPI

from app.routers import branch, student

app = FastAPI(
    title='Students API',
    description='Simple python students API',
    version='1.0.0',
    contact={
        'name': 'SuRu',
        'url': 'https://github.com/suru33/students-api-python',
        'email': '33urus@gmail.com'
    },
    license_info={
        'name': 'GNU General Public License v2.0',
        'url': 'https://github.com/suru33/students-api-python/blob/master/LICENSE'
    }
)

app.include_router(branch.router)
app.include_router(student.router)


@app.get("/")
@app.get("/health")
async def health_check():
    return {'health': 'OK'}
