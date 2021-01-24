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
    parser.add_argument('--origin_size', '-os', type=float,
                        help='origin size. if 0, no origin. (only when visualizing pointcloud)',
                        default=1)
    args = parser.parse_args()
    root, ext = os.path.splitext(args.input)

    if 'bin' in ext.lower():
        points_flatten = np.fromfile(args.input, dtype=np.float32)
        points = points_flatten.reshape(-1, args.channel)
        pcd = o3d.geometry.PointCloud()
        pcd.points = o3d.utility.Vector3dVector(points[:, :3])
        if args.origin_size:
            origin \
                = o3d.geometry.TriangleMesh.create_coordinate_frame(
                    size=args.origin_size)
            o3d.visualization.draw_geometries([pcd, origin])
        else:
            o3d.visualization.draw_geometries([pcd])

    elif 'pcd' in ext.lower():
        pcd = o3d.io.read_point_cloud(args.input)
        if args.origin_size:
            origin \
                = o3d.geometry.TriangleMesh.create_coordinate_frame(
                    size=args.origin_size)
            o3d.visualization.draw_geometries([pcd, origin])
        else:
            o3d.visualization.draw_geometries([pcd])

    elif 'obj' in ext.lower() or 'off' in ext.lower() \
         or 'ply' in ext.lower() or 'stl' in ext.lower():
        obj = skrobot.model.MeshLink(args.input)
        print(obj.visual_mesh)
        viewer = skrobot.viewers.TrimeshSceneViewer()
        viewer.add(obj)
        viewer._init_and_start_app()

    elif 'urdf' in ext.lower():
        obj = skrobot.models.urdf.RobotModelFromURDF(
            urdf_file=osp.abspath(args.input))
        viewer = skrobot.viewers.TrimeshSceneViewer()
        viewer.add(obj)
        viewer._init_and_start_app()


if __name__ == '__main__':
    main()
