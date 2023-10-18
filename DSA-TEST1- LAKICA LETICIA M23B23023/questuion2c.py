def is_uganda_martyr(name):
    # Define the lists of Catholic and Anglican martyrs
    catholic_martyrs = [
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
        "James",
        "Buuzaabalyaawo",
        "John Maria",
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
        "Ponsiano",
        "Ngondwe",
    ]

    anglican_martyrs = [
        "Aaron Lubega",
        "Apollo Kivebulaya",
        "Eria Sebukyala",
        "Fredrick Kizza",
        "George Kizza",
        "James Hannington",
        "Janani Luwum",
        "Joseph Balikuddembe",
        "Kizito",
        "Mark Kakumba",
        "Matia Mulumba",
        "Nuhu Mbegu",
        "Robert Munyagayirwa",
        "Samwiri Mukasa",
        "Yefusa Namayanja",
        "Yohana Mukasa",
        "Yosefu Lugalama",
        "Yowana Kitaka",
        "Yowana Maria Mukasa",
    ]

    # Check if the name is in both lists
    return name in catholic_martyrs and name in anglican_martyrs


# Allowing the user to input the martys name they desire
input_name = input("Please input any name in the list above: ")
result = is_uganda_martyr(input_name)

if result:
    print(f"{input_name} is a Uganda Martyr in both lists.")
else:
    print(f"{input_name} is not a Uganda Martyr in both lists.")
