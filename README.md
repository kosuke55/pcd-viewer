# PCD VIEWER

This app just launches the Open3D viewer with a command.  

## Install

```
git clone https://github.com/kosuke55/pcd-viewer.git  
cd pcd-viewer  
pip install -e .  
```

## Examples

`pcd-viewer -i input.pcd`

To visualize binary data, you need to specify the channel(default=4).  
`pcd-viewer -i input.pcd.bin -c 5`

For reference, KITTI pcd has 4 channels and Nuscene pcd has 5 channels.  
