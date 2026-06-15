from datetime import datetime
from datetime import timedelta


def ranking_general(connection):

    cursor = connection.cursor()

    sql = """
            SELECT
                user_id,
                SUM(time_sec) total_time_seconds,
                COUNT(*) total_sessions,
                COUNT(DISTINCT machine_id) total_machines

            FROM user_machine_times
            GROUP BY user_id
            ORDER BY total_time_seconds DESC
        """

    cursor.execute(sql)

    resultado = cursor.fetchall()

    insert_sql = """
        INSERT INTO ranking_general (

            user_id,
            position,
            total_time_seconds,
            total_sessions,
            total_machines,
            calculated_at

        )

        VALUES (

            %s,
            %s,
            %s,
            %s,
            %s,
            NOW()

        )

        ON DUPLICATE KEY UPDATE

        position=VALUES(position),
        total_time_seconds=VALUES(total_time_seconds),
        total_sessions=VALUES(total_sessions),
        total_machines=VALUES(total_machines),
        updated_at=NOW()
        """

    position = 1

    print("Ranking General:")
    for fila in resultado:

            print(f"Usuario {fila[0]} en posición {position}")

            cursor.execute(
                insert_sql,
                (
                    fila[0],
                    position,
                    fila[1],
                    fila[2],
                    fila[3]
                )
            )

            position += 1

    connection.commit()



def ranking_week(connection):

    cursor = connection.cursor()

    sql = """
            SELECT user_id, SUM(time_sec) total_time_seconds, COUNT(*) total_sessions, COUNT(DISTINCT machine_id) total_machines

            FROM user_machine_times
            WHERE created_at >= DATE_SUB(NOW(), INTERVAL 60 DAY)
            GROUP BY user_id
            ORDER BY total_time_seconds DESC
        """

    cursor.execute(sql)

    resultado = cursor.fetchall()

    insert_sql = """

        INSERT INTO ranking_week (

        user_id,
        position,

        week_start_date,
        week_end_date,

        year,
        week_number,

        total_time_seconds,
        total_sessions,
        total_machines,

        calculated_at

        )

        VALUES (

        %s,
        %s,

        %s,
        %s,

        %s,
        %s,

        %s,
        %s,
        %s,

        NOW()

        )

        ON DUPLICATE KEY UPDATE

        position=VALUES(position),

        total_time_seconds=
        VALUES(total_time_seconds),

        total_sessions=
        VALUES(total_sessions),

        total_machines=
        VALUES(total_machines),

        updated_at=NOW()

        """
    today = datetime.now()

    week_start = (
        today - timedelta(days=7)
    ).date()

    week_end = today.date()

    year = today.year

    week_number = (
        today.isocalendar()[1]
    )

    position = 1


    print("Ranking Semanal:")
    for fila in resultado:

        print(f"Usuario {fila[0]} en posición {position} para la semana {week_number}")

        cursor.execute(

                insert_sql, (
                    fila[0],
                    position,
                    week_start,
                    week_end,
                    year,
                    week_number,
                    fila[1],
                    fila[2],
                    fila[3]
                )

            )

        position += 1
        
    connection.commit()