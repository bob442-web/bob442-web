username = 'Jesper'
pasword = '1234'

# while True:
#     print('brugernavn')
#     usernameInput=input()
#     if usernameInput == username:
#         while True:
#         print('adgangskode')
#         paswordInput=input()
#         if paswordInput == pasword:
#             print('adgang givet')
#             print('velkomen ind på siden igen Jesper')
#             break
#         else:
#             print('forkert adgangskode, prøv igen')
#             continue
#     else:
#         print('forkert brugernavn')
#         continue


while True:
    print('brugernavn:')
    usernameInput=input()
    if usernameInput == username:
        break

    else:
        print('forkert brugernavn')
        print('prøv igen')
        continue
        
while True:
    print('adgangskode:')
    paswordInput=input()
    if paswordInput == pasword:
        print('adgang givet')
        print('velkomen ind på siden igen Jesper')
        break
    else:
        print('forkert adgangskode, prøv igen')
        continue