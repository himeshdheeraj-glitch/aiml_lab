from sympy import symbols,Not,Implies,Xor,satisfiable

Rain = symbols('Rain')
Harry_Visited_Hagrid = symbols('Harry_Visited_Hagrid')
Harry_Visited_Dumbledore = symbols('Harry_Visited_Dumbledore')

def run_test(test_name, kb):
    print("\n"+"="*50)
    print(test_name)
    print("="*50)
    result = satisfiable(kb)
    print("Satisfiable: "+str(result))
    if result is False:
        print("No satisfiable model(Contradiction)")
    elif Rain in result:
        if result[Rain]:
            print("It rained today")
        else:
            print("There is no rain today")
    else:
        print("Rain cannot be determined")

kb1 = (
    Implies(Not(Rain),Harry_Visited_Hagrid)
    &Xor(Harry_Visited_Hagrid, Harry_Visited_Dumbledore)
    &Harry_Visited_Dumbledore
)
run_test("Test Case 1 :", kb1)

kb2 = (
    Implies(Not(Rain),Harry_Visited_Hagrid)
    &Xor(Harry_Visited_Hagrid, Harry_Visited_Dumbledore)
    &Harry_Visited_Hagrid & Not(Rain)
)
run_test("Test Case 2 :", kb2)

kb3 = (
    Implies(Not(Rain),Harry_Visited_Hagrid)
    &Xor(Harry_Visited_Hagrid, Harry_Visited_Dumbledore)
    &Harry_Visited_Dumbledore & Rain
)
run_test("Test Case 3 :", kb3)

kb4 = (
    Implies(Not(Rain),Harry_Visited_Hagrid)
    &Xor(Harry_Visited_Hagrid, Harry_Visited_Dumbledore)
    &Harry_Visited_Hagrid & Harry_Visited_Dumbledore
)
run_test("Test Case 4 :", kb4)

kb5 = (
    Implies(Not(Rain),Harry_Visited_Hagrid)
)
run_test("Test Case 5 :", kb5)

