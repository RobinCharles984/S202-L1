from database import Database

db = Database(database="mercado", collection="produtos")

class ProductAnalyzer:
    def __init__(self, db: Database):
        _database = Database

    def totalDeVendas_dia(self, date: str):
        db.collection.aggregate([
            {"$unwind": "produtos"},
            {"$group": {"_id": "$data_compra", "$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}
        ])

    def produtoMaisVendido_geral():
        db.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$produtos.descricao", "total": {"$sum": "$produtos.quantidade"}}},
            {"$sort": {"total": -1}},
            {"$limit": 1}
        ])
    
    def clienteMaisGastou_unico():
        db.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$cliente_id", "total": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}}
        ])
    
    def produtosQueVenderamPeloMenos_1():
        db.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$produtos", "quantidade": "$produtos.quantidade", "quantidade": 1}}
        ])
