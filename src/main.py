from dotenv import load_dotenv
import os
import asyncio
import requests
from netsuite import NetSuite, Config, TokenAuth
import analysis.data_parser as data_parser

load_dotenv()

config = Config(
    account=os.getenv("NETSUITE_ACCOUNT"),
    auth=TokenAuth(
        consumer_key=os.getenv("NETSUITE_CONSUMER_KEY"),
        consumer_secret=os.getenv("NETSUITE_CONSUMER_SECRET"),
        token_id=os.getenv("NETSUITE_TOKEN"),
        token_secret=os.getenv("NETSUITE_TOKEN_SECRET"),
    )
)
ns = NetSuite(config)

async def async_main():
    # rest_api_results = await ns.rest_api.get("/record/v1/customer", params={"limit": 1})
    # print(rest_api_results)
    #
    # restlet_results = await ns.restlet.get(2130, deploy=1)
    restlet_results = await ns.restlet.post(2130, deploy=1, data={"internalId": 280375})
    print(restlet_results)


if __name__ == "__main__":
    csv = data_parser.parse_csv("csv/train_inflows(in).csv")
    print(csv.head())
    print(data_parser.get_columns(csv))
    # data_parser.preprocess_data(csv, "csv/processed_train_inflows(in).csv")
    # asyncio.run(async_main())


