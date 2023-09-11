from database import Database
from helper.writeAJson import writeAJson
from productAnalyzer import ProductAnalyzer

db = Database(database="mercado", collection="produtos")

products = ProductAnalyzer.clienteMaisGastou_unico()
writeAJson(products, "cliente_mais_gastou")

products = ProductAnalyzer.produtoMaisVendido_geral()
writeAJson(products, "produto_mais_vendeu")

products = ProductAnalyzer.produtosQueVenderamPeloMenos_1()
writeAJson(products, "produtos_que_venderam_maisde_1")

products = ProductAnalyzer.totalDeVendas_dia("2022-03-13") #pesquisando dia específico
writeAJson(products, "total_vendas_dia")

db.resetDatabase()