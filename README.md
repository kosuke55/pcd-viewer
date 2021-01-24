# VIEWER 3D

Display 3D objects using an external library.  
This app just launches the Open3D or sckit-robot(trimesh) viewer with a command.  

## Install

```
git clone https://github.com/kosuke55/viewer-3d.git  
cd viewer-3d  
pip install -e .  
```

## Supported formats  
PointCloud  
`.bin .pcd`  
Object  
`.obj .off .ply .stl .urdf`  

## Examples
For point cloud file,  
```
v3 input.pcd  
v3 input.pcd.bin -c 5  
```

To visualize binary data, you need to specify the channel(default=4).  
For reference, KITTI pcd has 4 channels and Nuscene pcd has 5 channels.  

Or for object file,  
```
v3 input.obj  
v3 input.off  
v3 input.ply  
v3 input.stl  
v3 input.urdf  
```
