import user_management

admin_db = user_management.database_admin()
admin_cursor = admin_db.cursor()


def add_row(cursor, tablename, rowdict):
    # XXX tablename not sanitized
    # XXX test for allowed keys is case-sensitive

    # filter out keys that are not column names
    cursor.execute("describe %s" % tablename)
    allowed_keys = set(row[0] for row in cursor.fetchall())
    keys = allowed_keys.intersection(rowdict)

    # if len(rowdict) > len(keys):
    #     unknown_keys = set(rowdict) - allowed_keys
    #     print >> sys.stderr, "skipping keys:", ", ".join(unknown_keys)

    columns = ", ".join(keys)
    values_template = ", ".join(["%s"] * len(keys))

    sql = "insert into %s (%s) values (%s)" % (
        tablename, columns, values_template)
    values = tuple(rowdict[key] for key in keys)
    cursor.execute(sql, values)


def register_user(name_in, email_in, phone_in, passwd_in, role_in):
    if role_in == "Doctor":
        role = 'd'
    elif role_in == "Nurse":
        role = 'n'
    elif role_in == "Patient":
        role = 'p'
    elif role_in == "Pharmacist":
        role = 'ph'
    elif role_in == "Accountant":
        role = 'a'
    elif role_in == "Reception":
        role = 'r'
    elif role_in == "Laboratory":
        role = 'l'

    instance_insert = {
        # sql column    variable value
        'role': role,
        'email': email_in,
        'phone': phone_in,
        'username': name_in,
        'password': passwd_in,
    }
    add_row(admin_cursor, "Registrations", instance_insert)
    admin_db.commit()
    return instance_insert["email"]