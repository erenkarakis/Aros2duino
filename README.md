# Aros2duino
You can communicate between ROS2 and serial device with this project. **(Now only for read data from serial device.)**

## How to download?
Go inside where you want download the repo. (Like `aros2duino_ws`)
1. Clone the repository to your device.
  ```sh-session  
  git clone https://github.com/erenkarakis/Aros2duino.git
  ```
2. Build with colcon.
  ```sh-session
  colcon build --symlink-install
  ```
3. Source the `setup.bash` file.
  ```sh-session
  source install/setup.bash
  ```
You can add the `setup.bash` file to `.bashrc` file if you  dont want to source `setup.bash` file every time.
 ## How to use?
 #### Using `find_ports` for find correct port:
 * You need to find correct serial port to use the package. For make this easier I wrote that `find_ports.py`. You can use this easily like that:
    ```sh-session
    ros2 run aros2duino find_ports
    ```
    This will print avaliable port paths and names.
#### Using `serial_comm` for communicate with given serial port and publish data:
* To run this code you need to know correct port path and baud rate.
    ```sh-session
    ros2 run aros2duino serial_comm --ros-args -p serial_port:=<device_port> -p baud_rate:=<baud_rate>
    ```
    **Don't type </> characters**
---

### **I am still developing the code. Now package can only read serial datas. I am working on write serial datas to serial device.**
##### *Sorry for my bad English :D*
