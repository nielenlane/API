from fastapi import FastAPI

app = FastAPI()
item_venda = {
    1: {"item": "coca-cola", "preco_unitario": 5, "quantidade": 5},
    2: {"item": "cerveja 600ml", "preco_unitario": 10, "quantidade": 5},
    3: {"item": "vinho 750ml", "preco_unitario": 30, "quantidade": 5},
    4: {"item": "gin", "preco_unitario": 100, "quantidade": 5}
}

@app.get("/home")
def home():
    return {"APP de Vendas com FastAPI"}

@app.get("/vendas/{id_venda}")
def selecionar_venda_por_id(id_venda: int):
    if id_venda in item_venda:
        return item_venda[id_venda]
    else:
        return {"Erro": "ID da Venda não existe"}