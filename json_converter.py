import json
import numpy as np


class JsonData:
    def __init__(self, file_path):
        self.file_path = file_path
        with open(self.file_path) as json_file:
            data = json.load(json_file)
            cost_map = np.array(data['cost'])
            mesh_grid = np.array([data['mesh_grid'][0], data['mesh_grid'][1]])
            path = []
            for i in range(0, len(data['t'])):
                point = [data['path']['waypoints'][i][0], data['path']['waypoints'][i][1],
                         data['t'][i], data['path']['heading'][i], data['path']['throttle'][i], \
                         data['path']['speed'][i]]
                path.append(point)

            self.cost_map = cost_map
            self.mesh_grid = mesh_grid
            self.data = data
            self.path = path
            self.time = [t for (x, y, t, psi, throttle, speed) in path]
            self.waypoints = [[x, y] for (x, y, t, psi, throttle, speed) in path]
            self.heading = [psi for (x, y, t, psi, throttle, speed) in path]
            self.throttle = [throttle for (x, y, t, psi, throttle, speed) in path]
            self.speed = [speed for (x, y, t, psi, throttle, speed) in path]
            self.t_step = data['t'][1] - data['t'][0]

    def get_path_information(self):
        return self.waypoints, self.heading, self.throttle, self.speed, self.t_step, self.path

    def get_carla_agent_info(self, new_t_step):
        t_array = np.arange(self.time[0], self.time[-1], new_t_step)
        speed_interp = list(np.interp(t_array, self.time, self.speed))
        heading_interp = list(np.interp(t_array, self.time, self.heading))
        with open('./car_info/car_0.txt', 'w') as data_file:
            for t in t_array[0:-1]:
                data_file.write(str(round(t, 3)) + ',')
            data_file.write(str(round(t_array[-1], 3)) + '\n')
            for speed in speed_interp[0:-1]:
                data_file.write(str(speed) + ',')
            data_file.write(str(speed) + '\n')
            for heading in heading_interp[0:-1]:
                data_file.write(str((180 / np.pi) * heading) + ',')
            data_file.write(str((180 / np.pi) * heading))

        return None


def main():
    pass


if __name__ == '__main__':
    main()
