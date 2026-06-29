def dens(data, pref_name):
    if pref_name == "全体":
        total_jinkou = 0
        total_menseki = 0
        for data_list in data.values():
            total_jinkou += data_list[1]
            total_menseki += data_list[2]
        return total_jinkou / total_menseki
    else:
        pref = data[pref_name]
        jinkou = pref[1]
        menseki = pref[2]
        return jinkou / menseki