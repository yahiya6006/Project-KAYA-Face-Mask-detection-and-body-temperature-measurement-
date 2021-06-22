# Project-KAYA

Current Output
---------------------------------------------------------------------
[
    {
        "data": {
            "id": 1,
            "time": "12:40:06 AM",
            "date": "13/06/2021",
            "temp": 34.927605
        },
        "message": null,
        "status": null
    },
    {
        "data": {
            "id": 2,
            "time": "12:41:07 AM",
            "date": "13/06/2021",
            "temp": 35.19441
        },
        "message": null,
        "status": null
    }
]


Expected output
--------------------------------------------------------------------------------------
[
    {
        "data": {
            "id": 1,
            "time": "12:40:06 AM",
            "date": "13/06/2021",
            "temp": 34.927605
        },
        "data": {
            "id": 2,
            "time": "12:41:07 AM",
            "date": "13/06/2021",
            "temp": 35.19441
        }
    },
    "message": "Success",
    "status": "true"
]
