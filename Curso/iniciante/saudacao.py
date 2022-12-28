hour = input('What time is it? ')

int_hour = int(hour)

morning = int_hour >= 0 and int_hour < 12
afternoon = int_hour >= 12 and int_hour< 18
night = int_hour >=18 and int_hour <= 23

if morning:
    print('Bom dia')
if afternoon:
    print('Boa tarde')
if night:
    print('Boa noite')
else:
    print('Informe um horário entre 00Hrs e 23Hrs')

