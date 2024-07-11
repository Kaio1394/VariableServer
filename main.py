from core.log import Log
from core.config import Config
from fastapi import FastAPI, HTTPException
from typing import Any, Dict, TypeVar, Generic, List

from models.Item import Item

path_dir_logs_system = Config.parse("Logs:path_file_system")
path_dir_logs_error = Config.parse("Logs:path_file_error")
CODE_ERROR_400 = "400"
CODE_ERROR_404 = "404"

app = FastAPI()
dictionary: Dict[str, Any] = {}

log = Log(path_dir_logs_system, path_dir_logs_error)

@app.get("/variables")
async def get_variables():
    return dictionary

@app.get("/variable/{key}")
async def get_variable(key: str):
    if key not in dictionary:
        log.error(f"Chave não encontrada")
        raise HTTPException(status_code=CODE_ERROR_404, detail="Chave não encontrada")
    return {"value": dictionary[key]}

@app.put("/update")
async def update_variable(item: Item):
    if item.key not in dictionary:
        log.error(f"Chave não encontrada")
        raise HTTPException(status_code=CODE_ERROR_404, detail="Chave não encontrada")
    dictionary[item.key] = item.value
    return {"value": dictionary[item.key]}

@app.delete("/delete/{key}")
async def remove_variable(key: str):
    if key not in dictionary:
        log.error(f"Chave não encontrada")
        raise HTTPException(status_code=CODE_ERROR_404, detail="Chave não encontrada")
    del dictionary[key]
    log.info(f"Deletada variável com sucesso! Variável: {key}")
    return {"message": "Item removido com sucesso", "data": dictionary}

@app.post("/addVariable/")
async def add_variable(item: Item):
    if item.key in dictionary:
        log.error(f"Chave {item.key} já existe")
        raise HTTPException(status_code=CODE_ERROR_400, detail=f"Chave {item.key} já existe")
    dictionary[item.key] = item.value
    log.info(f"Adicionado variável com sucesso! Variável: {item.key}")
    return {"message": "Item adicionado com sucesso", "data": dictionary}