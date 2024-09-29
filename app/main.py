import random
from fastapi import FastAPI

app = FastAPI()


@app.get("/helloworld")
async def root():
    return {"message": "Hello World"}


@app.get("/funcaoteste")
async def funcaoteste():
    return {"teste": True, "num_aleatorio": random.randint(0,1000)}

@app.get("/fatorial/{numero}")
async def fatorial(numero: int):
    def calc_fatorial(n):
        return 1 if n == 0 else n * calc_fatorial(n - 1)
    return {"numero": numero, "fatorial": calc_fatorial(numero)}

@app.get("/num_aleatorios/{inicio}/{fim}")
async def num_aleatorios(inicio: int, fim: int):
    return {"numero_aleatorio": random.randint(inicio, fim)}

@app.get("/converte_temperatura/{celsius}")
async def converte_temperatura(celsius: float):
    fahrenheit = (celsius * 9/5) + 32
    return {"celsius": celsius, "fahrenheit": fahrenheit}
