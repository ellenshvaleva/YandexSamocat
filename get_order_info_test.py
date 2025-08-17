# Елена Швалева, 33-я когорта — Финальный проект. Инженер по тестированию плюс
import sender_stand_request

def test_get_order_info():
    track = sender_stand_request.post_create_order().json()["track"]
    orderResponse = sender_stand_request.get_order_by_track(track)
    assert orderResponse.status_code == 200