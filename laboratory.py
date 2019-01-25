lab_id = None


def set_lab_id(id):
    global lab_id
    lab_id = id


def set_diagnose_report(report, test_id, cursor, db):
    sql = "update Test set DiagnoseReport = %s where increment = %s"
    cursor.execute(sql, (report, test_id))
    db.commit()
