import defs_query_estacionamento as f

print('---------------------')
print('estacionamento')
print('---------------------')
print('cadastro-carro')
print('---------------------')

while True:

    tipo_veiculo = str(input('[moto/carro]: ').lower())
    marca = str(input('marca veiculo: ').lower())
    modelo = str(input('modelo: ').lower())
    cor = str(input('cor: ').lower())
    placa = str(input('placa: '))

    if tipo_veiculo == 'carro':
        pcd = str(input('pcd? [s/n]: ').lower())

        if pcd == 'n':

            f.cria_veiculo(tipo_veiculo, marca, modelo, cor, placa)
            id_veic = f.procura_id_veiculo(placa)
            hora, data = f.gera_data_hora()
            f.estaciona_carro(data, hora, id_veic)
            break

        elif pcd == 's':

            f.cria_veiculo(tipo_veiculo, marca, modelo, cor, placa)
            id_veic = f.procura_id_veiculo(placa)
            hora, data = f.gera_data_hora()
            f.estaciona_pcd_carro(data, hora, id_veic)
            break

    elif tipo_veiculo == 'moto':
        f.cria_veiculo(tipo_veiculo, marca, modelo, cor, placa)
        id_veic = f.procura_id_veiculo(placa)
        hora, data = f.gera_data_hora()
        f.estaciona_moto(data, hora, id_veic)
        break




