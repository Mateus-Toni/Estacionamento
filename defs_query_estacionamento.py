import mysql.connector

#constantes:
NAME = 'root'
SENHA = ''
HOST = 'localhost'
DATABASE = 'shopping_estacionamento'
#constantes


def open_db(user, password, host, database):  #função para abrir o banco de dados
    try:
        db = mysql.connector.connect(user=user, password=password, host=host, database=database)
        cursor = db.cursor(dictionary=True)
    except:
        return None, None
    else:
        return db, cursor


def cria_veiculo(tipo_veiculo, marca, modelo, cor, placa):  #função para salvar um carro dentro do banco de dados (tabela veiculos)
    db, cursor = open_db(NAME, SENHA, HOST, DATABASE)
    if db:
        cursor.execute(f"""insert into veiculos 
        values (default,'{tipo_veiculo}','{marca}','{modelo}','{cor}','{placa}');""")
        db.commit()
        db.close()



def estaciona_carro(data_entrada, hora_entrada, id_veiculo):  #função para alterar a vaga com os dados do carro (tabela vagas)
    db, cursor = open_db(NAME, SENHA, HOST, DATABASE)
    if db:
        cursor.execute(f"""update vagas 
        set status_vaga = 'ocupado', data_entrada = '{data_entrada}', hora_entrada = '{hora_entrada}', id_veiculo = '{id_veiculo}' 
        where status_vaga = 'livre' and tipo = 'normal' and tipo_veiculo_vaga = 'carro' limit 1;""")
        db.commit()
        db.close()




def estaciona_pcd_carro(data_entrada, hora_entrada, id_veiculo):  #função para alterar a vaga com os dados do carro P.C.D (tabela vagas)
    db, cursor = open_db(NAME, SENHA, HOST, DATABASE)
    if db:
        cursor.execute(f"""UPDATE VAGAS SET DATA_ENTRADA = '{data_entrada}', hora_entrada = '{hora_entrada}', id_veiculo = '{id_veiculo}' 
        where status_vaga = 'livre' and tipo = 'PCD' and tipo_veiculo_vaga = 'carro' limit 1;""")
        db.commit()
        db.close()



def procura_id_veiculo(placa):  #função para retornar o I.D de um carro ou moto pela sua placa
    db, cursor = open_db(NAME, SENHA, HOST, DATABASE)
    if db:
        cursor.execute(f"""select id_veiculo from veiculos where placa = '{placa}'""")
        id_veic = cursor.fetchone()
        id_veic = id_veic['id_veiculo']
        db.close()

        return id_veic


def estaciona_moto(data_entrada, hora_entrada, id_veiculo):  #função para alterar a vaga com os dados da moto (tabela vagas)
    db, cursor = open_db(NAME, SENHA, HOST, DATABASE)
    if db:
        cursor.execute(f"""update vaga set status_vaga = 'ocupado', data_entrada = '{data_entrada}', hora_entrada = '{hora_entrada}', id_veiculo = '{id_veiculo}' 
        where status_vaga = 'livre' and not tipo = 'PCD' and tipo_veiculo_vaga = 'moto' limit 1;""")
        db.commit()
        db.close()




def gera_data_hora():  #função para gerar data e hora
    from datetime import datetime
    hora = datetime.today().hour
    minuto = datetime.today().minute
    hora_final = f'{hora}:{minuto}'
    data = datetime.today().date()

    return hora_final, data


def gera_busca_pcar(cor, modelo, marca):  #função que busca veículos pelos atributos de cor, modelo e marca
    db, cursor = open_db(NAME, SENHA, HOST, DATABASE)
    if db:
        cursor.execute(f"""select id_veiculo from veiculos 
        where cor = '{cor}' and modelo = '{modelo}' and marca = '{marca}';""")
        id_veiculo = cursor.fetchone()
        id_veiculo = id_veiculo['id_veiculo']
        cursor.execute(f"""select * from vagas where id_veiculo = '{id_veiculo}'""")
        vaga = cursor.fetchone()
        for k, v in vaga.items():
            if k != 'status_vaga':
                print(f'{k:-<30}> {v}')


def busca_placa(placa):  #função que busca veículos pela placa
    db, cursor = open_db(NAME, SENHA, HOST, DATABASE)
    if db:
        cursor.execute(f"""select id_veiculo from veiculos where placa = '{placa.upper()}';""")
        id_veiculo = cursor.fetchone()
        id_veiculo = id_veiculo['id_veiculo']
        cursor.execute(f"""select * from vagas where id_veiculo = '{id_veiculo}'""")
        vaga = cursor.fetchone()
        for k, v in vaga.items():
            if k != 'status_vaga':
                print(f'{k:-<30}> {v}')


def busca_vaga(vaga, bloco, andar):  #função que busca vagas
    secao = vaga[0]
    vaga1 = vaga[-2] + vaga[-1] if len(vaga) >= 3 else vaga[-1]
    db, cursor = open_db(NAME, SENHA, HOST, DATABASE)
    if db:
        cursor.execute(f"""select * from vagas where secao = '{secao}' and vaga = '{vaga1}' and bloco = '{bloco}' and andar = '{andar}'""")
        vagas = cursor.fetchone()
        for k, v in vagas.items():
            print(f'{k:-<30}> {v}')



def retorna_vaga(vaga):  #função que separa o número da vaga e a seção e retorna esses dois itens
    secao = vaga[0]
    vaga1 = vaga[-2] + vaga[-1] if len(vaga) >= 3 else vaga[-1]

    return secao, vaga1



