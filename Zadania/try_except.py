# def main():
#     x=get_in("jaki jest x?")
#     print(f"wawrtosc x to..{x}")
#
# # def get_in(prompt):
# #     while True:
# #         try:
# #             x=int(input(prompt))
# #         except ValueError:
# #             pass #print("zla wartosc")
# #         else:
# #             return (x) #break # return jest silniejszy niz break, bo wstrzymuje loop i do tego daje wartosc
#
# main()
# #get_in()

def dzielenie(x,y):
    assert y!=0, "zmienna równa zero" #służy jako zawór bezpieczeństwa, sprawdza czy y jest różny od zera, NIE (False) wywala błąd, TRue jedzie dalej
    if y==0:
        raise ZeroDivisionError("Dzielenie przez 0") #wywala czerwony bład z opisem
    print (x/y)
try:
    dzielenie(2,0)
except (ZeroDivisionError, ValueError,TypeError,NameError):
     print("Nie można dzielic przez zero lub nie jest zdefiniowana liczba")
     raise #przepchnelismy nasz wyjątek dalej jeśli mogło by coś go obsługiwać

