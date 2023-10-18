def martyr_count(martyr_name):
    # Defining the lists of Catholic and Anglican martyrs
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

    if martyr_name in catholic_martyrs:
        return "Catholic"
    elif martyr_name in anglican_martyrs:
        return "Anglican"
    else:
        return "Unknown"


# Get the martyr's name from the user
user_input = input("Enter the martyr's name: ")
group = martyr_count(user_input)

if group == "Unknown":
    print(f"Sorry, {user_input} is not found in either group.")
else:
    print(f"{user_input} belongs to the {group} group.")