from Process import Process as pr
import Connection as conn

# PRINCIPAIS VARIAVEIS DE AMBIENTE, CASO VOCÊ ALTERE NOMES DE ARQUIVOS, VOCE DEVE MUDA-LOS:
PATH = "databases/emailSintese.xlsx"
FUTUREPATH = "databases/emailSintese.csv"
MEMBROSGRUP = "databases/membros@sintesejr.com.br.csv"

process = pr(PATH)
conn.update(process.final, FUTUREPATH)
conn.update(process.membrosEmail, MEMBROSGRUP)
