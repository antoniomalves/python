"""
    Determine se um ano é bissexto.
"""
ano = 2000
if (ano % 400==0) or (ano % 4==0 and ano % 100!=0) :
    print("Ano bissexto")
else:
    print("Não é bissexto")
