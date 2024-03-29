import time

class TrafficLight:
    def __init__(self):
        self.states = [Red(), Green(), Yellow()]
        self.current_state = self.states[0]  # Initial state is Red

    def change_state(self):
        current_index = self.states.index(self.current_state)
        next_index = (current_index + 1) % len(self.states)
        self.current_state = self.states[next_index]

    def show_state(self):
        self.current_state.show()


class LightState:
    def show(self):
        pass


class Red(LightState):
    def show(self):
        print("Red Light")
        time.sleep(2)


class Green(LightState):
    def show(self):
        print("Green Light")
        time.sleep(1)


class Yellow(LightState):
    def show(self):
        print("Yellow Light")
        time.sleep(1)


def main():
    traffic_light = TrafficLight()

    while True:
        traffic_light.show_state()
        traffic_light.change_state()


if __name__ == "__main__":
    main()
