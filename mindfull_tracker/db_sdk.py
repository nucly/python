import sqlite3


def cursor():
    return sqlite3.connect("mindful.db").cursor()


c = cursor()
c.execute("CREATE TABLE IF NOT EXISTS meditations "
          "(m_type TEXT, m_date TEXT, m_time TEXT, comment TEXT)")
c.connection.close()


def add_meditation(meditation):
    c = cursor()
    with c.connection:
        c.execute("INSERT INTO meditations VALUES (?, ?, ?, ?)",
                  (meditation.m_type, meditation.date, meditation.time, meditation.comment))
    c.connection.close()


def get_meditation(id):
    c = cursor()
    with c.connection:
        c.execute("SELECT rowid, * FROM meditations WHERE rowid=?", (id,))
    meditation = c.fetchone()
    c.connection.close()

    if not meditation:
        return None

    return meditation


def get_meditations():
    c = cursor()
    meditations = []
    with c.connection:
        for meditation in c.execute("SELECT rowid, * FROM meditations"):
            meditations.append(meditation)
    c.connection.close()

    return meditations


def update_meditation(id, new_m_type, new_date, new_time, new_comment):
    c = cursor()
    with c.connection:
        c.execute("UPDATE meditations SET m_type=?, m_date=?, m_time=?, comment=? WHERE rowid=?",
                  (new_m_type, new_date, new_time, new_comment, id))


def delete_meditation(id):
    c = cursor()
    with c.connection:
        c.execute("DELETE FROM meditations WHERE rowid=?", (id,))


if __name__ == '__main__':
    print(get_meditations())
