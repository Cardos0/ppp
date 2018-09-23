f = open ('ppp.txt', 'r')
received = f.read()

char_iniciofim = hex(0x7e)
char_scape = hex(0x7d)
ant = hex(0x00)
ant2 = hex(0x00)
data = False
code = False
ident = False
lenght = 0

for c in received:
    c_hex = hex(ord(c))
    string_print = str(c_hex)

    if c_hex == char_iniciofim and ant == char_iniciofim:
        string_print = '\n-------------------\n--------------------\n' + string_print
    if c_hex == char_iniciofim and ant != char_scape:
        string_print +='-> Inicio/Fim'
    elif c_hex == hex(0xff) and ant == char_iniciofim:
        string_print += '-> Endereco'
    elif c_hex == char_scape:
        string_print += '-> Escape'
    elif ant == hex(0x7d):
        c_oct = hex(int(c_hex,0) - 0x20)
        if (c_oct == hex(0x03)):
            string_print += '-> Controle'
        elif data:
            if code:
                string_print += '-> Codigo da mensagem (' + c_oct + ')'
                code = False
            elif ident:
                string_print += '-> Sequencia das mensagens (' + c_oct + ')'
                ident = False
            elif lenght == 1:
                string_print += '-> Tamanho das mensagem parte 1 (' + c_oct + ')'
                lenght += 1
            elif lenght == 2:
                string_print += '-> Tamanho das mensagem parte 2(' + c_oct + ') total: ' + hex(int(ant2,0) - 0x20) + ' ' + c_oct
                lenght = 0
            else:
                data = False
        else:
            string_print += '-> ' + c_oct
    elif ant == hex(0x23):
        string_print += '-> protocol part 1'
    elif ant2 == hex(0x23):
        protocol = ant + c_hex
        string_print += '-> Protocol: '
        if protocol == '0xc0' + '0x21':
            string_print += ' LCP - Link Control Protocol'
        elif protocol == '0xc0' + '0x23':
            string_print += ' PAP - Password-Authentication-Protocol'
        elif protocol == '0xc0' + '0x25':
            string_print += ' LQR - Link Quality Report'
        elif protocol == '0xc2' + '0x23':
            string_print += ' CHAP - Challenge Handshake Authentication Protocol'
        elif protocol == '0x80' + '0x21':
            string_print += ' IPCP - IP Control Protocol'
        elif protocol == '0x80' + '0xfd':
            string_print += ' CCP - Compression Control Protocol'
        elif protocol == '0x08' + '0x00':
            string_print += ' Dados IP'
        string_print += '\n----------------------\nDATA:'
        data = True
        code = True
        ident = True
        lenght = 1
    print string_print
    ant2 = ant
    ant = c_hex
    
quit()