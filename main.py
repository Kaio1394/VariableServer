from core.log import Log
from fastapi import FastAPI, HTTPException
from typing import Any, TypeVar, Generic, List

from models.Item import Item

PATH_DIR_LOGS_SYSTEM = "C:/LOG"
PATH_DIR_LOGS_ERROR = "C:/LOG"

app = FastAPI()
dictionary = {}

log = Log(PATH_DIR_LOGS_SYSTEM, PATH_DIR_LOGS_ERROR)

@app.get("/")
async def root():
    return {"message": "Hello"}

@app.get("/variables")
async def get_variables():
    return dictionary

@app.delete("/delete/{key}")
async def remove_variable(key: str):
    if key not in dictionary:
        raise HTTPException(status_code=404, detail="Chave não encontrada")
    del dictionary[key]
    log.info(f"Deletada variável com sucesso! Variável: {key}")
    return {"message": "Item removido com sucesso", "data": dictionary}

@app.post("/addVariable/")
async def add_variable(item: Item):
    if item.key in dictionary:
        raise HTTPException(status_code=400, detail=f"Chave {item.key} já existe")
    dictionary[item.key] = item.value
    log.info(f"Adicionado variável com sucesso! Variável: {item.key}")
    return {"message": "Item adicionado com sucesso", "data": dictionary}