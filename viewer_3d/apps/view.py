import argparse
import numpy as np
import open3d as o3d
import os
import skrobot
import trimesh


def main():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--input', '-i', type=str,
                        help='Input filename', required=True)
    parser.add_argument('--channel', '-c', type=int,
                        help='Channel of pcd data.',
                        default=4)
    args = parser.parse_args()
    root, ext = os.path.splitext(args.input)

    if 'bin' in ext.lower():
        points_flatten = np.fromfile(args.input, dtype=np.float32)
        points = points_flatten.reshape(-1, args.channel)
        pcd = o3d.geometry.PointCloud()
        pcd.points = o3d.utility.Vector3dVector(points[:, :3])
        o3d.visualization.draw_geometries([pcd])

    elif 'pcd' in ext.lower():
        pcd = o3d.io.read_point_cloud(args.input)
        o3d.visualization.draw_geometries([pcd])

    elif 'ply' in ext.lower() or 'stl' in ext.lower():
        obj = skrobot.model.Link()
        obj._visual_mesh = trimesh.load(args.input)
        viewer = skrobot.viewers.TrimeshSceneViewer()
        viewer.add(obj)
        viewer.show()
        try:
            while not viewer.has_exit:
                pass
        except KeyboardInterrupt:
            pass

    elif 'urdf' in ext.lower():
        obj = skrobot.models.urdf.RobotModelFromURDF(
            urdf_file=args.input)
        viewer = skrobot.viewers.TrimeshSceneViewer()
        viewer.add(obj)
        viewer.show()
        try:
            while not viewer.has_exit:
                pass
        except KeyboardInterrupt:
            pass


if __name__ == '__main__':
    main()
