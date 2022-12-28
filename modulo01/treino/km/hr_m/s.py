speed = int(input('Informe a velocidade em M/s: '))
veiculo = input('Informe o Veículo: \n 1 - Carro \n 2 -Caminhão... \n\n')

SpeedKmh = speed * 3.6

print("{} M/s equivale a {:.3f} Km/Hr".format(speed, SpeedKmh))

if SpeedKmh > 80 and veiculo == '2':
    print('Motorista multado, Limite para caminhão de 80Km/Hr')

elif SpeedKmh > 110 and veiculo =='1':
    print('Motorista multado limite para carro de 110Km/Hr')

else:
    print('Velocidade dentro do limite permitido')

