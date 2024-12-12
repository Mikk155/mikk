import mikk

lista = [
    "index 0",
    "index 1",
    "index 2",
];

str1 = mikk.fmt.listdict( lista );
print(str1)

str1 = mikk.fmt.listdict( lista, True );
print(str1)

str1 = mikk.fmt.listdict( lista, value_int=True );
print(str1)
