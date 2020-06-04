#Author:Anliu

def file_db_handle(conn_parms):
    '''
    解析数据库文件路径
    :param conn_params:
    :return:
    '''
    #print('file db:', conn_parms)
    db_path = '%s/%s' % (conn_parms['path'], conn_parms['name'])
    return db_path

def db_handle(conn_parms):
    '''

    :param conn_parms:
    :return:
    '''
    if conn_parms['engine'] == 'file_storage':
        return file_db_handle(conn_parms)