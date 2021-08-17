import os
import glob
import cv2

if __name__ == "__main__":
    cwd = os.getcwd()
    down_dir = os.path.join(cwd, "downloads")
    video_list = glob.glob(os.path.join(down_dir, '*.mp4'))
    
    print(f"{len(video_list)} Videos Found")
    
    result_dir = os.path.join(cwd, "result")
    save_dir = os.path.join(cwd, "result", "extracted_frames")

    if not os.path.exists(result_dir):
        os.mkdir(result_dir)
    if not os.path.exists(save_dir):
        os.mkdir(save_dir)

    for idx, video in enumerate(video_list):
        filename = os.path.basename(video).split(".")[0]

        target_video = cv2.VideoCapture(video)

        # Find OpenCV version
        (major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')

        if int(major_ver)  < 3 :
            fps = target_video.get(cv2.cv.CV_CAP_PROP_FPS)
            #print(f"Frames per second using video.get(cv2.cv.CV_CAP_PROP_FPS): {int(fps)}")
        else :
            fps = target_video.get(cv2.CAP_PROP_FPS)
            #print(f"Frames per second using video.get(cv2.CAP_PROP_FPS) : {int(fps)}")
        
        count = 0
        while True:
            success, image = target_video.read()
            
            if not success:
                break
            
            if count % int(fps*10) == 0:
                out_path = os.path.join(save_dir, f"{idx}{count}.jpg")
                cv2.imwrite(out_path, image)
                print(f"Extracted a Frame from {filename}, Frame_{count}")
            
            count += 1
        
        target_video.release()
