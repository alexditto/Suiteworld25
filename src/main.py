import asyncio
import requests
import analysis.data_parser as data_parser
import netsuite_connection.connection as netsuite_connection


if __name__ == "__main__":
    csv = data_parser.parse_csv("csv/train_inflows(in).csv")
    print(data_parser.get_columns(csv))
    csv2 = data_parser.parse_csv("csv/train_inventory(in).csv")
    print(data_parser.get_columns(csv2))
    csv3 = data_parser.parse_csv("csv/train_outflows(in).csv")
    print(data_parser.get_columns(csv3))
    # data_parser.preprocess_data(csv, "csv/processed_train_inflows(in).csv")
    # asyncio.run(netsuite_connection.async_main())
    # asyncio.run(netsuite_connection.async_restlet_get("customsearch5402"))
    # asyncio.run(netsuite_connection.get_customer(4432102))

