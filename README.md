# YOLOv5-ORB: Real-time Feature Detection & Matching

The main functionality of the program is to work human detection (YOLOv5) and feature matching (ORB) algorithms concurrently, and in real-time footage. 
- Human detection detects the person and displays over the screen.
- Feature matching extracts features and compares them with all of the dataset images to find the best match.

To better understand what the algorithm can do, please check the following video:

## 1- Human Detection with YOLOv5

The human detection algorithm (YOLOv5) is able to detect the person within the frame in real time, and display:
- Percentage of frames including at least one person
- Time passed after the execution
- Total time having at least one preson within the frame
- How many frames are processed each second
- Average confidence of human detection

Here is an example interface of the human detection algorithm:
 
![Screen Shot 2022-06-21 at 19 50 07](https://user-images.githubusercontent.com/51164676/174854878-793ea0fb-904d-4a59-bc7f-93f523b9c5d4.png)

Here are some example results from human detection:

**Detection from Close Range:**

![1](https://user-images.githubusercontent.com/51164676/175028068-8c2b4477-cd6c-4a0c-bac7-b08fca1b50ae.JPG)

**Detection from Distance:**

![2](https://user-images.githubusercontent.com/51164676/175028045-9f58a8ea-ee68-41dd-8852-fef278fe7fa8.JPG)

**Detection from Behind:**

![3](https://user-images.githubusercontent.com/51164676/175027981-257f62e8-8a78-41f2-95aa-c4e9c352c1dd.JPG)

**Detection from the Side:**

![4](https://user-images.githubusercontent.com/51164676/175028010-9ce13382-e473-4aa6-84e1-23bf26b715f8.JPG)

## 2- Feature Matching with ORB

The feature matching algorithm (ORB) is currently able to work in real time and can:
- Extract features for each frame
- Match the current frame with a given reference image
- Select best match of the current frame among a dataset of reference images

Let's see some example results from feature matching:

**No possible match from the dataset:**

![21](https://user-images.githubusercontent.com/51164676/175026836-eb23b831-a63f-45b6-b599-83959cf08de0.JPG)


**Possible matches from the dataset:**

Here, the program chooses the best match among the dataset and displays on the left side of the real-time footage.

![23](https://user-images.githubusercontent.com/51164676/175026346-99e10792-a001-4701-84ca-41b0f6821bf0.JPG)

![22](https://user-images.githubusercontent.com/51164676/175026848-223e1a70-b335-4ad8-80dc-eb9a346ce9ee.JPG)


-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

## GUI

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
