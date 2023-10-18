# Creating the lists
catholic_martys = [
    "Achileo Kiwanuka",
    "Adolphus Ludigo",
    "Mukasa",
    "Ambrosius",
    "Kibuuka",
    "Anatoli",
    "Kiriggwajjo",
    "Andrew Kaggwa",
    "Antanansio",
    "Bazzekuketta",
    "Bruno",
    "Sserunkuuma",
    "Charles Lwanga",
    "Denis",
    "Ssebuggwawo",
    "Wasswa",
    "Gonzaga Gon",
    "Gyavira Musoke",
    "Yowana Mukiibi",
    "Yusufu Lugalama",
    "Zakayo Lubega",
    "  James ",
    "Buuzaabalyaawo",
    "John Maria ",
    "Muzeeyi",
    "Joseph Mukasa",
    "Kizito",
    "Lukka",
    "Baanabakintu",
    "Matiya Mulumba",
    "Mbaga Tuzinde",
    "Mugagga Lubowa",
    "Mukasa",
    "Kiriwawanvu",
    "Nowa Mawaggali",
    "Ponsiano ",
    "Ngondwe",
]

Anglican_martys = [
    "Aaron Lubega",
    "Apollo Kivebulaya",
    "Eria Sebukyala",
    "Fredrick Kizza",
    "George Kizza",
    "James Hannington",
    "Janani Luwum",
    "Joseph ",
    "Balikuddembe",
    "Kizito",
    "Mark Kakumba",
    "Matia Mulumba",
    "Nuhu Mbegu",
    "Robert ",
    "Munyagayirwa",
    "Samwiri Mukasa",
    "Yefusa Namayanja",
    "Yohana Mukasa",
    "Yosefu Lugalama",
    "Yowana Kitaka",
    "Yowana Maria ",
    "Mukasa",
]

# Removing repeated names in both lists
New_catholic_martys = set(catholic_martys)
New_Anglican_Martys = set(Anglican_martys)

# Printing the new lists with no repeated values
print(New_catholic_martys)
print(New_Anglican_Martys)