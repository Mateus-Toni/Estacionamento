import defs_query_estacionamento as f
NAME = 'root'
SENHA = ''
HOST = 'localhost'
DATABASE = 'shopping_estacionamento'

db, cursor = f.open_db(NAME, SENHA, HOST, DATABASE)

for bloco in range(1, 5):
    for andar in range(1, 4):
        for vaga in range(1, 81):
            if andar == 1 and vaga <= 25:
                secao = 'A'
            elif andar == 1:
                secao = 'B'
            elif andar == 2 and vaga <= 25:
                secao = 'C'
            elif andar == 2:
                secao = 'D'
            elif andar == 3 and vaga <= 25:
                secao = 'E'
            elif andar == 3:
                secao = 'F'


            tipo_veiculo_vaga = 'moto' if 50 <= vaga < 70 else 'carro'
            tipo = 'PCD' if vaga >= 70 else 'Normal'
            if db:
                cursor.execute(f"""insert into vagas(bloco,andar,secao,vaga,tipo,tipo_veiculo_vaga,status_vaga) 
                values ('{bloco}','{andar}','{secao}','{vaga}','{tipo}','{tipo_veiculo_vaga}','livre')""")

db.commit()
db.close()
