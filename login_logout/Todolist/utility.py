def setPerm_string(perm, app, model):
    return f"{app}.{perm}_{model}"


def getPermission(user, app, model):
    perm = {
        "add": user.has_perm(setPerm_string("add", app, model)),
        "change": user.has_perm(setPerm_string("change", app, model)),
        "delete": user.has_perm(setPerm_string("delete", app, model)),
        "view": user.has_perm(setPerm_string("view", app, model)),
    }

    return perm
