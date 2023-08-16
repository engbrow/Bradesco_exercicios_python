from Area import Retangulo
import math

while True:
    piso_a= float(input('Digite o lado A do piso: '))
    piso_b= float(input('Digite o lado B do piso: '))

    piso= Retangulo(piso_a, piso_b)

    az_a= float(input('Digite o lado A do azulejo: '))
    az_b= float(input('Digite o lado B do azulejo: '))

    azulejo= Retangulo(az_a, az_b)

    area_piso= piso.area()
    area_az= azulejo.area()

    qtd_az= area_piso/ area_az

    if area_piso% area_az== 0:
        print(f'A quantidade exata de azulejos para preencher o piso é de {qtd_az}')
    else:
        print(f'A quantidade minima de azulejos para preencher o piso é de {math.ceil(qtd_az)}')
