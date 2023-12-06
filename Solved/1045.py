def triangulo(primeiro, segundo, terceiro):
    
    if primeiro >= segundo + terceiro:
        print('NAO FORMA TRIANGULO')
    else:
        if (primeiro ** 2) == (segundo ** 2) + (terceiro ** 2):
            print('TRIANGULO RETANGULO')
        if (primeiro ** 2) > (segundo ** 2) + (terceiro ** 2):
            print('TRIANGULO OBTUSANGULO')
        if (primeiro ** 2) < (segundo ** 2) + (terceiro ** 2):
            print('TRIANGULO ACUTANGULO')
        if primeiro == segundo == terceiro:
            print('TRIANGULO EQUILATERO')
        if primeiro == segundo != terceiro or segundo == terceiro != primeiro or terceiro == primeiro != segundo:
            print('TRIANGULO ISOSCELES')

primeiro, segundo, terceiro = map(float, input().split())

if(terceiro > segundo):
    parametro = terceiro
    terceiro = segundo
    segundo = parametro

if(segundo > primeiro):
    parametro = segundo
    segundo = primeiro
    primeiro = parametro

if(terceiro > segundo):
    parametro = terceiro
    terceiro = segundo
    segundo = parametro

triangulo(primeiro, segundo, terceiro)
