# Motion Tracking using Odometry

Code to read phone's accelerometer data from a spreadsheet and visualize its motion.
Accelerometer data was obtained from the phone in spreadsheet format using the Phyphox app. The python code imports this data and calculates the position of the phone based on it.

## Running the code
Install the necessary python libraries:

* Pandas:
  ```sh
  pip install pandas
  ```
* NumPy:
  ```sh
  pip install numpy
  ```
* Matplotlib:
  ```sh
  pip install matplotlib
  ```
* vPython:
  ```sh
  pip install vpython
  ```
Run the 'position.py' file using
```sh
py position.py
```
or
```sh
python3 position.py
```

## Output
Running the code provides a visualization of the phone's motion and plots a graph of the x, y, and z coordinates w.r.t time.
