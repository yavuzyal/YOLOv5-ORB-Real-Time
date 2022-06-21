#YOLOv5-ORB: Feature Detection & Matching

This is a Sabancı University graduation project, in cooperation with General Electric. The title of the project is "Estimation of Cycle Time in Transformer Manufacturing Using a Vision Based Learning Technique". The aim of the project is to implement human detection and feature matching algorithms, which can work concurrently. 

On the current version of the algorithm, the human detection algorithm (YOLOv5) is able to detect the person within the frame in real time, and display:
- Percentage of frames including at least one person
- Time passed after the execution
- Total time having at least one preson within the frame
- How many frames are processed each second
- Average confidence of human detection

Here is an example interface of the human detection algorithm:
 
![Screen Shot 2022-06-21 at 19 50 07](https://user-images.githubusercontent.com/51164676/174854878-793ea0fb-904d-4a59-bc7f-93f523b9c5d4.png)

On the feature matching algorithm (ORB), program is currently able to work in real time and able to do:
- Extract features for each frame
- Match the current frame with a given reference image
- Select best match of the current frame among a dataset of reference images



The program starts with a very simple GUI, which can be seen below:

![Screen Shot 2022-06-19 at 21 20 07](https://user-images.githubusercontent.com/51164676/174855725-8abdd8ea-d142-4dd2-915b-0a1cad9ba111.png)

### **Buttons and their use cases:**

**Choose Dataset Folder:**
This button opens the file explorer of the used computer, and lets user to choose a folder path. This path will be used to 
