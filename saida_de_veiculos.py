import defs_query_estacionamento as f
import re

#constates
NAME = 'root'
PASSWORD = ''
HOST = 'localhost'
NAME_DB = 'shopping_estacionamento'

regex_placa_mercosul = r'[A-Z]{3}\s?-\s?[0-9]{4}'
regex_placa_normal = r'[A-Z0-9]{7}'
#constantes


print('buscar vaga por: ')
print('[1] - placa\n[2] - atributos veículo (cor, marca, modelo)\n[3] - bloco, '
      'andar e vaga')  #menu para localizar carro
opc = int(input('escolha: '))

if opc == 1:
    while True:
        print('digite a placa do veículo: [placa antiga: XXX-9999]')
        placa = str(input('-> '))

        if (
            re.match(regex_placa_normal, placa)
            or not re.match(regex_placa_normal, placa)
            and re.match(regex_placa_mercosul, placa)
        ):
            break

        else:
            print('Placa errada, tente todas as letras maiúsculas')

    id_veiculo = f.procura_id_veiculo(placa)

    if id_veiculo:

        db, cursor = f.open_db(NAME, PASSWORD, HOST, NAME_DB)
        if db:

            cursor.execute(f"select * from vagas where id_veiculo = '{id_veiculo}'")
            vaga = cursor.fetchone()
            cursor.execute(f"""select * from veiculos where id_veiculo = '{id_veiculo}'""")
            carro = cursor.fetchone()
            cursor.execute(f"""update vagas set status_vaga = 'livre', data_entrada = null, 
            hora_entrada = null, id_veiculo = null where id_veiculo = '{id_veiculo}';""")
            db.commit()
            cursor.execute(f"""delete from veiculos where placa = '{placa}';""")
            db.commit()
            db.close()

            hora_saida, data_saida = f.gera_data_hora()

            print('dados carro')
            print('-'*30)

            for k, v in carro.items():
                if k not in ['id_veiculo', 'tipo_veiculo']:
                    print(f'{k:-<20}> {v}')

            print('dados vaga')
            print('-' * 30)

            for k, v in vaga.items():
                if k not in ['id_vaga', 'tipo_veiculo', 'tipo_veiculo_vaga', 'status_vaga', 'id_veiculo']:
                    print(f'{k:-<30}> {v}')
            print(f'{hora_saida:->20}\ndata saida {data_saida:->20}')

    else:
        print('veículo não encontrado')

elif opc == 2:
    print('Digite os atributos do carro:')
    cor = str(input('cor -> '))
    marca = str(input('marca -> '))
    modelo = str(input('modelo -> '))

    db, cursor = f.open_db(NAME, PASSWORD, HOST, NAME_DB)
    if db:

        cursor.execute(f"""select id_veiculo from veiculos where cor = '{cor}' 
        and marca = '{marca}' and modelo = '{modelo};'""")
        id_veiculo = cursor.fetchone()

        if id_veiculo:

            cursor.execute(f"select * from vagas where id_veiculo = '{id_veiculo}'")
            vaga = cursor.fetchone()
            cursor.execute(f"""update vagas set status_vaga = 'livre', 
            data_entrada = null, hora entrada = null, id_veiculo = null where id_veiculo = '{id_veiculo}';""")
            db.commit()
            cursor.execute(f"""delete from veiculos where id_veiculo = '{id_veiculo}';""")
            db.commit()
            db.close()

elif opc == 3:
    print('digite os atributos da vaga ex: [bloco : 1], [andar : 1], [vaga : a1]')
    bloco = int(input('bloco ->'))
    andar = int(input('andar ->'))
    vaga = str(input('vaga ->')).lower()
    secao, vaga = f.retorna_vaga(vaga)

    db, cursor = f.open_db(NAME, PASSWORD, HOST, NAME_DB)
    if db:

        cursor.execute(f"""select id_veiculo from vagas where bloco = '{bloco}' and andar = '{andar}' 
        and vaga = '{vaga}' and secao = '{secao}';""")
        id_veiculo = cursor.fetchone()

        cursor.execute(f"select * from vagas where id_veiculo = '{id_veiculo}'")
        vaga = cursor.fetchone()
        cursor.execute(f"""update vagas set status_vaga = 'livre', data_entrada = null, 
        hora entrada = null, id_veiculo = null where id_veiculo = '{id_veiculo}';""")
        db.commit()
        cursor.execute(f"""delete from veiculos where id_veiculo = '{id_veiculo}';""")
        db.commit()
        db.close()

else:
    print('digite uma opção válida')
