obj = connect_gpib(8, 8);

data1 = query(obj, 'WAV 1560');
data2 = query(obj, 'ATT:DB 5');

%com = serialport("COM3", 9600, "Timeout", 0.001);



