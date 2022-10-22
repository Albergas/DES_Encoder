
###################################################
# Práctica 4 - Tarea 3 - Alejandro Bergasa Alonso #
###################################################

# Método que recibe K y devuelve K_{offset}
def cycleKey(key, offset):
    skey = list(key)
    l = [skey[(i+offset)%(len(key)-1)] for i in range(len(key)-1)]
    key2 = ''
    for i in range(len(l)):
      key2 += l[i]
    return key2

# Método que calcula S1(T), con T un dato de 4 bits
def S1(T):
  S1dict = {'0000': '101',
            '0001': '011',
            '0010': '100',
            '0011': '000',
            '0100': '111',
            '0101': '001',
            '0110': '110',
            '0111': '010',
            '1000': '011',
            '1001': '101',
            '1010': '000',
            '1011': '010',
            '1100': '001',
            '1101': '100',
            '1110': '111',
            '1111': '110'}
  return S1dict[T]

# Método que calcula S2(T), con T un dato de 4 bits
def S2(T):
  S2dict = {'0000': '100',
            '0001': '000',
            '0010': '110',
            '0011': '111',
            '0100': '101',
            '0101': '001',
            '0110': '010',
            '0111': '011',
            '1000': '111',
            '1001': '100',
            '1010': '101',
            '1011': '110',
            '1100': '011',
            '1101': '001',
            '1110': '010',
            '1111': '000'}
  return S2dict[T]

# Método que calcula La función F(R,K), donde R es un dato de 6 bits y K una clave de 8
def F(R,K):
  ER = R[0] + R[1] + R[3] + R[2] + R[3] + R[2] + R[4] + R[5]
  T = (bin(int(ER,2) ^ int(K,2)))[2:]
  while len(T) < 8:
    T = '0' + T
  T1 = T[0:4]
  T2 = T[4:]
  return (S1(T1) + S2(T2))

# Método que devuelve el resultado de la i-ésima iteración, para data de 12 bits y key de 9 bits
def iteration(data, key, i):
  L = int(data[0:6],2)
  R = data[6:]
  L2 = R
  R2 = bin(L ^ int(F(R,cycleKey(key,i)),2))[2:]
  while len(L2) < 6:
    L2 = '0' + L2
  while len(R2) < 6:
    R2 = '0' + R2
  return L2+R2

# Método main del programa
def __main__():
    print('')
    print(' ----- Welcome to Alejandro Bergasa\'s DES ENCODER -----')
    print('   - You MUST enter data and key in binary, i.e. 100100 (with no preceding 0b and no blank spaces)')
    print('   - All data MUST have the specified length')
    print('   - Number of iterations must be an integer (given in decimal)')
    b = True
    opt = ''
    while b:
        print(' ---------------------------------------------------------------')
        data = input('  Enter 12 bits data to encode: ')
        key = input('  Enter 9 bits key: ')
        n = int(input('  Enter number of iterations: '))
        
        for i in range(n):
            data = iteration(data,key,i)
        
        print('')
        print(f'     - RESULT: {data}')
        print('')
        while opt not in ('y','Y','n','N'):
            opt = input('  Encode again? [y/n]: ')
        if opt in ('n','N'):
            b = False
    print('')
    print(' ----- Closed --------------------------------------------------')
    print('')
        
# Llamada al método main
__main__()