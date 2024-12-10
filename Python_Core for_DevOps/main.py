class SlowResponse(Exception):
    def __init__(self, name: str, response: int) -> None:
        self.name = name
        self.response = response

        if 51 <= self.response <= 75:
            super().__init__(f"Warning! {self.name} has a slow response of {self.response} ms.")


class ExtraSlowResponse(SlowResponse):
    def __init__(self, name: str, response: int) -> None:
        self.name = name
        self.response = response

        if 76 <= response <= 100:
            raise ValueError(f"Alarm! {self.name} has a very slow response of {self.response} ms.")


class DangerouslySlowResponse(ExtraSlowResponse):
    def __init__(self, name: str, response: int) -> None:
        self.name = name
        self.response = response

        if response > 100:
            raise ValueError(
                f"Nuclear power station is under the danger! {self.name} has a dangerously slow response of {self.response} ms."
            )


def check_device_response(device: dict):
    name = device["name"]
    response = device["response"]
    if 51 <= response <= 75:
        raise SlowResponse(name, response)
    elif 76 <= response <= 100:
        raise ExtraSlowResponse(name, response)
    elif response > 100:
        raise DangerouslySlowResponse(name, response)


def check_station_devices(devices: list):
    for device in devices:
        check_device_response(device)


check_station_devices([
    {"name": "Polar crane", "response": 52},
    {"name": "Reactor shaft", "response": 81},
    {"name": "Pressure compensator", "response": 149},
    {"name": "Steam generator", "response": 40},
])
# Warning! Polar crane has a slow response of 52 ms. Take attention!
# Alarm! Reactor shaft has a very slow response of 81 ms. Needs to be repaired!
# Nuclear power station is under the danger! Pressure compensator has a dangerously slow response of 149 ms. We have a serious troubles!
# -----------------------------------------------------------------------

# ------------------------------------------------------------------
# class SlowResponse(Exception):
#     def __init__(self, name: str, response: int) -> None:
#         self.name = name
#         self.response = response
#
#     def __str__(self):
#         if 51 <= self.response <= 75:
#             return f"Warning! {self.name} has a slow response of {self.response} ms."
#
#
# class ExtraSlowResponse(SlowResponse):
#     def __init__(self, name: str, response: int) -> None:
#         self.name = name
#         self.response = response
#
#     def __str__(self):
#         if 76 <= self.response <= 100:
#             return f"Alarm! {self.name} has a very slow response of {self.response} ms."
#
#
# class DangerouslySlowResponse(ExtraSlowResponse):
#     def __init__(self, name: str, response: int) -> None:
#         self.name = name
#         self.response = response
#
#     def __str__(self):
#         if self.response > 100:
#             return f"Nuclear power station is under the danger! {self.name} has a dangerously slow response of {self.response} ms."


# def check_device_response(device: dict):
#     try:
