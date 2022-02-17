# Automatic Door for Face Mask detection.		  							
The application of AI specifically DeepLearning in IOT is no longer a strange thing. We can see its application every day such as (Face recognition on phones, Smart virtual assistants, Self-driving cars,.. ..)
In this project, we will present the idea and how to apply Deep Learning in the problem of identifying people wearing a mask, thereby helping to intelligently close and open the door.

Preparing components: (1) Arduino, (1) Servo motor, (1)  door lock.

  <img width="419" alt="Screen Shot 2022-02-17 at 16 14 13" src="https://user-images.githubusercontent.com/81319640/154443780-b42ffacb-36ed-4b5e-8c9e-c4988a513313.png">

Implementation steps:

   <img width="485" alt="Screen Shot 2022-02-17 at 16 14 22" src="https://user-images.githubusercontent.com/81319640/154444047-1d756310-3f79-4011-bf88-1220c4dc1460.png">


Step 1: Collect data:
   The facemask dataset is taken from the Face Mask Detection set on Kaggel.
   
Step 2:Training Model:
   Because of the real time object detection problem, the model here is chosen as the Yolo V5 model.
   
Step 3: Install the deploy model circuit into the kit
  The circuit will be connected as .
  The Trained model part will be included in the Test class. Here we will use the OpenCV library to detect the box from the Trained Model section . Create a Controller class to adjust the rotation angle of the Servo motor.
  
Step 4: Connect the motor to the key.
After installing the circuit and repeating the code to adjust, finally connect the servo motor with the latch accordingly.

<img width="585" alt="Test_Image" src="https://user-images.githubusercontent.com/81319640/154444091-79e1d15c-063d-4d48-9449-a29e0e865307.png">
