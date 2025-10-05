import asyncio
import requests
import analysis.data_parser as data_parser
import netsuite_connection.connection as netsuite_connection
from src.analysis.data_parser import time_series_forcasting, time_series_forcasting_with_year_filtering

if __name__ == "__main__":
    print(time_series_forcasting("csv/train_inventory(in).csv"))
    print(time_series_forcasting_with_year_filtering("csv/train_inventory(in).csv", 5))
    # csv = data_parser.parse_csv("csv/train_inflows(in).csv")
    # print(data_parser.get_columns(csv))
    # print(data_parser.example_perform_regress®ion("csv/train_inflows(in).csv"))
    # csv2 = data_parser.parse_csv("csv/train_inventory(in).csv")
    # print(data_parser.get_columns(csv2))
    # csv3 = data_parser.parse_csv("csv/train_outflows(in).csv")
    # print(data_parser.get_columns(csv3))
    # asyncio.run(netsuite_connection.async_restlet_get("customsearch5402"))
    # asyncio.run(netsuite_connection.get_customer(4432102))

# 0.08174636491489448