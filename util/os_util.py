import os
from constants import file_path_constants as fpc


def create_directory(path):
    try:
        os.mkdir(path)
        return True
    except Exception as e:
        print("Error: ", e)
        return False


def create_company_directory(company_name):
    path = fpc.STOCK_COMPANY_FOLDER.replace("###FOLDER_NAME###", company_name)
    create_directory(path)


def create_pattern_directory(company_name, pattern_name):
    path = fpc.STOCK_PATTERN_FOLDER.replace("###FOLDER_NAME###", company_name)\
                                   .replace("###PATTERN_NAME###", pattern_name)

    create_directory(path)


def get_profit_loss_json_path(company_name, pattern_name):
    return fpc.PROFIT_LOSS_JSON.replace("###FOLDER_NAME###", company_name)\
                               .replace("###PATTERN_NAME###", pattern_name)


def get_profit_loss_csv_path(company_name, pattern_name):
    return fpc.PROFIT_LOSS_CSV.replace("###FOLDER_NAME###", company_name)\
                              .replace("###PATTERN_NAME###", pattern_name)
