#########################################################################
# This program is free software: you can redistribute it and/or modify  #
# it under the terms of the GNU General Public License as published by  #
# the Free Software Foundation, either version 3 of the License, or     #
# (at your option) any later version.                                   #
#                                                                       #
# This program is distributed in the hope that it will be useful,       #
# but WITHOUT ANY WARRANTY; without even the implied warranty of        #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         #
# GNU General Public License for more details.                          #
#                                                                       #
# You should have received a copy of the GNU General Public License     #
# along with this program.  If not, see <https://www.gnu.org/licenses/> #
#                                                                       #
#                       Joel Grigolo - https://matehacker.org - 06/2020 #
#########################################################################

def por_extenso(n):

    unidades = ["zero", "um", "dois", "três", "quatro",
                "cinco", "seis", "sete", "oito", "nove"]
    dez = ["dez", "onze", "doze", "treze", "quatorze",
           "quinze", "dezesseis", "dezessete", "dezoito", "dezenove"]
    dezenas = ["vinte", "trinta", "quarenta", "cinquenta",
               "sessenta", "setenta", "oitenta", "noventa"]
    centenas = ["cento", "duzentos", "trezentos", "quatrocentos",
                "quinhentos", "seiscentos", "setecentos", "oitocentos", "novecentos"]

    if n <= 9:
        return unidades[n]

    elif n >= 10 and n <= 19:
        return dez[n-10]

    elif n >= 20 and n <= 99:
        return dezenas[(n//10)-2] + (" e " + unidades[n % 10] if n % 10 != 0 else "")

    elif n >= 100 and n <= 999:
        return centenas[(n//100-1)] + (" e " + por_extenso(n % 100) if n % 100 != 0 else "")

    elif n >= 1000 and n <= 9999:
        return unidades[(n//1000)] + " mil" + (" e " + por_extenso(n % 1000) if n % 1000 !=0 else "")
    
    elif n >= 10000 and n <= 19999:
        return dez[(n-10000)//1000] + " mil"  + (" e " + por_extenso(n % 1000) if n % 1000 !=0 else "")

    elif n >= 20000 and n <= 99999:
        return dezenas[(n-20000)//10000] +  (" e " + por_extenso(n % 10000) if n % 10000 !=0 else " mil")  
    
    elif n >= 100000 and n <= 999999:
        return centenas[(n-100000)//100000] + (" e " + por_extenso(n % 100000) if n % 100000 !=0 else " mil")
    
    elif n >= 1000000 and n <= 1999999:
        return unidades[(n//1000000)] + " milhão" + (" e " + por_extenso(n % 1000000) if n % 100000 !=0 else "")
    
    elif n >= 2000000 and n <= 9999999:
        return unidades[(n//1000000)] + " milhões" + (" e " + por_extenso(n % 1000000) if n % 100000 !=0 else "")
    
    elif n >= 10000000 and n <= 19999999:
        return(dez[(n-10000000)//1000000]) + " milhões"+ (" e " + por_extenso(n % 1000000) if n % 100000 !=0 else "")
    
    elif n >= 20000000 and n <= 99999999:
        return(dezenas[(n-20000000)//10000000]) + (" e " + por_extenso(n % 10000000) if n % 100000 !=0 else " milhões")
    
    elif n >= 100000000 and n <= 999999999:
        return(centenas[(n-100000000)//100000000]) + (" e " + por_extenso(n % 100000000) if n % 1000000 !=0 else " milhões")



num = input("Digite um número de 0 a 999999999: ")
print(por_extenso(int(num)))
