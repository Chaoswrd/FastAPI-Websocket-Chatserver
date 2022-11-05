from . import main_test
from fastapi import status

def test_get_devices():
    response = main_test.client.get("/devices?skip=0&limit=1")
    assert response.status_code == status.HTTP_200_OK 
    assert response.json() == [
        {
            "id": 0,
            "time": 1451624458,
            "energy_consumption_kw": 0.003417,
            "temperature": 35.87,
            "icon": "partly-cloudy-night",
            "humidity": 0.61,
            "visibility": 10.0,
            "summary": "Mostly Cloudy",
            "apparent_temperature": 29.4,
            "pressure": 1016.25,
            "wind_speed": 8.29,
            "cloud_cover": 1,
            "wind_bearing": 285,
            "precip_intensity": 0.0,
            "dew_point": 23.9,
            "precip_probability": 0.0
        }] 

def test_get_devices_negative_skip():
    response = main_test.client.get("/devices?skip=-1&limit=1")
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.json() == {"detail": "skip must be non-negative"}


def test_get_devices_zero_limit():
    response = main_test.client.get("/devices?skip=0&limit=0")
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.json() == {"detail": "limit must be larger than zero"}

def test_get_device():
    response = main_test.client.get("/devices/0")
    assert response.status_code == status.HTTP_200_OK 
    assert response.json() == {
            "id": 0,
            "time": 1451624458,
            "energy_consumption_kw": 0.003417,
            "temperature": 35.87,
            "icon": "partly-cloudy-night",
            "humidity": 0.61,
            "visibility": 10.0,
            "summary": "Mostly Cloudy",
            "apparent_temperature": 29.4,
            "pressure": 1016.25,
            "wind_speed": 8.29,
            "cloud_cover": 1,
            "wind_bearing": 285,
            "precip_intensity": 0.0,
            "dew_point": 23.9,
            "precip_probability": 0.0
        }  

def test_create_device():
    response = main_test.client.post(
        "/devices/",
        headers={},
        json={
            "id": 0,
            "time": 1451624458,
            "energy_consumption_kw": 0.003417,
            "temperature": 35.87,
            "icon": "partly-cloudy-night",
            "humidity": 0.61,
            "visibility": 10.0,
            "summary": "Mostly Cloudy",
            "apparent_temperature": 29.4,
            "pressure": 1016.25,
            "wind_speed": 8.29,
            "cloud_cover": 1,
            "wind_bearing": 285,
            "precip_intensity": 0.0,
            "dew_point": 23.9,
            "precip_probability": 0.0
        }
    )
    assert response.status_code == status.HTTP_201_CREATED 
    assert response.json() == {
            "id": 0,
            "time": 1451624458,
            "energy_consumption_kw": 0.003417,
            "temperature": 35.87,
            "icon": "partly-cloudy-night",
            "humidity": 0.61,
            "visibility": 10.0,
            "summary": "Mostly Cloudy",
            "apparent_temperature": 29.4,
            "pressure": 1016.25,
            "wind_speed": 8.29,
            "cloud_cover": 1,
            "wind_bearing": 285,
            "precip_intensity": 0.0,
            "dew_point": 23.9,
            "precip_probability": 0.0
        }  

def test_create_device_missing_fields():
    response = main_test.client.post(
        "/devices/",
        json={}
    )
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY 
    assert response.json() == {
    "detail": [
        {
            "loc": [
                "body",
                "id"
            ],
            "msg": "field required",
            "type": "value_error.missing"
        },
        {
            "loc": [
                "body",
                "time"
            ],
            "msg": "field required",
            "type": "value_error.missing"
        },
        {
            "loc": [
                "body",
                "energy_consumption_kw"
            ],
            "msg": "field required",
            "type": "value_error.missing"
        },
        {
            "loc": [
                "body",
                "temperature"
            ],
            "msg": "field required",
            "type": "value_error.missing"
        },
        {
            "loc": [
                "body",
                "icon"
            ],
            "msg": "field required",
            "type": "value_error.missing"
        },
        {
            "loc": [
                "body",
                "humidity"
            ],
            "msg": "field required",
            "type": "value_error.missing"
        },
        {
            "loc": [
                "body",
                "visibility"
            ],
            "msg": "field required",
            "type": "value_error.missing"
        },
        {
            "loc": [
                "body",
                "summary"
            ],
            "msg": "field required",
            "type": "value_error.missing"
        },
        {
            "loc": [
                "body",
                "apparent_temperature"
            ],
            "msg": "field required",
            "type": "value_error.missing"
        },
        {
            "loc": [
                "body",
                "pressure"
            ],
            "msg": "field required",
            "type": "value_error.missing"
        },
        {
            "loc": [
                "body",
                "wind_speed"
            ],
            "msg": "field required",
            "type": "value_error.missing"
        },
        {
            "loc": [
                "body",
                "cloud_cover"
            ],
            "msg": "field required",
            "type": "value_error.missing"
        },
        {
            "loc": [
                "body",
                "wind_bearing"
            ],
            "msg": "field required",
            "type": "value_error.missing"
        },
        {
            "loc": [
                "body",
                "precip_intensity"
            ],
            "msg": "field required",
            "type": "value_error.missing"
        },
        {
            "loc": [
                "body",
                "dew_point"
            ],
            "msg": "field required",
            "type": "value_error.missing"
        },
        {
            "loc": [
                "body",
                "precip_probability"
            ],
            "msg": "field required",
            "type": "value_error.missing"
        }
    ]
}
