import configuration
import data
import requests

def post_create_order():
    return requests.post(
        url=configuration.URL_SERVICE + configuration.CREATE_ORDER,
        json=data.create_order_body
    )

def get_order_by_track(track):
    return requests.get(
        url=configuration.URL_SERVICE + configuration.GET_ORDER_BY_TRACK,
        params={"t": track}
    )

