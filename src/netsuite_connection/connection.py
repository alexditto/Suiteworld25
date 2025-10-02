import os
from dotenv import load_dotenv
from netsuite import NetSuite, Config, TokenAuth

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
    restlet_results = await ns.restlet.post(2130, deploy=1, data={"internalId": 280375})
    print(restlet_results)

async def async_restlet_get(search_id: str):
    restlet_results = await ns.restlet.get(2130, deploy=1, params={"search": search_id})
    print(restlet_results)

async def async_restlet_post(customer_ids: list):
    restlet_results = await ns.restlet.post(2130, deploy=1, data={"internal_ids": customer_ids})
    print(restlet_results)

async def get_customer(customer_id: int):
    customer = await ns.rest_api.get("/record/v1/customer/" + str(customer_id))

    print(customer)