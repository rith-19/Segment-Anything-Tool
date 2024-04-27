# Segment-Anything Annotation Tool
This Python-based user interface harnesses the power of Labelme and the Segment-Anything model from Meta AI to achieve precise pixel-level annotation. Our tool offers a seamless workflow for creating multiple masks through SAM prompts (including boxes and points), efficient polygon editing, and comprehensive category management. Looking ahead, we're excited to integrate CLIP-based techniques for enhanced category proposal and incorporate VOS methods to streamline mask association in video datasets.

## Key Features
- [x] Interactive Segmentation with SAM (supports both boxes and points prompts)
- [x] Flexible Output Options
- [x] Category Annotation Capability
- [x] Intuitive Polygon Editing
- [ ] Integration of CLIP for Category Proposal
- [x] Integration of STCN for Video Dataset Annotation

## Installation Requirements
1. Python version 3.10 or higher
2. [PyTorch](https://pytorch.org/)
3. Execute `pip install -r requirements.txt`

## How to Use
### 1. Launch the Annotation Platform

```bash
py annotator.py 
```

### 2. Load the Category List File
If you wish to annotate object categories, click on `Category File` in the top toolbar and select your desired file, such as `categories.txt` provided in this repository.

### 3. Specify Image and Save Folders
Click on `Image Directory` in the top toolbar to specify the folder containing images (in .jpg or .png format).
Similarly, click on `Save Directory` in the top toolbar to specify the folder for saving the annotations. Each image's annotations will be saved as a JSON file in the following format:
```json
[
  {
    "label": "<category>",
    "group_id": <id>,
    "shape_type": "polygon",
    "points": [[x1, y1], [x2, y2], [x3, y3], ...]
  },
  ...
]
```

### 4. Load the SAM Model
Download the required [models](https://github.com/facebookresearch/segment-anything#model-checkpoints) and place them in the root directory named `vit_b.pth`, `vit_l.pth`, and `vit_h.pth`. Then, click on `Load SAM` in the top toolbar to load the SAM model.

### 5. Annotation Functions
`Manual Polygons`: manually add masks by clicking on the boundary of the objects, just like the Labelme (Press right button and drag to draw the arcs easily).

`Point Prompt`: generate mask proposals with clicks. The mouse leftpress/rightpress represent positive/negative clicks respectively.
You can see several mask proposals below in the boxes: `Proposal1-4`, and you could choose one by clicking or shortcuts `1`,`2`,`3`,`4`.

`Box Prompt`: generate mask proposals with boxes.

`Accept`(shortcut:`a`): accept the chosen proposal and add to the annotation dock.

`Reject`(shortcut:`r`): reject the proposals and clean the workspace.

`Save`(shortcut:'s'): save annotations to file. Do not forget to save your annotation for each image, or it will be lost when you switch to the next image.

`Edit Polygons`: in this mode, you could modify the annotated objects, such as changing the category labels or ids by double click on object items in the
annotation dock. And you can modify the boundary by draging the points on the boundary.

`Delete`(shortcut:'d'): under `Edit Mode`, delete selected/hightlight objects from annotation dock.

`Reduce Point`: under `Edit Mode`, if you find the polygon is too dense to edit, you could use this button to reduce the points on the selected polygons. But this will slightly reduce the annotation quality.

`Zoom in/out`: press 'CTRL' and scroll wheel on the mouse

`Class On/Off`: if the Class is turned on, a dialog will show after you accept a mask to record category and id, or the catgeory will be default value "Object".

## Video Usage
### 1. Clone STCN
Clone the [STCN repository](https://github.com/hkchengrex/STCN), download the [stcn.pth](https://drive.google.com/file/d/1mRrE0uCI2ktdWlUgapJI_KmgeIiF2eOm/view), and place them in the root directory as shown:
```
-| segment-anything-annotator
    -| annotation_video.py
    .....
    -| STCN
    -| stcn.pth
```

### 2. Start the Annotation Platform
```bash
python annotator_video.py --app_resolution 1000,1600 --model_type vit_b --keep_input_size True --max_size 720 --max_size_STCN 600
```
- `--model_type`: Choose from `vit_b`, `vit_l`, or `vit_h`.
- `--keep_input_size`: Set to `True` to keep the original image size for SAM, or `False` to resize the input image to `--max_size` (to save GPU memory).
- `--max_size_STCN`: Specify the maximum input image size for STCN.

### 3. Specify the Video and Save Folders
Click on `Video Directory` and `Save Directory`. The video folders should have the following structure:
```
-| video_fold
    -| video1
        -| 00000.jpg
        -| 00001.jpg
        ...
    -| video2
        -| 00000.jpg
        -| 00001.jpg     
    ...
```

### 4. Load STCN and SAM
Click on `Load STCN` and `Load SAM`.

### 5. Video Annotation Functions
- **Finish Annotations**: Complete annotations for the first frame with SAM.
- **Object Selection**: Press and hold `left control`, then click `left mouse button` to select objects to track.
- **Add Object to Memory**: Initialize tracklets by clicking `Add object to memory`.
- **Frame Navigation**: Move to the next or previous frame using `n` and `b` shortcuts.
- **Propagate**: Obtain tracked masks for new frames by clicking `Propagate`.
- **Edit Mode**: Press 'e' to enter edit mode and manually correct masks.
- **Shortcuts**: Various shortcuts available for efficient annotation (e.g., 'a' for accept proposal, 'r' for reject proposal, 'd' for delete, 's' for save, 'space' for propagate).

## To Do
- [ ] Integration of CLIP for Category Proposal
- [x] Integration of STCN for Video Dataset Annotation
- [ ] Bug Fixes and UI Optimizations
- [ ] Support for Various Annotation File Formats (e.g., Labelme, COCO, Youtube-VIS)

## Acknowledgement 
This repository is built upon the Segment anything model and Labelme projects.

##NOTE
**Feel free to contribute your ideas to this repo** 
