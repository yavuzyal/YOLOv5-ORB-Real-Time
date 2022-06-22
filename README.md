# YOLOv5-ORB: Real-time Feature Detection & Matching

The main functionality of the program is to work both human detection (YOLOv5) and feature matching (ORB) algorithms algorithm at the same time! On feature matching part, the implementation finds the best match of current frame among a dataset of reference images in real-time. 

To understand what the algorithm can do, please check the following video:



On the current version of the algorithm, the human detection algorithm (YOLOv5) is able to detect the person within the frame in real time, and display:
- Percentage of frames including at least one person
- Time passed after the execution
- Total time having at least one preson within the frame
- How many frames are processed each second
- Average confidence of human detection

Here is an example interface of the human detection algorithm:
 
![Screen Shot 2022-06-21 at 19 50 07](https://user-images.githubusercontent.com/51164676/174854878-793ea0fb-904d-4a59-bc7f-93f523b9c5d4.png)

Here are some example results from human detection:

**Detection from Close Range:**

![1](https://user-images.githubusercontent.com/51164676/175025807-c7adaa18-83bf-4028-b3b3-e42d3d2a1e89.JPG)

**Detection from Distance:**

![2](https://user-images.githubusercontent.com/51164676/175025834-e2168d9e-a869-4bb9-96e0-c6a252f04321.JPG)

**Detection from Behind:**

![3](https://user-images.githubusercontent.com/51164676/175025876-ee63a455-ba41-4d9a-b38e-e317dfb1f789.JPG)

**Detection from the Side:**

![4](https://user-images.githubusercontent.com/51164676/175025927-44472178-1ce7-4259-a5b6-b9a1fd205b1c.JPG)


On the feature matching algorithm (ORB), program is currently able to work in real time and able to do:
- Extract features for each frame
- Match the current frame with a given reference image
- Select best match of the current frame among a dataset of reference images

Let's see some example results from feature matching:

**No possible match from the dataset:**

![21](https://user-images.githubusercontent.com/51164676/175026185-c52d44b5-97cd-4f3f-978b-c9bb9b15ccb4.JPG)

**Possible matches from the dataset:**

Here, the program chooses the best match among the dataset and displays on the left side of the real-time footage.

![23](https://user-images.githubusercontent.com/51164676/175026346-99e10792-a001-4701-84ca-41b0f6821bf0.JPG)

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

## From scratch:

The program starts with a very simple GUI, which can be seen below:

![Screen Shot 2022-06-19 at 21 20 07](https://user-images.githubusercontent.com/51164676/174855725-8abdd8ea-d142-4dd2-915b-0a1cad9ba111.png)

### **Buttons and their use cases:**

**Choose Dataset Folder:**
This button opens the file explorer of the local computer, and lets user to choose a folder path. This path must be used as a dataset and must be filled with desired reference images out of the program. 

**Choose Reference Image:**
This button opens the file explorer of the local computer, and lets user to choose a reference image. This reference image will be used as the main reference image, and each of the real-time frames will be compared with this reference image.

**Path:**
Path will show the chosen path of the dataset folder or the reference image. If none of them have been chosen, an error message will be displayed. 

**Detect:**
Detect will start the execution of the program. Both human detection and feature matching will start concurrently after pressing the detect button. This is done through threads. 

**Cancel:**
Cancel will stop close the interface
