from quatro import log, sql_query, scalar_data, tabular_data, configuration as c


# Insert converted quote data into 'daily_orders_updated' table
def converted_order(change_type, ord_no):
    sql_exp = f'INSERT INTO daily_orders_updated ' \
              f'(change_type, ord_no) ' \
              f'VALUES (\'{change_type}\', {ord_no})'
    log(sql_exp)
    c.config.log_db_cursor.execute(sql_exp)


# Insert added part data into 'daily_orders_updated' table
def added_part(change_type, ord_no, orl_id):
    sql_exp = f'INSERT INTO daily_orders_updated ' \
              f'(change_type, ord_no, orl_id) ' \
              f'VALUES (\'{change_type}\', {ord_no}, {orl_id})'
    log(sql_exp)
    c.config.log_db_cursor.execute(sql_exp)


# Insert price changed data into 'daily_orders_updated' table
def price_changed(change_type, ord_no, orl_id, orl_price):
    sql_exp = f'INSERT INTO daily_orders_updated ' \
              f'(change_type, ord_no, orl_id, orl_price) ' \
              f'VALUES (\'{change_type}\', {ord_no}, {orl_id}, {orl_price})'
    log(sql_exp)
    c.config.log_db_cursor.execute(sql_exp)


# Insert removed part data into 'daily_orders_updated' table
def removed_part(change_type, ord_no, orl_id, orl_price, prt_no, orl_quantity, prt_dscnt):
    sql_exp = f'INSERT INTO daily_orders_updated ' \
              f'(change_type, ord_no, orl_id, orl_price, prt_no, orl_quantity, prt_dscnt) ' \
              f'VALUES (\'{change_type}\', {ord_no}, {orl_id}, {orl_price}, \'{prt_no}\', {orl_quantity}, {prt_dscnt})'
    log(sql_exp)
    c.config.log_db_cursor.execute(sql_exp)


def printed_packing_slip(change_type, ord_no):
    sql_exp = f'INSERT INTO daily_orders_updated ' \
              f'(change_type, ord_no) ' \
              f'VALUES (\'{change_type}\', {ord_no})'
    log(sql_exp)
    c.config.log_db_cursor.execute(sql_exp)


def get_order_creator(ord_no):
    sql_exp = f"SELECT user_name FROM order_header WHERE ord_no = {ord_no} AND tg_op = 'INSERT'"
    result_set = sql_query(sql_exp, c.config.log_db_cursor)
    creator = scalar_data(result_set)
    return creator


# TODO : Add a 'sent' boolean column to daily_orders log table instead of deleting sent orders
# Clear log of orders that are already sent, add orders to log that have just been sent
def exclusion_log():
    sql_exp = f'DELETE FROM daily_orders'
    c.config.log_db_cursor.execute(sql_exp)
    log('Cleared daily_orders table on log DB')

    grouping_view_list = ['', '_quotes', '_pending', '_updated', '_cancelled']

    for grouping in grouping_view_list:
        sql_exp = f'SELECT ord_no FROM daily_orders{grouping}'
        c.config.sigm_db_cursor.execute(sql_exp)
        result_set = c.config.sigm_db_cursor.fetchall()

        for row in result_set:
            for cell in row:
                ord_no = cell
                if grouping != '_cancelled':
                    sql_exp = f'INSERT INTO daily_orders (ord_no) VALUES ({ord_no})'
                    log(f'Added order {ord_no} to daily_orders table on log DB')
                else:
                    sql_exp = f'INSERT INTO daily_orders_cancelled (ord_no)' \
                              f'SELECT {ord_no} ' \
                              f'WHERE NOT EXISTS ( ' \
                              f'    SELECT ord_no ' \
                              f'    FROM daily_orders_cancelled ' \
                              f'    WHERE ord_no = {ord_no} ' \
                              f')'
                    log(f'Added order {ord_no} to daily_orders_cancelled table on log DB')
                c.config.log_db_cursor.execute(sql_exp)


# TODO : Add a 'sent' boolean column to daily_orders_updated log table instead of deleting sent updated orders
# Clear log of updated orders
def clear_updated():
    sql_exp = f'DELETE FROM daily_orders_updated'
    c.config.log_db_cursor.execute(sql_exp)
    log('Cleared daily_orders_updated table on log DB')


def ord_no_view(view):
    sql_exp = f'SELECT DISTINCT ord_no FROM {view}'
    result_set = sql_query(sql_exp, c.config.sigm_db_cursor)
    ord_nos = tabular_data(result_set)
    return ord_nos
