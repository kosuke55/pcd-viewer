import argparse
import os
import os.path as osp

import numpy as np
import open3d as o3d
import skrobot
import trimesh


def main():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('input', type=str,
                        help='Input filename')
    parser.add_argument('--channel', '-c', type=int,
                        help='Channel of pcd data.',
                        default=4)
    args = parser.parse_args()
    root, ext = os.path.splitext(args.input)

    viewer = skrobot.viewers.TrimeshSceneViewer()

    if 'bin' in ext.lower() or 'pcd' in ext.lower():
        if 'bin' in ext.lower():
            points_flatten = np.fromfile(args.input, dtype=np.float32)
            points = points_flatten.reshape(-1, args.channel)
            pcd = o3d.geometry.PointCloud()
            pcd.points = o3d.utility.Vector3dVector(points[:, :3])

        elif 'pcd' in ext.lower():
            pcd = o3d.io.read_point_cloud(args.input)

        trimesh_pc = trimesh.PointCloud(
            np.asarray(
                pcd.points), np.asarray(
                pcd.colors))
        skrobot_pc = skrobot.model.PointCloudLink(trimesh_pc)
        viewer.add(skrobot_pc)

    elif 'obj' in ext.lower() or 'off' in ext.lower() \
         or 'ply' in ext.lower() or 'stl' in ext.lower():
        obj = skrobot.model.MeshLink(args.input)
        viewer.add(obj)

    elif 'urdf' in ext.lower():
        obj = skrobot.models.urdf.RobotModelFromURDF(
            urdf_file=osp.abspath(args.input))
        viewer.add(obj)
    else:
        raise ValueError(
            'The extension should be .bin .pcd .obj .off .ply .stl .urdf')

    viewer._init_and_start_app()


if __name__ == '__main__':
    main()
