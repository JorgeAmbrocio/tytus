reglasOpt = []
codOpt = ''
def optimizar(pOpt):
    global codOpt
    listaOp = pOpt
    size = len(listaOp)
    for indice in range(size):
        valor = listaOp[indice]
        if "=" in valor:
            if "+" in valor:
                suma = valor.split('+')
                if str(suma[1]).strip() == '0':
                    operador = suma[0].split('=')
                    if str(operador[0]).strip() == str(operador[1]).strip():
                        reglasOpt.append("Regla 8:" + str(valor) +'. Se elimina.')
                    else:
                        val = str(suma[0]) + '\n'
                        reglasOpt.append ( "Regla 12:" + str ( valor ) +'. Se optimiza por: ' + val)
                        codOpt += val
                else:
                    codOpt += valor + '\n'
            elif "-" in valor:
                resta = valor.split("-")
                if str(resta[1]).strip() == '0':
                    operador = resta[0].split('=')
                    if str(operador[0]).strip() == str(operador[1]).strip():
                        reglasOpt.append("Regla 9:" + str(valor) + '. Se elimina.')
                    else:
                        val = str(resta[0]) + ';\n'
                        reglasOpt.append ( "Regla 13:" + str ( valor ) + '. Se optimiza por: ' + str(val).strip() )
                        codOpt += val
                else:
                    codOpt += valor + '\n'
            elif "/" in valor:
                div = valor.split("/")
                if str(div[1]).strip() == '1':
                    operador = div[0].split('=')
                    if str(operador[0]).strip() == str(operador[1]).strip():
                        reglasOpt.append("Regla 11:" + str(valor) + '. Se elimina.')
                    else:
                        val = str(div[0]) + '\n'
                        reglasOpt.append ( "Regla 15:" + str ( valor ) + '. Se optimiza por: ' + str(val).strip() )
                        codOpt += val
                else:
                    operador = div[0].split('=')
                    if str(operador[1]).strip() == '0':
                        val = str(div[0]) + '\n'
                        reglasOpt.append( "Regla 18:" + str(valor) + '. Se optimiza por: ' + str(val).strip())
                        codOpt += val
                    else:
                        codOpt += valor + '\n'
            elif "*" in valor:
                mult = valor.split("*")
                if str(mult[1]).strip() == '1':
                    operador = mult[0].split('=')
                    if str(operador[0]).strip() == str(operador[1]).strip():
                        reglasOpt.append("Regla 10:" + str(valor) + '. Se elimina.')
                    else:
                        val = str(mult[0]) + '\n'
                        reglasOpt.append ( "Regla 14:" + str ( valor ) + '. Se optimiza por: ' + str(val).strip() )
                        codOpt += val
                elif str(mult[1]).strip() == '2':
                    opt = mult[0].split('=')
                    val = str(opt[0]) + ' = ' + str(opt[1]) + '+' + str(opt[1])
                    reglasOpt.append("Regla 16:" + valor +'. Se optimiza por: ' + str(val).strip())
                elif str(mult[1]).strip() == '0':
                    operador = mult[0].split('=')
                    val =  str(operador[0]).strip() + ' = 0'
                    reglasOpt.append("Regla 17:" + valor + '.Se optimiza por: '+str(val).strip())
                    codOpt += val
                else:
                    codOpt += valor + '\n'
            elif 'if' in valor:
                print('valor')
            else:
                codOpt += valor +'\n'
        else:
            if 'if' in valor:
                print(valor)
            codOpt += valor + '\n'

def retornoOpt():
    return codOpt
